from cards.card import Card
from config.config_ritual import ritual_set

class Ritual(Card):
    def __init__(self, name):
        super().__init__(name, ritual_set[name]["cost"])


    def activate(self, ally_player, ennemy_player, target):
        pass