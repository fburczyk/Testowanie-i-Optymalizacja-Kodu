import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\Testowanie-i-Optymalizacja-Kodu\szczeniak.jpg")
(h, w) = image.shape[:2]

new_h = h // 3
new_w = w // 3

middle_slice = image[new_h:2*new_h, new_w:2*new_w]

cv2.imshow("Changed", middle_slice)
cv2.waitKey(0)
cv2.destroyAllWindows()