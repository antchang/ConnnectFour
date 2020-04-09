import random  
from Game import *

class AIPlayer(Player):
    """AI Player inherits from Player"""

    def __init__(self, checker, tiebreak, lookahead):
        """constructor for AIPlayer"""

        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker)

        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """overrides repr"""

        return("Player " + self.checker + " (" + self.tiebreak +
               ", " + str(self.lookahead) + ")")

    def max_score_column(self, scores):
        """returns the index of the column with the max score"""

        maximum = max(scores)
        indicies = []
        
        for i in range(len(scores)):
            if maximum == scores[i]:
                indicies += [i]

        if self.tiebreak == "LEFT":
            return indicies[0]
        elif self.tiebreak == "RIGHT":
            return indicies[-1]
        else:
            randindex = random.choice(range(len(indicies)))
            return indicies[randindex]

    def scores_for(self, board):
        """determines AIPlayer's score for each column"""

        scores = [50] * board.width

        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak,
                                    self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                else:
                    scores[col] = 50
                board.remove_checker(col)

        return scores

    def next_move(self, board):
        """overrides next_move inherited from Player"""

        scores = self.scores_for(board)
        col = self.max_score_column(scores)
        self.num_moves += 1
        return col
        
    
