from cards.card import Card
from config.config_artefact import artefact_set

class Artefact(Card):
    def __init__(self, name):
        super().__init__(name, artefact_set[name]["cost"])