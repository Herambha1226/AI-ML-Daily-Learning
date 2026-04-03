import cv2
import numpy as np

cap = cv2.VideoCapture(0)

GRID_SIZE = 12
FONT_SCALE = 0.4

cap.set(3,1280)
cap.set(4,720)

while True:
    ret,frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    _,thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)

    output = np.zeros_like(frame)

    four_cc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("Sample.mp4",four_cc,20,(1280,720))

    h,w = thresh.shape
    for y in range(0,h,GRID_SIZE):
        for x in range(0,w,GRID_SIZE):
            char = "1" if thresh[y,x] == 255 else "0"

            cv2.putText(output,char,(x,y),cv2.FONT_HERSHEY_SIMPLEX,FONT_SCALE,(0,255,0),1,cv2.LINE_AA)

    cv2.imshow("Camera Different",output)
    out.write(frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()