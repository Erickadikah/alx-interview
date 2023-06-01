# Prime Game

## Description:

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

For example, there are n=10  to choose from. Maria first picks 7 and removes it and its multiples from the set. In this case, Ben can pick any prime number from  to  and remove it and its multiples from the set. 2 and 3 are the only numbers left, and Maria loses. If instead Maria picks 5, Ben chooses 7 and removes it and its multiples from the set, leaving only 2 and 3. Maria then picks 2 and wins because Ben cannot make any more moves.