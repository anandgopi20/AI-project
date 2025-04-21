
import pygame
from board import Board

WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8
WHITE = (245, 245, 220)
BLACK = (139, 69, 19)
HIGHLIGHT = (100, 200, 100)

PIECE_IMAGES = {}

def load_images():
    pieces = ['P', 'R', 'N', 'B', 'Q', 'K', 'p', 'r', 'n', 'b', 'q', 'k']
    for piece in pieces:
        PIECE_IMAGES[piece] = pygame.transform.scale(
            pygame.image.load(f"images/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE)
        )

def draw_board(screen, board):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board.state[row][col]
            if piece != '.':
                screen.blit(PIECE_IMAGES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess AI GUI")
    load_images()

    board = Board()
    selected = None
    running = True

    while running:
        draw_board(screen, board)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
                coord = f"{chr(col + ord('a'))}{8 - row}"

                if selected:
                    move = (selected, coord)
                    board.apply_move(move)
                    selected = None
                else:
                    selected = coord

    pygame.quit()

if __name__ == "__main__":
    main()
