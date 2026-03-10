import cv2 

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret: 
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    cv2.imshow("Gaussian Blur",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()