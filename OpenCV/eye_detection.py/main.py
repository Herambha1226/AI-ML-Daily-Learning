import cv2 

cap = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    if not ret:
        print("There is Problem in Capturing Frame ! ")
    
    frame = cv2.flip(frame,1)
    
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    eye = eye_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=3,minSize=(30,30))

    font = cv2.FONT_ITALIC
    frame = cv2.putText(frame,f"Eyes Count : {len(eye)}",(20,20),color=(128,231,51),thickness=5,fontFace=font,fontScale=1)

    for (x,y,w,h) in eye:
        #cv2.rectangle(frame,(x+y),(x+w,y+h),(230,182,51),8)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(230,182,51),8)
    
    cv2.imshow("Eye Detection",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()