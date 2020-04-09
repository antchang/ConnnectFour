# ConnnectFour
Connect Four Game played versus another player or AI Computer 

Play a game of Connect Four versus a friend or an AI Player. 

To play a game versus a friend type in console:
connect_four(Player('X'), Player('O'))

An AI player has a mechanic called "lookahead" where it analyzes the current
state of the board and thinks in advance of what would the best move be. A 
higher lookahead value means the AI looks more moves in advance. The AI 
also has a tie-breaking strategy to determine it's move out of all possible best 
moves if there are multiple best moves. 

To play a game versus an AI player that has a lookahead value of 3 and 
a random tie breaking strategy:
connect_four(Player('X'), AIPlayer('O', 'RANDOM', 3))

To watch 2 AI Players play each other where each has a lookahead value of 3
and a random tie breaking strategy:
connect_four(AIPlayer('X', 'RANDOM', 3), AIPlayer('O', 'RANDOM', 3))
