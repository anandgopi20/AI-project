from evaluate import evaluate_board
import pygame
import os
from board import Board
from minimax import find_best_move_minimax
from mcts import find_best_move_mcts

TILE_SIZE = 80
WIDTH, HEIGHT = TILE_SIZE * 8, TILE_SIZE * 8
ASSET_PATH = os.path.join(os.path.dirname(__file__), 'assets')

PIECE_IMAGES = {}

def load_images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK',
              'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        image = pygame.image.load(os.path.join(ASSET_PATH, f"{piece}.png"))
        PIECE_IMAGES[piece] = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

class ChessGUI:
    def __init__(self, use_mcts=False):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Human vs MCTS' if use_mcts else 'Human vs Minimax')
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.use_mcts = use_mcts
        self.selected = None
        self.move_log = []
        self.last_eval = ''
        self.legal_moves = []
        load_images()

    def run(self):
        running = True
        while running and not self.board.is_game_over():
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.board.turn == 'white':
                    self.handle_click(pygame.mouse.get_pos())

            if self.board.turn == 'black':
                if not self.board.is_game_over():
                    print('[DEBUG] AI thinking...')
                    if self.use_mcts:
                        move = find_best_move_mcts(self.board, simulations=50, prefer_captures=True)
                    else:
                        move = find_best_move_minimax(self.board, depth=3)
                    if move:
                        print(f"AI plays: {move}")
                        self.board.make_move(move)
                        self.board.turn = 'white'
                        self.move_log.append(move)
                        eval_score = evaluate_board(self.board)
                        print(f"[EVAL] After AI move ({move}): {eval_score:.2f}")

            self.draw_board()
            self.draw_selection()
            self.draw_eval()
            if self.board.is_game_over():
                self.draw_game_over()
            pygame.display.flip()

        print("Game Over")
        print("Moves:", self.move_log)
        pygame.quit()

    def handle_click(self, pos):
        row, col = pos[1] // TILE_SIZE, pos[0] // TILE_SIZE
        square = (row, col)
        if self.selected:
            move = self.convert_move(self.selected, square)
            if self.board.is_valid_move(move):
                print(f"Human plays: {move}")
                success = self.board.make_move(move)
                if success:
                    self.board.turn = 'black'
                    self.move_log.append(move)
                self.selected = None
                self.legal_moves = []
            else:
                self.selected = None
        else:
            self.selected = square
            self.legal_moves = [m for m in self.board.get_legal_moves() if m[:2] == f"{chr(col+97)}{8-row}"]

    def convert_move(self, start, end):
        return f"{chr(start[1] + ord('a'))}{8 - start[0]}{chr(end[1] + ord('a'))}{8 - end[0]}"

    def draw_board(self):
        light = pygame.Color(238, 200, 160)
        dark = pygame.Color(170, 120, 80)
        highlight_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
        highlight_surface.set_alpha(100)
        highlight_surface.fill((255, 255, 0))  # Yellow
        for row in range(8):
            for col in range(8):
                color = light if (row + col) % 2 == 0 else dark
                pygame.draw.rect(self.screen, color, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if self.selected:
                    move_str = f"{chr(col + 97)}{8 - row}"
                    if any(m[2:] == move_str for m in self.legal_moves):
                        self.screen.blit(highlight_surface, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                piece = self.board.board[row][col]
                if piece != '.':
                    color_prefix = 'w' if piece.isupper() else 'b'
                    piece_code = color_prefix + piece.upper()
                    self.screen.blit(PIECE_IMAGES[piece_code], (col * TILE_SIZE, row * TILE_SIZE))

    def draw_selection(self):
        if self.selected:
            row, col = self.selected
            pygame.draw.rect(self.screen, pygame.Color('red'), pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 3)

    def draw_eval(self):
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Turn: {self.board.turn}", True, pygame.Color('blue'))
        self.screen.blit(text, (10, HEIGHT - 30))

    def draw_game_over(self):
        font = pygame.font.SysFont(None, 48)
        if self.board.is_checkmate():
            winner = 'Black' if self.board.turn == 'white' else 'White'
            message = f"Checkmate! {winner} wins."
        else:
            message = "Stalemate!"
        text = font.render(message, True, pygame.Color('red'))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        pygame.draw.rect(self.screen, pygame.Color('black'), rect.inflate(20, 20))
        self.screen.blit(text, rect)
