import numpy as np
import random

spots = {
    # spades:
    '2♠': [(0,1), (8,6)],
    '3♠': [(0,2), (8,5)],
    '4♠': [(0,3), (8,4)],
    '5♠': [(0,4), (8,3)],
    '6♠': [(0,5), (8,2)],
    '7♠': [(0,6), (8,1)],
    '8♠': [(0,7), (7,1)],
    '9♠': [(0,8), (6,1)],
    '10♠': [(1,9), (5,1)],
    'Q♠': [(2,9), (4,1)],
    'K♠': [(3,9), (3,1)],
    'A♠': [(4,9), (2,1)],

    # clubs:
    '2♣': [(1,4), (3,6)],
    '3♣': [(1,3), (3,5)],
    '4♣': [(1,2), (3,4)],
    '5♣': [(1,1), (3,3)],
    '6♣': [(1,0), (3,2)],
    '7♣': [(2,0), (4,2)],
    '8♣': [(3,0), (5,2)],
    '9♣': [(4,0), (6,2)],
    '10♣': [(5,0), (7,2)],
    'Q♣': [(6,0), (7,3)],
    'K♣': [(7,0), (7,4)],
    'A♣': [(8,0), (7,5)],
    
    # hearts:
    '2♥': [(5,4), (8,7)],
    '3♥': [(5,5), (8,8)],
    '4♥': [(4,5), (7,8)],
    '5♥': [(4,4), (6,8)],
    '6♥': [(4,3), (5,8)],
    '7♥': [(5,3), (4,8)],
    '8♥': [(6,3), (3,8)],
    '9♥': [(6,4), (2,8)],
    '10♥': [(6,5), (1,8)],
    'Q♥': [(6,6), (1,7)],
    'K♥': [(5,6), (1,6)],
    'A♥': [(4,6), (1,5)],

    # diamonds: 
    '2♦': [(2,2), (5,9)],
    '3♦': [(2,3), (6,9)],
    '4♦': [(2,4), (7,9)],
    '5♦': [(2,5), (8,9)],
    '6♦': [(2,6), (9,8)],
    '7♦': [(9,7), (2,7)],
    '8♦': [(9,6), (3,7)],
    '9♦': [(9,5), (4,7)],
    '10♦': [(9,4), (5,7)],
    'Q♦': [(9,3), (6,7)],
    'K♦': [(9,2), (7,7)],
    'A♦': [(9,1), (7,6)],
}

def print_board(spots):
    board = [['   ' for _ in range(10)] for _ in range (10)]

    for card, positions in spots.items():
        for pos in positions:
            row, col = pos
            board[row][col] = card
    
    cell_width = max(len(card) for card in spots.keys()) + 1

    header = "    " + "   ".join(f"{i:2}" for i in range(10))
    print(header)
    top_border = "   " + "+" + "-" * (len(header) - 1)
    print(top_border)

    for row_idx, row in enumerate(board):
        print(f"{row_idx:2} | " + ' '.join(f"{cell:{cell_width}}" for cell in row))
        print(f"   | ")

class SequenceEnv:
    def __init__(self):
        self.board = np.zeros((10, 10), dtype=int)
        self.current_player = 1
        self.deck = Deck()

    def reset(self):
        self.board = np.zeros((10, 10), dtype=int)
        self.hand = self.draw_hand()
        self.current_player = 1
        return self.board, self.hand
    
    def draw_hand(self):
        return [self.deck.draw() for _ in range(7)]
    
    def play(self, hand, idx, play):
        hand[idx] = self.deck.draw()
        self.board[play[0]][play[1]] = self.current_player
        self.current_player *= -1
        return hand
    
    def check_win_condition(self):
        return False
    

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_str(self):
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        return self.get_str()
    
    def to_spot(self):
        if self.rank == 'J':
            if self.suit == 'H' or self.suit == 'S':
                return 1
            return 2
        return spots[self.get_str()]

class Deck:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['H', 'D', 'C', 'S']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        cards2 = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.cards += cards2
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def len(self):
        return len(self.cards)


if __name__ == '__main__':
    seq = SequenceEnv()

    player1 = seq.draw_hand( )

    print(seq.draw_hand())

    print_board(spots)
