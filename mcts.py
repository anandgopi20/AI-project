
import random
import math
import copy

class Node:
    def __init__(self, board, move=None, parent=None):
        self.board = board
        self.move = move
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self, legal_moves):
        return len(self.children) == len(legal_moves)

    def best_child(self, c_param=1.4):
        choices = [(child, child.wins / child.visits + c_param * (math.sqrt(math.log(self.visits) / child.visits)))
                   for child in self.children if child.visits > 0]
        return max(choices, key=lambda x: x[1])[0] if choices else random.choice(self.children)

def mcts_decision(root_board, simulations=100):
    root = Node(copy.deepcopy(root_board))

    for _ in range(simulations):
        node = root
        board_copy = copy.deepcopy(root_board)

        while node.children:
            node = node.best_child()
            board_copy.apply_move(node.move)

        legal_moves = board_copy.get_legal_moves('white')
        if legal_moves:
            for move in legal_moves:
                new_board = copy.deepcopy(board_copy)
                new_board.apply_move(move)
                node.children.append(Node(new_board, move, node))

        if node.children:
            node = random.choice(node.children)
            board_copy.apply_move(node.move)

        result = simulate_random_game(board_copy)

        while node:
            node.visits += 1
            node.wins += result
            node = node.parent

    if not root.children:
        print("⚠️ MCTS found no legal moves.")
        return None

    best = max(root.children, key=lambda child: child.visits)
    return best.move

def simulate_random_game(board):
    for _ in range(5):
        moves = board.get_legal_moves('white')
        if not moves:
            return 0
        move = random.choice(moves)
        board.apply_move(move)
    return 1
