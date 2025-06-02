import cv2

image = cv2.imread('figury.jpg')

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel_size = (5,5)

kernels = {
    'Square': cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size),
    'Cross': cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size),
    'Ellipse': cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
}

for name,kernel in kernels.items():
    erosion = cv2.erode(img_gray, kernel, iterations=1)
    dilation = cv2.dilate(img_gray, kernel, iterations=1)
    opening = cv2.morphologyEx(img_gray, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img_gray, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(img_gray, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow(f'Original ({name})', img_gray)
    cv2.imshow(f'Erosion ({name})', erosion)
    cv2.imshow(f'Dilation ({name})', dilation)
    cv2.imshow(f'Opening ({name})', opening)
    cv2.imshow(f'Closing ({name})', closing)
    cv2.imshow(f'Gradient ({name})', gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()