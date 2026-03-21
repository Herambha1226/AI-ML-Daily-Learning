import cv2 
import mediapipe as mp 

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

fingers = [8,12,16,20]
thumb_tip = 4


while True:
    ret,frame = cap.read()

    if not ret:
        print("There is problem in getting frames")
    
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_lm in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand_lm,mp_hands.HAND_CONNECTIONS)

            landmarks = hand_lm.landmark
            finger_count = 0

            if result.multi_handedness:
                handedness_label = result.multi_handedness[0].classification[0].label

                if handedness_label == 'Right':
                    if landmarks[thumb_tip].x < landmarks[thumb_tip - 1].x:
                        finger_count += 1
                elif handedness_label == 'Left':
                    if landmarks[thumb_tip].x > landmarks[thumb_tip - 1].x:
                        finger_count += 1

            for tip in fingers:
                if landmarks[tip].y < landmarks[tip - 2].y:
                    finger_count += 1 
            
            cv2.putText(frame,f"Fingers : {finger_count}",(10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(148, 225, 241),6)
    cv2.imshow("Fingers Count",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()