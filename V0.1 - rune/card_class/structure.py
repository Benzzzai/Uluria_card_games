from card_class.card import Card
from card_class.unit import Unit

class Structure(Unit):
    def __init__(self, name, cost, pv, effect, row):
        super().__init__(name, cost, pv, effect)
        self.row = row
    
    def activate_inv(self, ally_player, ennemy_player, target=None):
        pass

    def take_damage(self, value):
        # interaction entre robuste et bouclier ?
        if value > 0:
            if self.robuste:
                value -= 1
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