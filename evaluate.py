def evaluate_board(board):
    values = {
        'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0
    }

    score = 0
    for row in board.board:
        for piece in row:
            if piece.isalpha():
                val = values.get(piece.upper(), 0)
                score += val if piece.isupper() else -val

    return round(score, 2)
