import cv2

image = cv2.imread('dog.jpg')

(h, w) = image.shape[:2]
new_dimensions = (w*3,h*3)

resized_nearest = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_NEAREST)
resized_linear = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_LINEAR)
resized_cubic = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_CUBIC)
resized_lanczos4 = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('Original', image)
cv2.imshow('INTER_NEAREST', resized_nearest)
cv2.imshow('INTER_LINEAR', resized_linear)
cv2.imshow('INTER_CUBIC', resized_cubic)
cv2.imshow('INTER_LANCZOS4', resized_lanczos4)

cv2.waitKey(0)
cv2.destroyAllWindows()