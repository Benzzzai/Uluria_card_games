from card_class.card import Card


class Divine(Card):
    def __init__(self, name, cost):
        super().__init__(name, cost)

    def activate_divine(self):
        pass

class Offering(Divine):
    def __init__(self, name, cost):
        super().__init__(name, cost)

    def activate_divine(self, active_player, ennemy_player):
        if active_player.avatar.level < 3:
            active_player.avatar.level += 1
            active_player.max_frontrow_size += 1
            active_player.max_backrow_size += 1
        active_player.avatar.activate_avatar_on_hit(active_player, ennemy_player)

        if self.name == "Offrande protectrice":
            active_player.gain_armor(2)
        elif self.name == "Offrande florissante":
            active_player.draw_card(1)
        elif self.name == "Offrande arcanique":
            active_player.extra_mana += 2
        elif self.name == "Offrande nocturne":
            pass


class Alteration(Divine):
    def __init__(self, name, cost):
        super().__init__(name, cost)

    def activate_alteration(self):
        if self.name == "quest":
            pass

