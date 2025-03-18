import cv2
import numpy as np

blue = (255, 0, 0)
red = (0,0,255)
canvas = np.zeros((400, 400, 3), dtype="uint8")
center = (40,40)

cv2.circle(canvas, center, 40, blue)

middle = (canvas.shape[1] // 2, canvas.shape[0] // 2)

cv2.circle(canvas, middle, 60, red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)