import pygame
import numpy as np

pygame.init()

ROWS = 6
COLS = 7
SIZE = 100

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 40, bold=True)
sub_font = pygame.font.SysFont("Arial", 20)

board = np.zeros((ROWS, COLS))
screen = pygame.display.set_mode((COLS * SIZE, (ROWS + 1) * SIZE))
pygame.display.set_caption("Connect Four")
turn = 0


def drop_piece(row, col, piece):
    board[row][col] = piece


def valid_location(col):
    return board[ROWS - 1][col] == 0


def next_row(col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r
    return None


def check_tie():
    return np.all(board != 0)


def winning(piece):
    # Horizontal
    for c in range(COLS - 3):
        for r in range(ROWS):
            if (board[r][c] == piece and board[r][c + 1] == piece
                    and board[r][c + 2] == piece and board[r][c + 3] == piece):
                return True

    # Vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if (board[r][c] == piece and board[r + 1][c] == piece
                    and board[r + 2][c] == piece and board[r + 3][c] == piece):
                return True

    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if (board[r][c] == piece and board[r + 1][c + 1] == piece
                    and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece):
                return True

    # Diagonal
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if (board[r][c] == piece and board[r - 1][c + 1] == piece
                    and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece):
                return True
    return False


def draw_board():
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c * SIZE, (r + 1) * SIZE, SIZE, SIZE))
            pygame.draw.circle(screen, BLACK, (c * SIZE + SIZE // 2,
                                               (r + 1) * SIZE + SIZE // 2), 40)
    for c in range(COLS):
        for r in range(ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c * SIZE + SIZE // 2,
                                                 (ROWS - r) * SIZE + SIZE // 2), 40)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c * SIZE + SIZE // 2,
                                                    (ROWS - r) * SIZE + SIZE // 2), 40)
    pygame.display.update()


def reset_game():
    global board, turn
    board = np.zeros((ROWS, COLS))
    turn = 0
    pygame.draw.rect(screen, BLACK, (0, 0, COLS * SIZE, SIZE))
    draw_board()


draw_board()
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_r:
                reset_game()
                game_over = False

        if event.type == pygame.MOUSEMOTION and not game_over:
            pygame.draw.rect(screen, BLACK, (0, 0, COLS * SIZE, SIZE))
            pos_x = event.pos[0]
            current_color = RED if turn == 0 else YELLOW
            pygame.draw.circle(screen, current_color, (pos_x, SIZE // 2), 40)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            col = event.pos[0] // SIZE
            if valid_location(col):
                row = next_row(col)
                piece = 1 if turn == 0 else 2
                drop_piece(row, col, piece)

                if winning(piece):
                    game_over = True
                    text_color = RED if piece == 1 else YELLOW
                    winner_name = "Player 1 (Red)" if piece == 1 else "Player 2 (Yellow)"
                    pygame.draw.rect(screen, BLACK, (0, 0, COLS * SIZE, SIZE))
                    win_text = font.render(f"{winner_name} Wins!", True, text_color)
                    sub_text = sub_font.render("Press R to Restart or Q to Quit", True, WHITE)
                    screen.blit(win_text, (20, 15))
                    screen.blit(sub_text, (20, 65))
                elif check_tie():
                    game_over = True
                    pygame.draw.rect(screen, BLACK, (0, 0, COLS * SIZE, SIZE))
                    tie_text = font.render("It's a Tie!", True, WHITE)
                    sub_text = sub_font.render("Press R to Restart or Q to Quit", True, WHITE)
                    screen.blit(tie_text, (20, 15))
                    screen.blit(sub_text, (20, 65))
                else:
                    turn = (turn + 1) % 2

                draw_board()

pygame.quit()
