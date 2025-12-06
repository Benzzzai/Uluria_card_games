from card_class.card import Card


class Unit(Card):
    def __init__(self, name, cost, pv, effect):
        super().__init__(name, cost)
        self.pv = pv
        self.pv_max = pv
        self.pv_ori = pv
        self.pos = (-3, -3)

        self.actionable = False
        self.paralyse = False

        self.inv = ("inv" in effect)
        self.front = ("front" in effect)
        self.attaque = ("attaque" in effect)
        self.mort = ("mort" in effect)
        self.start_turn = ("start_turn" in effect)
        self.end_turn = ("end_turn" in effect)
        self.card_played = ("card_played" in effect)

        self.target_ennemy = ("target_ennemy" in effect)
        self.target_ally = ("target_ally" in effect)

        self.bouclier = ("bouclier" in effect)
        self.defenseur = ("defenseur" in effect)
        self.insaisisable = ("insaisisable" in effect)
        self.inciblable = ("inciblable" in effect)
        self.percant = ("percant" in effect)
        self.protecteur = ("protecteur" in effect)
        self.puissance = ("puissance" in effect)
        self.rapide = ("rapide" in effect)
        self.robuste = ("robuste" in effect)
        self.rush = ("rush" in effect)
        self.vol_vie = ("vol_vie" in effect)

    def activate_inv(self, ally_player, ennemy_player, target=None):
        pass # in subclasses

    def take_damage(self, value):
        pass # in subclasses

    def heal(self, value):
        pass # in subclasses

    def buff(self, atk, pv):
        pass # in subclasses