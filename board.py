
class Board:
    def __init__(self):
        self.board = self.initialize_board()
        self.turn = 'white'

    def initialize_board(self):
        return [
            list("rnbqkbnr"),
            list("pppppppp"),
            list("........"),
            list("........"),
            list("........"),
            list("........"),
            list("PPPPPPPP"),
            list("RNBQKBNR")
        ]

    def copy(self):
        new_board = Board()
        new_board.board = [row[:] for row in self.board]
        new_board.turn = self.turn
        return new_board

    def make_move(self, move):
        start_row = 8 - int(move[1])
        start_col = ord(move[0]) - ord('a')
        end_row = 8 - int(move[3])
        end_col = ord(move[2]) - ord('a')

        piece = self.board[start_row][start_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = '.'
        self.turn = 'black' if self.turn == 'white' else 'white'

    def is_valid_move(self, move):
        return move in self.get_legal_moves()

    def get_legal_moves(self):
        moves = []
        direction = -1 if self.turn == 'white' else 1
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece == '.':
                    continue
                is_white = piece.isupper()
                if (is_white and self.turn == 'white') or (not is_white and self.turn == 'black'):
                    if piece.upper() == 'P':
                        if 0 <= r + direction < 8 and self.board[r + direction][c] == '.':
                            moves.append(f"{chr(c + 97)}{8 - r}{chr(c + 97)}{8 - (r + direction)}")
                        for dc in [-1, 1]:
                            if 0 <= c + dc < 8 and 0 <= r + direction < 8:
                                target = self.board[r + direction][c + dc]
                                if target != '.' and (target.isupper() != is_white):
                                    moves.append(f"{chr(c + 97)}{8 - r}{chr(c + dc + 97)}{8 - (r + direction)}")
                    elif piece.upper() == 'N':
                        for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < 8 and 0 <= nc < 8:
                                target = self.board[nr][nc]
                                if target == '.' or target.isupper() != is_white:
                                    moves.append(f"{chr(c + 97)}{8 - r}{chr(nc + 97)}{8 - nr}")
                    elif piece.upper() == 'B':
                        moves.extend(self.get_sliding_moves(r, c, is_white, [(-1, -1), (-1, 1), (1, -1), (1, 1)]))
                    elif piece.upper() == 'R':
                        moves.extend(self.get_sliding_moves(r, c, is_white, [(-1, 0), (1, 0), (0, -1), (0, 1)]))
                    elif piece.upper() == 'Q':
                        moves.extend(self.get_sliding_moves(r, c, is_white, [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]))
                    elif piece.upper() == 'K':
                        for dr in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                if dr == 0 and dc == 0:
                                    continue
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < 8 and 0 <= nc < 8:
                                    target = self.board[nr][nc]
                                    if target == '.' or target.isupper() != is_white:
                                        moves.append(f"{chr(c + 97)}{8 - r}{chr(nc + 97)}{8 - nr}")
        return moves

    def get_sliding_moves(self, r, c, is_white, directions):
        moves = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                target = self.board[nr][nc]
                if target == '.':
                    moves.append(f"{chr(c + 97)}{8 - r}{chr(nc + 97)}{8 - nr}")
                elif target.isupper() != is_white:
                    moves.append(f"{chr(c + 97)}{8 - r}{chr(nc + 97)}{8 - nr}")
                    break
                else:
                    break
                nr += dr
                nc += dc
        return moves

    def is_in_check(self, color):
        king = 'K' if color == 'white' else 'k'
        king_pos = None
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == king:
                    king_pos = (r, c)
                    break
        if not king_pos:
            return False
        temp_board = self.copy()
        temp_board.turn = 'black' if color == 'white' else 'white'
        opponent_moves = temp_board.get_legal_moves()
        return any((8 - int(m[3]), ord(m[2]) - ord('a')) == king_pos for m in opponent_moves)

    def is_checkmate(self):
        return self.is_in_check(self.turn) and not self.get_legal_moves()

    def is_game_over(self):
        return self.is_checkmate() or not self.get_legal_moves()
