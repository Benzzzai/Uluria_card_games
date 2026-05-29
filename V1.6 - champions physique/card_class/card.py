from config_card import card_set
import pygame
from parameters import CARD_SIZE


class Card:
    def __init__(self, name, cost, classe, description=""):
        self.name = name    
        self.cost = cost
        self.cost_ori = cost
        self.classe = classe
        self.description = description
        self.legendary = False
        self.rectangle = pygame.Rect(0, 0, CARD_SIZE, CARD_SIZE) 

    def reduce_cost(self, value):
        self.cost = max(0, self.cost - value)

    def activate_hand(self, player):
        if self.name == "(mv)":
            if player.trigger_thot:
                self.reduce_cost(1)
        elif self.name == "Tablette de la destinée":
            if player.trigger_thot:
                self.reduce_cost(1)
        elif self.name == "Infection":
            player.take_damage(1)