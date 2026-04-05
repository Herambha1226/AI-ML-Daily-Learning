import cv2
import mediapipe as mp 
import numpy as np 

mp_hands = mp.solutions.hands
hand_detect = mp_hands.Hands(
    max_num_hands = 1,
    min_detection_confidence = 0.8,
    min_tracking_confidence = 0.8
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

canvas = np.zeros((720,1280,3),np.uint8)
px,py = 0,0

def fingers_up(frame):
    h,w,_ = frame.shape
    lm = []

    for id,point in enumerate(hand.landmark):
        cx,cy = int(point.x * w),int(point.y * h)
        lm.append((cx,cy))
    
    fingers = []
    if lm[4][0] > lm[2][0]:
        fingers.append(1)
    else:
        fingers.append(0)

    tips = [8,12,16,20]

    for tip in tips:
        if lm[tip][1] < lm[tip -2][1]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers


while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    if not ret:
        break
    h,w,_ =frame.shape
    dark_glass = np.zeros((h,w,3),np.uint8)
    frame = cv2.addWeighted(frame,0.2,dark_glass,0.8,0)

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hand_detect.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)

            thumb = hand.landmark[4]
            index = hand.landmark[8]

            fx,fy = int(thumb.x*w),int(thumb.y*h)
            ix,iy = int(index.x*w),int(index.y*h)

            distance = int(((fx - ix)**2 + (fy - iy)**2)**0.5)

            fingers = fingers_up(frame)

            if distance < 30:
                # draw the lines when thumb and index are forming pinch 

                cv2.circle(frame,(ix,iy),10,(255,0,255),cv2.FILLED)
                if px == 0 and py == 0:px,py = ix,iy
                cv2.line(canvas,(px,py),(ix,iy),(255,54,200),5)
                px,py = ix,iy
            elif fingers == [1,1,1,1,1]:
                # when all fingers are up erase the draw lines
                cv2.circle(frame, (ix, iy), 60, (255, 255, 255), 2) # Show eraser ring
                if px == 0 and py == 0: px, py = ix, iy
                cv2.line(canvas, (px, py), (ix, iy), (0, 0, 0), 80) # Black line = erase
                px, py = ix, iy
            else:
                px,py = 0,0

    canvas_gray = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)
    _,mask_inv = cv2.threshold(canvas_gray,20,255,cv2.THRESH_BINARY_INV)

    frame_bg = cv2.bitwise_and(frame,frame,mask=mask_inv)
    final_frame = cv2.add(frame_bg,canvas)

    cv2.imshow("Paint Application",final_frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()