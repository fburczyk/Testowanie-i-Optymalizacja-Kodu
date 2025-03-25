import cv2
import imutils

image = cv2.imread("plaza.jpg")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
image_2 = imutils.rotate(image,90)

for i in range(3):
    M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
    image = cv2.warpAffine(image, M, (w, h))


cv2.imshow("Rotated by 30 degrees 3 times ",image)
cv2.imshow("Rotated by 90 degrees", image_2)
cv2.waitKey(0)