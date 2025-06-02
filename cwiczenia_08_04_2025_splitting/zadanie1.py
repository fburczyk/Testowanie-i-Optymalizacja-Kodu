import cv2
import numpy as np

image = cv2.imread('car.jpg')

(B, G, R) = cv2.split(image)

cv2.imwrite('car_B.jpg', B)
cv2.imwrite('car_G.jpg', G)
cv2.imwrite('car_R.jpg', R)


cv2.imshow('Original image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()