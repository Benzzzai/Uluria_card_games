from card_class.card import Card
from card_class.unit import Unit

class Structure(Unit):
    def __init__(self, name, cost, pv, effect, row, classe, archetype, description):
        super().__init__(name, cost, pv, effect, classe, archetype, description)
        self.row = row
    
    def activate_inv(self, ally_player, ennemy_player, target=None):
        pass

    def activate_mort(self, ally_player, ennemy_player):
        pass

    def activate_start_turn(self, ally_player, ennemy_player):
        if self.name == "Tactirelle":
            self.pv -= 1
        elif self.name == "Chalutier":
            ally_player.draw_card(1)
            self.pv -= 1

    def activate_end_turn(self, ally_player, ennemy_player):
        if self.name == "Harponneuse":
            self.pv -= 1
        elif self.name == "Foreuse":
            ennemy_player.take_damage(2)
            self.pv -= 1
        elif self.name == "Gardienne":
            self.pv -= 1
        elif self.name == "Bathyscaphe":
            ally_player.gain_armor(2)
            self.pv -= 1

    def take_damage(self, value):
        if self.robuste:
                value -= 1
        if value > 0:
            if self.bouclier:
                self.bouclier = False
            else:
                self.pv -= 1
    
    def heal(self, value):
        pass # pas sur encore
        # self.pv = min(self.pv + value, self.pv_max)

    def buff(self, atk, pv):
        self.pv += pv
        self.pv_max += pv