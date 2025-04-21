
class Board:
    def __init__(self):
        self.state = self.create_initial_board()
        self.move_history = []

    def create_initial_board(self):
        return [['R','N','B','Q','K','B','N','R'],
                ['P']*8,
                ['.']*8,
                ['.']*8,
                ['.']*8,
                ['.']*8,
                ['p']*8,
                ['r','n','b','q','k','b','n','r']]

    def print_board(self):
        for row in self.state:
            print(" ".join(row))

    def get_legal_moves(self, color):
        # Expanded pawn move logic with debug info
        direction = -1 if color == 'white' else 1
        pawn = 'P' if color == 'white' else 'p'
        legal_moves = []

        for row in range(8):
            for col in range(8):
                if self.state[row][col] == pawn:
                    next_row = row + direction
                    if 0 <= next_row < 8 and self.state[next_row][col] == '.':
                        start = f"{chr(col + ord('a'))}{8 - row}"
                        end = f"{chr(col + ord('a'))}{8 - next_row}"
                        legal_moves.append((start, end))
                        # Initial double-step
                        if (color == 'white' and row == 6) or (color == 'black' and row == 1):
                            next_row2 = row + 2 * direction
                            if self.state[next_row2][col] == '.':
                                end2 = f"{chr(col + ord('a'))}{8 - next_row2}"
                                legal_moves.append((start, end2))
        print(f"Legal moves ({color}):", legal_moves)
        return legal_moves

    def apply_move(self, move):
        src, dst = move
        src_row, src_col = 8 - int(src[1]), ord(src[0]) - ord('a')
        dst_row, dst_col = 8 - int(dst[1]), ord(dst[0]) - ord('a')
        piece = self.state[src_row][src_col]
        captured = self.state[dst_row][dst_col]

        self.move_history.append((src, dst, piece, captured))
        self.state[dst_row][dst_col] = piece
        self.state[src_row][src_col] = '.'

    def undo_move(self, move):
        if not self.move_history:
            return
        src, dst, piece, captured = self.move_history.pop()
        src_row, src_col = 8 - int(src[1]), ord(src[0]) - ord('a')
        dst_row, dst_col = 8 - int(dst[1]), ord(dst[0]) - ord('a')

        self.state[src_row][src_col] = piece
        self.state[dst_row][dst_col] = captured

    def evaluate(self):
        piece_values = {
            'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0,
            'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': 0
        }
        total = 0
        for row in self.state:
            for piece in row:
                total += piece_values.get(piece, 0)
        return total
