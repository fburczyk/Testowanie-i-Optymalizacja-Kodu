import cv2

image = cv2.imread('puppy.jpg')

modified_image = image.copy()

modified_image[:,:,0] = cv2.add(modified_image[:,:,0], 10)
modified_image[:,:,1] = cv2.subtract(modified_image[:,:,1], 20)
modified_image[:,:,2] = cv2.add(modified_image[:,:,2], 30)

cv2.imshow('Original', image)
cv2.imshow('Modified image', modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
