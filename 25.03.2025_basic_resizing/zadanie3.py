import cv2

image = cv2.imread('dog.jpg')

resized = cv2.resize(image,(200,300), interpolation=cv2.INTER_LINEAR)

cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
