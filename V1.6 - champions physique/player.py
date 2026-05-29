from card_class.card import Card
from card_class.fighter import Fighter
from card_class.structure import Structure
from card_class.spell import Spell
from card_class.ritual import Ritual
from avatar import Avatar
from config_deck import deck_set
from config_card import card_set
import random

class Player:
    def __init__(self, deck_name):
        self.name = deck_name
        self.avatar = deck_set[deck_name]["avatar"]
        
        self.deck = []
        self.hand = []
        self.frontrow = []
        self.backrow = []
        self.discard = []
        self.build_deck_and_hand(deck_name)

        self.health = 20
        self.armor = 0
        self.basic_mana = 1
        self.extra_mana = 0
        self.max_mana_turn = 1
        self.max_mana = 8
        self.blocked_mana = 0
        self.surcharge = 0

        self.fatigue = 0
        self.puissance = 0
        self.inspiration = False
        self.bonus_ishtar = False
        self.rage_ishtar = False
        self.trigger_thot = 0

        self.infection_2 = False
        self.clepsydre = False

        self.max_row_size = 5

    def create_card(self, name):
        card_type = card_set[name]["type"]
        if card_type == "fighter":
            return Fighter(name, card_set[name]["cost"], card_set[name]["atk"], card_set[name]["pv"], card_set[name]["effect"], card_set[name]["classe"], card_set[name]["archetype"], card_set[name]["description"])
        elif card_type == "structure":
            return Structure(name, card_set[name]["cost"], card_set[name]["pv"], card_set[name]["effect"], card_set[name]["row"], card_set[name]["classe"], card_set[name]["archetype"], card_set[name]["description"])
        elif card_type == "spell":
            return Spell(name, card_set[name]["cost"], card_set[name]["target"], card_set[name]["classe"], card_set[name]["description"])
        elif card_type == "ritual":
            return Ritual(name, card_set[name]["cost"], card_set[name]["classe"], card_set[name]["description"])

    def build_deck_and_hand(self, deck_name):
        for card_name, n_copy in deck_set[deck_name]["main_deck"].items():
            for _ in range(n_copy):
                self.deck.append(self.create_card(card_name))
        random.shuffle(self.deck)
        self.draw_card(4)

    def start_turn(self, ennemy):
        for avatar in self.avatar.values():
            avatar.activate_avatar_start_turn(self, ennemy)
        self.draw_card(1)
        self.refresh_actionable()
        self.refresh_mana()
        for card in self.hand:
            card.activate_hand(self)
        self.inspiration = False
        self.rage_ishtar = False
        self.trigger_thot = 0
        
        for card in self.backrow:
            if card.start_turn:
                card.activate_start_turn(self, ennemy)
        for card in self.frontrow:
            if card.start_turn:
                card.activate_start_turn(self, ennemy)

    def end_turn(self, ennemy):
        for card in self.backrow:
            card.paralyse = False
            if card.end_turn:
                card.activate_end_turn(self, ennemy)
        for card in self.frontrow:
            card.paralyse = False
            if card.end_turn:
                card.activate_end_turn(self, ennemy)
        for avatar in self.avatar.values():
            avatar.activate_avatar_end_turn(self, ennemy)

    def draw_card(self, n=1, card_type=None, archetype=None, reduce_cost=0):
        for _ in range(n):
            if card_type:
                for card in self.deck:
                    if isinstance(card, card_type):
                        if archetype:
                            if card.archetype == archetype:
                                self.deck.remove(card)
                                random.shuffle(self.deck)
                                if len(self.hand) < 8:
                                    self.hand.append(card)
                                    card.reduce_cost(reduce_cost)
                                else:
                                    self.discard.append(card)
                                break
                        else:
                            self.deck.remove(card)
                            random.shuffle(self.deck)
                            if len(self.hand) < 8:
                                self.hand.append(card)
                                card.reduce_cost(reduce_cost)
                            else:
                                self.discard.append(card)
                            break
            else:
                if self.deck:
                    card = self.deck.pop(0)
                    if len(self.hand) < 8:
                        self.hand.append(card)
                        card.reduce_cost(reduce_cost)
                    else:
                        self.discard.append(card)
                else:
                    self.fatigue += 1
                    self.take_damage(self.fatigue)
                    
    def refresh_actionable(self):
        for card in self.backrow:
            card.actionable = True
        for card in self.frontrow:
            card.actionable = True

    def gain_mana(self, value):
        self.extra_mana = min(self.extra_mana + value, 10 - self.basic_mana)

    def refresh_mana(self):
        self.max_mana_turn = min(self.max_mana_turn + 1, self.max_mana)
        self.blocked_mana = self.surcharge
        self.surcharge = 0
        mana_left = (self.basic_mana + self.extra_mana) // 2
        self.basic_mana = max(self.max_mana_turn - self.blocked_mana, 0)
        if self.clepsydre:
            mana_left += 2
            self.clepsydre = False
        self.extra_mana = min(mana_left, 10 - self.basic_mana - self.blocked_mana)

    def use_mana(self, cost):
        if cost > self.basic_mana + self.extra_mana:
            return False
        elif cost > self.extra_mana:
            self.basic_mana -= (cost - self.extra_mana)
            self.extra_mana = 0
            return True
        else:
            self.extra_mana -= cost
            return True
        
    def play_unit(self, card, ennemy_player, target=None, row="back", pos=0):
        player_row = self.frontrow if row == "front" else self.backrow
        if len(player_row) < self.max_row_size:
            if self.use_mana(card.cost):
                self.hand.remove(card)
                player_row.insert(pos, card)
                if (card.inv_ennemy or card.inv_ally) and target:
                    card.activate_inv_target(self, ennemy_player, target)
                if card.inv and target == None:
                    card.activate_inv(self, ennemy_player)
                if card.charge:
                    card.actionable = True

    def front_fighter(self, card, ennemy_player, target=None, pos=0):
        if card.actionable and not card.paralyse and len(self.frontrow) < self.max_row_size:
            self.backrow.remove(card)
            self.frontrow.insert(pos, card)
            if self.bonus_ishtar:
                card.buff(1, 0)
            card.activate_front(self, ennemy_player, target)
    
    def back_fighter(self, card):
        if card.actionable and not card.paralyse:
            self.frontrow.remove(card)
            self.backrow.append(card)
            card.actionable = False

    def summon_unit(self, unit_name, row, buff_atk=0, buff_pv=0):
        if row == "front" and len(self.frontrow) < self.max_row_size:
            unit = self.create_card(unit_name)
            self.frontrow.append(unit)
            unit.buff(buff_atk, buff_pv)
        elif row == "back" and len(self.backrow) < self.max_row_size:
            unit = self.create_card(unit_name)
            self.backrow.append(unit)
            unit.buff(buff_atk, buff_pv)
            
    def play_spell(self, card, ennemy_player, target=None):
        if self.use_mana(card.cost):
            self.hand.remove(card)
            self.discard.append(card)
            card.activate_spell(self, ennemy_player, target)
            self.inspiration = True

    def play_ritual(self, card, target, ennemy_player):
        if target.actionable and card.cost <= target.cost:
            self.hand.remove(card)
            self.discard.append(card)
            card.activate_ritual(self, ennemy_player, target)
            target.actionable = False
    
    def offering(self, card, ennemy_player):
        avatar = self.avatar.get(card.classe)
        if avatar.offering():
            self.hand.remove(card)
            self.discard.append(card)
            avatar.activate_avatar_on_hit(self, ennemy_player)
        
    def check_death(self, ennemy_player, is_not_turn=False):
        for card in self.frontrow:
            if card.pv <= 0:
                if card.mort:
                    card.activate_mort(self, ennemy_player)
                self.frontrow.remove(card)
                self.discard.append(card)
                if is_not_turn:
                    self.trigger_thot += 1
        for card in self.backrow:
            if card.pv <= 0:
                if card.mort:
                    card.activate_mort(self, ennemy_player)
                self.backrow.remove(card)
                self.discard.append(card)
                if is_not_turn:
                    self.trigger_thot += 1

    def get_puissance(self):
        puissance = 0
        for card in self.backrow:
            if card.puissance:
                puissance += 1
        for card in self.frontrow:
            if card.puissance:
                puissance += 1
        puissance += self.puissance
        return puissance
    
    def heal(self, value):
        self.health = min(self.health + value, 20)

    def gain_armor(self, value):
        self.armor += value

    def reduce_armor(self, value):
        self.armor = max(0, self.armor - value)

    def take_damage(self, value, active=False):
        if value <= self.armor:
            self.armor -= value
        else:
            value -= self.armor
            self.armor = 0
            self.health = max(0, self.health - value)
        if active:
            self.rage_ishtar = True

    def debuff_alchimiste(self):
        for card in self.hand:
            if isinstance(card, Spell):
                card.cost += 1
        for card in self.deck:
            if isinstance(card, Spell):
                card.cost += 1

    def is_archetype_on_board(self, archetype):
        for card in self.backrow:
            if card.archetype == archetype:
                return True
        for card in self.frontrow:
            if card.archetype == archetype:
                return True
        return False
    
    def is_card_in_hand(self, card_name):
        for card in self.hand:
            if card.name == card_name:
                return True
        return False
    
    def check_celestial(self):
        for card in self.hand:
            if card.archetype == "célestial":
                return True
        return False