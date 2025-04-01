import cv2

image = cv2.imread(r"puppy.jpg")
cv2.imshow("Original", image)

flipped_vertical = cv2.flip(image,0)
cv2.imshow("Flipped", flipped_vertical)

cv2.waitKey(0)
cv2.destroyAllWindows()