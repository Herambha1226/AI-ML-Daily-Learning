import cv2 
import mediapipe as mp 
import numpy as np


mp_hands = mp.solutions.hands
hand_detector = mp_hands.Hands(
    max_num_hands = 2,
    min_detection_confidence = 0.8,
    min_tracking_confidence = 0.8
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    if not ret:
        break
    h,w,_ = frame.shape

    black_overlay = np.zeros((h,w,3),dtype=np.uint8)

    frame = cv2.addWeighted(frame,0.3,black_overlay,0.7,0)

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hand_detector.process(rgb)

    mask = np.zeros((h,w,3),dtype=np.uint8)

    if result.multi_hand_landmarks:
        all_hands_tip = []
        tips_id = [i for i in range(0,21)]
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)
            
            current_hand_tip = {}
            for tip in tips_id:
                cx,cy = int(hand.landmark[tip].x * w),int(hand.landmark[tip].y * h)
                current_hand_tip[tip] = (cx,cy)
            all_hands_tip.append(current_hand_tip)

        if len(all_hands_tip) == 2:
            hand1 = all_hands_tip[0]
            hand2 = all_hands_tip[1]

            for tip in tips_id:
                p1,p2 = hand1[tip],hand2[tip]
                color = (255,54,200)

                cv2.line(mask, p1, p2, color, 12)
                
                cv2.line(mask, p1, p2, (255, 100, 230), 5)

                cv2.line(frame, p1, p2, (255, 255, 255), 2)

                """for thickness in [15,10,5]:
                    cv2.line(frame,p1,p2,color,thickness)
                cv2.line(frame,p1,p2,(255,255,255),2)"""
    blurred_mask = cv2.GaussianBlur(mask,(41,41),0)

    final_frame = cv2.addWeighted(frame,1.0,blurred_mask,1.5,0)

    cv2.imshow("Hand Gel",final_frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

