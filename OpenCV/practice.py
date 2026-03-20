import cv2
import datetime

cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,500)

while True:
  ret,frame = cap.read()
  if ret:
    font = cv2.FONT_HERSHEY_COMPLEX
    text = ' Heigh :' + str(cap.get(4)) + 'width : '+str(cap.get(3))
    datet = "Date: "+str(datetime.datetime.now())

    frame = cv2.putText(frame,text,(10,50),font,1,(0,255,255),5,cv2.LINE_AA)
    frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),5,cv2.LINE_AA)

    cv2.rectangle(frame,(384,10),(510,128),(128,0,255),8)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break 
cap.release()
cv2.destroyAllWindows()
