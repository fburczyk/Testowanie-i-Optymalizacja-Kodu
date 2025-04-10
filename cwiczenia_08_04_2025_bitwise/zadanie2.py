import cv2
import numpy as np


circle1 = np.zeros((300,300), dtype = "uint8")
cv2.circle(circle1, (150,150), 100, 255, -1)

circle2 = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle2, (150,150), 110, 255, -1)

bitwise_xor = cv2.bitwise_xor(circle1, circle2)


cv2.imshow("Circle1", circle1)
cv2.imshow("Circle2", circle2)
cv2.imshow("bitwise_xor", bitwise_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
