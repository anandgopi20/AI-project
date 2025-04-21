class Board:
    def __init__(self):
        self.state = self.create_initial_board()

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
        # Placeholder for legal move generation
        return [("e2", "e4"), ("d2", "d4")]

    def apply_move(self, move):
        # Placeholder for move application
        pass

    def evaluate(self):
        # Simple material count evaluation
        return 0
