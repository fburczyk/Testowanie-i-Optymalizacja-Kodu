import cv2


image = cv2.imread("puppy_numpy.jpg")

roi = image[0:100,0:100]

cv2.imshow("Original", image)
cv2.imshow("ROI - left top corner", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()