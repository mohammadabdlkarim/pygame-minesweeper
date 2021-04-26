import pygame
from game_package.constants import BLACK, WHITE, WIDTH, HEIGHT, main_menu_font, get_board_left, get_board_top
from game_package.Minesweeper import Minesweeper
from game_package.Board import *
pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")


def check_reset_from_mouse(pos):
    x, y = pos
    return 285 <= x < 335 and 25 <= y <= 50


def main(level):
    run = True
    fps = 60
    board = Board(10, 10, 50)
    if level == 1:
        board = BeginnerBoard()
    elif level == 2:
        board = MediumBoard()
    elif level == 3:
        board = HardBoard()
    elif level == 4:
        board = ExtremeBoard()
    minesweeper = Minesweeper(board)
    clock = pygame.time.Clock()

    def get_row_col_from_mouse(pos):
        board_left = get_board_left(level)
        baord_top = get_board_top(level)
        x, y = pos
        row = (y - baord_top) // board.box_side
        col = (x - board_left) // board.box_side
        return row, col

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if check_reset_from_mouse(pos):
                    run = False
                row, col = get_row_col_from_mouse(pos)
                if 0 <= row < minesweeper.board.rows and 0 <= col < minesweeper.board.cols:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        minesweeper.reveal_boxes(row, col)
                    elif pygame.mouse.get_pressed() == (0, 0, 1):
                        minesweeper.set_box_flag(row, col)

        minesweeper.draw_window(WIN)
        pygame.display.update()


def main_menu():
    run = True
    while run:
        WIN.fill(WHITE)
        title_label = main_menu_font.render('Minesweeper', True, BLACK)
        level_beginner_label = main_menu_font.render('Press B for Beginner(9x9, 10 mines)', True, BLACK)
        level_medium_label = main_menu_font.render('Press M for Medium(16x16, 99 mines)', True, BLACK)
        level_hard_label = main_menu_font.render('Press H for Hard(16x30, 10 mines)', True, BLACK)
        level_extreme_label = main_menu_font.render('Press E for Extreme(30x24, 10 mines)', True, BLACK)

        WIN.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 100))
        WIN.blit(level_beginner_label, (WIDTH // 2 - level_beginner_label.get_width() // 2, 200))
        WIN.blit(level_medium_label, (WIDTH // 2 - level_medium_label.get_width() // 2, 250))
        WIN.blit(level_hard_label, (WIDTH // 2 - level_hard_label.get_width() // 2, 300))
        WIN.blit(level_extreme_label, (WIDTH // 2 - level_extreme_label.get_width() // 2, 350))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            main(1)
        elif keys[pygame.K_m]:
            main(2)
        elif keys[pygame.K_h]:
            main(3)
        elif keys[pygame.K_e]:
            main(4)

if __name__ == "__main__":
    main_menu()
