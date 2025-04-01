import cv2
import numpy as np

image1 = cv2.imread('puppy.jpg')
image2 = cv2.imread('puppy_diff_scene.jpg')

diff = cv2.absdiff(image1, image2)

cv2.imshow("Original", image1)
cv2.imshow("Moved", image2)
cv2.imshow("Diff", diff)
#Jasne obszary na obrazie końcowym pokazują miejsca w których wystąpiły zmiany
cv2.waitKey(0)
cv2.destroyAllWindows()
