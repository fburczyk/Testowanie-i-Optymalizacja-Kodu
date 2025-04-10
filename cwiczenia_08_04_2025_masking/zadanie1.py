import cv2
import numpy as np

image = cv2.imread('face.jpg')

mask = np.zeros(image.shape[:2], dtype="uint8")

cv2.circle(mask,(510,215), 100,255,-1)
masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original image', image)
cv2.imshow("Mask Applied to Image", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()