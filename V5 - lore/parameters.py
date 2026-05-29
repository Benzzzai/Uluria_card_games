import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 740

POS_Y = [20, 160, 250, 390, 540, 620]
POS_X_HAND = 310

CARD_SIZE = 100
CARD_MARGIN = 20

NAME_X = 80
TRAP_X = 350
ARTIFACT_X = 690
MANA_X = 872
MANA_RAD = 8
INFO_HEIGHT = 40

# COLOR
C_BACKGROUND = (245, 255, 235)
C_BORDER = (90, 70, 50)

C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_GREY_LIGHT = (180, 180, 180)
C_GREY = (90, 80, 80)

C_BLUE_COST = (0, 200, 255)
C_BLUE_MANA = (0, 80, 255)
C_YELLOW_ATK = (255, 210, 0)
C_RED_PV = (255, 50, 50)
C_RED_DMG = (155, 0, 0)
C_GREEN_BOOST = (0, 190, 0)
C_GREEN_COST = (0, 110, 0)
C_INSTANT = (180, 51, 255)
C_GREEN_SEL = (0, 255, 0)

C_P2 = (0, 130, 255)
C_P1 = (255, 120, 0)
C_P2_HEALTH = (200, 230, 255)
C_P1_HEALTH = (255, 230, 200)

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

# FONT
pygame.font.init()

FONT_NAME = pygame.font.SysFont("Arial", 16)
FONT_STAT = pygame.font.SysFont("Arial", 20)
FONT_COST = pygame.font.SysFont("Arial", 24)

FONT_BIG = pygame.font.SysFont("Arial", 36)
FONT_BIG.set_bold(True)