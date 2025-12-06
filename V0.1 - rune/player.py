from card_class.card import Card
from card_class.fighter import Fighter, Champion, Creature
from card_class.structure import Structure
from card_class.spell import Spell
from card_class.divine import Divine, Offering, Alteration
from avatar import Avatar
from config_deck import deck_set
from config_card import card_set
import random

class Player:
    def __init__(self, deck_name):
        self.name = deck_name
        self.avatar = Avatar.create_avatar(deck_set[deck_name]["avatar"])
        
        self.deck = []
        self.hand = []
        self.frontrow = []
        self.backrow = []
        self.discard = []
        self.build_deck_and_hand(deck_name)

        self.health = 20
        self.armor = 0
        self.basic_mana = 0
        self.extra_mana = 0
        self.ramp = 0
        self.max_mana = 8

        self.fatigue = 1
        self.inspiration = False

        self.bonus_ishtar = False
        self.debuff_glace = False
        self.trigger_thot = False
        self.trigger_ishtar = False

        self.max_backrow_size = 3
        self.max_frontrow_size = 3

    def create_card(self, name):
        card_type = card_set[name]["type"]
        if card_type == "champion":
            return Champion(name, card_set[name]["cost"], card_set[name]["atk"], card_set[name]["pv"], card_set[name]["effect"])
        elif card_type == "creature":
            return Creature(name, card_set[name]["cost"], card_set[name]["atk"], card_set[name]["pv"], card_set[name]["effect"])
        elif card_type == "structure":
            return Structure(name, card_set[name]["cost"], card_set[name]["pv"], card_set[name]["effect"], card_set[name]["row"])
        elif card_type == "spell":
            return Spell(name, card_set[name]["cost"], card_set[name]["target"])
        elif card_type == "offering":
            return Offering(name, card_set[name]["cost"])
        elif card_type == "alteration":
            return Alteration(name, card_set[name]["cost"])


    def build_deck_and_hand(self, deck_name):
        alteration_set = []
        for card_name in deck_set[deck_name]["alteration_deck"]:
            alteration_set.append(self.create_card(card_name))
        random.shuffle(alteration_set)
        card = alteration_set.pop(0)
        self.hand.append(card)
        for card_name in deck_set[deck_name]["main_deck"]:
            self.deck.append(self.create_card(card_name))
        random.shuffle(self.deck)
        self.draw_card(3)
        for card in alteration_set:
            alteration_set.remove(card)
            self.deck.append(card)
        random.shuffle(self.deck)

    def start_turn(self, turn, ennemy):
        self.avatar.activate_avatar_start_turn(self, ennemy)
        self.draw_card(1)
        self.refresh_actionable()
        self.refresh_mana((1+turn)//2)
        self.inspiration = False
        self.trigger_thot = False
        self.trigger_ishtar = False

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
        self.avatar.activate_avatar_end_turn(self, ennemy)
        self.trigger_thot = False
        self.trigger_ishtar = False

    def draw_card(self, n=1, card_type=None): # est ce qu'on peux donner une classe comme argument ici ?
        for _ in range(n):
            if card_type:
                for card in self.deck:
                    if card.card_type == card_type:
                        self.deck.remove(card)
                        random.shuffle(self.deck)
                        if len(self.hand) < 8:
                            self.hand.append(card)
                        else:
                            self.discard.append(card)
                        break
            else:
                if self.deck:
                    card = self.deck.pop(0)
                    if len(self.hand) < 8:
                        self.hand.append(card)
                    else:
                        self.discard.append(card)
                else:
                    self.take_damage(self.fatigue)
                    self.fatigue += 1

    def refresh_actionable(self):
        for card in self.backrow:
            card.actionable = True
        for card in self.frontrow:
            card.actionable = True

    def refresh_mana(self, turn):
        mana_left = self.basic_mana // 2
        self.basic_mana = min(turn + self.ramp, self.max_mana)
        self.extra_mana = min(mana_left, 10-self.basic_mana)

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
        if row == "front" and len(self.frontrow) < self.max_frontrow_size:
            if self.use_mana(card.cost):
                self.check_card_played(ennemy_player, card)
                self.hand.remove(card)
                self.frontrow.insert(pos, card)
                if card.rush:
                    card.actionable = True
                if card.inv:
                    card.activate_inv(self, ennemy_player, target)
        elif row == "back" and len(self.backrow) < self.max_backrow_size:
            if self.use_mana(card.cost):
                self.check_card_played(ennemy_player, card)
                self.hand.remove(card)
                self.backrow.insert(pos, card)
                if card.rush:
                    card.actionable = True
                if card.inv:
                    card.activate_inv(self, ennemy_player, target)

    def front_fighter(self, card, ennemy_player, target=None, pos=0):
        if card.actionable and not card.paralyse and len(self.frontrow) < self.max_frontrow_size:
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

    def discard_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
        elif card in self.backrow:
            self.backrow.remove(card)
        elif card in self.frontrow:
            self.frontrow.remove(card)
        self.discard.append(card)

    def play_spell(self, ennemy_player, card, target=None):
        if self.use_mana(card.cost):
            self.check_card_played(ennemy_player, card)
            self.hand.remove(card)
            self.discard.append(card)
            self.inspiration = True
            card.activate_spell(self, ennemy_player, target)
        
    def play_divine(self, ennemy_player, card):
        if self.use_mana(card.cost):
            self.check_card_played(ennemy_player, card)
            self.hand.remove(card)
            self.discard.append(card)
            card.activate_divine(self, ennemy_player)
        
    def get_puissance(self):
        puissance = 0
        for card in self.backrow:
            if card.puissance:
                puissance += 1
        for card in self.frontrow:
            if card.puissance:
                puissance += 1
        return puissance
    
    def heal(self, value):
        self.health = min(self.health + value, 20)

    def gain_armor(self, value):
        self.armor += value

    def take_damage(self, value):
        if value <= self.armor:
            self.armor -= value
        else:
            value -= self.armor
            self.armor = 0
            self.health = max(0, self.health - value)

    def summon_unit(self, unit_name, row):
        if row == "front" and len(self.frontrow) < self.max_frontrow_size:
            self.frontrow.append(self.create_card(unit_name))
        elif row == "back" and len(self.backrow) < self.max_backrow_size:
            self.backrow.append(self.create_card(unit_name))

    def check_card_played(self, ennemy_player, card):
        for unit in self.frontrow:
            if unit.card_played:
                unit.activate_card_played(self, ennemy_player, card)
        for unit in self.backrow:
            if unit.card_played:
                unit.activate_card_played(self, ennemy_player, card)
