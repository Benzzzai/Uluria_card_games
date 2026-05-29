
from cards.card import Card
from cards.fighter import Fighter
from cards.trap import Trap
from cards.artefact import Artefact
from cards.enchantment import Enchantment
from cards.spell import Spell
from cards.ritual import Ritual

from config.config_deck import deck_set
from config.config_card import card_set
import random


class Player():
    def __init__(self, deck_name):
        self.name = deck_name
       
        self.deck = []
        self.hand = []
        self.discard = []
        self.build_deck()
        self.board = []
        self.trap_zone = []
        self.artefact_zone = []
        self.enchantment_zone = []

        self.health = 20
        self.armor = 0
        self.mana = 0
        self.mana_max = 0
        self.encre = False
        self.surcharge = 0


    def build_deck(self):
        for card_name, n_copy in deck_set[self.name].items():
            for _ in range(n_copy):
                self.deck.append(self.create_card(card_name))
        random.shuffle(self.deck)
        self.draw_card(3)

    def create_card(self, card_name):
        card_type = card_set[card_name]
        if card_type == "fighter":
            return Fighter(card_name)
        elif card_type == "spell":
            return Spell(card_name)
        elif card_type == "ritual":
            return Ritual(card_name)
        elif card_type == "trap":
            return Trap(card_name)
        elif card_type == "artefact":
            return Artefact(card_name)
        elif card_type == "enchantment":
            return Enchantment(card_name)

    def draw_card(self, n=1):
        for _ in range(n):
            if len(self.deck) > 0:
                card = self.deck.pop(0)
                self.hand.append(card)
            else:
                self.take_damage(1)

    def start_turn(self, ennemy):
        for unit in self.board:
            unit.status = "actionable"
        self.refresh_mana()
        if len(self.hand) < 5:
            self.draw_card(2)
        else:
            self.draw_card(1)
        
        for card in self.board:
            if card.start_turn:
                card.activate_start_turn(self, ennemy)

    def end_turn(self, ennemy):
        for card in self.board:
            card.paralyse = False
            if card.end_turn:
                card.activate_end_turn(self, ennemy)        

    def gain_mana(self, value):
        self.mana += value

    def refresh_mana(self):
        self.mana = self.mana_max
        self.mana -= self.surcharge
        self.surcharge = 0
        self.encre = False

    def use_mana(self, cost):
        if cost > self.mana:
            return False
        else:
            self.mana -= cost
            return True
       
    def encre_card(self, card):
        if not self.encre:
            self.hand.remove(card)
            self.mana += 1
            self.mana_max += 1
            self.encre = True

    def play_card(self, card, ennemy_player, target=None):
        if self.use_mana(card.cost):
            self.hand.remove(card)

            if isinstance(card, Fighter):
                if len(self.board) < 7:
                    self.board.append(card)
                    if card.on_inv:
                        card.activate_inv(self, ennemy_player)
            elif isinstance(card, Trap):
                if len(self.trap_zone) < 3:
                    self.trap_zone.append(card)
            elif isinstance(card, Artefact):
                if len(self.artefact_zone) < 1:
                    self.artefact_zone.append(card)
            elif isinstance(card, Enchantment):
                if len(self.enchantment_zone) < 1:
                    self.enchantment_zone.append(card)
            elif isinstance(card, Spell):
                card.activate(self, ennemy_player, target)
                self.discard.append(card)
            elif isinstance(card, Ritual):
                card.activate(self, ennemy_player, target)
                self.discard.append(card)


    def take_damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health = min(20, self.health + amount)

    def check_death(self, ennemy_player):
        for card in self.board:
            if card.pv <= 0:
                if card.on_mort:
                    card.activate_mort(self, ennemy_player)
                self.board.remove(card)
                self.discard.append(card)
