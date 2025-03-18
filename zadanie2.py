import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")

green = (0, 255,0)
red = (0,0,255)

cv2.rectangle(canvas, (5,5), (105, 55), green)

top_left = (canvas.shape[1] - 100, canvas.shape[0] - 100)
bottom_right = (canvas.shape[1] - 1, canvas.shape[0] - 1)

cv2.rectangle(canvas, top_left, bottom_right, red,3 )


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)