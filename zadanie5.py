import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\zdjecie_kota.jpg")
image_gray = cv2.imread(r"C:\Users\Student\Desktop\zdjecie_kota_szare.jpg")

cv2.imshow("Obraz 1", image)
cv2.imshow("Obraz 2", image_gray)

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('1'):
        cv2.destroyWindow("Obraz 1")
    elif key == ord('2'):
        cv2.destroyWindow("Obraz 2")
