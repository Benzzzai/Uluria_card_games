
import pygame
import sys
from config_parameters import *
from game import Game


class App:
    def __init__(self, deck_name_1, deck_name_2):
        self.game = Game(deck_name_1, deck_name_2)

        self.selected_card = None
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
                        pass
                    elif event.button == 3:
                        pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        pass

            # self.game.check_death()
            # self.check_end()
            self.display_app()
            if self.tooltip_active:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.display_tooltip(mouse_x, mouse_y)

            pygame.display.flip()
            self.clock.tick(30)

    def display_app(self):
        self.screen.fill(C_BACKGROUND)

        board_2 = pygame.Rect((SCREEN_WIDTH - 7 * (CARD_SIZE + CARD_MARGIN))/2, POS_Y[2] - CARD_MARGIN/2, 7 * (CARD_SIZE + CARD_MARGIN), CARD_SIZE + CARD_MARGIN)
        pygame.draw.rect(self.screen, C_GREY_LIGHT, board_2, 2)
        board_1 = pygame.Rect((SCREEN_WIDTH - 7 * (CARD_SIZE + CARD_MARGIN))/2, POS_Y[3] - CARD_MARGIN/2, 7 * (CARD_SIZE + CARD_MARGIN), CARD_SIZE + CARD_MARGIN)
        pygame.draw.rect(self.screen, C_GREY_LIGHT, board_1, 2)

        self.display_hand(self.game.player_2.hand, POS_Y[0])
        self.display_hand(self.game.player_1.hand, POS_Y[5])
        
        self.display_board(self.game.player_2.board, POS_Y[2])
        self.display_board(self.game.player_1.board, POS_Y[3])
        


    def display_hand(self, hand, pos_y):
        for i, card in enumerate(hand):
            card_rect = pygame.Rect(POS_X_HAND + i * (CARD_SIZE + CARD_MARGIN), pos_y, CARD_SIZE , CARD_SIZE)
            pygame.draw.rect(self.screen, C_GREY_LIGHT, card_rect)
        
            # NAME
            name_surface = FONT_NAME.render(card.name, True, C_WHITE)
            name_rect = name_surface.get_rect(center=card_rect.center)
            self.screen.blit(name_surface, name_rect)

            # COST
            cost_box_rect = pygame.Rect(card_rect.left + 5, card_rect.top + 5, 30, 25)
            pygame.draw.rect(self.screen, C_BLUE_COST, cost_box_rect)
            cost_surface = FONT_COST.render(str(card.cost), True, C_BLACK)
            cost_rect = cost_surface.get_rect(center=cost_box_rect.center)
            self.screen.blit(cost_surface, cost_rect)

            # USE
            use_box_rect = pygame.Rect(card_rect.right - 35, card_rect.top + 5, 30, 25)
            pygame.draw.rect(self.screen, C_RED_PV, use_box_rect)
            use_surface = FONT_COST.render(str(card.use), True, C_BLACK)
            use_rect = use_surface.get_rect(center=use_box_rect.center)
            self.screen.blit(use_surface, use_rect)


    def display_board(self, board, pos_y):
        n = len(board)
        pos_x = (SCREEN_WIDTH - n * CARD_SIZE - (n-1) * CARD_MARGIN)/2
        for i, card in enumerate(board):
            card_rect = pygame.Rect(pos_x + i * (CARD_SIZE + CARD_MARGIN), pos_y, CARD_SIZE , CARD_SIZE)
            pygame.draw.rect(self.screen, C_GREY_LIGHT, card_rect)
        



app = App("base 1", "base 1")