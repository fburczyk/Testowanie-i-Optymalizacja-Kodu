import cv2

image = cv2.imread("puppy_numpy.jpg")

height, width = image.shape[:2]

fragment = image[0:100, 0:100]

image[height-100:height, width-100:width] = fragment

cv2.imshow("Copy and paste", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
