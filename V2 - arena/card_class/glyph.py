from card_class.enchantment import Enchantment

class Glyph(Enchantment):
    def __init__(self, name, cost, size, durability):
        super().__init__(name, cost)
        self.size = size
        self.durability = durability