from card_class.card import Card
from card_class.fighter import Fighter
from card_class.structure import Structure
from card_class.spell import Spell
from card_class.trap import Trap
from card_class.enchantment import Enchantment
from card_class.equipment import Equipment
from card_class.weapon import Weapon
from card_class.artefact import Artefact
from tile import Tile
from player import Player
from parameters import HEX_RADIUS, POS_TILE
import math


class Game:
    def __init__(self, deck_name_1, deck_name_2):
        self.player_1 = Player(deck_name_1)
        self.player_2 = Player(deck_name_2)
        self.turn = 1
        self.active_player = self.player_1
        self.ennemy_player = self.player_2
        self.active_player.draw_card()
        self.active_player.refresh_mana(1)
        self.board = self.create_board()
    
    def create_board(self):
        board = []
        for row in range(-2, 3):
            for pos in range(5-abs(row)):
                board.append(Tile((row, pos), POS_TILE[0] + (abs(row)/2 + pos) * math.sqrt(3) * HEX_RADIUS, POS_TILE[1] + (row+2) * 3/2 * HEX_RADIUS))

        return board
    
    def change_turn(self):
        self.active_player.end_turn(self.ennemy_player)

        if self.active_player == self.player_1:
            self.active_player = self.player_2
            self.ennemy_player = self.player_1
        else:
            self.active_player = self.player_1
            self.ennemy_player = self.player_2
        self.turn += 1

        self.active_player.start_turn(self.turn, self.ennemy_player)

    def upgrade_tile(self, tile):
        if self.active_player.essence > 0:
            if (tile.pos[0] == -1 or tile.pos[0] == -2) and self.active_player == self.player_2:
                tile.upgrade(self.active_player)
                self.active_player.essence -= 1
            elif (tile.pos[0] == 1 or tile.pos[0] == 2) and self.active_player == self.player_1:
                tile.upgrade(self.active_player)
                self.active_player.essence -= 1

    def use_weapon(self, tile):
        self.active_player.weapon.durability -= 1
        self.active_player.weapon.actionable = False

    def play_card(self, card, tile=None):
        if isinstance(card, Fighter) and (self.get_unit(tile)[0] == None) and tile.land != "empty":
            if (tile.pos[0] == -2 and self.active_player == self.player_2) or (tile.pos[0] == 2 and self.active_player == self.player_1):
                self.active_player.play_unit(card, tile.pos, self.ennemy_player)
        elif isinstance(card, Spell):
            target = None if tile == None else self.get_unit(tile)[0]
            if card.target_type == "ennemy" and target in self.ennemy_player.board:
                self.active_player.play_spell(card, self.ennemy_player, target)
            elif card.target_type == "ally" and target in self.active_player.board:
                self.active_player.play_spell(card, self.ennemy_player, target)
            elif card.target_type == None:
                self.active_player.play_spell(card, self.ennemy_player)
        elif isinstance(card, Weapon):
            self.active_player.play_weapon(card)
        elif isinstance(card, Artefact):
            self.active_player.play_artefact(card)
            

    def action_board(self, origin_tile, target_tile):
        pass

    def get_unit(self, tile):
        for unit in self.player_2.board:
            if tile.pos == unit.pos:
                return unit, self.player_2
        for unit in self.player_1.board:
            if tile.pos == unit.pos:
                return unit, self.player_1
        return None, None

    def check_death(self):
        for card in self.active_player.board:
            if card.pv <= 0:
                if card.mort:
                    card.activate_mort(self.active_player, self.ennemy_player)
                self.active_player.discard_card(card)
        for card in self.ennemy_player.board:
            if card.pv <= 0:
                if card.mort:
                    card.activate_mort(self.ennemy_player, self.active_player)
                self.ennemy_player.discard_card(card)

        if self.active_player.weapon:
            if self.active_player.weapon.durability == 0:
                self.active_player.discard.append(self.active_player.weapon.durability)
                self.active_player.weapon = None
        if self.active_player.artefact:
            if self.active_player.artefact.durability == 0:
                self.active_player.discard.append(self.active_player.artefact.durability)
                self.active_player.artefact = None
        if self.ennemy_player.weapon:
            if self.ennemy_player.weapon.durability == 0:
                self.ennemy_player.discard.append(self.ennemy_player.weapon.durability)
                self.ennemy_player.weapon = None
        if self.ennemy_player.artefact:
            if self.ennemy_player.artefact.durability == 0:
                self.ennemy_player.discard.append(self.ennemy_player.artefact.durability)
                self.ennemy_player.artefact = None

