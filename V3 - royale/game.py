from player import Player

class Game:
    def __init__(self, deck_name_1, deck_name_2):
        self.player_1 = Player(deck_name_1)
        self.player_2 = Player(deck_name_2)
        self.turn = 1
        self.active_player = self.player_1
        self.ennemy_player = self.player_2

        def change_turn(self):
            # self.active_player.end_turn(self.ennemy_player)

            if self.active_player == self.player_1:
                self.active_player = self.player_2
                self.ennemy_player = self.player_1
            else:
                self.active_player = self.player_1
                self.ennemy_player = self.player_2
            self.turn += 1

            # self.active_player.start_turn(self.turn, self.ennemy_player)