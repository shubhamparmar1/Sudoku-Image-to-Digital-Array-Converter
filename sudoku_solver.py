from sudoku import generate_sudoku_board # import the function from sudoku.py

def valid_sp(board, row, col, num):
    # check in row
    for x in range(9):
        if board[row][x] == num:
            return False

    # check in column
    for x in range(9):
        if board[x][col] == num:
            return False

    # check in 3*3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def sudoku_solver_sp(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if valid_sp(board, i, j, num):
                        board[i][j] = num
                        if sudoku_solver_sp(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# get the sudoku board
# board = generate_sudoku_board()

# # solve the sudoku
# if sudoku_solver_sp(board):
#     print("Sudoku solved!")
#     for row in board:
#         print(row)
# else:
#     print("No solution exists")