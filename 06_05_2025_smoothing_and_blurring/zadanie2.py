import cv2

image = cv2.imread('puppy.jpg')

kernel_sizes = [3,5,9,15]

#basic blur
for k in kernel_sizes:
    blurred = cv2.blur(image,(k,k))
    cv2.imshow(f"Blurred {k}", blurred)
    cv2.waitKey(0)

#GaussianBlur
for k in kernel_sizes:
    blurred_gaussian = cv2.GaussianBlur(image, (k,k), 0)
    cv2.imshow(f"Blurred Gauss {(k,k)}",blurred_gaussian)
    cv2.waitKey(0)

#medianBlur
for k in kernel_sizes:
    blurred_median = cv2.medianBlur(image,k)
    cv2.imshow(f"Blurred Median {k}", blurred_median)
    cv2.waitKey(0)

#bilateralFilter
for k in kernel_sizes:
    blurred_bilateral = cv2.bilateralFilter(image,k,75,75)
    cv2.imshow(f"Bilateral {k}",blurred_bilateral)
    cv2.waitKey(0)
cv2.imshow('Original', image)

#1. Im większy kernel tym większe rozmycie. Dla prostego i Gaussowego obraz staje się nie wyrażny.
#2. 5x5 lub 9x9

cv2.waitKey(0)
cv2.destroyAllWindows()