import cv2

image = cv2.imread("plaza.jpg")

(h, w) = image.shape[:2]

cv2.imshow("Oryginal", image)

M = cv2.getRotationMatrix2D((0,0), 45, 1.0)

rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated by 30 Degrees", rotated)

cv2.waitKey(0)