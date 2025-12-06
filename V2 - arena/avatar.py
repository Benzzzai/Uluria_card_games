import random

class Avatar():
    def __init__(self):
        self.level = 0

    @staticmethod
    def create_avatar(name):
        avatar_classes = {
            "Marduk": Marduk,
            "Enlil": Enlil,
            "Enki": Enki,
            "Ishtar": Ishtar,
            "Alchimiste": Alchimiste,
            "Kraken": Kraken,
            "Inconnu": Inconnu,
            "Thot": Thot
        }
        
        return avatar_classes[name]()

    def activate_avatar_on_hit(self, ally_player, ennemy_player):
        pass

    def activate_avatar_start_turn(self, ally_player, ennemy_player):
        pass

    def activate_avatar_end_turn(self, ally_player, ennemy_player):
        pass


class Marduk(Avatar):
    def __init__(self):
        super().__init__()

    def activate_avatar_start_turn(self, ally_player, ennemy_player):
        if self.level >= 5:
            ennemy_player.take_damage(2)
        elif self.level >= 3:
            ennemy_player.take_damage(1)

class Enlil(Avatar):
    def __init__(self):
        super().__init__()

    def activate_avatar_end_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            for card in ally_player.board:
                card.heal(1)
            ally_player.heal(2)
        elif self.level >= 3:
            for card in ally_player.board:
                card.heal(1)
        elif self.level >= 2:
            target = random.choice(ally_player.board)
            target.heal(1)

class Enki(Avatar):
    def __init__(self):
        super().__init__()

    def activate_avatar_start_turn(self, ally_player, ennemy_player):
        if self.level >= 5:
            ally_player.gain_armor(3)
        elif self.level >= 3:
            ally_player.gain_armor(1)

class Ishtar(Avatar):
    def __init__(self):
        super().__init__()

    def activate_avatar_on_hit(self, ally_player, ennemy_player):
        pass # carac heros actif

    def activate_avatar_end_turn(self, ally_player, ennemy_player):
        pass

class Alchimiste(Avatar):
    def __init__(self):
        super().__init__()

    def activate_avatar_on_hit(self, ally_player, ennemy_player):
        if self.level == 4:
            ally_player.max_mana = 8
        elif self.level == 2:
            pass # graine actif

class Kraken(Avatar):
    def __init__(self):
        super().__init__()

    def activate_avatar_start_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            for card in ally_player.board:
                if card.name == "Tentacule":
                    card.buff(1, 1)
            # ally_player.summon_unit("Tentacule", "front")
        elif self.level >= 3:
            pass
            # ally_player.summon_unit("Tentacule", "front") # refaire cette fonction avec la case précise

class Inconnu(Avatar):
    def __init__(self):
        super().__init__()

    def activate_avatar_start_turn(self, ally_player, ennemy_player):
        if self.level >= 4:
            ally_player.draw_card(1)
        elif self.level >= 3:
            if len(ally_player.hand) < 3:
                ally_player.draw_card(1)

class Thot(Avatar):
    def __init__(self):
        super().__init__()

    def activate_avatar_start_turn(self, ally_player, ennemy_player):
        pass
        # pareil faire des attribut d'avatar et la fonction summon
        """ 
        if self.level >= 3 and ally_player.trigger_thot:
            ally_player.summon_unit("Squelette d'élite", "back")
        elif self.level >= 1:
            ally_player.summon_unit("Squelette", "back")
        """