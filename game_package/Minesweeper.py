import pygame
import random
from .constants import BLACK, WHITE, RED, GREEN, WIDTH
from .constants import box_font, win_lose_font, remaining_bombs_font
from .Box import Box
pygame.font.init()


class Minesweeper:
    def __init__(self, board):
        self.board = board
        self.lost = False
        self.won = False
        self.number_of_bombs = self.board.number_of_mines
        self.bombs = self._create_bombs(self.number_of_bombs, self.board.rows, self.board.cols)
        self.boxes = self._create_boxes(self.board.rows, self.board.cols)
        self.remaining_bombs = self.board.number_of_mines

    def _create_boxes(self, rows, cols):
        boxes = []
        for row in range(rows):
            boxes.append([])
            for col in range(cols):
                box = Box(row, col, self.bombs)
                boxes[row].append(box)
        
        return boxes

    def _create_bombs(self, number_of_bombs, rows, cols):
        bombs = []
        while len(bombs) < number_of_bombs:
            bomb = (random.randrange(0, rows), random.randrange(0, cols))
            if bomb not in bombs:
                bombs.append(bomb)
        return bombs

    def draw_window(self, win):
        self.board.draw_window(win)
        self._draw_won_lost(win)
        self._draw_remaining_bombs(win)
        self.board.draw_boxes(win, self.boxes, self.board.rows, self.board.cols)
        pygame.display.flip()

    def _draw_remaining_bombs(self, win):
        remaining_bombs_label = remaining_bombs_font.render(f"Mines Left: {self.remaining_bombs}", True, BLACK)
        win.blit(remaining_bombs_label, (25, 25))

    def _draw_won_lost(self, win):
        if self.lost:
            win_lose_label = win_lose_font.render("You Lost!", True, RED)
        if self.won:
            win_lose_label = win_lose_font.render("You Won!", True, GREEN)
        if self.won or self.lost:
            win.blit(win_lose_label, (WIDTH - 100 - win_lose_label.get_width() // 2, 25))

    def set_box_flag(self, row, col):
        if not self.won and not self.lost:
            box = self.boxes[row][col]
            if box.flagged and not box.opened:
                self.remaining_bombs += 1
                box.unflag()
            else:
                if not box.opened:
                    self.remaining_bombs -= 1
                    box.flag()

    def reveal_boxes(self, row, col):
        if not self.lost and not self.won:
            if 0 <= row < self.board.rows and 0 <= col < self.board.cols:
                box = self.boxes[row][col]
                
                if box.open():
                    if not box.content:
                        adjacent_boxes = self._get_adjacent_boxes(row, col)
                        for b in adjacent_boxes:
                            self.reveal_boxes(b.row, b.col)
                    elif box.bomb:
                        self._open_bombs()
                        self.lost = True
                    self.check_win()

    def _get_adjacent_boxes(self, row, col):
        tiles = []
        y = row - 1
        while y <= row + 1:
            x = col - 1
            while x <= col + 1:
                if 0 <= x < self.board.cols and 0 <= y < self.board.rows:
                    if x != col or y != row:
                        box = self.boxes[y][x]
                        tiles.append(box)
                x += 1
            y += 1
        
        return tiles

    def _open_bombs(self):
        for bomb in self.bombs:
            self.boxes[bomb[0]][bomb[1]].open()

    def check_win(self):
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if (row, col) not in self.bombs and not self.boxes[row][col].opened:
                    return False
        self.won = True
        return True
