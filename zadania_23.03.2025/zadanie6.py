import cv2
import imutils

image = cv2.imread("plaza.jpg")

cv2.imshow("Oryginal", image)

rotated = imutils.rotate_bound(image, -33)

cv2.imshow("Rotated by -33 Degrees", rotated)

cv2.waitKey(0)