import cv2
import imutils

image = cv2.imread("plaza.jpg")

for angle in range(0,361,15):
    rotated = imutils.rotate(image, angle)
    cv2.imshow("Rotated", rotated)

    cv2.waitKey(500)
cv2.waitKey(0)