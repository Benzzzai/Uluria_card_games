
from card_class.card import Card
import random

class Ritual(Card):
    def __init__(self, name, cost, classe, description):
        super().__init__(name, cost, classe, description)
        
    def activate_ritual(self, ally_player, ennemy_player, target):
        if self.name == "Rituel forestier":
            for _ in range(len(ennemy_player.frontrow)):
                ally_player.summon_unit("Tréant", "front")
        elif self.name == "Maitrise du blocage":
            ally_player.gain_armor(target.atk)
        elif self.name == "Préparation au combat":
            target.buff(2, 2)
        elif self.name == "Roue de la fortune":
            ennemy_player.deck = ennemy_player.deck[5:]
        elif self.name == "Ruée animale":
            for unit in ally_player.frontrow:
                if unit.archetype == "bête":
                    ennemy_player.take_damage(1)
        elif self.name == "Prière des profondeurs":
            ally_player.summon_unit("Tentacule", "front")
            ally_player.summon_unit("Tentacule", "front")
        elif self.name == "Rage de combat":
            for unit in ally_player.frontrow:
                if unit.pv < unit.pv_max:
                    ally_player.draw_card(1)
            for unit in ally_player.backrow:
                if unit.pv < unit.pv_max:
                    ally_player.draw_card(1)
        elif self.name == "Bagarre générale":
            for unit in ennemy_player.backrow:
                unit.take_damage(target.atk)
                target.take_damage(unit.atk)
        elif self.name == "Appel de la tombe":
            pass