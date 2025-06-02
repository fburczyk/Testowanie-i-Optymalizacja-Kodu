import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\Testowanie-i-Optymalizacja-Kodu\szczeniak.jpg")
(h, w) = image.shape[:2]

half_h = h // 2
half_w = w // 2

image[0:half_h, 0:half_w] = (255, 0, 0)

cv2.imshow("Changed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()