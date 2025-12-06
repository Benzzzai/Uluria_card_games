from config_card import card_set
import pygame
from parameters import CARD_SIZE


class Card:
    def __init__(self, name, cost, description=""):
        self.name = name
        self.cost = cost
        self.cost_ori = cost
        self.rectangle = pygame.Rect(0, 0, CARD_SIZE, CARD_SIZE)
        self.description = description

