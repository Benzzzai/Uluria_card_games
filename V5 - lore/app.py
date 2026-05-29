
import pygame
import sys
from parameters import *
from game import Game
from cards.fighter import Fighter

class App:
    def __init__(self, deck_name_1, deck_name_2):
        self.game = Game(deck_name_1, deck_name_2)

        self.selected_card = None
        self.selected_unit = None
        self.tooltip_active = False

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Uluria TCG")
        # self.background_image = pygame.image.load("grass.png").convert()
        # self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.run = True
        self.clock = pygame.time.Clock()

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        card = self.check_card_hand_clicked(self.game.active_player, event.pos)
                        unit = self.check_unit_clicked(event.pos)
                        if self.selected_card:
                            if card == self.selected_card:
                                self.game.play_card_without_target(self.selected_card)
                            elif unit:
                                self.game.play_card_with_target(self.selected_card, unit)
                            self.selected_card = None
                        elif self.selected_unit:
                            if unit == self.selected_unit:
                                self.game.fight_face(self.selected_unit)
                            elif unit:
                                self.game.fight(self.selected_unit, unit)
                            self.selected_unit = None
                        elif card:
                            self.selected_card = card
                        elif unit:
                            if unit in self.game.active_player.board:
                                self.selected_unit = unit
                    elif event.button == 3:
                        if self.selected_unit:
                            self.game.mode_blocage(self.selected_unit)
                        elif self.selected_card:
                            self.game.encre_card(self.selected_card)
                        self.selected_card = None
                        self.selected_unit = None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.selected_card = None
                        self.selected_unit = None
                        self.game.change_turn()

            self.game.check_death()
            # self.check_end()
            self.display_app()

            pygame.display.flip()
            self.clock.tick(30)

    def check_card_hand_clicked(self, player, pos):
        pos_y = POS_Y[0] if player == self.game.player_2 else POS_Y[5]
        n = len(player.hand)
        pos_x = (SCREEN_WIDTH - n * CARD_SIZE - (n-1) * CARD_MARGIN)/2
        for i, card in enumerate(player.hand):
            card_rect = pygame.Rect(pos_x + i * (CARD_SIZE + CARD_MARGIN), pos_y, CARD_SIZE , CARD_SIZE)
            if card_rect.collidepoint(pos):
                return card
        return None
    
    def check_unit_clicked(self, pos):
        n2 = len(self.game.player_2.board)
        pos_x2 = (SCREEN_WIDTH - n2 * CARD_SIZE - (n2-1) * CARD_MARGIN)/2
        for i, unit in enumerate(self.game.player_2.board):
            unit_rect = pygame.Rect(pos_x2 + i * (CARD_SIZE + CARD_MARGIN), POS_Y[2], CARD_SIZE , CARD_SIZE)
            if unit_rect.collidepoint(pos):
                return unit
        n1 = len(self.game.player_1.board)
        pos_x1 = (SCREEN_WIDTH - n1 * CARD_SIZE - (n1-1) * CARD_MARGIN)/2
        for i, unit in enumerate(self.game.player_1.board):
            unit_rect = pygame.Rect(pos_x1 + i * (CARD_SIZE + CARD_MARGIN), POS_Y[3], CARD_SIZE , CARD_SIZE)
            if unit_rect.collidepoint(pos):
                return unit
        return None
    
    def display_app(self):
        self.screen.fill(C_BACKGROUND)

        self.display_board(self.game.player_2.board, POS_Y[2]) 
        self.display_board(self.game.player_1.board, POS_Y[3])

        self.display_player_info(self.game.player_2, POS_Y[1], C_P2, C_P2_HEALTH)
        self.display_player_info(self.game.player_1, POS_Y[4], C_P1, C_P1_HEALTH)

        self.display_hand(self.game.player_2.hand, POS_Y[0])
        self.display_hand(self.game.player_1.hand, POS_Y[5])

        pass_rect = pygame.Rect(NAME_X, POS_Y[2], 2 * INFO_HEIGHT, INFO_HEIGHT)
        color_turn = C_P1 if self.game.active_player == self.game.player_1 else C_P2
        pygame.draw.rect(self.screen, color_turn, pass_rect)
        pass_surface = FONT_STAT.render("PASSER", True, C_BLACK)
        pass_rect = pass_surface.get_rect(center=pass_rect.center)
        self.screen.blit(pass_surface, pass_rect)


    def display_hand(self, hand, pos_y):
        n = len(hand)
        pos_x = (SCREEN_WIDTH - n * CARD_SIZE - (n-1) * CARD_MARGIN)/2
        for i, card in enumerate(hand):
            card_rect = pygame.Rect(pos_x + i * (CARD_SIZE + CARD_MARGIN), pos_y, CARD_SIZE , CARD_SIZE)
            
            # SELECTED
            if card == self.selected_card:
                border_rect = card_rect.inflate(10, 10)
                pygame.draw.rect(self.screen, C_GREEN_SEL, border_rect)

            # CARD RECTANGLE
            pygame.draw.rect(self.screen, C_GREY, card_rect)

            # NAME
            name_surface = FONT_NAME.render(card.name, True, C_WHITE)
            name_rect = name_surface.get_rect(center=card_rect.center)
            self.screen.blit(name_surface, name_rect)

            # COST
            cost_box_rect = pygame.Rect(card_rect.left + 5, card_rect.top + 5, 30, 25)
            pygame.draw.rect(self.screen, C_BLUE_COST, cost_box_rect)
            if card.cost > card.cost_ori:
                color = C_RED_DMG
            elif card.cost < card.cost_ori:
                color = C_GREEN_BOOST
            else:
                color = C_BLACK
            cost_surface = FONT_COST.render(str(card.cost), True, color)
            cost_rect = cost_surface.get_rect(center=cost_box_rect.center)
            self.screen.blit(cost_surface, cost_rect)

    def display_board(self, board, pos_y):
        board_box = pygame.Rect((SCREEN_WIDTH - 7 * (CARD_SIZE + CARD_MARGIN))/2, pos_y - CARD_MARGIN/2, 7 * (CARD_SIZE + CARD_MARGIN), CARD_SIZE + CARD_MARGIN)
        pygame.draw.rect(self.screen, C_GREY_LIGHT, board_box, 2)

        n = len(board)
        pos_x = (SCREEN_WIDTH - n * CARD_SIZE - (n-1) * CARD_MARGIN)/2
        for i, unit in enumerate(board):
            unit_rect = pygame.Rect(pos_x + i * (CARD_SIZE + CARD_MARGIN), pos_y, CARD_SIZE , CARD_SIZE)
            
            # SELECTED
            if unit == self.selected_unit:
                border_rect = unit_rect.inflate(10, 10)
                pygame.draw.rect(self.screen, C_GREEN_SEL, border_rect)

            # CARD RECTANGLE
            pygame.draw.rect(self.screen, C_GREY, unit_rect)

            # NAME
            name_surface = FONT_NAME.render(unit.name, True, C_WHITE)
            if unit.status == "engagé":
                name_surface = pygame.transform.rotate(name_surface, -90)
            elif unit.status == "blocage":
                name_surface = pygame.transform.rotate(name_surface, 90)
            name_rect = name_surface.get_rect(center=unit_rect.center)
            self.screen.blit(name_surface, name_rect)

            # ATK
            if unit.status == "engagé":
                atk_box_rect = pygame.Rect(unit_rect.left + 5, unit_rect.top + 5, 25, 25)
            elif unit.status == "blocage":
                atk_box_rect = pygame.Rect(unit_rect.right - 30, unit_rect.bottom - 30, 25, 25)
            else:
                atk_box_rect = pygame.Rect(unit_rect.left + 5, unit_rect.bottom - 30, 25, 25)
            pygame.draw.rect(self.screen, C_YELLOW_ATK, atk_box_rect)
            if unit.atk > unit.atk_ori:
                color = C_GREEN_BOOST
            else:
                color = C_BLACK
            atk_surface = FONT_STAT.render(str(unit.atk), True, color)
            atk_rect = atk_surface.get_rect(center=atk_box_rect.center)
            self.screen.blit(atk_surface, atk_rect)

            # STRIKE
            if unit.status == "engagé":
                strike_box_rect = pygame.Rect(unit_rect.left + 5, unit_rect.top + 40, 20, 20)
            elif unit.status == "blocage":
                strike_box_rect = pygame.Rect(unit_rect.right - 25, unit_rect.top + 40, 20, 20)
            else:
                strike_box_rect = pygame.Rect(unit_rect.left + 40, unit_rect.bottom - 25, 20, 20)
            pygame.draw.rect(self.screen, C_BLACK, strike_box_rect)
            strike_surface = FONT_STAT.render(str(unit.strike), True, C_WHITE)
            strike_rect = strike_surface.get_rect(center=strike_box_rect.center)
            self.screen.blit(strike_surface, strike_rect)

            # PV
            if unit.status == "engagé":
                pv_box_rect = pygame.Rect(unit_rect.left + 5, unit_rect.bottom - 30, 25, 25)
            elif unit.status == "blocage":
                pv_box_rect = pygame.Rect(unit_rect.right - 30, unit_rect.top + 5, 25, 25)
            else:
                pv_box_rect = pygame.Rect(unit_rect.right - 30, unit_rect.bottom - 30, 25, 25)

            pygame.draw.rect(self.screen, C_RED_PV, pv_box_rect)
            if unit.bouclier:
                color = C_YELLOW_ATK
            elif unit.pv < unit.pv_max:
                color = C_RED_DMG
            elif unit.pv > unit.pv_ori:
                color = C_GREEN_BOOST
            else:
                color = C_BLACK
            pv_surface = FONT_STAT.render(str(unit.pv), True, color)
            pv_rect = pv_surface.get_rect(center=pv_box_rect.center)
            self.screen.blit(pv_surface, pv_rect)

    def display_player_info(self, player, pos_y, color_p, color_health):
        # NAME
        n_rect = pygame.Rect(NAME_X, pos_y, 5 * INFO_HEIGHT, INFO_HEIGHT)
        pygame.draw.rect(self.screen, color_p, n_rect)
        n_surface = FONT_COST.render(str(player.name) + " (" + str(len(player.deck)) + ")", True, C_BLACK)
        n_rect = n_surface.get_rect(center=n_rect.center)
        self.screen.blit(n_surface, n_rect)

        # TRAP
        for i in range(3):
            tr_rect = pygame.Rect(TRAP_X + i * 1.5 * INFO_HEIGHT, pos_y, INFO_HEIGHT, INFO_HEIGHT)
            pygame.draw.rect(self.screen, color_p, tr_rect)

        # HEALTH
        health_center = (SCREEN_WIDTH/2, pos_y + INFO_HEIGHT/2)

        pygame.draw.circle(self.screen, color_health, health_center, INFO_HEIGHT)
        pygame.draw.circle(self.screen, color_p, health_center, INFO_HEIGHT, width=3)
        h_surface = FONT_BIG.render(str(player.health), True, C_BLACK)
        h_rect = h_surface.get_rect(center=health_center)
        self.screen.blit(h_surface, h_rect)

        if player.armor > 0:
            ar_rect = pygame.Rect(health_center[0] + 20, health_center[1] + 20, INFO_HEIGHT - 20, INFO_HEIGHT - 20)
            pygame.draw.rect(self.screen, C_BORDER, ar_rect)
            ar_surface = FONT_STAT.render(str(player.armor), True, C_WHITE)
            ar_rect = ar_surface.get_rect(center=ar_rect.center)
            self.screen.blit(ar_surface, ar_rect)
        
        # ARTIFACT
        arti_rect = pygame.Rect(ARTIFACT_X, pos_y, INFO_HEIGHT, INFO_HEIGHT)
        pygame.draw.rect(self.screen, color_p, arti_rect)

        # ENCHANTMENT
        ench_rect = pygame.Rect(ARTIFACT_X + 2 * INFO_HEIGHT, pos_y, INFO_HEIGHT, INFO_HEIGHT)
        pygame.draw.rect(self.screen, color_p, ench_rect)
            
        # MANA
        mana_box = pygame.Rect(MANA_X, pos_y + MANA_RAD/2, 31 * MANA_RAD, 4 * MANA_RAD)
        pygame.draw.rect(self.screen, C_GREY_LIGHT, mana_box)

        for i in range(player.mana_max):
            circle_x = 2 * MANA_RAD + MANA_X + i * (2.5 * MANA_RAD)
            circle_y = 2.5 * MANA_RAD + pos_y

            if i < player.mana:
                pygame.draw.circle(self.screen, C_BLUE_MANA, (circle_x, circle_y), MANA_RAD)
            else:
                pygame.draw.circle(self.screen, C_GREY, (circle_x, circle_y), MANA_RAD, 2)
        
        tot_box = pygame.Rect(MANA_X + 26 * MANA_RAD, pos_y + MANA_RAD/2, 5 * MANA_RAD, 4 * MANA_RAD)
        tot_surface = FONT_STAT.render(str(player.mana) + "/" + str(player.mana_max), True, C_BLUE_MANA)
        tot_rect = tot_surface.get_rect(center=tot_box.center)
        self.screen.blit(tot_surface, tot_rect)


app = App("Ocre soin", "Zéphyr Midrange")