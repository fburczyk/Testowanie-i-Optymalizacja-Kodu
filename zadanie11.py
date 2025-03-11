import cv2
import numpy as np
image = cv2.imread(r"C:\Users\Student\Desktop\Testowanie-i-Optymalizacja-Kodu\szczeniak.jpg")

max_brightness = -1
max_brightness_coords  = (0,0)
max_pixel_value = (0,0,0)

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        pixel = image[y,x]
        brightness = np.mean(pixel)
        if brightness > max_brightness:
            max_brightness = brightness
            max_brightness_coords = (x,y)
            max_pixel_value = tuple(pixel)

print(f"Coordinates of brightness pixel: {max_brightness_coords}")
print(f"Value of brightness pixel: {max_pixel_value}")