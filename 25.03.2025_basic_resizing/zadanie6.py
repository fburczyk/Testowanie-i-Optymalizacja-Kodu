import cv2
import imutils

image = cv2.imread('dog.jpg')

resized = imutils.resize(image, height=400)

cv2.imshow('Original', image)
cv2.imshow('Resized', resized)
cv2.waitKey(0)