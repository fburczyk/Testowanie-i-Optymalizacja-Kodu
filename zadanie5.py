import cv2
import imutils

image = cv2.imread("plaza.jpg")

tx = int(input("Podaj przesunięcie w X (poziom): "))
ty = int(input("Podaj przesunięcie w Y (pion): "))

shifted = imutils.translate(image, tx,ty)

cv2.imshow("Original", image)
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
