from player import Player

class Game:
    def __init__(self, deck_name_1, deck_name_2):
        self.player_1 = Player(deck_name_1)
        self.player_2 = Player(deck_name_2)
        self.turn = 1
        self.active_player = self.player_1
        self.ennemy_player = self.player_2
        self.active_player.draw_card(2)

    def change_turn(self):
        self.active_player.end_turn(self.ennemy_player)

        if self.active_player == self.player_1:
            self.active_player = self.player_2
            self.ennemy_player = self.player_1
        else:
            self.active_player = self.player_1
            self.ennemy_player = self.player_2
        self.turn += 1

        self.active_player.start_turn(self.ennemy_player)

    def play_card_with_target(self, selected_card, target_unit):
        self.active_player.play_card(selected_card, self.ennemy_player, target_unit)

    def play_card_without_target(self, selected_card):
        self.active_player.play_card(selected_card, self.ennemy_player)

    def fight(self, off_unit, def_unit):
        if off_unit.status == "actionable":
            def_unit.take_damage(off_unit.atk)
            off_unit.take_damage(def_unit.atk)
            off_unit.status = "engagé"

    def fight_face(self, off_unit):
        if off_unit.status == "actionable":
            self.ennemy_player.take_damage(off_unit.strike)
            off_unit.status = "engagé"

    def mode_blocage(self, unit):
        if unit.status == "actionable":
            unit.status = "blocage"

    def encre_card(self, card):
        self.active_player.encre_card(card)

    def check_death(self):
        self.active_player.check_death(self.ennemy_player)
        self.ennemy_player.check_death(self.active_player)
