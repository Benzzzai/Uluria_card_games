from card_class.card import Card
import random


class Avatar():
    def __init__(self, level_max):
        self.level = 0
        self.level_max = level_max

    def offering(self):
        if self.level < self.level_max:
            self.level += 1
            return True
        else:
            return False
        
    def activate_avatar_on_hit(self, ally_player, ennemy_player):
        pass

    def activate_avatar_start_turn(self, ally_player, ennemy_player):
        pass

    def activate_avatar_end_turn(self, ally_player, ennemy_player):
        pass


class Marduk(Avatar):
    def __init__(self, level_max):
        super().__init__(level_max)

    def activate_avatar_end_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            ennemy_player.take_damage(3)
        elif self.level >= 3:
            ennemy_player.take_damage(2)
        elif self.level >= 2:
            ennemy_player.take_damage(1)

class Enlil(Avatar):
    def __init__(self, level_max):
        super().__init__(level_max)

    def activate_avatar_end_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            for card in ally_player.frontrow:
                card.heal(1)
            ally_player.heal(2)
        elif self.level >= 3:
            if len(ally_player.frontrow) > 0:
                target = random.choice(ally_player.frontrow)
                target.heal(1)
            ally_player.heal(2)
        elif self.level >= 1:
            if len(ally_player.frontrow) > 0:
                target = random.choice(ally_player.frontrow)
                target.heal(1)

class Enki(Avatar):
    def __init__(self, level_max):
        super().__init__(level_max)

    def activate_avatar_end_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            ally_player.gain_armor(4)
        elif self.level >= 3:
            ally_player.gain_armor(3)
        elif self.level >= 2:
            ally_player.gain_armor(1)

class Ishtar(Avatar):
    def __init__(self, level_max):
        super().__init__(level_max)

    def activate_avatar_on_hit(self, ally_player, ennemy_player):
        if self.level == 3:
            ally_player.bonus_ishtar = True

    def activate_avatar_end_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            if len(ennemy_player.frontrow) > 0:
                target = random.choice(ennemy_player.frontrow)
                target.take_damage(1)
        if self.level >= 1 and ally_player.rage_ishtar:
            ennemy_player.take_damage(1)

class Alchimiste(Avatar):
    def __init__(self, level_max):
        super().__init__(level_max)

    def activate_avatar_on_hit(self, ally_player, ennemy_player):
        if self.level == 4:
            ennemy_player.debuff_alchimiste()
        elif self.level == 2:
            ally_player.max_mana = 9
        elif self.level == 1:
            ally_player.extra_mana += 1

class Kraken(Avatar):
    def __init__(self, level_max):
        super().__init__(level_max)

    def activate_avatar_end_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            ally_player.summon_unit("Tentacule", "front")
            for card in ally_player.frontrow:
                if card.name == "Tentacule":
                    card.buff(1, 0)
        elif self.level >= 3:
            ally_player.summon_unit("Tentacule", "front", buff_atk=1)
        elif self.level >= 2:
            ally_player.summon_unit("Tentacule", "front")

class Inconnu(Avatar):
    def __init__(self, level_max):
        super().__init__(level_max)

    def activate_avatar_start_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            ally_player.draw_card(1)
        elif self.level >= 2:
            if len(ally_player.hand) < 3:
                ally_player.draw_card(1)

    def activate_avatar_on_hit(self, ally_player, ennemy_player):
        if self.level == 3:
            ally_player.puissance += 1

class Thot(Avatar):
    def __init__(self, level_max):
        super().__init__(level_max)

    def activate_avatar_start_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            ally_player.summon_unit("Squelette", "back", buff_atk=ally_player.trigger_thot, buff_pv=ally_player.trigger_thot)
        elif self.level >= 3:
            ally_player.summon_unit("Squelette", "back")
        elif self.level >= 1 and ally_player.trigger_thot > 0:
            ally_player.summon_unit("Squelette", "back")
