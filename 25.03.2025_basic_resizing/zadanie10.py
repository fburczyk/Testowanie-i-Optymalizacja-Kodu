import cv2
import imutils

image = cv2.imread('dog.jpg')

resized = imutils.resize(image, width=800)

cv2.imwrite('resized_output.jpg', resized)

cv2.imshow("original",image)
cv2.imshow('Resize', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()