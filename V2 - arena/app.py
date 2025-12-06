import pygame
import math
from game import Game
from parameters import *
from card_class.unit import Unit
from card_class.fighter import Fighter
from card_class.structure import Structure
from card_class.spell import Spell
from card_class.trap import Trap
from card_class.enchantment import Enchantment
from card_class.glyph import Glyph
from card_class.equipment import Equipment
from card_class.weapon import Weapon

class App:
    def __init__(self, deck_name_1, deck_name_2):
        self.game = Game(deck_name_1, deck_name_2)

        self.selected_essence = False
        self.selected_weapon = False
        self.selected_card = None
        self.selected_tile = None

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Hexagonal Game Board")
        self.clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        button = self.check_button_clicked(event.pos)
                        card = self.check_card_hand_clicked(self.game.active_player, event.pos)
                        tile = self.check_tile_clicked(event.pos)
                        if self.selected_essence:
                            if tile:
                                self.game.upgrade_tile(tile)
                            self.selected_essence = False
                        elif self.selected_weapon:
                            if tile:
                                self.game.use_weapon(tile)
                            self.selected_weapon = False
                        elif self.selected_card:
                            if card == self.selected_card:
                                self.game.play_card(card)
                            elif tile:
                                self.game.play_card(self.selected_card, tile)
                            self.selected_card = None
                        elif self.selected_tile:
                            if tile:
                                self.game.action_board(self.selected_tile, tile)
                            self.selected_tile = None
                        else:
                            if button == "mana":
                                self.game.active_player.gain_mana(1)
                                self.game.active_player.essence -= 1
                            elif button == "draw":
                                self.game.active_player.draw_card(1)
                                self.game.active_player.essence -= 1
                            elif button == "land":
                                self.selected_essence = True
                            elif button == "weapon":
                                self.selected_weapon = True
                            elif card:
                                self.selected_card = card
                            elif tile:
                                self.selected_tile = tile
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.selected_essence = False
                        self.selected_weapon = False
                        self.selected_card = None
                        self.selected_tile = None
                        self.game.change_turn()

            self.game.check_death()          
            self.display_app()
            pygame.display.flip()
            self.clock.tick(30)

    def check_button_clicked(self, pos):
        y_button = ESS_Y[0] if self.game.active_player == self.game.player_2 else ESS_Y[1]
        y_weapon = (HEALTH_2_CENTER[1] - 2 * HEALTH_RAD - 30) if self.game.active_player == self.game.player_2 else (HEALTH_1_CENTER[1] + HEALTH_RAD + 30)
        if pygame.Rect(MANA_X + 10, y_button + 10, BUTTON_SIZE, BUTTON_SIZE).collidepoint(pos) and self.game.active_player.essence > 0:
            return "land"
        elif pygame.Rect(MANA_X + BUTTON_SIZE + 20, y_button + 10, BUTTON_SIZE, BUTTON_SIZE).collidepoint(pos) and self.game.active_player.essence > 0:
            return "mana"
        elif pygame.Rect(MANA_X + 2 * BUTTON_SIZE + 30, y_button + 10, BUTTON_SIZE, BUTTON_SIZE).collidepoint(pos) and self.game.active_player.essence > 0:
            return "draw"
        elif pygame.Rect(HEALTH_2_CENTER[0] + 2.4 * HEALTH_RAD, y_weapon, HEALTH_RAD, HEALTH_RAD).collidepoint(pos) and self.game.active_player.weapon:
            if self.game.active_player.weapon.actionable:
                return "weapon"
        else:
            return None
    
    def check_card_hand_clicked(self, player, pos):
        n = len(player.hand)
        pos_x = (SCREEN_WIDTH - n * CARD_SIZE - (n-1) * CARD_MARGIN)/2
        for i in range(n):
            if pygame.Rect(pos_x + i * (CARD_SIZE + CARD_MARGIN), POS_HAND[0] if player == self.game.player_2 else POS_HAND[1], CARD_SIZE, CARD_SIZE).collidepoint(pos):
                return player.hand[i]
        return None
    
    def check_tile_clicked(self, pos):
        tile_clicked = None
        for tile in self.game.board:
            if math.sqrt((pos[0] - tile.center[0]) ** 2 + (pos[1] - tile.center[1]) ** 2) < HEX_RADIUS:
                tile_clicked = tile
        return tile_clicked

    def find_card_by_pos(self, rows, pos):
        for row in rows:
            for card in row:
                if card.rectangle.collidepoint(pos):
                    return card, row
        return None, None
    
    def display_app(self):
        self.screen.fill(C_BACKGROUND)
        self.display_left_info()
        self.display_board()
        self.display_hand(self.game.player_2, POS_HAND[0])
        self.display_hand(self.game.player_1, POS_HAND[1])
        self.display_mana_bar(self.game.player_2, MANA_X, MANA_Y[0])
        self.display_mana_bar(self.game.player_1, MANA_X, MANA_Y[1])
        self.display_right_info(self.game.player_2, MANA_X, ESS_Y[0])
        self.display_right_info(self.game.player_1, MANA_X, ESS_Y[1])
        
    def display_hand(self, player, pos_y):
        n = len(player.hand)
        pos_x = (SCREEN_WIDTH - n * CARD_SIZE - (n-1) * CARD_MARGIN)/2
        for i, card in enumerate(player.hand):
            rectangle = pygame.Rect(pos_x + i * (CARD_SIZE + CARD_MARGIN), pos_y, CARD_SIZE, CARD_SIZE)

            # SELECTED
            if card == self.selected_card:
                border_rect = rectangle.inflate(10, 10)
                pygame.draw.rect(self.screen, C_GREEN_SEL, border_rect)

            # CARD RECTANGLE
            if isinstance(card, Unit):
                color_rect = C_UNIT
            elif isinstance(card, Spell):
                color_rect = C_SPELL
            elif isinstance(card, Enchantment):
                color_rect = C_ENCHANTMENT
            elif isinstance(card, Equipment):
                color_rect = C_EQUIPMENT
            else:
                color_rect = C_GREY_LIGHT
            pygame.draw.rect(self.screen, color_rect, rectangle)

            # NAME
            name_surface = FONT_NAME.render(card.name, True, C_WHITE)
            name_rect = name_surface.get_rect(center=rectangle.center)
            self.screen.blit(name_surface, name_rect)

            # MANA
            cost_box_rect = pygame.Rect(rectangle.left + 5, rectangle.top + 5, 30, 25)
            pygame.draw.rect(self.screen, C_BLUE_COST, cost_box_rect)
            if card.cost < card.cost_ori:
                color = C_GREEN_COST
            elif card.cost > card.cost_ori:
                color = C_RED_DMG
            else:
                color = C_BLACK
            cost_surface = FONT_STAT.render(str(card.cost), True, color)
            cost_rect = cost_surface.get_rect(center=cost_box_rect.center)
            self.screen.blit(cost_surface, cost_rect)

            # ATK
            if isinstance(card, Fighter) or isinstance(card, Weapon):
                atk_box_rect = pygame.Rect(rectangle.left + 5, rectangle.bottom - 30, 30, 25)
                pygame.draw.rect(self.screen, C_YELLOW_ATK, atk_box_rect)
                atk_surface = FONT_STAT.render(str(card.atk), True, C_BLACK)
                atk_rect = atk_surface.get_rect(center=atk_box_rect.center)
                self.screen.blit(atk_surface, atk_rect)

            # PV
            if isinstance(card, Unit):
                pv_box_rect = pygame.Rect(rectangle.right - 35, rectangle.bottom - 30, 30, 25)
                pygame.draw.rect(self.screen, C_RED_PV, pv_box_rect)
                pv_surface = FONT_STAT.render(str(card.pv), True, C_BLACK)
                pv_rect = pv_surface.get_rect(center=pv_box_rect.center)
                self.screen.blit(pv_surface, pv_rect)
            elif isinstance(card, Glyph) or isinstance(card, Equipment):
                pv_box_rect = pygame.Rect(rectangle.right - 35, rectangle.bottom - 30, 30, 25)
                pygame.draw.rect(self.screen, C_GREY_LIGHT, pv_box_rect)
                pv_surface = FONT_STAT.render(str(card.durability), True, C_BLACK)
                pv_rect = pv_surface.get_rect(center=pv_box_rect.center)
                self.screen.blit(pv_surface, pv_rect)
            

    def display_board(self):
        for tile in self.game.board:
            pygame.draw.polygon(self.screen, color_tile[tile.land], tile.corners)
            pygame.draw.polygon(self.screen, C_BLACK, tile.corners, 2)
            unit, player = self.game.get_unit(tile)
            if unit:
                rectangle = pygame.Rect(tile.center[0] - HEX_RADIUS/2, tile.center[1] - HEX_RADIUS/2, HEX_RADIUS, HEX_RADIUS)

                # ACTIONABLE
                if unit.actionable and player == self.game.active_player:
                    border_rect = rectangle.inflate(8, 8)
                    pygame.draw.rect(self.screen, C_GREY_LIGHT, border_rect)

                # SELECTED
                if tile == self.selected_tile:
                    border_rect = rectangle.inflate(8, 8)
                    pygame.draw.rect(self.screen, C_GREEN_SEL, border_rect)

                # CARD RECTANGLE
                pygame.draw.rect(self.screen, C_UNIT, rectangle) # pe utiliser la couleur des joueurs pour bien voir qu'est ce qui est à qui
                
                # ATK
                if isinstance(unit, Fighter):
                    atk_box_rect = pygame.Rect(rectangle.left, rectangle.bottom - 25, 25, 25)
                    pygame.draw.rect(self.screen, C_YELLOW_ATK, atk_box_rect)
                    atk_surface = FONT_STAT.render(str(unit.atk), True, C_BLACK)
                    atk_rect = atk_surface.get_rect(center=atk_box_rect.center)
                    self.screen.blit(atk_surface, atk_rect)

                # PV
                pv_box_rect = pygame.Rect(rectangle.right - 25, rectangle.bottom - 25, 25, 25)
                pygame.draw.rect(self.screen, C_RED_PV, pv_box_rect)
                pv_surface = FONT_STAT.render(str(unit.pv), True, C_BLACK)
                pv_rect = pv_surface.get_rect(center=pv_box_rect.center)
                self.screen.blit(pv_surface, pv_rect)

                # CARD BORDER
                pygame.draw.rect(self.screen, C_BLACK, rectangle, 1)


    def display_left_info(self):
        pygame.draw.circle(self.screen, C_P2_HEALTH, HEALTH_2_CENTER, HEALTH_RAD)
        pygame.draw.circle(self.screen, C_P2, HEALTH_2_CENTER, HEALTH_RAD, width=3)
        color = C_GREY_LIGHT if self.game.player_2.health == 0 else C_BLACK
        h2_surface = FONT_BIG.render(str(self.game.player_2.health), True, color)
        h2_rect = h2_surface.get_rect(center=HEALTH_2_CENTER)
        self.screen.blit(h2_surface, h2_rect)

        if self.game.player_2.armor > 0:
            armor_rect = pygame.Rect(HEALTH_2_CENTER[0] + 20, HEALTH_2_CENTER[1] + 20, HEALTH_RAD - 20, HEALTH_RAD - 20)
            pygame.draw.rect(self.screen, C_BLACK, armor_rect)
            ar_surface = FONT_STAT.render(str(self.game.player_2.armor), True, C_WHITE)
            ar_rect = ar_surface.get_rect(center=armor_rect.center)
            self.screen.blit(ar_surface, ar_rect)
        
        pygame.draw.circle(self.screen, C_P1_HEALTH, HEALTH_1_CENTER, HEALTH_RAD)
        pygame.draw.circle(self.screen, C_P1, HEALTH_1_CENTER, HEALTH_RAD, width=3)
        color = C_GREY_LIGHT if self.game.player_1.health == 0 else C_BLACK
        h1_surface = FONT_BIG.render(str(self.game.player_1.health), True, color)
        h1_rect = h1_surface.get_rect(center=HEALTH_1_CENTER)
        self.screen.blit(h1_surface, h1_rect)

        if self.game.player_1.armor > 0:
            armor_rect = pygame.Rect(HEALTH_1_CENTER[0] + 20, HEALTH_1_CENTER[1] + 20, HEALTH_RAD - 20, HEALTH_RAD - 20)
            pygame.draw.rect(self.screen, C_BLACK, armor_rect)
            ar_surface = FONT_STAT.render(str(self.game.player_1.armor), True, C_WHITE)
            ar_rect = ar_surface.get_rect(center=armor_rect.center)
            self.screen.blit(ar_surface, ar_rect)

        turn_rect = pygame.Rect(HEALTH_1_CENTER[0] - 2 * HEALTH_RAD, TURN_Y, 2 * HEALTH_RAD, HEALTH_RAD + 5)
        turn_surface = FONT_STAT.render("tour " + str(self.game.turn), True, C_BLACK)
        turn_rect = turn_surface.get_rect(center=turn_rect.center)
        self.screen.blit(turn_surface, turn_rect)

        pass_rect = pygame.Rect(HEALTH_1_CENTER[0], TURN_Y, 2 * HEALTH_RAD, HEALTH_RAD + 5)
        color_turn = C_P1 if self.game.active_player == self.game.player_1 else C_P2
        pygame.draw.rect(self.screen, color_turn, pass_rect)
        pass_surface = FONT_STAT.render("PASSER", True, C_BLACK)
        pass_rect = pass_surface.get_rect(center=pass_rect.center)
        self.screen.blit(pass_surface, pass_rect)

        p2_rect = pygame.Rect(HEALTH_2_CENTER[0] - 2 * HEALTH_RAD, HEALTH_2_CENTER[1] - 2 * HEALTH_RAD - 30, 4 * HEALTH_RAD, HEALTH_RAD)
        pygame.draw.rect(self.screen, C_P2, p2_rect)
        p2_surface = FONT_STAT.render(str(self.game.player_2.name), True, C_BLACK)
        p2_rect = p2_surface.get_rect(center=p2_rect.center)
        self.screen.blit(p2_surface, p2_rect)

        p1_rect = pygame.Rect(HEALTH_1_CENTER[0] - 2 * HEALTH_RAD, HEALTH_1_CENTER[1] + HEALTH_RAD + 30, 4 * HEALTH_RAD, HEALTH_RAD)
        pygame.draw.rect(self.screen, C_P1, p1_rect)
        p1_surface = FONT_STAT.render(str(self.game.player_1.name), True, C_BLACK)
        p1_rect = p1_surface.get_rect(center=p1_rect.center)
        self.screen.blit(p1_surface, p1_rect)

        weapon_2 = pygame.Rect(HEALTH_2_CENTER[0] + 2.4 * HEALTH_RAD, HEALTH_2_CENTER[1] - 2 * HEALTH_RAD - 30, HEALTH_RAD, HEALTH_RAD)
        if self.game.player_2.weapon:
            weapon_color = C_GREEN_BOOST if (self.selected_weapon and self.game.active_player == self.game.player_2) else C_GREY_LIGHT
            pygame.draw.rect(self.screen, weapon_color, weapon_2)
            wea_surface = FONT_STAT.render(str(self.game.player_2.weapon.durability), True, C_BLACK)
            wea_rect = wea_surface.get_rect(center=weapon_2.center)
            self.screen.blit(wea_surface, wea_rect)
        else:
            pygame.draw.rect(self.screen, C_GREY_LIGHT, weapon_2, width=3)

        artefact_2 = pygame.Rect(HEALTH_2_CENTER[0] + 3.8 * HEALTH_RAD, HEALTH_2_CENTER[1] - 2 * HEALTH_RAD - 30, HEALTH_RAD, HEALTH_RAD)
        if self.game.player_2.artefact:
            pygame.draw.rect(self.screen, C_GREY_LIGHT, artefact_2)
            art_surface = FONT_STAT.render(str(self.game.player_2.artefact.durability), True, C_BLACK)
            art_rect = art_surface.get_rect(center=artefact_2.center)
            self.screen.blit(art_surface, art_rect)
        else:
            pygame.draw.rect(self.screen, C_GREY_LIGHT, artefact_2, width=3)

        weapon_1 = pygame.Rect(HEALTH_1_CENTER[0] + 2.4 * HEALTH_RAD, HEALTH_1_CENTER[1] + HEALTH_RAD + 30, HEALTH_RAD, HEALTH_RAD)
        if self.game.player_1.weapon:
            weapon_color = C_GREEN_BOOST if (self.selected_weapon and self.game.active_player == self.game.player_1) else C_GREY_LIGHT
            pygame.draw.rect(self.screen, weapon_color, weapon_1)
            wea_surface = FONT_STAT.render(str(self.game.player_1.weapon.durability), True, C_BLACK)
            wea_rect = wea_surface.get_rect(center=weapon_1.center)
            self.screen.blit(wea_surface, wea_rect)
        else:
            pygame.draw.rect(self.screen, C_GREY_LIGHT, weapon_1, width=3)

        artefact_1 = pygame.Rect(HEALTH_1_CENTER[0] + 3.8 * HEALTH_RAD, HEALTH_1_CENTER[1] + HEALTH_RAD + 30, HEALTH_RAD, HEALTH_RAD)
        if self.game.player_1.artefact:
            pygame.draw.rect(self.screen, C_GREY_LIGHT, artefact_1)
            art_surface = FONT_STAT.render(str(self.game.player_1.artefact.durability), True, C_BLACK)
            art_rect = art_surface.get_rect(center=artefact_1.center)
            self.screen.blit(art_surface, art_rect)
        else:
            pygame.draw.rect(self.screen, C_GREY_LIGHT, artefact_1, width=3)

        

    def display_mana_bar(self, player, bar_x, bar_y):
        mana_box = pygame.Rect(bar_x, bar_y, 26.5 * MANA_RAD, 4 * MANA_RAD)
        pygame.draw.rect(self.screen, C_GREY_LIGHT, mana_box)

        for i in range(10):
            circle_x = 2 * MANA_RAD + bar_x + i * (2.5 * MANA_RAD)
            circle_y = 2 * MANA_RAD + bar_y

            if i < player.basic_mana:
                pygame.draw.circle(self.screen, C_BLUE_MANA, (circle_x, circle_y), MANA_RAD)
            elif i < (player.basic_mana + player.extra_mana):
                pygame.draw.circle(self.screen, C_BLUE_COST, (circle_x, circle_y), MANA_RAD)
            else:
                pygame.draw.circle(self.screen, C_BLACK, (circle_x, circle_y), MANA_RAD, 2)

    def display_right_info(self, player, pos_x, pos_y):
        corner = pygame.Rect(pos_x, pos_y, 3 * BUTTON_SIZE + 40, BUTTON_SIZE + 20)
        pygame.draw.rect(self.screen, C_BLACK, corner, 2)

        essence_button = pygame.Rect(pos_x + 10, pos_y + 10, BUTTON_SIZE, BUTTON_SIZE)
        button_color = C_GREEN_BOOST if (self.selected_essence and player == self.game.active_player) else C_GREY_LIGHT
        pygame.draw.rect(self.screen, button_color, essence_button)
        ess_surface = FONT_STAT.render(str(player.essence), True, C_BLACK)
        ess_rect = ess_surface.get_rect(center=essence_button.center)
        self.screen.blit(ess_surface, ess_rect)

        b1 = pygame.Rect(pos_x + BUTTON_SIZE + 20, pos_y + 10, BUTTON_SIZE, BUTTON_SIZE)
        pygame.draw.rect(self.screen, C_GREY_LIGHT, b1)

        b2 = pygame.Rect(pos_x + 2 * BUTTON_SIZE + 30, pos_y + 10, BUTTON_SIZE, BUTTON_SIZE)
        pygame.draw.rect(self.screen, C_GREY_LIGHT, b2)

        deck_box = pygame.Rect(pos_x + 5 * BUTTON_SIZE, pos_y, BUTTON_SIZE + 20, BUTTON_SIZE + 20)
        deck_color = C_P1 if player == self.game.player_1 else C_P2
        pygame.draw.rect(self.screen, deck_color, deck_box)
        deck_surface = FONT_STAT.render(str(len(player.deck)), True, C_BLACK)
        deck_rect = deck_surface.get_rect(center=deck_box.center)
        self.screen.blit(deck_surface, deck_rect)


app = App("deck 1", "deck 2")