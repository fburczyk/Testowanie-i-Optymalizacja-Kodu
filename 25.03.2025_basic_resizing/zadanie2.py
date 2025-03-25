import cv2

image = cv2.imread('dog.jpg')
cv2.imshow('Original', image)

(h, w) = image.shape[:2]
new_size = (w*2, h*2)

new_image = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized', new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()