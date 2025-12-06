import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

POS_Y = [20, 140, 240, 380, 500, 600]
POS_X_HAND = 310

CARD_SIZE = 100
CARD_MARGIN = 20

# COLOR
C_BACKGROUND = (245, 255, 235)
C_GREY_LIGHT = (180, 180, 180)

C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)

C_BLUE_COST = (0, 200, 255)
C_BLUE_MANA = (0, 80, 255)
C_YELLOW_ATK = (255, 210, 0)
C_RED_PV = (255, 50, 50)
C_RED_DMG = (155, 0, 0)
C_GREEN_BOOST = (0, 190, 0)
C_GREEN_COST = (0, 110, 0)
C_INSTANT = (180, 51, 255)

# FONT
pygame.font.init()

FONT_NAME = pygame.font.SysFont("Arial", 16)
FONT_STAT = pygame.font.SysFont("Arial", 20)
FONT_COST = pygame.font.SysFont("Arial", 24)

FONT_BIG = pygame.font.SysFont("Arial", 36)
FONT_BIG.set_bold(True)