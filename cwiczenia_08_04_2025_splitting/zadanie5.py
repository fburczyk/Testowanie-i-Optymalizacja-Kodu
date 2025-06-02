import cv2
import numpy as np

image = cv2.imread('car.jpg')
(B, G, R) = cv2.split(image)

red_mask = (R > 100) & (G < 80) & (B < 80)
red_mask = red_mask.astype(np.uint8) * 255

R_boosted = np.where(red_mask > 0, np.clip(R + 80, 0, 255), R).astype(np.uint8)

result = cv2.merge([B, G, R_boosted])
cv2.imshow('Original image', image)
cv2.imshow('Red mask', result)
cv2.waitKey(0)
cv2.destroyAllWindows()