import sys
import os

# Add the src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '/Users/hadvi/Documents/Masters/2025Spring/IntrotoAI/AI_Chess_Project_Final'))

from chess_game import ChessGame

if __name__ == "__main__":
    game = ChessGame()
    game.start()
