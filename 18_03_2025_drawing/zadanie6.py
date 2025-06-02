import cv2
import numpy as np

image = cv2.imread(r"zdjecie.jpg")

eye1, eye2 = (408,408),(598,408)
mouth = (500,575)
face_center = (550,400)

eye_radius = 45
mouth_width = 180
mouth_height = 90
face_radius = 350

red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)

cv2.circle(image,eye1, eye_radius, red, -1)
cv2.circle(image,eye2, eye_radius, red, -1)

cv2.rectangle(image,(mouth[0]- mouth_width //2, mouth[1]-mouth_height//2),(mouth[0] + mouth_width //2, mouth[1]+mouth_height//2),green,-1)

cv2.circle(image,face_center,face_radius, blue)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()