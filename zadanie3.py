import cv2

image_gray = cv2.imread(r"C:\Users\Student\Desktop\zdjecie_kota.jpg",cv2.IMREAD_GRAYSCALE)
if image_gray.ndim == 2:
    print("Obraz w skali szarości, liczba kanałów: 1")
else:
    print(f"Obraz kolorowy, liczba kanałów: {image_gray.ndim}")
cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()