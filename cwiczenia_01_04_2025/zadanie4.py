import cv2

image = cv2.imread(r"puppy.jpg")

flipped_horizontal = cv2.flip(image,1)
flipped_vertical = cv2.flip(image,0)
flipped = cv2.flip(image,-1)

cv2.imshow("Original", image)
cv2.imshow("Flipped horizontal", flipped_horizontal)
cv2.imshow("Flipped vertical", flipped_vertical)
cv2.imshow("Flipped both axes", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
