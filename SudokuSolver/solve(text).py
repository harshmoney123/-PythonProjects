import pprint
import math

# solve.py
# returns false if can't solve, returns true if can solve
def solve(bo):
    find = find_empty(bo)
    if find :
        row, col = find
    else :
        return True

    for i in range(1,10):
        bo[row][col] = i
        valid = test_valid(bo, row, col)
        if (valid):
            solve_board = solve(bo)
            if (solve_board):
                return True
    
    ## unsolvable board
    return False

    # find the next row and col
    # if find returns the end, then we have solved it, return true
    # else, try each number
    # if it eventually solves the board with that random number, return true
    # else return false, (which recursively will solve the board)


# returns a tuple for then next empty square
# returns None if there is no empty square
def find_empty(bo):
    for row in range(len(bo)):
        for col in range (len(bo[row])):
            if bo[row][col] == 0:
                return row, col
    return None

def test_valid(bo, row, col):
    return test_row(bo, row) and test_col(bo, col) and test_square(bo, row, col)

## Tests row for validity
def test_row(bo, row):
    row_test = [True for j in range(9)]
    for col in range(len(bo[row])):
        if bo[row][col] > 0:
            if row_test[bo[row][col]-1]:
                row_test[bo[row][col]-1] = False
            else :
                 return False
    return True

## Tests column for validity
def test_col(bo, col):
    col_test = [True for j in range(9)]
    for row in range(len(bo)):
        square_val = bo[row][col]
        if square_val > 0:
            if col_test[square_val-1]:
                col_test[square_val-1] = False
            else :
                return False
    return True

# Tests sqaure for validity
def test_square(bo, row, col):
    row_by_3 = math.floor(row/3)*3
    col_by_3 = math.floor(col/3)*3
    square_test = [True for j in range(9)]
    for i in range(row_by_3, row_by_3+3):
        for j in range(col_by_3, col_by_3+3):
            square_val = bo[i][j]
            if square_val > 0:
                if square_test[square_val-1]:
                    square_test[square_val-1] = False
                else :
                    return False
    return True

# Prints sudoku board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")

board = [
    [1, 0, 5, 3, 2, 7, 6, 9, 8],
 [8, 3, 9, 6, 5, 4, 1, 2, 7],
 [6, 7, 2, 9, 1, 8, 5, 0, 3],
 [4, 9, 0, 1, 8, 5, 3, 7, 2],
 [2, 1, 8, 4, 7, 3, 9, 0, 6],
 [7, 5, 3, 2, 9, 0, 4, 8, 1],
 [0, 6, 7, 5, 4, 2, 8, 0, 9],
 [9, 8, 0, 7, 6, 1, 2, 3, 5],
 [5, 2, 1, 8, 3, 9, 0, 6, 4]
]

print_board(board)
print(solve(board))
print_board(board)