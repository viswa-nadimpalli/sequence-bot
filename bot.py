class Bot:
    def __init__(self, board, hand):
        self.board = board
        self.hand = hand

    def calc_score(self):
        #  0 1 0 0 1 = 2^2 = 4
        #  0 1 0 0 0 = 1 = 1
        #  0 1
        return sum(self.board)

    def generate_possibilities(self):
        pass

    