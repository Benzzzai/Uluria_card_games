from cards.card import Card
from config.config_trap import trap_set

class Trap(Card):
    def __init__(self, name):
        super().__init__(name, trap_set[name]["cost"])