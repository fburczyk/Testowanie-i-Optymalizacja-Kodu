import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\Testowanie-i-Optymalizacja-Kodu\szczeniak.jpg")
cv2.imshow("Original", image)

image[50:100, 50:100] = (255, 255, 255)

cv2.imshow("Changed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()