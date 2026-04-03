import cv2
import mediapipe as mp
import time

class Camera:
    def __init__(self):
        
        self.mp_hands = mp.solutions.hands
        self.hand_detector = self.mp_hands.Hands(
            max_num_hands = 1,
            min_detection_confidence = 0.7,
            min_tracking_confidence = 0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,1280)
        self.cap.set(4,720)

        self.countdown = -1
        self.last_timer_update = 0
        self.show_saved_msg = 0
        self.show_saved_video = 0

        self.is_recording = False
        self.video_writer = None

        self.mode = "idle"
    
    
    def start_capture_timer(self):
        self.countdown = 3
        self.last_timer_update = time.time()

    def take_picture(self,frame):
        if self.countdown > 0:

            cv2.putText(frame,str(self.countdown),(600,400),cv2.FONT_HERSHEY_SIMPLEX,5,(255,255,255),3)

            if time.time() - self.last_timer_update > 1.0:
                self.countdown -= 1
                self.last_timer_update = time.time()

                if self.countdown == 0:
                    self.show_saved_msg =40
                    self.countdown = -1
                    self.mode = "idle"

        if self.show_saved_msg > 0:
            clone = frame.copy()
            cv2.putText(frame,"Saved Image",(540,650),cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC,1,(255,255,255),2)
            cv2.imwrite("OpenCV/Sample.png",clone)
            self.show_saved_msg -= 1
        
        return frame
    
    def capture_video(self,frame,hand):
        if self.countdown > 0:
            cv2.putText(frame,str(self.countdown),(900,400),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)

            if time.time() - self.last_timer_update > 1.0:
                self.countdown -= 1
                self.last_timer_update = time.time()
                if self.countdown == 0 and self.mode == "video":
                    
                    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                    self.video_writer = cv2.VideoWriter("sample.mp4",fourcc,20,(1280,720))
                    self.is_recording = True
                    self.countdown = -1
        if self.is_recording:
            clone = frame.copy()
            self.video_writer.write(clone)
            cv2.putText(frame,"Recording....",(540,650),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX | cv2.FONT_ITALIC,1,(255,255,255),2)
            fingers = self.fingers_up(hand,frame)

            if fingers == [0,0,0,0,0]:
                # Stops the video Capturing 
                self.is_recording = False
                self.video_writer.release()
                self.video_writer = None
                self.show_saved_video =40
                self.mode = "idle"
        
        if self.show_saved_video > 0:
            cv2.putText(frame,"Saved Video",(540,650),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
            self.show_saved_video -= 1
        
        return frame

    
    def fingers_up(self,hand_landmark,frame):
        h,w,_ = frame.shape
        lm = []

        for id, point in enumerate(hand_landmark.landmark):
            cx,cy = int(point.x * w),int(point.y * h)
            lm.append((cx,cy))
        
        fingers = []

        # thumb points finding
        if lm[4][0] > lm[3][0]:
            fingers.append(1)
        else:
            fingers.append(0)

        tips = [8,12,16,20]
        for tip in tips:
            if lm[tip][1] < lm[tip - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
    
    def main(self):
        while True:
            ret,frame = self.cap.read()

            if not ret:
                break

            frame = cv2.flip(frame,1)

            rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            result = self.hand_detector.process(rgb)

            if result.multi_hand_landmarks:
                for hand in result.multi_hand_landmarks:
                    nothing = None 
                                    
                fingers = self.fingers_up(hand,frame)

                if self.mode == "idle":

                    if fingers == [0,1,1,0,0] and self.countdown == -1:
                        self.mode = "photo"
                        self.start_capture_timer()
                    elif fingers == [0,1,0,0,1] and self.countdown == -1:
                        self.mode = "video"
                        self.start_capture_timer()
                frame = self.capture_video(frame,hand)
            
            frame = self.take_picture(frame)
            
            cv2.imshow("Camera",frame)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        self.cap.release()    
        cv2.destroyAllWindows()
    
if __name__ == "__main__":
    obj = Camera()
    obj.main()