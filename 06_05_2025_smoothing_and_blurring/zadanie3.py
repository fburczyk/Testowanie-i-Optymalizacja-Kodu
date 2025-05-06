import cv2

image = cv2.imread("photo.jpg")

bilateral_params = [
    (5, 50, 50),
    (9, 75, 75),
    (15, 100, 100)
]
for d, sigmaColor, sigmaSpace in bilateral_params:
    result = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    cv2.imshow("Bilateral", result)
    cv2.waitKey(0)

blur = cv2.blur(image, (9, 9))
cv2.imshow("Blur", blur)

gauss = cv2.GaussianBlur(image, (9, 9), 0)
cv2.imshow("Gaussian", gauss)

median = cv2.medianBlur(image, 9)
cv2.imshow("Median", median)

cv2.imshow('Original', image)

#1. Rozmycie dwustronne sktecznie redukuje szum
#2. Zdecydowanie tak, nie rozmywa tak krawędzi jak blur
#3. Dla typowego obrazu z szumem - d = 9, sigmaColor = 75, sigmaSpace = 75 daje dobry kompromis między wygładzeniem a zachowaniem szczegółów.
cv2.waitKey(0)
cv2.destroyAllWindows()