import cv2
import numpy as np
import easyocr

# Function to order the points in the contour
def order_points(pts):
    rect = np.zeros((4, 2), dtype = "float32")

    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect

image = cv2.imread('s2.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150, apertureSize = 3)

# Find contours - to detect the Sudoku grid
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

# Approximate the contour to a polygon (means if detection have more than four edge converting it into four edge)
polygon = cv2.approxPolyDP(contours[0], 0.01*cv2.arcLength(contours[0], True), True)

# If the polygon has 4 vertices, apply a perspective transformation (tilted image to square form)
if len(polygon) == 4:
    src = polygon.reshape(4, 2).astype(np.float32)
    src = order_points(src)
    dst = np.array([[0, 0], [449, 0], [449, 449], [0, 449]], dtype="float32")
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(image, M, (450, 450))

cropped = warped[0:450, 0:450] # Crop the image to the Sudoku grid

# If Want to save the cropped image
cv2.imwrite('sudoku_cropped.jpg', cropped)

reader = easyocr.Reader(['en'])

sudoku_grid = []
# Divide the image into 9 rows
for i in range(9):
    row = []
    for j in range(9):
        # Divide each row into 9 cells
        cell = cropped[i*50:(i+1)*50, j*50:(j+1)*50]
        cell = cv2.resize(cell, (128, 128))
        cv2.imwrite(f'cell_{i}_{j}.jpg', cell)
        result = reader.readtext(cell, allowlist='123456789') 
        # print(f"Cell ({i}, {j}): {result}")
        if result:
            number = result[0][-2]
            row.append(int(number))
        else:
            row.append(' ')
    sudoku_grid.append(row)

for row in sudoku_grid:
    print(row)