# Concept : Instead of processing the entire image, we select only important area.

import cv2 

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    _,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    roi = thresh[100:300,200:400]

    cv2.imshow("ROI",roi)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()