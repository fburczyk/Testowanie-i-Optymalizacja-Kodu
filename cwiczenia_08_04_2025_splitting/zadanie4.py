import cv2
import numpy as np

image = cv2.imread('car.jpg')
(B, G, R) = cv2.split(image)
R = cv2.add(R,50)

merged = cv2.merge((B,G,R))

cv2.imshow('Original image', image)
cv2.imshow('Merged image with increased intensity channel ', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

