from card_class.equipment import Equipment

class Weapon(Equipment):
    def __init__(self, name, cost, atk, durability):
        super().__init__(name, cost, durability)
        self.atk = atk
        self.atk_ori = atk

        self.actionable = True