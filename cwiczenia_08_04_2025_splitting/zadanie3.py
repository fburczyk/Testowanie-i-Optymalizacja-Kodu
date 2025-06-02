import cv2
import numpy as np

image=cv2.imread('car.jpg')
(B, G, R) = cv2.split(image)

marged = cv2.merge([R,G,B])

zero_chanel = np.zeros_like(B)
marged2 = cv2.merge([zero_chanel, G,R])

cv2.imshow('Original image', image)
cv2.imshow('Merged image with changed channels', marged)
cv2.imshow('Merged image with one channel set to 0', marged2)
cv2.waitKey(0)
cv2.destroyAllWindows()