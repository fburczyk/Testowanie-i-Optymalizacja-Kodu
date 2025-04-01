import cv2
import numpy as np

image = cv2.imread('puppy.jpg')

numpy_overexposed = image+150

opencv_overexposed= cv2.add(image, np.ones(image.shape, dtype=np.uint8) * 150)

cv2.imshow('Overexpose numpy', numpy_overexposed)
cv2.imshow('Overexpose opencv', opencv_overexposed)

cv2.waitKey(0)
cv2.destroyAllWindows()