import pygame
import sys
from parameters import *
from game import Game

from card_class.fighter import Fighter
from card_class.structure import Structure
from card_class.unit import Unit
from card_class.spell import Spell
from card_class.ritual import Ritual

class App:
    def __init__(self, deck_name_1, deck_name_2):
        self.game = Game(deck_name_1, deck_name_2)

        self.selected_card = None
        self.tooltip_active = False

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Runeterra TCG")
        self.background_image = pygame.image.load("grass.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.start_menu = True
        self.run = False
        self.end_menu = False
        self.clock = pygame.time.Clock()

        while self.start_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.start_menu = False
                        self.run = True
            self.display_start_menu()
            pygame.display.flip()
            self.clock.tick(30)

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        card, row = self.find_card_by_pos([self.game.player_2.hand, self.game.player_2.backrow, self.game.player_2.frontrow,
                                                           self.game.player_1.hand, self.game.player_1.backrow, self.game.player_1.frontrow], event.pos)
                        if card:
                            if self.selected_card:
                                if self.selected_card == card:
                                    self.game.move_without_target(self.selected_card)
                                else:
                                    self.game.move_with_target(self.selected_card, card)
                                self.selected_card = None
                            else:
                                self.selected_card = card                 
                        else:
                            self.selected_card = None
                    elif event.button == 3:
                        if self.selected_card:
                            self.game.offering(self.selected_card)
                            self.selected_card = None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.selected_card = None
                        self.game.change_turn()
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN:
                        if self.selected_card:
                            self.game.move_back(self.selected_card)
                            self.selected_card = None
                    elif event.key == pygame.K_z:
                        self.tooltip_active = not self.tooltip_active

            self.game.check_death()
            self.check_end()
            self.display_app()
            if self.tooltip_active:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.display_tooltip(mouse_x, mouse_y)

            pygame.display.flip()
            self.clock.tick(30)

        while self.end_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.display_end_menu()
            pygame.display.flip()
            self.clock.tick(30)


    def check_end(self):
        if self.game.check_end():
            self.run = False
            self.end_menu = True

    def find_card_by_pos(self, rows, pos):
        for row in rows:
            for card in row:
                if card.rectangle.collidepoint(pos):
                    return card, row
        return None, None

    def center_cards(self, row, y_position):
        total_width = len(row) * CARD_SIZE + (len(row) - 1) * CARD_MARGIN
        start_x = (SCREEN_WIDTH - total_width) // 2

        for i, card in enumerate(row):
            card.rectangle.x = start_x + i * (CARD_SIZE + CARD_MARGIN)
            card.rectangle.y = y_position


    def display_cards(self, row):
        for card in row:
            # ACTIONABLE
            if row == self.game.active_player.backrow or row == self.game.active_player.frontrow:
                if card.actionable:
                    border_rect = card.rectangle.inflate(10, 10)
                    pygame.draw.rect(self.screen, C_GREY_LIGHT, border_rect)

            # PARA
            if row == self.game.active_player.backrow or row == self.game.active_player.frontrow or row == self.game.ennemy_player.backrow or row == self.game.ennemy_player.frontrow:
                if card.paralyse:
                    border_rect = card.rectangle.inflate(10, 10)
                    pygame.draw.rect(self.screen, C_BLUE_COST, border_rect)

            # SELECTED
            if card == self.selected_card:
                border_rect = card.rectangle.inflate(10, 10)
                pygame.draw.rect(self.screen, C_GREEN_SEL, border_rect)

            # CARD RECTANGLE
            pygame.draw.rect(self.screen, C_CLASSES[card.classe], card.rectangle)

            # NAME
            color_name = C_YELLOW_ATK if card.legendary else C_WHITE
            name_surface = FONT_NAME.render(card.name, True, color_name)
            name_rect = name_surface.get_rect(center=card.rectangle.center)
            self.screen.blit(name_surface, name_rect)

            # MANA
            cost_box_rect = pygame.Rect(card.rectangle.left + 5, card.rectangle.top + 5, 30, 25)
            color = C_RED_PV if isinstance(card, Ritual) else C_BLUE_COST
            pygame.draw.rect(self.screen, color, cost_box_rect)
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
            if isinstance(card, Fighter):
                atk_box_rect = pygame.Rect(card.rectangle.left + 5, card.rectangle.bottom - 30, 30, 25)
                pygame.draw.rect(self.screen, C_YELLOW_ATK, atk_box_rect)
                if card.atk > card.atk_ori:
                    color = C_GREEN_BOOST
                else:
                    color = C_BLACK
                atk_surface = FONT_STAT.render(str(card.atk), True, color)
                atk_rect = atk_surface.get_rect(center=atk_box_rect.center)
                self.screen.blit(atk_surface, atk_rect)

            # PV
            if isinstance(card, Unit):
                pv_box_rect = pygame.Rect(card.rectangle.right - 35, card.rectangle.bottom - 30, 30, 25)
                pygame.draw.rect(self.screen, C_RED_PV, pv_box_rect)
                if card.bouclier:
                    color = C_YELLOW_ATK
                elif card.pv < card.pv_max:
                    color = C_RED_DMG
                elif card.pv > card.pv_ori:
                    color = C_GREEN_BOOST
                else:
                    color = C_BLACK
                pv_surface = FONT_STAT.render(str(card.pv), True, color)
                pv_rect = pv_surface.get_rect(center=pv_box_rect.center)
                self.screen.blit(pv_surface, pv_rect)


    def zoom_card(self, card, player):
        offset = - 1.2 * CARD_SIZE if player == 1 else 0
        big_rect = pygame.Rect(card.rectangle.x - 0.25 * CARD_SIZE, card.rectangle.y + offset, 1.5 * CARD_SIZE, 2.2 * CARD_SIZE)

        # ACTIONABLE
        if card in self.game.active_player.backrow or card in self.game.active_player.frontrow:
            if card.actionable:
                border_rect = big_rect.inflate(10, 10)
                pygame.draw.rect(self.screen, C_GREY_LIGHT, border_rect)

        # PARA
        if card in self.game.active_player.backrow or card in self.game.active_player.frontrow or card in self.game.ennemy_player.backrow or card in self.game.ennemy_player.frontrow:
            if card.paralyse:
                border_rect = big_rect.inflate(10, 10)
                pygame.draw.rect(self.screen, C_BLUE_COST, border_rect)

        # SELECTED
        if card == self.selected_card:
            border_rect = big_rect.inflate(10, 10)
            pygame.draw.rect(self.screen, C_GREEN_SEL, border_rect)

        # CARD RECTANGLE
        pygame.draw.rect(self.screen, C_CLASSES[card.classe], big_rect)
        pygame.draw.rect(self.screen, C_BLACK, big_rect, width=1)

        # NAME
        name_box = pygame.Rect(big_rect.left + 40, big_rect.top + 5, 105, 25)
        color_name = C_YELLOW_ATK if card.legendary else C_WHITE
        name_surface = FONT_NAME.render(card.name, True, color_name)
        name_rect = name_surface.get_rect(center=name_box.center)
        self.screen.blit(name_surface, name_rect)

        # MANA
        cost_box_rect = pygame.Rect(big_rect.left + 5, big_rect.top + 5, 30, 25)
        color = C_RED_PV if isinstance(card, Ritual) else C_BLUE_COST
        pygame.draw.rect(self.screen, color, cost_box_rect)
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
        if isinstance(card, Fighter):
            atk_box_rect = pygame.Rect(big_rect.left + 5, big_rect.bottom - 30, 30, 25)
            pygame.draw.rect(self.screen, C_YELLOW_ATK, atk_box_rect)
            if card.atk > card.atk_ori:
                color = C_GREEN_BOOST
            else:
                color = C_BLACK
            atk_surface = FONT_STAT.render(str(card.atk), True, color)
            atk_rect = atk_surface.get_rect(center=atk_box_rect.center)
            self.screen.blit(atk_surface, atk_rect)

        # PV
        if isinstance(card, Unit):
            pv_box_rect = pygame.Rect(big_rect.right - 35, big_rect.bottom - 30, 30, 25)
            pygame.draw.rect(self.screen, C_RED_PV, pv_box_rect)
            if card.bouclier:
                color = C_YELLOW_ATK
            elif card.pv < card.pv_max:
                color = C_RED_DMG
            elif card.pv > card.pv_ori:
                color = C_GREEN_BOOST
            else:
                color = C_BLACK
            pv_surface = FONT_STAT.render(str(card.pv), True, color)
            pv_rect = pv_surface.get_rect(center=pv_box_rect.center)
            self.screen.blit(pv_surface, pv_rect)

        # ARTWORK
        img_box = pygame.Rect(big_rect.left + 15, big_rect.top + 40, 120, 100)
        pygame.draw.rect(self.screen, C_GREY_LIGHT, img_box)

        # DESCRIPTION
        name_box = pygame.Rect(big_rect.left + 10, big_rect.top + 150, 130, 30)
        name_surface = FONT_NAME.render(card.description, True, C_WHITE)
        name_rect = name_surface.get_rect(center=name_box.center)
        self.screen.blit(name_surface, name_rect)

        # Archetype
        name_box = pygame.Rect(big_rect.left + 40, big_rect.bottom - 30, 70, 25)
        text = card.archetype if isinstance(card, Unit) else ""
        name_surface = FONT_NAME.render(text, True, C_WHITE)
        name_rect = name_surface.get_rect(center=name_box.center)
        self.screen.blit(name_surface, name_rect)
                
    def display_mana_bar(self, player, bar_x, bar_y):
        mana_box = pygame.Rect(bar_x, bar_y, 25.5 * MANA_RAD, 4 * MANA_RAD)
        pygame.draw.rect(self.screen, C_GREY_LIGHT, mana_box)

        for i in range(10):
            circle_x = 1.5 * MANA_RAD + bar_x + i * (2.5 * MANA_RAD)
            circle_y = 2 * MANA_RAD + bar_y

            if i < player.blocked_mana:
                pygame.draw.circle(self.screen, C_BLACK, (circle_x, circle_y), MANA_RAD)
            elif i < (player.blocked_mana + player.basic_mana):
                pygame.draw.circle(self.screen, C_BLUE_MANA, (circle_x, circle_y), MANA_RAD)
            elif i < (player.blocked_mana + player.basic_mana + player.extra_mana):
                pygame.draw.circle(self.screen, C_BLUE_COST, (circle_x, circle_y), MANA_RAD)
            else:
                pygame.draw.circle(self.screen, C_GREY_CO, (circle_x, circle_y), MANA_RAD, 2)

    def display_avatar(self, pos_y, width, offset_x, level, classe):
        av_rect = pygame.Rect(MANA_X + offset_x, pos_y, width, DECK_SIZE)
        pygame.draw.rect(self.screen, C_CLASSES[classe], av_rect)
        av_surface = FONT_STAT.render(level, True, C_WHITE)
        av_rect = av_surface.get_rect(center=av_rect.center)
        self.screen.blit(av_surface, av_rect)
        
    def display_app(self):
        self.screen.blit(self.background_image, (0, 0))

        # LEFT
        pygame.draw.circle(self.screen, C_P2_HEALTH, HEALTH_2_CENTER, HEALTH_RAD)
        pygame.draw.circle(self.screen, C_P2, HEALTH_2_CENTER, HEALTH_RAD, width=3)
        color = C_GREY_SP if self.game.player_2.health == 0 else C_BLACK
        h2_surface = FONT_BIG.render(str(self.game.player_2.health), True, color)
        h2_rect = h2_surface.get_rect(center=HEALTH_2_CENTER)
        self.screen.blit(h2_surface, h2_rect)

        if self.game.player_2.armor > 0:
            armor_rect = pygame.Rect(HEALTH_2_CENTER[0] + 20, HEALTH_2_CENTER[1] + 20, HEALTH_RAD - 20, HEALTH_RAD - 20)
            pygame.draw.rect(self.screen, C_BORDER, armor_rect)
            ar_surface = FONT_STAT.render(str(self.game.player_2.armor), True, C_WHITE)
            ar_rect = ar_surface.get_rect(center=armor_rect.center)
            self.screen.blit(ar_surface, ar_rect)
        
        pygame.draw.circle(self.screen, C_P1_HEALTH, HEALTH_1_CENTER, HEALTH_RAD)
        pygame.draw.circle(self.screen, C_P1, HEALTH_1_CENTER, HEALTH_RAD, width=3)
        color = C_GREY_SP if self.game.player_1.health == 0 else C_BLACK
        h1_surface = FONT_BIG.render(str(self.game.player_1.health), True, color)
        h1_rect = h1_surface.get_rect(center=HEALTH_1_CENTER)
        self.screen.blit(h1_surface, h1_rect)

        if self.game.player_1.armor > 0:
            armor_rect = pygame.Rect(HEALTH_1_CENTER[0] + 20, HEALTH_1_CENTER[1] + 20, HEALTH_RAD - 20, HEALTH_RAD - 20)
            pygame.draw.rect(self.screen, C_BORDER, armor_rect)
            ar_surface = FONT_STAT.render(str(self.game.player_1.armor), True, C_WHITE)
            ar_rect = ar_surface.get_rect(center=armor_rect.center)
            self.screen.blit(ar_surface, ar_rect)

        p2_rect = pygame.Rect(HEALTH_2_CENTER[0] - 2 * HEALTH_RAD, HEALTH_2_CENTER[1] - HEALTH_RAD - 30 - CARD_SIZE // 2, 4 * HEALTH_RAD, CARD_SIZE // 2)
        pygame.draw.rect(self.screen, C_P2, p2_rect)
        p2_surface = FONT_STAT.render(str(self.game.player_2.name), True, C_BLACK)
        p2_rect = p2_surface.get_rect(center=p2_rect.center)
        self.screen.blit(p2_surface, p2_rect)

        p1_rect = pygame.Rect(HEALTH_1_CENTER[0] - 2 * HEALTH_RAD, HEALTH_1_CENTER[1] + HEALTH_RAD + 30, 4 * HEALTH_RAD, CARD_SIZE // 2)
        pygame.draw.rect(self.screen, C_P1, p1_rect)
        p1_surface = FONT_STAT.render(str(self.game.player_1.name), True, C_BLACK)
        p1_rect = p1_surface.get_rect(center=p1_rect.center)
        self.screen.blit(p1_surface, p1_rect)

        turn_rect = pygame.Rect(HEALTH_1_CENTER[0] - 2 * HEALTH_RAD, TURN_Y, 2 * HEALTH_RAD, CARD_SIZE // 2)
        turn_surface = FONT_STAT.render("tour " + str(self.game.turn), True, C_BLACK)
        turn_rect = turn_surface.get_rect(center=turn_rect.center)
        self.screen.blit(turn_surface, turn_rect)

        pass_rect = pygame.Rect(HEALTH_1_CENTER[0], TURN_Y, 2 * HEALTH_RAD, CARD_SIZE // 2)
        color_turn = C_P1 if self.game.active_player == self.game.player_1 else C_P2
        pygame.draw.rect(self.screen, color_turn, pass_rect)
        pass_surface = FONT_STAT.render("PASSER", True, C_BLACK)
        pass_rect = pass_surface.get_rect(center=pass_rect.center)
        self.screen.blit(pass_surface, pass_rect)

        # CENTER
        for y in (POSITION_Y[1], POSITION_Y[2], POSITION_Y[3], POSITION_Y[4]):
            row_rect = pygame.Rect((SCREEN_WIDTH - (6 * CARD_SIZE + 7 * CARD_MARGIN)) // 2, y - 10, 6 * CARD_SIZE + 7 * CARD_MARGIN, CARD_SIZE + CARD_MARGIN)
            pygame.draw.rect(self.screen, C_BACKGROUND, row_rect)
            pygame.draw.rect(self.screen, C_BORDER, row_rect, width=2)  

        self.center_cards(self.game.player_2.hand, POSITION_Y[0])
        self.center_cards(self.game.player_2.backrow, POSITION_Y[1])
        self.center_cards(self.game.player_2.frontrow, POSITION_Y[2])
        self.center_cards(self.game.player_1.frontrow, POSITION_Y[3])
        self.center_cards(self.game.player_1.backrow, POSITION_Y[4])
        self.center_cards(self.game.player_1.hand, POSITION_Y[5])

        self.display_cards(self.game.player_2.hand)
        self.display_cards(self.game.player_2.frontrow)
        self.display_cards(self.game.player_2.backrow)
        self.display_cards(self.game.player_1.backrow)
        self.display_cards(self.game.player_1.frontrow)
        self.display_cards(self.game.player_1.hand)
        
        # RIGHT
        if self.tooltip_active:
            z_rect = pygame.Rect(MANA_X, 375, 20, 20)
            pygame.draw.rect(self.screen, C_BLACK, z_rect)
            z_surface = FONT_STAT.render("Z", True, C_WHITE)
            z_rect = z_surface.get_rect(center=z_rect.center)
            self.screen.blit(z_surface, z_rect)

        if self.game.active_player.rage_ishtar:
            r_rect = pygame.Rect(MANA_X + 30, 375, 20, 20)
            pygame.draw.rect(self.screen, C_RED_DMG, r_rect)
            r_surface = FONT_STAT.render("R", True, C_WHITE)
            r_rect = r_surface.get_rect(center=r_rect.center)
            self.screen.blit(r_surface, r_rect)

        self.display_mana_bar(self.game.player_2, MANA_X, POSITION_Y[1] + 30)
        self.display_mana_bar(self.game.player_1, MANA_X, POSITION_Y[4] + 30)

        if len(self.game.player_2.avatar) == 2:
            self.display_avatar(POS_DECK_Y[0], DECK_SIZE/2, 0, str(list(self.game.player_2.avatar.values())[0].level), list(self.game.player_2.avatar.keys())[0])
            self.display_avatar(POS_DECK_Y[0], DECK_SIZE/2, DECK_SIZE/2, str(list(self.game.player_2.avatar.values())[1].level), list(self.game.player_2.avatar.keys())[1])
        else:
            self.display_avatar(POS_DECK_Y[0], DECK_SIZE, 0, str(list(self.game.player_2.avatar.values())[0].level), list(self.game.player_2.avatar.keys())[0])

        d2_rect = pygame.Rect(MANA_X + DECK_SIZE + DECK_MARGIN, POS_DECK_Y[0], DECK_SIZE, DECK_SIZE)
        pygame.draw.rect(self.screen, C_BLACK, d2_rect, width=2)
        d2_surface = FONT_STAT.render(str(len(self.game.player_2.discard)), True, C_BLACK)
        d2_rect = d2_surface.get_rect(center=d2_rect.center)
        self.screen.blit(d2_surface, d2_rect)

        d2_rect = pygame.Rect(MANA_X + 2 * (DECK_SIZE + DECK_MARGIN), POS_DECK_Y[0], DECK_SIZE, DECK_SIZE)
        pygame.draw.rect(self.screen, C_P2, d2_rect)
        d2_surface = FONT_STAT.render(str(len(self.game.player_2.deck)), True, C_BLACK)
        d2_rect = d2_surface.get_rect(center=d2_rect.center)
        self.screen.blit(d2_surface, d2_rect)

        if len(self.game.player_1.avatar) == 2:
            self.display_avatar(POS_DECK_Y[1], DECK_SIZE/2, 0, str(list(self.game.player_1.avatar.values())[0].level), list(self.game.player_1.avatar.keys())[0])
            self.display_avatar(POS_DECK_Y[1], DECK_SIZE/2, DECK_SIZE/2, str(list(self.game.player_1.avatar.values())[1].level), list(self.game.player_1.avatar.keys())[1])
        else:
            self.display_avatar(POS_DECK_Y[1], DECK_SIZE, 0, str(list(self.game.player_1.avatar.values())[0].level), list(self.game.player_1.avatar.keys())[0])

        d1_rect = pygame.Rect(MANA_X + DECK_SIZE + DECK_MARGIN, POS_DECK_Y[1], DECK_SIZE, DECK_SIZE)
        pygame.draw.rect(self.screen, C_BLACK, d1_rect, width=2)
        d1_surface = FONT_STAT.render(str(len(self.game.player_1.discard)), True, C_BLACK)
        d1_rect = d1_surface.get_rect(center=d1_rect.center)
        self.screen.blit(d1_surface, d1_rect)

        d1_rect = pygame.Rect(MANA_X + 2 * (DECK_SIZE + DECK_MARGIN), POS_DECK_Y[1], DECK_SIZE, DECK_SIZE)
        pygame.draw.rect(self.screen, C_P1, d1_rect)
        d1_surface = FONT_STAT.render(str(len(self.game.player_1.deck)), True, C_BLACK)
        d1_rect = d1_surface.get_rect(center=d1_rect.center)
        self.screen.blit(d1_surface, d1_rect)

    def display_tooltip(self, mx, my):
        for card in self.game.player_1.hand:
            if card.rectangle.collidepoint(mx, my):
                self.zoom_card(card, 1)
        for card in self.game.player_1.backrow:
            if card.rectangle.collidepoint(mx, my):
                self.zoom_card(card, 1)
        for card in self.game.player_1.frontrow:
            if card.rectangle.collidepoint(mx, my):
                self.zoom_card(card, 1)
        for card in self.game.player_2.hand:
            if card.rectangle.collidepoint(mx, my):
                self.zoom_card(card, 2)
        for card in self.game.player_2.backrow:
            if card.rectangle.collidepoint(mx, my):
                self.zoom_card(card, 2)
        for card in self.game.player_2.frontrow:
            if card.rectangle.collidepoint(mx, my):
                self.zoom_card(card, 2)

    def display_start_menu(self):
        self.screen.fill(C_BACKGROUND)

        p2_rect = pygame.Rect(HEALTH_2_CENTER[0] - 2 * HEALTH_RAD, HEALTH_2_CENTER[1] - HEALTH_RAD - 30 - CARD_SIZE // 2, 4 * HEALTH_RAD, CARD_SIZE // 2)
        pygame.draw.rect(self.screen, C_P2, p2_rect)
        p2_surface = FONT_STAT.render(str(self.game.player_2.name), True, C_BLACK)
        p2_rect = p2_surface.get_rect(center=p2_rect.center)
        self.screen.blit(p2_surface, p2_rect)

        p1_rect = pygame.Rect(HEALTH_1_CENTER[0] - 2 * HEALTH_RAD, HEALTH_1_CENTER[1] + HEALTH_RAD + 30, 4 * HEALTH_RAD, CARD_SIZE // 2)
        pygame.draw.rect(self.screen, C_P1, p1_rect)
        p1_surface = FONT_STAT.render(str(self.game.player_1.name), True, C_BLACK)
        p1_rect = p1_surface.get_rect(center=p1_rect.center)
        self.screen.blit(p1_surface, p1_rect)

        turn_rect = pygame.Rect(HEALTH_1_CENTER[0] - 2 * HEALTH_RAD, TURN_Y, 4 * HEALTH_RAD, CARD_SIZE // 2)
        turn_surface = FONT_STAT.render("Press Space to start the game", True, C_BLACK)
        turn_rect = turn_surface.get_rect(center=turn_rect.center)
        self.screen.blit(turn_surface, turn_rect)

    def display_end_menu(self):
        self.screen.fill(C_BACKGROUND)
    
        turn_rect = pygame.Rect(HEALTH_1_CENTER[0] - 2 * HEALTH_RAD, TURN_Y, 4 * HEALTH_RAD, CARD_SIZE // 2)
        turn_surface = FONT_STAT.render("Game Over", True, C_BLACK)
        turn_rect = turn_surface.get_rect(center=turn_rect.center)
        self.screen.blit(turn_surface, turn_rect)

app = App("deck bêtes", "OTK rouge-noir")