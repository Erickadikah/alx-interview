n = int(input("Enter the value of n:"))

# the board
board = [[ 0 for i in range(n)] for i in range(n)]
# for row in board:
#     print(row)

def check_column(board, row, column):
    """board: 2D representation of current state of chessboard
        row: an iterger representing the row number of the board that we are currently placing
        solution: list that stores all the valid soluions
    """
    for i in range(row, -1, -1):
        if board[i][column]==1:
            return False
    return True

def check_diagonal(board, row, column):
    """
    #function for diagonal
    """
    for i, j in zip(range(row,-1,-1), range(column,-1,-1)):
        if board[i][j]==1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, n)):
        if board[i][j]==1:
            return False
    return True


#backtracking fucntion
def nqn(board, row):
    if row==n:
        return True
    
    for i in range(n):
        if(check_column(board, row, i)==True and check_diagonal(board, row, i)==True):
            board[row][i]=1
            if nqn(board, row+1):
                return True
            board[row][i]=0

    return False
    
nqn(board,0)

for row in board:
    print(row)
