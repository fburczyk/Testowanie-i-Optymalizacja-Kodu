import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")

square_size = 100
radius = 30

top_left = ((canvas.shape[1] - square_size) // 2, (canvas.shape[0] - square_size) // 2)
bottom_right = (top_left[0] + square_size, top_left[1] + square_size)

center = (canvas.shape[1] // 2, canvas.shape[0] // 2)

cv2.rectangle(canvas, top_left, bottom_right, (255,255,255), 2)
cv2.circle(canvas, center, radius, (255, 0, 0), 1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)