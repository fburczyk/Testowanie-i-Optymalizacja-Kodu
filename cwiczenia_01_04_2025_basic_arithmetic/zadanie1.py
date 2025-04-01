import cv2
import numpy as np

image = cv2.imread('puppy.jpg')

numpy_brightened = image + 50

opencv_brightened = cv2.add(image, np.ones(image.shape, dtype=np.uint8) * 50)

cv2.imshow('image', image)
cv2.imshow('numpy ', numpy_brightened)
cv2.imshow('opencv', opencv_brightened)

cv2.waitKey(0)
cv2.destroyAllWindows()