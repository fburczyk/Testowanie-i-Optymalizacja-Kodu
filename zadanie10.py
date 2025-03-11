import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\Testowanie-i-Optymalizacja-Kodu\szczeniak.jpg")
(b1, g1, r1) = image[50, 50]
(b2, g2, r2) = image[200, 200]

print(f"Pixel at (50,50) - Red: {r1}, Green: {g1}, Blue: {b1}")
print(f"Pixel at (200,200) - Red: {r2}, Green: {g2}, Blue: {b2}")
print(f"Difference at Red: {abs(r1-r2)}, Green: {abs(g1-g2)}, Blue: {abs(b1-b2)}")
