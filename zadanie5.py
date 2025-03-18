import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")

center = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(20,180,20):
    top_left = (center[0] - r // 2, center[1] - r // 2)
    bottom_right = (center[0] + r // 2, center[1] + r // 2)

    cv2.rectangle(canvas, top_left, bottom_right, white, 1)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)