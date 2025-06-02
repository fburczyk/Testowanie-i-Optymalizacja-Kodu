import cv2
image_gray = cv2.imread(r"C:\Users\Student\Desktop\zdjecie_kota.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imwrite(r"C:\Users\Student\Desktop\zdjecie_kota_szare.jpg", image_gray)
cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()