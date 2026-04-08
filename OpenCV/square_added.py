import mediapipe as mp 
import cv2

mp_hand = mp.solutions.hands
hand_detect = mp_hand.Hands(
    max_num_hands = 1
)
mp_draw = mp.solutions.drawing_utils

squres = []

cap = cv2.VideoCapture(0)

while True:
    success,frame = cap.read()
    frame = cv2.flip(frame,1)
    if not success:
        break
    h,w,_ = frame.shape
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hand_detect.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            index = hand.landmark[8]
            thumb = hand.landmark[4]

            ix,iy = int(thumb.x*w),int(thumb.y*h)
            fx,fy = int(index.x*w),int(index.y*h)

            distance = int(((ix - fx)**2 + (iy - fy)**2)**0.5)
            cv2.circle(frame,(ix,iy),10,(210,45,60),4)
            cv2.circle(frame,(fx,fy),10,(210,45,60),4)

            if distance < 30:
                squres.append((fx,fy))
    for (x,y) in squres:
        cv2.rectangle(frame,(x-20,y-20),(x+20,y+20),(100,210,50),5)

    cv2.imshow("Square Added",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

                



