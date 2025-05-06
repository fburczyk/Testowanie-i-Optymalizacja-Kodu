import cv2

image = cv2.imread("puppy.jpg")

kernel = (15, 15)
blured_kernel = cv2.blur(image, kernel)
blured_gauss = cv2.GaussianBlur(image, kernel, 0)
for k in (3, 9, 15):
    blured_median = cv2.medianBlur(image,k)
    cv2.imshow("Median {}".format(k), blured_median)
    cv2.waitKey(0)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = "Blurred d={}, sc={}, ss={}".format(
        diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)

cv2.imshow("Original", image)
cv2.imshow("Blurring kernel", blured_kernel)
cv2.imshow("Blurring Gauss", blured_gauss)
cv2.imshow("Blurring median", blured_median)

#1. Szum najlepiej usuwa rozmycie medianowe, ponieważ bierze medianę z dwóch sąsiedujących pikseli
#2. Najwięcej szczgółów zachowuje rozmycie dwustronne
#3. cv2.blur:
#       Zalety: szybka, prosta.
#       Wady: zamazuje wszystko jednakowo, tracone są szczegóły.
#   cv2.GaussianBlur:
#       Zalety: lepsze niż blur, mniej artefaktów, rozmywa bardziej naturalnie.
#       Wady: nadal gubi krawędzie i detale.
#   cv2.medianBlur:
#       Zalety: zachowuje krawędzie
#       Wady: może wprowadzać nienaturalne kształty przy wyższych kernelach.
#   cv2.bilateralFilter:
#       Zalety: zachowuje krawędzie, dobra jakość rozmycia.
#       Wady: wolniejsza, bardziej zasobożerna.

cv2.waitKey(0)
cv2.destroyAllWindows()
