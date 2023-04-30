# Nqueens

## Description

What is the N queens puzzle?
The N Queens problem is a classic puzzle that involves placing
N chess queens on an NxN chessboard so that
no two queens threaten each other.
In other words, no two queens should
be placed on the same row, column, or diagonal.

## My Nqueens solution Implementation Using Backtracking

The isinstance() function is used to check if n is an integer. If it is not an integer, the function prints the error message "N must be a number" and exits the program with a status code of 1 using the sys.exit(1) statement.

If n is an integer, the function checks if it is less than 4. If it is less than 4, the function prints the error message "N must be an integer greater than or equal to 4" and exits the program with a status code of 1 using the sys.exit(1) statement.

If n is a valid integer greater than or equal to 4, the function proceeds with solving the n Queens problem using the backtracking algorithm.

The backtrack() function takes three arguments: board, row, and solutions. board is a 2D list representing the chessboard. row is the current row being checked, and solutions is a list of all the solutions found so far.

If the current row is equal to n, this means that a valid solution has been found, and the board is appended to the solutions list using board.copy() to avoid modifying the original board.

If a valid solution has not been found, the function checks if it is possible to place a queen on the current row and column by calling the is_valid() function. If it is valid, the queen is placed on the board, and the function is called recursively with the next row (row+1). After the recursive call, the queen is removed from the board to backtrack and explore other possible solutions.

Finally, the function initializes the board and solutions lists, and calls the backtrack() function with the starting row of 0 to begin solving the n Queens problem.


## Usage
```sh

$ ./0-nqueens.py N
```Python
```
## Example
```sh
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Author

* **Erick Adikah** - [Erick Adikah](lau1088*happy)