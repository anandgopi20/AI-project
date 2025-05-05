
from evaluate import evaluate_board

values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0}

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    legal_moves = board.get_legal_moves()

    # Sort: prioritize capturing moves by assigning higher weight to them
    def move_priority(move):
        to_row, to_col = 8 - int(move[3]), ord(move[2]) - ord('a')
        piece = board.board[to_row][to_col]
        return values.get(piece.upper(), 0) if piece != '.' else 0

    sorted_moves = sorted(legal_moves, key=move_priority, reverse=True)

    if maximizing_player:
        max_eval = float('-inf')
        for move in sorted_moves:
            board.make_move(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board.undo_move()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in sorted_moves:
            board.make_move(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board.undo_move()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def find_best_move_minimax(board, depth=3):
    _, best = minimax(board, depth, float('-inf'), float('inf'), board.turn == 'white')
    return best
