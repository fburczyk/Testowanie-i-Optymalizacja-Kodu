import cv2
import imutils

image = cv2.imread("plaza.jpg")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

rotated_by_imutils = imutils.rotate(image, 60)
cv2.imshow("Rotated by cv2.warpAffine", rotated)
cv2.imshow("Rotated by imutils.rotate", rotated_by_imutils)

cv2.waitKey(0)
