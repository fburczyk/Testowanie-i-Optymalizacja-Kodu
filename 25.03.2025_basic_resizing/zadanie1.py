import cv2

image = cv2.imread('dog.jpg')
cv2.imshow('Original', image)

(h, w) = image.shape[:2]
resized = cv2.resize(image, (w//2, h//2))

cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()