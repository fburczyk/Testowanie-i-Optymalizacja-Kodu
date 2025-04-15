import cv2

image = cv2.imread('litery.png', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)


kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

closed_rect = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_rect)
closed_ellipse = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_ellipse)

cv2.imshow('Original', image)
cv2.imshow('Closed rectangle', closed_rect)
cv2.imshow('Closed ellipse', closed_ellipse)

cv2.waitKey()
cv2.destroyAllWindows()