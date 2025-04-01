import cv2

image = cv2.imread("puppy_numpy.jpg")


height, width = image.shape[:2]


cell_height = height // 3
cell_width = width // 3


for i in range(3):
    for j in range(3):
        part = image[i*cell_height:(i+1)*cell_height, j*cell_width:(j+1)*cell_width]
        cv2.imshow(f"Część {i*3 + j + 1}", part)

cv2.waitKey(0)
cv2.destroyAllWindows()
