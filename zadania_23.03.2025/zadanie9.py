import cv2
import imutils

image = cv2.imread("plaza.jpg")

rotated = imutils.rotate(image,75)

cv2.imwrite("rotated_output.jpg",rotated)

cv2.imshow("A",rotated)
cv2.waitKey(0)