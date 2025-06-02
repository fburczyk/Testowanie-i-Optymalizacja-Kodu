import cv2
import numpy as np

image = cv2.imread("trees.jpg")

h, w = image.shape[:2]

mask = np.zeros((h, w), dtype=np.uint8)

foreground_poly = np.array([
    [0, 413],
    [203, 413],
    [203, 556],
    [0, 556]
], dtype=np.int32)

cv2.fillPoly(mask, [foreground_poly], 255)

mask_bg = cv2.bitwise_not(mask)

blurred = cv2.GaussianBlur(image, (21, 21), sigmaX=0, sigmaY=0)

background = cv2.bitwise_and(blurred, blurred, mask=mask_bg)

foreground = cv2.bitwise_and(image, image, mask=mask)

result = cv2.add(background, foreground)

cv2.imshow("Original", image)
cv2.imshow('Wynik (DOF)', result)
cv2.waitKey(0)
cv2.destroyAllWindows()