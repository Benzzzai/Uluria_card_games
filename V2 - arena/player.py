from avatar import Avatar
from card_class.fighter import Fighter
from card_class.structure import Structure
from card_class.spell import Spell
from card_class.trap import Trap
from card_class.glyph import Glyph
from card_class.weapon import Weapon
from card_class.artefact import Artefact
from config_deck import deck_set
from config_card import card_set
import random


class Player:
    def __init__(self, deck_name):
        self.name = deck_name

        self.avatar = Avatar.create_avatar(deck_set[deck_name]["avatar"])
        self.deck = self.build_deck(deck_name)
        self.hand = []
        self.board = []
        self.discard = []
        self.draw_card(3)

        self.weapon = None
        self.artefact = None

        self.health = 20
        self.armor = 0
        self.basic_mana = 0
        self.extra_mana = 0
        self.ramp = 0
        self.max_mana = 7
        self.essence = 1

        self.fatigue = 1
        self.inspiration = False

    def create_card(self, name):
        card_type = card_set[name]["type"]
        if card_type == "fighter":
            return Fighter(name, card_set[name]["cost"], card_set[name]["atk"], card_set[name]["pv"], card_set[name]["effect"])
        elif card_type == "structure":
            return Structure(name, card_set[name]["cost"], card_set[name]["pv"], card_set[name]["effect"])
        elif card_type == "spell":
            return Spell(name, card_set[name]["cost"], card_set[name]["target_type"])
        elif card_type == "trap":
            return Trap(name, card_set[name]["cost"], card_set[name]["trigger_type"])
        elif card_type == "glyph":
            return Glyph(name, card_set[name]["cost"], card_set[name]["size"], card_set[name]["durability"])
        elif card_type == "weapon":
            return Weapon(name, card_set[name]["cost"], card_set[name]["atk"], card_set[name]["durability"])
        elif card_type == "artefact":
            return Artefact(name, card_set[name]["cost"], card_set[name]["durability"])
        

    def build_deck(self, deck_name):
        deck = []
        for card_name in deck_set[deck_name]["main_deck"]:
            deck.append(self.create_card(card_name))
        random.shuffle(deck)
        return deck
    
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

    def start_turn(self, turn, ennemy):
        # self.avatar.activate_avatar_start_turn(self, ennemy)
        self.draw_card(1)
        self.refresh_actionable()
        self.refresh_mana((1+turn)//2)
        self.essence += 1
        self.inspiration = False

        for card in self.board:
            if card.start_turn:
                card.activate_start_turn(self, ennemy)

    def end_turn(self, ennemy):
        for card in self.board:
            card.paralyse = False
            if card.end_turn:
                card.activate_end_turn(self, ennemy)
        # self.avatar.activate_avatar_end_turn(self, ennemy)

    def refresh_actionable(self):
        for unit in self.board:
            unit.actionable = True
        if self.weapon:
            self.weapon.actionable = True

    def gain_mana(self, m):
        self.extra_mana = min(self.extra_mana + m, 10 - self.basic_mana)

    def refresh_mana(self, turn):
        mana_left = self.basic_mana // 2
        self.basic_mana = min(turn + self.ramp, self.max_mana)
        self.extra_mana = min(mana_left, 10 - self.basic_mana)

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
        
    def discard_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
        elif card in self.board:
            self.board.remove(card)
        self.discard.append(card)

    def play_unit(self, card, pos, ennemy_player, target=None):
        if self.use_mana(card.cost):
            # self.check_card_played(ennemy_player, card)
            self.hand.remove(card)
            self.board.append(card)
            card.pos = pos
            if card.rush:
                card.actionable = True
            if card.inv:
                card.activate_inv(self, ennemy_player, target)

    def play_spell(self, card, ennemy_player, target=None):
        if self.use_mana(card.cost):
            self.hand.remove(card)
            self.discard.append(card)
            card.activate_spell(self, ennemy_player, target)
            self.inspiration = True

    def play_weapon(self, card):
        if self.use_mana(card.cost):
            if self.weapon != None:
                self.discard.append(self.weapon)
            self.hand.remove(card)
            self.weapon = card

    def play_artefact(self, card):
        if self.use_mana(card.cost):
            if self.artefact != None:
                self.discard.append(self.artefact)
            self.hand.remove(card)
            self.artefact = card

    def get_puissance(self):
        puissance = 0
        for unit in self.board:
            if unit.puissance:
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
        