import math
import mediapipe as mp 
import cv2

class HandTracking:
    def __init__(self):
        self.mp_hands =  mp.solutions.hands
        self.hand_detector = self.mp_hands.Hands(
            max_num_hands = 1,
            min_detection_confidence = 0.7,
            min_tracking_confidence = 0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,1280)
        self.cap.set(4,720)

        self.angle = 0

    def main(self):
        while True:
            ret,frame = self.cap.read()
            if not ret:
                break
            frame = cv2.flip(frame,1)
            h,w,_ = frame.shape
            rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            result = self.hand_detector.process(rgb)

            if result.multi_hand_landmarks:
                for hand in result.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(frame,hand,self.mp_hands.HAND_CONNECTIONS)

                    cx,cy = int(hand.landmark[9].x * w),int(hand.landmark[9].y * h)

                    overlay = frame.copy()

                    cv2.circle(overlay,(cx,cy),80,(0,255,255),2)
                    cv2.circle(overlay,(cx,cy),120,(0,255,255),1)

                    for i in range(1,4):
                        cv2.circle(overlay,(cx,cy),100+i,(0,255,255),1)

                    self.angle += 5
                    for i in range(0,360,20):
                        angle = math.radians(i + self.angle)
                        x = int(cx + 100 * math.cos(angle))
                        y = int(cy + 100 * math.sin(angle))
                        cv2.circle(overlay,(x,y),5,(0,255,255),-1)


                    alpha = 0.5
                    frame = cv2.addWeighted(overlay,alpha,frame,1 - alpha,0)



                    for id in [4,8,12,16,20]:
                        fx = int(hand.landmark[id].x * w)
                        fy = int(hand.landmark[id].y * h)
                        cv2.line(frame,(cx,cy),(fx,fy),(0,255,255),2)


            cv2.imshow("Futuristic Hand",frame)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    obj = HandTracking()
    obj.main()