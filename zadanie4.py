import cv2
import numpy as np
import imutils

image = cv2.imread("plaza.jpg")

M = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))


translated_image_imutils = imutils.translate(image, 100, 50)

cv2.imshow("Shifted", translated_image_imutils)
cv2.imshow("Shifted", shifted)
cv2.waitKey()
cv2.destroyAllWindows()

