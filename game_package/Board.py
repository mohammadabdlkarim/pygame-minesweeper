import os

import pygame

from .constants import BLACK, WHITE, RED, WIDTH, HEIGHT
from .constants import box_font
pygame.font.init()


class Board:
    # boxes
    CLOSED_BOX_IMAGE = pygame.image.load(os.path.join('game_package/assets', 'box.jpeg'))
    FLAG_IMAGE = pygame.image.load(os.path.join('game_package/assets', 'flag.png'))
    BOMB_IMAGE = pygame.image.load(os.path.join('game_package/assets', 'mine.png'))
    

    def __init__(self, rows, cols, box_side):
        self.rows = rows
        self.cols = cols
        # Corners
        self.top_left_corner = 0, 0
        self.top_right_corner = WIDTH, 0
        self.bottom_left_corner = 0, HEIGHT
        self.bottom_right_corner = WIDTH, HEIGHT
        # box
        self.box_side = box_side
        self.closed_box = pygame.transform.scale(self.CLOSED_BOX_IMAGE, (self.box_side - 3, self.box_side - 3))
        self.flag = pygame.transform.scale(self.FLAG_IMAGE, (self.box_side // 2, self.box_side // 2))
        self.bomb_image = pygame.transform.scale(self.BOMB_IMAGE, (self.box_side-3, self.box_side-3))
    
    def _draw_borders(self, win):
        pygame.draw.line(win, BLACK, self.top_left_corner, self.top_right_corner)
        pygame.draw.line(win, BLACK, self.top_left_corner, self.bottom_left_corner)
        pygame.draw.line(win, BLACK, self.top_right_corner, self.bottom_right_corner)
        pygame.draw.line(win, BLACK, self.bottom_left_corner, self.bottom_right_corner)

    def _draw_in_lines(self, win):
        box_side = self.box_side
        
        left_point_x, top_point_y = self.top_left_corner
        right_point_x, bottom_point_y = self.bottom_right_corner

        x = left_point_x + box_side
        y = top_point_y + box_side

        while x < right_point_x:
            pygame.draw.line(win, BLACK, (x, top_point_y), (x, bottom_point_y))
            x += box_side
        
        while y < bottom_point_y:
            pygame.draw.line(win, BLACK, (left_point_x, y), (right_point_x, y))
            y += box_side

    def draw_boxes(self, win, boxes, rows, cols):
        for row in range(rows):
            for col in range(cols):
                for box in boxes[row]:
                    b = boxes[row][col]

                    board_top = self.top_left_corner[1]
                    board_left = self.top_left_corner[0]

                    left = board_left + 2 + (self.box_side * col)
                    top = board_top + 2 + (self.box_side * row)

                    if b.opened:
                        if b.bomb:
                            win.blit(self.bomb_image, (left, top))
                        else:
                            box_label = box_font.render(b.content, True, BLACK)
                            win.blit(box_label, (((left + self.box_side // 2) - box_label.get_width()//2), ((top + self.box_side // 2) - box_label.get_height()//2)))
                            
                    else:
                        win.blit(self.closed_box, (left, top))
                        if b.flagged:
                            win.blit(self.flag, ((left + self.box_side // 2 - self.flag.get_width()//2), (top + self.box_side // 2 - self.flag.get_height()//2)))

    def _draw_reset(self, win):
        reset_rect = pygame.Rect(285, 25, 50, 25)
        pygame.draw.rect(win, RED, reset_rect)

    def draw_window(self, win):
        win.fill(WHITE)
        self._draw_reset(win)
        self._draw_borders(win)
        self._draw_in_lines(win)

class BeginnerBoard(Board):
    def __init__(self):
        self.rows = self.cols = 9
        # boxes
        self.box_side = 50
        # super
        super().__init__(self.rows, self.cols, self.box_side)
        # Corners
        self.top_left_corner = 85, 110
        self.top_right_corner = WIDTH - 85, 110
        self.bottom_left_corner = 85, HEIGHT - 60
        self.bottom_right_corner = WIDTH - 85, HEIGHT - 60
        # Mines
        self.number_of_mines = 10


class MediumBoard(Board):
    def __init__(self):
        self.rows = self.cols = 16
        # boxes
        self.box_side = 35
        # super
        super().__init__(self.rows, self.cols, self.box_side)
        # Corners
        self.top_left_corner = 30, 50
        self.top_right_corner = WIDTH - 30, 50
        self.bottom_left_corner = 30, HEIGHT - 10
        self.bottom_right_corner = WIDTH - 30, HEIGHT - 10
        # Mines
        self.number_of_mines = 40
        

class HardBoard(Board):
    def __init__(self):
        self.rows, self.cols = 16, 30
        # Boxes
        self.box_side = 20
        # super
        super().__init__(self.rows, self.cols, self.box_side)
        # Corners
        self.top_left_corner = 10, 150
        self.top_right_corner = WIDTH - 10, 150
        self.bottom_left_corner = 10, HEIGHT - 150
        self.bottom_right_corner = WIDTH - 10, HEIGHT - 150
        # Mines
        self.number_of_mines = 99
        

class ExtremeBoard(Board):
    def __init__(self):
        self.rows, self.cols = 24, 30
        # Boxes
        self.box_side = 20
        # super attributes
        super().__init__(self.rows, self.cols, self.box_side)
        # Corners
        self.top_left_corner = 10, 100
        self.top_right_corner = WIDTH - 10, 100
        self.bottom_left_corner = 10, HEIGHT - 40
        self.bottom_right_corner = WIDTH - 10, HEIGHT - 40
        # Mines
        self.number_of_mines = 180
