# Making Sudoku Solver Web app.

## Dependencies

- OpenCV
- EasyOCR
- Python 3.x
- Web Technologies : HTML, CSS, JavaScript

# 1. Sudoku Image to Digital Array Converter

- The file named `sudoku.py`, which is aimed at converting Sudoku images into digital arrays, focusing on essential component of a larger Sudoku solver application. 

## Overview

- The process involves capturing a Sudoku puzzle image via a camera.

<img src="https://cdn.jsdelivr.net/gh/shubhamparmar1/Sudoku-Image-to-Digital-Array-Converter/images/s2.png" alt="Captured image" width="200px" height="200px"/>

- Utilizing OpenCV to detect the puzzle's four points, rectifying the image into a square, and subsequently cropping it.

<img src="https://cdn.jsdelivr.net/gh/shubhamparmar1/Sudoku-Image-to-Digital-Array-Converter/images/sudoku_cropped.jpg" alt="Cropped image" width="200px" height="200px"/>

- The cropped image is then segmented into a 9x9 grid, resulting in 81 individual sub-images, each corresponding to a Sudoku block.

<img src="https://cdn.jsdelivr.net/gh/shubhamparmar1/Sudoku-Image-to-Digital-Array-Converter/images/image.png" alt="Cut block of sudoku" width="200px" height="200px"/>


- The EasyOCR library is employed to recognize and extract the numerical content from each block, ultimately producing a digital representation of the Sudoku puzzle.

Output:
- [' ', ' ', ' ', ' ', 4, ' ', ' ', ' ', ' '] <br>
[8, ' ', 1, ' ', ' ', ' ', 3, ' ', 7] <br>
[' ', ' ', 4, 8, ' ', 2, 6, ' ', ' '] <br>
[2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', 4] <br>
[' ', ' ', 8, 5, ' ', 6, 1, ' ', ' '] <br>
[' ', ' ', ' ', ' ', 8, ' ', ' ', ' ', ' '] <br>
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] <br>
[' ', ' ', 5, 2, ' ', 9, 7, ' ', ' '] <br>
[' ', 6, 3, 4, ' ', 7, 2, 5, ' '] <br>

# 2. Solving this sudoku.

- The `sudoku_solver.py` file offers a streamlined solution for solving arrays of Sudoku puzzles. With a focus on simplicity and efficiency, this Python script provides a reliable tool for automating the resolution of Sudoku grids.
- The `visualize.py` file dynamically generates and overlays solved Sudoku solutions onto images of the original puzzles, enhancing the user's understanding and providing a clear visual representation of the solved grids.


# 3. Making Web App.

- This Sudoku Solver Web App is a professional-grade implementation leveraging web technologies such as HTML, CSS, and JavaScript. It provides an intuitive and efficient platform for solving Sudoku puzzles with a user-friendly interface, ensuring a seamless and enjoyable experience for enthusiasts.
## Preview of Website for Sudoku Solver.

<img alt="Preview" width="650px" src="https://github.com/shubhamparmar1/Sudoku-Solver/assets/134207725/fca7dbc0-d1e2-4144-b836-8045523360b9">

## Contribution

Contributions to enhance and optimize the code are welcome. Feel free to open an issue or submit a pull request.
