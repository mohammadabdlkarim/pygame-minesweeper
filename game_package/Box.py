import pygame
from .constants import BLACK, RED, WHITE, box_font
pygame.font.init()


class Box:
    def __init__(self, row, col, bombs):
        self.row = row
        self.col = col
        self.opened = False
        self.flagged = False
        self.bomb = self._set_bomb(bombs)
        self.content = self._set_content(bombs)

    def open(self):
        if not self.opened and not self.flagged:
            self.opened = True
            return True

    def flag(self):
        self.flagged = True

    def unflag(self):
        if self.flagged:
            self.flagged = False

    def _set_bomb(self, bombs):
        return (self.row, self.col) in bombs

    def _set_content(self, bombs):
        if not self.bomb:
            bombs_counter = 0
            y = self.row - 1
            while y <= self.row + 1:
                x = self.col - 1
                while x <= self.col + 1:
                    if (y, x) in bombs:
                        bombs_counter += 1
                    x += 1
                y += 1
            if bombs_counter > 0:
                return str(bombs_counter)
            return ""
        return "*"
