import cv2
import numpy as np

triangle = np.zeros((300, 300), dtype="uint8")

# Define triangle points
pts = np.array([[20,275], [20, 20], [275, 275]], dtype=np.int32)

# Reshape for drawContours: needs (n_points, 1, 2)
pts = pts.reshape((-1, 1, 2))
cv2.drawContours(triangle, [pts], contourIdx=0, color=255, thickness=-1)
cv2.imshow("Triangle", triangle)

# draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150,150), 100, 255, -1)
cv2.imshow("Circle", circle)

bitwise_and = cv2.bitwise_and(triangle, circle)
bitwise_or = cv2.bitwise_or(triangle, circle)
bitwise_xor = cv2.bitwise_xor(triangle, circle)
bitwiseTriNot = cv2.bitwise_not(triangle)
bitwiseCirNot = cv2.bitwise_not(circle)

cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT triangle", bitwiseTriNot)
cv2.imshow("Bitwise NOT circle", bitwiseCirNot)

cv2.waitKey(0)
cv2.destroyAllWindows()
