import cv2

image = cv2.imread('logo.png')

kernel_sizes = [3, 5, 9, 15]
bilateral_params = [(5, 50, 50), (9, 75, 75), (15, 100, 100)]

for k in kernel_sizes:
    blurred = cv2.blur(image, (k, k))
    cv2.imshow(f'Blurred {k}',blurred)
    cv2.waitKey(0)

for k in kernel_sizes:
    blurred = cv2.GaussianBlur(image, (k, k), 0)
    cv2.imshow(f'Blurred Gaussian ({k},{k})', blurred)
    cv2.waitKey(0)

for k in kernel_sizes:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Blurred median {k}", blurred)
    cv2.waitKey(0)

for d, sigmaColor, sigmaSpace in bilateral_params:
    result = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    cv2.imshow(f"Blurred bilateral {d,sigmaColor,sigmaSpace}", result)
    cv2.waitKey(0)
cv2.imshow("original", image)

#1. cv2.Blur i cv2.GaussianBlur
#2. Rozmycie medianowe i dwustronne

cv2.waitKey(0)
cv2.destroyAllWindows()