import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\Testowanie-i-Optymalizacja-Kodu\szczeniak.jpg")
(h, w) = image.shape[:2]
cv2.imshow("Orginal", image)
image[h-1,w-1] = (0, 0, 255)
cv2.imshow('Changed', image)
(b,g,r) = image[h-1,w-1]
print(f"Pixel at ({h-1},{w-1}) - Red: {r}, Green: {g}, Blue: {b}")

cv2.waitKey(0)
cv2.destroyAllWindows()
