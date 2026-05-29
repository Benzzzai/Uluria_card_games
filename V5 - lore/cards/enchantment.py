from cards.card import Card
from config.config_enchantment import enchantment_set

class Enchantment(Card):
    def __init__(self, name):
        super().__init__(name, enchantment_set[name]["cost"])