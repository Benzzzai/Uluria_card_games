import pygame

# Size and position of elements on the screen
SCREEN_WIDTH = 1120
SCREEN_HEIGHT = 780

POS_HAND = [20, 660]

CARD_SIZE = 100
CARD_MARGIN = 20

HEX_RADIUS = 60
POS_TILE = (352, 210)

HEALTH_RAD = 45
HEALTH_2_CENTER = (150, 280)
HEALTH_1_CENTER = (150, 500)
TURN_Y = 365
# est ce que la manière la plus simple de réarranger ca serait pas de faire un param = 1 valeur, pas de liste et mettre des noms plus explicites ?

MANA_RAD = 10
MANA_X = 800
MANA_Y = (160, 580)
ESS_Y = (260, 470)
BUTTON_SIZE = 40

# Colors
C_BACKGROUND = (215, 245, 255)

C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_GREY_LIGHT = (180, 180, 180)

C_BLUE_COST = (0, 200, 255)
C_BLUE_MANA = (0, 80, 255)
C_YELLOW_ATK = (255, 210, 0)
C_RED_PV = (255, 50, 50)
C_RED_DMG = (155, 0, 0)
C_GREEN_BOOST = (0, 190, 0)
C_GREEN_COST = (0, 110, 0)
C_INSTANT = (180, 51, 255)

C_GREEN_SEL = (0, 255, 0)

C_UNIT = (110, 80, 80)
C_SPELL = (110, 120, 140)
C_ENCHANTMENT = (100, 140, 100)
C_EQUIPMENT = (60, 60, 60)


C_P2 = (0, 130, 255)
C_P1 = (255, 120, 0)
C_P2_HEALTH = (200, 230, 255)
C_P1_HEALTH = (255, 230, 200)

color_tile = {
    "empty" : C_BACKGROUND,
    "center" : (225, 225, 225),
    "basic" : (220, 240, 190),
    "upgraded" : C_WHITE
}


# Font
pygame.font.init()

FONT_NAME = pygame.font.SysFont("Arial", 16)
FONT_STAT = pygame.font.SysFont("Arial", 24)

FONT_BIG = pygame.font.SysFont("Arial", 36)
FONT_BIG.set_bold(True)
