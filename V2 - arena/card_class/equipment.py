from card_class.card import Card

class Equipment(Card):
    def __init__(self, name, cost, durability):
        super().__init__(name, cost)
        self.durability = durability


