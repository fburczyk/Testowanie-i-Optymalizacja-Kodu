import cv2

image = cv2.imread("puppy_numpy.jpg")

startX = int(input("Podaj startX: "))
endX = int(input("Podaj endX: "))
startY = int(input("Podaj startY: "))
endY = int(input("Podaj endY: "))


dynamic_roi = image[startY:endY, startX:endX]

cv2.imshow("Dynamiczny ROI", dynamic_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()