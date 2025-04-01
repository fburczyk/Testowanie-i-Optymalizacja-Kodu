import cv2

image = cv2.imread("puppy_numpy.jpg")
height, width = image.shape[:2]

right_half = image[:, width//2:]


cv2.imshow("Right side", right_half)
cv2.waitKey(0)
cv2.destroyAllWindows()
