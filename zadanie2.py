import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\zdjecie_kota.jpg")
(h, w, c) = image.shape[:3]
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f"channels: {c}")