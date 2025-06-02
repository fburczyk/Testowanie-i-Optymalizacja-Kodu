import cv2
import numpy as np

image = cv2.imread('logo.png')

b,g,r = cv2.split(image)

swapped = cv2.merge([r,g,b])

without_red = cv2.merge([g,b,np.zeros_like(r)])
cv2.imshow('Original image', image)
cv2.imshow('Swapped image', swapped)
cv2.imshow('Image without red', without_red)
cv2.waitKey(0)
cv2.destroyAllWindows()
