from src.minimax import minimax_decision
from src.mcts import mcts_decision
from src.board import Board

class ChessGame:
    def __init__(self):
        self.board = Board()

    def start(self):
        print("Starting Chess Game (Text-Based Mode)")
        self.board.print_board()
        # Example move selection
        best_move_minimax = minimax_decision(self.board, depth=3)
        best_move_mcts = mcts_decision(self.board, simulations=100)
        print(f"Minimax Move: {best_move_minimax}")
        print(f"MCTS Move: {best_move_mcts}")
