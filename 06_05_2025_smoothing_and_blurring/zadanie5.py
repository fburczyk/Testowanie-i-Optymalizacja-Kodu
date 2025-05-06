import cv2
import numpy as np

image = cv2.imread("puppy.jpg")

noise = np.zeros(image.shape, np.uint8)

cv2.randn(noise,0,200)

noisy_image = cv2.add(image,noise)
kernel_size = [3, 5, 9, 15]
bilateral_params = [(5, 50, 50), (9, 75, 75), (15, 100, 100)]

for k in kernel_size:
    blurred = cv2.blur(image, (k, k))
    cv2.imshow(f'Blurred {k}', blurred)
    cv2.waitKey(0)

for k in kernel_size:
    blurred = cv2.GaussianBlur(image, (k, k), 0)
    cv2.imshow(f'Blurred Gaussian ({k},{k})', blurred)
    cv2.waitKey(0)

for k in kernel_size:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Blurred median {k}", blurred)
    cv2.waitKey(0)

for d, sigmaColor, sigmaSpace in bilateral_params:
    result = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    cv2.imshow(f"Blurred bilateral {d,sigmaColor,sigmaSpace}", result)
    cv2.waitKey(0)

cv2.imshow("original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()