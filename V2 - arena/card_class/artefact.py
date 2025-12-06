from card_class.equipment import Equipment

class Artefact(Equipment):
    def __init__(self, name, cost, durability):
        super().__init__(name, cost, durability)