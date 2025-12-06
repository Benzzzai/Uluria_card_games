from card_class.enchantment import Enchantment

class Trap(Enchantment):
    def __init__(self, name, cost, trigger_type):
        super().__init__(name, cost)
        self.trigger_type = trigger_type