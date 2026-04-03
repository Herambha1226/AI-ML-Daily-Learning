import cv2
import mediapipe as mp 
import math

class ZoomCamera:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hand_detector = self.mp_hands.Hands(
            max_num_hands = 2,
            min_detection_confidence = 0.7,
            min_tracking_confidence = 0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

        self.cap = cv2.VideoCapture(0)

        self.cap.set(4,1280)
        self.cap.set(3,720)

        self.distance_zoom = 0
        self.default_zoom = 1.0

    
    def distance(self,hand1,hand2,frame):
        h,w,_ = frame.shape

        x1 = int(hand1.landmarks[0].x * w)
        y1 = int(hand1.landmarks[0].y * h)

        x2 = int(hand2.landmarks[0].x * w)
        y2 = int(hand2.landmarks[0].y * h)

        return math.hypot(x2 -x1, y2 - y1)
    
    def apply_zoom(self,frame):
        h,w,_ = frame.shape

        new_w = int(w / self.default_zoom)
        new_h = int(h / self.default_zoom)

        x1 = (w - new_w)//2
        y1 = (h - new_h)//2

        cropped = frame[y1:y1+new_h, x1:x1+new_w]

        return cropped
    
    def fingers_up(self,hand,frame):
        h,w,_ = frame.shape()
        lm = []

        for id, point in enumerate(hand.landmark):
            cx,cy = int(point.x * w),int(point.y * h)
            lm.append[(cx,cy)]

        fingers = []

        if lm[4][0] > lm[3][0]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        tips = [8,12,16,20]

        for tip in tips:
            if [tip][1] > [tip - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
    



