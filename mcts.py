import random
from evaluate import evaluate_board

class MCTSNode:
    def __init__(self, board, parent=None, move=None):
        self.board = board.copy()
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.value = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.board.get_legal_moves())

    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.value / (child.visits or 1)) + c_param * ((2 * (self.visits or 1)) ** 0.5 / (child.visits or 1))
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

def select_promising_node(node):
    while node.children:
        node = node.best_child()
    return node

def expand_node(node):
    tried_moves = [child.move for child in node.children]
    legal_moves = node.board.get_legal_moves()
    for move in legal_moves:
        if move not in tried_moves:
            new_board = node.board.copy()
            new_board.make_move(move)
            child_node = MCTSNode(new_board, parent=node, move=move)
            node.children.append(child_node)
            return child_node
    return node

def simulate_random_playout(board):
    temp_board = board.copy()
    max_turns = 20
    while not temp_board.is_game_over() and max_turns > 0:
        legal_moves = temp_board.get_legal_moves()
        if not legal_moves:
            break

        capture_moves = [m for m in legal_moves if temp_board.board[8 - int(m[3])][ord(m[2]) - ord('a')] != '.']
        move = random.choice(capture_moves if capture_moves else legal_moves)
        temp_board.make_move(move)
        temp_board.turn = 'black' if temp_board.turn == 'white' else 'white'
        max_turns -= 1

    if temp_board.is_checkmate():
        return 100 if temp_board.turn == 'black' else -100
    return evaluate_board(temp_board)

def backpropagate(node, result):
    while node:
        node.visits += 1
        node.value += result
        node = node.parent

def find_best_move_mcts(board, simulations=100, prefer_captures=False):
    root = MCTSNode(board)

    for _ in range(simulations):
        promising_node = select_promising_node(root)
        if not promising_node.board.is_game_over():
            node_to_explore = expand_node(promising_node)
            playout_result = simulate_random_playout(node_to_explore.board)
            backpropagate(node_to_explore, playout_result)

    best_move = None
    best_value = float('-inf')
    for child in root.children:
        if prefer_captures:
            start = (8 - int(child.move[1]), ord(child.move[0]) - ord('a'))
            end = (8 - int(child.move[3]), ord(child.move[2]) - ord('a'))
            captured_piece = board.board[end[0]][end[1]]
            is_capture = captured_piece != '.' and (captured_piece.isupper() != board.board[start[0]][start[1]].isupper())
        else:
            is_capture = False

        score = child.value / (child.visits or 1)
        if prefer_captures and is_capture:
            score += 1  # Incentivize capturing moves
        if score > best_value:
            best_value = score
            best_move = child.move

    return best_move
