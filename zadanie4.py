import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\Testowanie-i-Optymalizacja-Kodu\szczeniak.jpg")
(h, w) = image.shape[:2]

def podaj_wspolrzedne():
    while True:
        x = int(input("Podaj x: "))
        y = int(input("Podaj y: "))

        if 0 <= x < w and 0 <= y < h:
            return (x, y)
        else:
            print("Wartość poza zakresem, spróbuj ponownie")
(x,y) = podaj_wspolrzedne()
image[y,x] = (0, 0,0)
cv2.imshow("Changed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
