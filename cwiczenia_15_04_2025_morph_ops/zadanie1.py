import cv2

image = cv2.imread('figury.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(0,3):
    eroded = cv2.erode(gray.copy(),None,iterations=i+1)
    cv2.imshow(f"Eroded {i+1} times",eroded)
    cv2.waitKey()
cv2.imshow("Original", image)
cv2.waitKey()
cv2.destroyAllWindows()

#figury się poszerzeają