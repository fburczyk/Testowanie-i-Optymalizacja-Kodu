import cv2
import numpy as np


image = cv2.imread('puppy.jpg')

height, width = image.shape[:2]

center_y, center_x = height // 2, width // 2
half_height, half_width = height // 4, width // 4

cropped = image[center_y - half_height : center_y + half_height, center_x - half_width : center_x + half_width]

flipped_cropped = cv2.flip(cropped, 1)

image[center_y - half_height : center_y + half_height, center_x - half_width : center_x + half_width] = flipped_cropped

cv2.imwrite('new_puppy.jpg', image)

cv2.imshow('New image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()