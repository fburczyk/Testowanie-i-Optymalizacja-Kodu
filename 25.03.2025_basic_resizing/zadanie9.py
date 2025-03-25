import cv2
import imutils

image = cv2.imread('dog.jpg')

(h,w) = image.shape[:2]

for size in range(100,301,20):
    new_width = int(w * (size / 100))
    new_height = int(h * (size / 100))

    resized = cv2.resize(image, (new_width,new_height), interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow('Resize', resized)
    cv2.waitKey(500)