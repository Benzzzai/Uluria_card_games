import pygame

# Size and position of element on the screen
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 770

POSITION_Y = [20, 150, 271, 399, 520, 650]

# Card settings
CARD_SIZE = 100
CARD_MARGIN = 20

MANA_RAD = 10
MANA_X = 1100

HEALTH_RAD = 50
HEALTH_2_CENTER = (200, 270)
HEALTH_1_CENTER = (200, 500)
TURN_Y = 360

POS_DECK_Y = (285, 425)
DECK_SIZE = 55
DECK_MARGIN = 45

# Colors
# C_BACKGROUND = (245, 255, 235)
C_BACKGROUND = (245, 255, 205)
C_BORDER = (90, 70, 50)

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

C_GREEN_SEL = (0, 255, 0)

C_GREY_CO = (90, 80, 80)
C_GREY_ST = (60, 60, 60)
C_GREY_SP = (110, 120, 140)
C_GREY_ALT = (100, 140, 100)
C_GREY_LIGHT = (180, 180, 180)

C_P2 = (0, 130, 255)
C_P1 = (255, 120, 0)
C_P2_HEALTH = (200, 230, 255)
C_P1_HEALTH = (255, 230, 200)

C_GRASS = (180, 240, 120)

# Font
pygame.font.init()

FONT_NAME = pygame.font.SysFont("Arial", 16)
FONT_STAT = pygame.font.SysFont("Arial", 24)

FONT_BIG = pygame.font.SysFont("Arial", 36)
FONT_BIG.set_bold(True)