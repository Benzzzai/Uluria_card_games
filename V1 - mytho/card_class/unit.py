from card_class.card import Card


class Unit(Card):
    def __init__(self, name, cost, pv, effect, classe, archetype, description):
        super().__init__(name, cost, classe, description)
        self.pv = pv
        self.pv_max = pv
        self.pv_ori = pv
        self.archetype = archetype

        self.actionable = False
        self.paralyse = False

        self.inv = ("inv" in effect)
        self.inv_ennemy = ("inv_ennemy" in effect)
        self.inv_ally = ("inv_ally" in effect)
        self.front = ("front" in effect)
        self.attaque = ("attaque" in effect)
        self.soin = ("soin" in effect)
        self.mort = ("mort" in effect)
        self.start_turn = ("start turn" in effect)
        self.end_turn = ("end turn" in effect)

        self.avant_garde = ("avant-garde" in effect)
        self.bouclier = ("bouclier" in effect)
        self.charge = ("charge" in effect)
        self.insaisissable = ("insaisisable" in effect)
        self.magnetisme = ("magnétisme" in effect)
        self.percant = ("percant" in effect)
        self.protecteur = ("protecteur" in effect)
        self.puissance = ("puissance" in effect)
        self.rapide = ("rapide" in effect)
        self.robuste = ("robuste" in effect)
        self.vol_vie = ("vol de vie" in effect)

    def activate_inv(self, ally_player, ennemy_player, target=None):
        pass # in subclasses

    def activate_mort(self, ally_player, ennemy_player):
        pass # in subclasses

    def activate_start_turn(self, ally_player, ennemy_player):
        pass # in subclasses

    def activate_end_turn(self, ally_player, ennemy_player):
        pass # in subclasses

    def take_damage(self, value):
        pass # in subclasses

    def heal(self, value):
        pass # in subclasses

    def buff(self, atk, pv):
        pass # in subclasses