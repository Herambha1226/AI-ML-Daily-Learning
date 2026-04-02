import cv2 
import mediapipe as mp 
import pyautogui
import math
import time
import os

pyautogui.FAILSAFE = False

class AirMouse:
    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands = 1,
            min_detection_confidence = 0.7,
            min_tracking_confidence = 0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

        self.screen_w,self.screen_h = pyautogui.size()

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,1280)
        self.cap.set(4,720)

        self.prev_x, self.prev_y = 0,0 
        self.alpha = 0.2

        self.last_click_time = 0
        self.click_delay = 0.4

        self.last_action_time =0 
        self.action_delay = 1.5

        self.dragging = False

        self.margin = 100

    def get_fingers(self,hand):
        fingers = []

        if hand.landmark[4].x < hand.landmark[3].x:
            fingers.append(1)
        else:
            fingers.append(0)
            

        tips = [8,12,16,20]
        mids = [6,10,14,18]

        for tip,mid in zip(tips,mids):
            if hand.landmark[tip].y < hand.landmark[mid].y:
                fingers.append(1)

            else:
                fingers.append(0)
        return fingers
    def is_app_running(self,process_name):
        import subprocess

        result = subprocess.run(
            ['tasklist'],capture_output=True,text=True
        )
        return process_name.lower() in result.stdout.lower()
        
    def run(self):
        while True:
            ret,frame = self.cap.read()
            if not ret:
                break

            frame = cv2.flip(frame,1)
            h,w,_ = frame.shape

            rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            result = self.hands.process(rgb)

            cv2.rectangle(frame,(self.margin,self.margin),(w - self.margin,h - self.margin),
                              (255,0,255),2)
                
            if result.multi_hand_landmarks:
                for hand in result.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(
                        frame,hand,self.mp_hands.HAND_CONNECTIONS
                    )

                    idx = hand.landmark[8]
                    thumb = hand.landmark[4]

                    cx,cy = int(idx.x * w),int(idx.y * h)
                    tx,ty = int(thumb.x * w),int(thumb.y*h)

                    cv2.circle(frame,(cx,cy),10,(0,255,0),-1)
                    cv2.circle(frame,(tx,ty),10,(255,0,0),-1)

                    distance = math.sqrt((cx - tx)**2 + (cy - ty)**2)

                    fingers = self.get_fingers(hand)

                    if fingers == [0,1,0,0,0]:
                        if self.margin < cx < w - self.margin and self.margin < cy < h - self.margin:

                            screen_x = (cx - self.margin) * self.screen_w / (w -2 * self.margin)
                            screen_y = (cy - self.margin) * self.screen_h / (h - 2 * self.margin)

                            curr_x = self.alpha * screen_x + (1 - self.alpha) * self.prev_x
                            curr_y = self.alpha * screen_y + (1 - self.alpha) * self.prev_y

                            pyautogui.moveTo(curr_x,curr_y)
                            self.prev_x,self.prev_y = curr_x,curr_y

                            cv2.putText(frame,"MOVE",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

                        
                    if distance < 30:
                        if time.time() - self.last_click_time > self.click_delay:
                            pyautogui.click()
                            self.last_click_time = time.time()

                            cv2.putText(frame,"CLICK",(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

                        
                    if fingers == [0,1,1,0,0]:
                        pyautogui.scroll(20)
                        cv2.putText(frame,"SCROLL",(10,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
                        

                    if time.time() - self.last_action_time > self.action_delay:
                        if fingers == [0,1,1,1,0]:
                            pyautogui.hotkey('alt','tab')
                            self.last_action_time = time.time()
                        
                    if time.time() - self.last_action_time > self.action_delay:
                        if fingers == [0,1,0,0,1]:
                            pyautogui.hotkey('ctrl','c')
                            self.last_action_time = time.time()

                        
                    if time.time() - self.last_action_time > self.action_delay:
                        if fingers == [1,1,0,0,1]:
                            if self.is_app_running("chrome.exe"):
                                os.system("taskkill /f /im chrome.exe")
                            else:
                                os.system("start chrome")
                            self.last_action_time = time.time()

                    if time.time() - self.last_action_time > self.action_delay:
                        if fingers == [0,0,0,0,0]:
                            if self.is_app_running("msedge.exe"):
                                os.system("taskkill /f /im msedge.exe")
                            else:
                                os.system("msedge.exe")
                            self.last_action_time = time.time()
                    cv2.putText(frame,f"fingers : {fingers}",(10,250),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

            cv2.imshow("Air Mouse Pro Max",frame)

            if cv2.waitKey(1) & 0xff == ord('2'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = AirMouse()
    app.run()