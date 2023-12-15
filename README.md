# Sudoku Image to Digital Array Converter

This project is aimed at converting Sudoku images into digital arrays, focusing on essential component of a larger Sudoku solver application.

## Overview

The process involves capturing a Sudoku puzzle image via a camera, utilizing OpenCV to detect the puzzle's four points, rectifying the image into a square, and subsequently cropping it. The cropped image is then segmented into a 9x9 grid, resulting in 81 individual sub-images, each corresponding to a Sudoku block. The EasyOCR library is employed to recognize and extract the numerical content from each block, ultimately producing a digital representation of the Sudoku puzzle.

## Usage

To use the Sudoku Image to Digital Array Converter, follow these steps:

1. Capture an image of the Sudoku puzzle using a camera.
2. Run the provided Python code, which employs OpenCV for image processing and EasyOCR for optical character recognition.
3. Obtain the digital representation of the Sudoku puzzle as an array.

## Dependencies

- OpenCV
- EasyOCR
- Python 3.x

## Contribution

Contributions to enhance and optimize the code are welcome. Feel free to open an issue or submit a pull request.


