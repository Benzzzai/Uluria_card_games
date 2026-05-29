from cards.card import Card
from config.config_spell import spell_set

class Spell(Card):
    def __init__(self, name):
        super().__init__(name, spell_set[name]["cost"])


    def activate(self, ally_player, ennemy_player, target):
        if self.name == "Concentration":
            ally_player.gain_mana(2)
        elif self.name == "Floraison":
            ally_player.mana_max += 1
        elif self.name == "Pluie de balles":
            for unit in ally_player.board:
                unit.take_damage(1)
            for unit in ennemy_player.board:
                unit.take_damage(1)
        elif self.name == "Régénération":
            ally_player.heal(3)
        elif self.name == "Boule de feu":
            ennemy_player.take_damage(4)
        elif self.name == "Intelligence":
            ally_player.draw_card(3)
        elif self.name == "":
            pass
        elif self.name == "":
            pass
        elif self.name == "":
            pass
        elif self.name == "":
            pass
        elif self.name == "":
            pass
        