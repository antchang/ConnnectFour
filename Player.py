from Board import Board

class Player:

    def __init__(self, checker):
        """constructs a Player object"""

        assert(checker == 'X' or checker == 'O')

        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """return a string representing a Player object"""

        return("Player " + self.checker)
    
    def opponent_checker(self):
        """returns the checker of the opponent Player object"""

        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """returns the column where the player wants to make the next move"""

        while True:
            col = int(input("Enter a column: "))
            if col >= 0 and col < board.width:
                break
            else:
                print("Try again!")
        
        self.num_moves += 1
        return col
            
