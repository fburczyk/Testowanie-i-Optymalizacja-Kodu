import cv2
import numpy as np

image = cv2.imread("plaza.jpg")

height, width = image.shape[:2]

M = np.float32([
    [1, 0, width//2],
    [0, 1, height//2]
])

shifted = cv2.warpAffine(image, M, (width,height))
cv2.imshow("Shifted", shifted)
cv2.waitKey()
cv2.destroyAllWindows()