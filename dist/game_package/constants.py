import pygame
pygame.font.init()

# SIZE
WIDTH, HEIGHT = 620, 620

# COLORS
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

# Fonts
box_font = pygame.font.SysFont("comicsans", 15)
remaining_bombs_font = pygame.font.SysFont("comicsans", 25)
win_lose_font = pygame.font.SysFont("comicsans", 40)
main_menu_font = pygame.font.SysFont("comicsans", 35)


def get_board_top(level):
    if level == 1:
        return 110
    if level == 2:
        return 50
    if level == 3:
        return 150
    return 100


# def get_board_bottom(level):
#     if level == 1:
#         return HEIGHT - 60
#     if level == 2:
#         return HEIGHT - 10
#     if level == 3:
#         return HEIGHT - 150
#     return HEIGHT - 40


def get_board_left(level):
    if level == 1:
        return 85
    if level == 2:
        return 30
    return 10


# def get_board_right(level):
#     if level == 1:
#         return WIDTH - 85
#     if level == 2:
#         return WIDTH - 30
#     return WIDTH - 10
