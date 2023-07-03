def backtrack(board, col):
    # base case
    if col >= len(board[0]):
        return True
    # Iterate all possible candidates
    for i in range(len(board[0])):
        #isValid
        if isValid(board, i, col):
            # place
            board[i][col] = 1
            # recursive
            if backtrack(board, col+1) == True:
                return True
            # backtrack
            board[i][col] = 0
    return False
def isValid(board, row, col):
    for i in range(len(board[0])):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board[0]),1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
# O(n^n) time