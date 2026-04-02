import math
import cv2
import mediapipe as mp
import pyautogui
pyautogui.FAILSAFE = False
import time
last_time_click = 0


mp_hands = mp.solutions.hands
hand_detectot = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


screen_w,screen_h = pyautogui.size()

button_pos = (300,100)
button_size = (200,100)

clicked = False

prev_x,prev_y = 0, 0

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    if not ret:
        print("There is a Problem")
        break
    h,w,c = frame.shape

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hand_detectot.process(rgb)

    index_x,index_y = 0,0
    thumb_x,thumb_y = 0,0

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            for id ,lm in enumerate(hand.landmark):
                cx,cy = int(lm.x*w),int(lm.y*h)

                if id == 8:
                    index_x,index_y = cx,cy
                    cv2.circle(frame,(cx,cy),10,(200,150,200),2)
                    screen_x = int(lm.x * screen_w)
                    screen_y = int(lm.y * screen_h)

                    
                    smooth = 5
                    curr_x = prev_x + (screen_x - prev_x)/smooth
                    curr_y = prev_y + (screen_y - prev_y)/smooth

                    pyautogui.moveTo(screen_x,screen_y,_pause=False)
                    prev_x = curr_x
                    prev_y = curr_y
                
                if id == 4:
                    thumb_x,thumb_y = cx,cy
                    cv2.circle(frame,(cx,cy),10,(200,150,200),2)

                

            mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)

        distance = math.sqrt((index_x - thumb_x)**2 + (index_y - thumb_y)**2)

        dx,dy = button_pos
        dw,dh = button_size
        if distance < 40:
                color = (0,255,200)
                clicked =True

                if time.time() - last_time_click > 0.5:
                    pyautogui.click()
                    last_time_click = time.time()

        if dx < index_x < dx + dw and dy < index_y < dy + dh:

            if distance < 40:
                color = (0,255,200)
                clicked =True

                if time.time() - last_time_click > 0.5:
                    pyautogui.click()
                    last_time_click = time.time()
            else:
                clicked = False
        else:
            color = (0,200,255)
    else:
        color = (0,200,255)

    cv2.rectangle(frame,button_pos,(button_pos[0]+button_size[0],button_size[1]+button_pos[1]),color,2)
    cv2.putText(frame,"Click",(button_pos[0]+20,button_size[1]+50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    if clicked:
        cv2.putText(frame,"Button Clicked",(100,150),cv2.FONT_HERSHEY_SIMPLEX,1,(200,200,120),3)

    cv2.imshow("Button Pressed",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


