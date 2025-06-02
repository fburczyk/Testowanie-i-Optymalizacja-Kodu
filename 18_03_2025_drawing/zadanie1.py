import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

blue = (255, 0, 0)
start_point = (canvas.shape[1] // 2, canvas.shape[0] // 2)
end_point = (canvas.shape[1] - 1, canvas.shape[0] - 1)

cv2.line(canvas, start_point, end_point,blue, 3)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)