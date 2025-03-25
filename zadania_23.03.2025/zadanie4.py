import cv2


image = cv2.imread("plaza.jpg")

rotate_degree = int(input("Podaj kąt rotacji: "))

cv2.imshow("Oryginal", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), rotate_degree, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow(f"Rotated by {rotate_degree} Degrees", rotated)

cv2.waitKey(0)