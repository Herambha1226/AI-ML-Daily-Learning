import cv2 
import mediapipe as mp 

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands= mp_hands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if not ret:
        print("There is Problem for getting frame")

    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_lm in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand_lm,mp_hands.HAND_CONNECTIONS)   

    cv2.imshow("MediaPipe + CV2",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()