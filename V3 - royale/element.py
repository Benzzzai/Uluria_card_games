

class Unit():
    def __init__(self, name, effect):
        self.name = name
       
        self.actionable = False
        self.paralyse = False
        # pe regroupé sous un "status" avec les 3 pos + le premier tour


        self.mort = ("mort" in effect)
        self.start_turn = ("start_turn" in effect)
        self.end_turn = ("start_turn" in effect)


        self.bouclier = ("bouclier" in effect)
        self.defenseur = ("defenseur" in effect)
        self.insaisisable = ("insaisisable" in effect)
        self.puissance = ("puissance" in effect)
        self.rapide = ("rapide" in effect)
        self.robuste = ("robuste" in effect)
        self.rush = ("rush" in effect)


    # def take_damage():


class Fighter(Unit):
    def __init__(self, name, atk, lore, pv, effect):
        super().__init__(name, effect)
        self.atk = atk
        self.atk_ori = atk
        self.lore = lore
        self.lore_ori = lore # nécessaire ?
        self.pv = pv
        self.pv_max = pv
        self.pv_ori = pv


class Structure(Unit):
    def __init__(self, name, durability, effect):
        super().__init__(name, effect)
        self.name = name
        self.durability = durability


class Trap():
    def __init__(self, name):
        self.name = name


class Artefact():
    def __init__(self, name):
        self.name = name

class Enchantment():
    def __init__(self, name):
        self.name = name


class Spell():
    def __init__(self, name):
        self.name = name

    def activate(self):
        pass