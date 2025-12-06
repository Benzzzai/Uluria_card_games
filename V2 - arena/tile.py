import math
from parameters import HEX_RADIUS

class Tile:
    def __init__(self, pos, x, y):
        self.pos = pos
        self.center = (x, y)
        self.corners = [self.hex_corner(self.center, i) for i in range(6)]
        self.land = "center" if pos[0] == 0 else "empty"

        self.graine = False
        self.os = False

    def hex_corner(self, center, i):
        angle = math.radians(60 * i + 30)
        x = center[0] + HEX_RADIUS * math.cos(angle)
        y = center[1] + HEX_RADIUS * math.sin(angle)
        return (x, y)
    
    def upgrade(self, player):
        if self.land == "empty":
            self.land = "basic"
        elif self.land == "basic":
            self.land = "upgraded"
            player.avatar.level += 1

    def is_free(self, game):
        for unit in game.player_1:
            if unit.pos == (self.row, self.pos):
                return False
        for unit in game.player_2:
            if unit.pos == (self.row, self.pos):
                return False
        return True
