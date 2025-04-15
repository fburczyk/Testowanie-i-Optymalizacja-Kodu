import cv2
import numpy as np
import pandas as pd
image = cv2.imread('figury.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thicknesses = []

for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(),None, iterations=i + 1)

    thickness = np.sum(dilated > 0)
    thicknesses.append(thickness)

    cv2.imshow(f"Dilated {i+1} times", dilated)
    cv2.waitKey(0)

data = {
    'Liczba iteracji': list(range(0, 3)),
    'Grubość obiektów (liczba pikseli)': thicknesses
}

result_df = pd.DataFrame(data)
print(result_df)

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


