import cv2
from sudoku import generate_sudoku_board, image_ip
from sudoku_solver import sudoku_solver_sp

def write_solution_on_image(image, board, original_board):
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0 and original_board[i][j] == 0:
                cv2.putText(image, str(board[i][j]), (j*50+20, i*50+40), font, 1, (150, 150, 0), 2, cv2.LINE_AA)
    return image

# # get the cropped image
# cropped_image = image_ip('s2.png')

# # get the sudoku board
# original_board = generate_sudoku_board(cropped_image)

# # make a copy of the original board to solve
# board = [row.copy() for row in original_board]

# # solve the sudoku
# if sudoku_solver_sp(board):
#     print("Sudoku solved!")
#     # write the solution on the image
#     image_with_solution = write_solution_on_image(cropped_image, board, original_board)
#     cv2.imwrite('sudoku_solution.jpg', image_with_solution)  # save the image with the solution
# else:
#     print("No solution exists")


def solve_sudoku_from_image(image_path):
    # Load the image
    cropped_image = image_ip(image_path)

    # Get the sudoku board
    original_board = generate_sudoku_board(cropped_image)

    # Make a copy of the original board to solve
    board = [row.copy() for row in original_board]

    # Solve the sudoku
    if sudoku_solver_sp(board):
        print("Sudoku solved!")
        # Write the solution on the image
        solved_image = write_solution_on_image(cropped_image, board, original_board)

        # Save the solved Sudoku image
        solved_image_path = 'static/uploads/sudoku_solution.jpg'
        cv2.imwrite(solved_image_path, solved_image)

        # Return the path of the solved Sudoku image
        return solved_image_path
    else:
        print("No solution exists")
        return None