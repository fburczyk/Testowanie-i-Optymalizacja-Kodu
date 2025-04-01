import cv2

image = cv2.imread("tsunoda.jpeg")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

if len(faces) == 0:
    print("Brak wykrytych twarzy.")
else:
    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        cv2.imshow("Face", face)

cv2.waitKey(0)
cv2.destroyAllWindows()
