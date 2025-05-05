import pygame
from gui import ChessGUI

def main():
    print("Choose Mode:")
    print("1. Human vs Minimax")
    print("2. Human vs MCTS")
    choice = input("Enter 1 or 2: ").strip()

    use_mcts = choice == '2'
    game = ChessGUI(use_mcts=use_mcts)
    game.run()

if __name__ == '__main__':
    main()