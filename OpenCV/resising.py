import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret:
        break
    _,thresh = cv2.threshold(frame,255,255,cv2.THRESH_BINARY)
    roi = thresh[100:300,100:300]

    resized = cv2.resize(roi,(28,28))
    flatten = resized.flatten()
    print(flatten.shape)

    cv2.imshow("Resized",resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()