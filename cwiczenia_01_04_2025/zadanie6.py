import cv2

user_choice = int(input("(0 – pionowe, 1 – poziome, -1 – oba) \n Podaj parametr:"))

image = cv2.imread("puppy.jpg")

flipped = cv2.flip(image, user_choice)

cv2.imshow("Original", image)
cv2.imshow(f"Flipped by {user_choice}", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()