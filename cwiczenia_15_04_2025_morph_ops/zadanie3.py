import cv2

image = cv2.imread('salt_and+pepper.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernelSizes = [(3, 3), (5, 5), (7, 7)]

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)
cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Wyniki po operacji są bardziej rozmazane