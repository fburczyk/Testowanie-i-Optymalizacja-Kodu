import cv2

image = cv2.imread('plate.jpg')

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(img_gray, ksize=3)
gauss = cv2.GaussianBlur(blurred, (7, 7), sigmaX=0)
unsharp = cv2.addWeighted(blurred, 1.5, gauss, -0.5, 0)
kernel_size = (2,2)

bin_img = cv2.adaptiveThreshold(
    unsharp,
    maxValue=255,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY_INV,
    blockSize=21,
    C=8
)
closing = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel_size, iterations=1)



cv2.imshow('Original', image)
cv2.imshow('Closing', closing)


cv2.waitKey(0)
cv2.destroyAllWindows()

