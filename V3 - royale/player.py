
from element import Fighter, Structure, Trap, Artefact, Enchantment, Spell
from config_deck import deck_set
from config_card import card_set
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
        self.mana_max = 1
        self.basic_mana = 0
        self.extra_mana = 0


    def build_deck(self):
        for card_name in deck_set[self.name]:
            self.deck.append(Card(card_name))
        random.shuffle(self.deck)
        for _ in range(5):
            self.draw_card()


    def draw_card(self):
        if len(self.deck) == 0:
            if len(self.discard) > 0:
                self.deck, self.discard = self.discard[:], []
                random.shuffle(self.deck)
                card = self.deck.pop(0)
                self.hand.append(card)
            else:
                self.take_damage(1)
        else:
            card = self.deck.pop(0)
            self.hand.append(card)

    def refresh_mana(self, turn):
        mana_left = self.basic_mana // 2
        self.basic_mana = min(turn, 7)
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
       
    def play_card(self, card):
        if self.use_mana(card.cost):
            self.hand.remove(card)
            card.use -= 1
            if card.use > 0:
                self.discard.append(card)
            self.draw_card()

            if card.card_type == "fighter":
                if len(self.board) < 7:
                    self.board.append(Fighter(card.name))
            elif card.card_type == "structure":
                if len(self.board) < 7:
                    self.board.append(Structure(card.name))
            elif card.card_type == "trap":
                if len(self.trap_zone) < 3:
                    self.trap_zone.append(Trap(card.name))
            elif card.card_type == "artefact":
                if len(self.artefact_zone) < 1:
                    self.artefact_zone.append(Artefact(card.name))
            elif card.card_type == "enchantment":
                if len(self.enchantment_zone) < 1:
                    self.enchantment_zone.append(Enchantment(card.name))
            elif card.card_type == "spell":
                spell = Spell(card.name)
                spell.activate()
            else:
                pass
                # si on veut des cartes composées, les hard coder ici


    def take_damage(self, amount):
        self.health -= amount



class Card():
    def __init__(self, name):
        self.name = name
        self.card_type = card_set[name]["card_type"]
        self.cost = card_set[name]["cost"]
        self.use = card_set[name]["use"]

