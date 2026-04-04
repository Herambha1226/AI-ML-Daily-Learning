import cv2
import pyautogui
pyautogui.FAILSAFE = False
import ctypes
import mediapipe as mp

mp_hands = mp.solutions.hands
hand_detector = mp_hands.Hands(
    max_num_hands = 1,
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

volume = 0

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    if not ret:
        break

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hands = hand_detector.process(rgb)

    h,w,_ = frame.shape

    if hands.multi_hand_landmarks:
        for hand in hands.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)

            thumb = hand.landmark[4]
            index = hand.landmark[8]

            fx , fy = int(thumb.x *w),int(thumb.y * h)
            ix,iy = int(index.x * w),int(index.y * h)
            
            cv2.circle(frame,(fx,fy),5,(250,150,175),2)
            cv2.circle(frame,(ix,iy),5,(250,150,175),2)
            cv2.line(frame,(fx,fy),(ix,iy),(200,255,200),2)

            distance = int(((ix - fx)**2 + (iy - fy)**2)**0.5)

            if distance > 100:
                pyautogui.press("volumeup")
                #cv2.waitKey(100)
            elif distance < 30:
                pyautogui.press("volumedown")
                #cv2.waitKey(100)

            

    cv2.imshow("Volume Controller",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


