import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\Testowanie-i-Optymalizacja-Kodu\szczeniak.jpg")
(h, w) = image.shape[:2]
(x,y) = w // 2, h // 2
half_size = 50
start_x = x - half_size
start_y = y - half_size

image[start_y:start_y + 100, start_x:start_x + 100] = (0, 0, 255)

cv2.imshow("Changed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()