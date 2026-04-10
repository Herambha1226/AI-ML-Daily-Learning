import cv2

# intialize face detector
face_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Choose tracker
tracker = cv2.TrackerCSRT_create()

cap = cv2.VideoCapture(0)
tracking = False
bbox = None

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    if not ret:
        break

    if not tracking:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_casecade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"Press 'S' to select",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
        
        key = cv2.waitKey(1) & 0xff
        if key == ord('s') and len(faces) > 0:
            bbox = tuple(faces[0])
            tracker.init(frame,bbox)
            tracking = True
    else:
        success,bbox = tracker.update(frame)
        if success:
            x,y,w,h = [int(v) for v in bbox]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,"Tracker",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
        else:
            cv2.putText(frame,"Lost! Press 'D' to redetect",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        
        key = cv2.waitKey(1)&0xff
        if key == ord('q'):
            tracking = False
    cv2.imshow("Face Tracker",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()