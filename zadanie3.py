import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\Testowanie-i-Optymalizacja-Kodu\szczeniak.jpg")
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
(b,g,r) = image[cX,cY]
print(f"Middle: {cX}, {cY}. Color red: {r}, green: {g}, blue: {b} ")
