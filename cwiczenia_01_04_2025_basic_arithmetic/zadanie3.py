import cv2
import numpy as np

image = cv2.imread('puppy.jpg')

numpy_darkened = image - 80
opencv_darkened = cv2.subtract(image, np.ones(image.shape, dtype=np.uint8) * 80)

cv2.imshow('Darkened image by opencv', opencv_darkened)
cv2.imshow('Darkened image by numpy', numpy_darkened)

cv2.waitKey(0)
cv2.destroyAllWindows()
