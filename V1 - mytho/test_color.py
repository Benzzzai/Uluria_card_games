

import pygame
import sys

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 770

CARD_SIZE = 100
CARD_MARGIN = 20

C_BACKGROUND = (245, 255, 205)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_BLUE_COST = (0, 180, 255)
C_YELLOW_ATK = (255, 210, 0)
C_RED_PV = (255, 0, 0)

pygame.font.init()
FONT_NAME = pygame.font.SysFont("Arial", 16)
FONT_STAT = pygame.font.SysFont("Arial", 24)

"""
C_CLASSES = {
    "Marduk" : (184, 0, 0),
    "Enlil" : (200, 128, 20),
    "Enki" : (69, 129, 142),
    "Ishtar" : (85, 143, 67),
    "Alchimiste" : (110, 67, 10),
    "Kraken" : (24, 69, 121),
    "Inconnu" : (103, 78, 167),
    "Thot" : (67, 67, 67)
}
"""
C_CLASSES = [
    (184, 0, 0),
    (200, 128, 20),
    (69, 129, 142),
    (85, 143, 67),
    (110, 67, 10),
    (24, 69, 121),
    (103, 78, 167),
    (67, 67, 67)
]


class App:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Runeterra TCG")
        self.background_image = pygame.image.load("grass.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(C_BACKGROUND)
            for i in range(8):
                # CARD RECTANGLE
                rectangle = pygame.Rect((i + 1) * (CARD_SIZE + CARD_MARGIN), 100, CARD_SIZE, CARD_SIZE)
                pygame.draw.rect(self.screen, C_CLASSES[i], rectangle)

                # NAME
                name_surface = FONT_NAME.render("Garde lumière", True, C_WHITE)
                name_rect = name_surface.get_rect(center=rectangle.center)
                self.screen.blit(name_surface, name_rect)

                # MANA
                cost_box_rect = pygame.Rect(rectangle.left + 5, rectangle.top + 5, 30, 25)
                pygame.draw.rect(self.screen, C_BLUE_COST, cost_box_rect)
                cost_surface = FONT_STAT.render("4", True, C_BLACK)
                cost_rect = cost_surface.get_rect(center=cost_box_rect.center)
                self.screen.blit(cost_surface, cost_rect)

                # ATK
                atk_box_rect = pygame.Rect(rectangle.left + 5, rectangle.bottom - 30, 30, 25)
                pygame.draw.rect(self.screen, C_YELLOW_ATK, atk_box_rect)
                atk_surface = FONT_STAT.render("2", True, C_BLACK)
                atk_rect = atk_surface.get_rect(center=atk_box_rect.center)
                self.screen.blit(atk_surface, atk_rect)

                # PV
                pv_box_rect = pygame.Rect(rectangle.right - 35, rectangle.bottom - 30, 30, 25)
                pygame.draw.rect(self.screen, C_RED_PV, pv_box_rect)
                pv_surface = FONT_STAT.render("3", True, C_BLACK)
                pv_rect = pv_surface.get_rect(center=pv_box_rect.center)
                self.screen.blit(pv_surface, pv_rect)

            pygame.display.flip()
            self.clock.tick(30)

app = App()