import cv2
import math
import mediapipe as mp 

mp_hands = mp.solutions.hands
hand_detector = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

clicked = False

button_pos = (300,100)
button_size = (200,100)

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    if not ret:
        print("There is a problem for getting frame")
        break
    
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hand_detector.process(rgb)

    h,w,c = frame.shape

    index_x,index_y = 0,0
    thumb_x,thumb_y = 0,0

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            for id,lm in enumerate(hand.landmark):
                cx,cy = int(lm.x*w),int(lm.y*h)

                if id == 8:
                    index_x,index_y = cx,cy
                    cv2.circle(frame,(cx,cy),10,(255,0,255),2)

                if id == 4:
                    thumb_x,thumb_y = cx,cy
                    cv2.circle(frame,(cx,cy),10,(255,255,0),2)
            mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)

        distance = math.sqrt((index_x-thumb_x)**2+(index_y-thumb_y)**2)

        dw,dh = button_size
        dx,dy = button_pos

        if dx < index_x < dx + dw and dy < index_y < dy + dh:

            if distance < 40:
                color = (255,0,0)
                clicked = True
            else:
                clicked = False
        else:
            color = (255,0,0)
    else:
        color = (255,0,0)

    cv2.rectangle(frame,button_pos,(button_pos[0]+button_size[0],button_pos[1]+button_size[1]),(255,144,200),2)
    cv2.putText(frame,"Click",(button_pos[0]+20,button_size[1]+50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,222,222),3)

    if clicked:
        cv2.putText(frame,"Button Pressed",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(222,200,122),3)

    cv2.imshow("Button Press",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
