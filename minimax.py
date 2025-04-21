def minimax_decision(board, depth, maximizing=True):
    def minimax(board, depth, alpha, beta, maximizing):
        if depth == 0:
            return board.evaluate(), None
        moves = board.get_legal_moves('white' if maximizing else 'black')
        best_move = None
        if maximizing:
            max_eval = float('-inf')
            for move in moves:
                board.apply_move(move)
                eval, _ = minimax(board, depth-1, alpha, beta, False)
                board.undo_move(move)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in moves:
                board.apply_move(move)
                eval, _ = minimax(board, depth-1, alpha, beta, True)
                board.undo_move(move)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    _, best_move = minimax(board, depth, float('-inf'), float('inf'), maximizing)
    return best_move
