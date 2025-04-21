import random

def mcts_decision(board, simulations=100):
    moves = board.get_legal_moves('white')  # Assuming white's turn
    if not moves:
        return None
    return random.choice(moves)  # Placeholder for real MCTS logic
