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

        self.cap.set(3,1280)
        self.cap.set(4,720)

        self.distance_zoom = 0
        self.default_zoom = 1.0
        self.smooth_zoom = 0

        self.gesture_active = True
        self.last_dist = 0

    
    def distance(self,hand1,hand2,frame):
        h,w,_ = frame.shape

        x1 = int(hand1.landmarks[0].x * w)
        y1 = int(hand1.landmarks[0].y * h)

        x2 = int(hand2.landmarks[0].x * w)
        y2 = int(hand2.landmarks[0].y * h)

        return math.hypot(x2 -x1, y2 - y1)
        
    def fingers_up(self,hand,frame):
        h,w,_ = frame.shape
        lm = []

        for id, point in enumerate(hand.landmark):
            cx,cy = int(point.x * w),int(point.y * h)
            lm.append((cx,cy))

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
    def apply_zoom(self, frame):
        h, w, _ = frame.shape

        # 🔥 FIX: clamp zoom range
        self.default_zoom = max(1.0, min(self.default_zoom, 5.0))

        new_w = int(w / self.default_zoom)
        new_h = int(h / self.default_zoom)

        # 🔥 FIX: use OR instead of AND
        if new_w <= 0 or new_h <= 0:
            return frame

        x1 = max((w - new_w) // 2, 0)
        y1 = max((h - new_h) // 2, 0)

        cropped = frame[y1:y1 + new_h, x1:x1 + new_w]

        # 🔥 FIX: use OR instead of AND
        if cropped is None or cropped.size == 0:
            return frame

        # 🔥 IMPORTANT: resize back to original size (real zoom effect)
        return cv2.resize(cropped, (w, h))

    def main(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = self.hand_detector.process(rgb)

            h, w, _ = frame.shape

            if result.multi_hand_landmarks:
                for hand in result.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(
                        frame, hand, self.mp_hands.HAND_CONNECTIONS
                    )

                    # Thumb & Index
                    thumb = hand.landmark[4]
                    index = hand.landmark[8]

                    fx, fy = int(thumb.x * w), int(thumb.y * h)
                    ix, iy = int(index.x * w), int(index.y * h)

                    dist = math.hypot(ix - fx, iy - fy)

                    # 🔥 NEW: smoothing (reduces jitter)
                    self.smooth_zoom = 0.7 * self.smooth_zoom + 0.3 * dist

                    cv2.line(frame, (fx, fy), (ix, iy), (255, 0, 255), 3)

                    # 🔥 NEW: activate gesture only in valid range
                    if 30 < self.smooth_zoom < 200:
                        self.gesture_active = True
                    else:
                        self.gesture_active = False

                    # 🔥 NEW: use CHANGE in distance (delta), not absolute
                    if self.gesture_active:
                        if self.last_dist != 0:
                            diff = self.smooth_zoom - self.last_dist

                            # Zoom IN
                            if diff > 5:
                                self.default_zoom += 0.03

                            # Zoom OUT
                            elif diff < -5:
                                self.default_zoom -= 0.03

                    # 🔥 NEW: store previous distance
                    self.last_dist = self.smooth_zoom

            # 🔥 IMPORTANT: apply zoom ALWAYS (even if no hand)
            frame = self.apply_zoom(frame)

            # 🔥 NEW: show zoom level on screen
            cv2.putText(frame, f"Zoom: {round(self.default_zoom,2)}",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

            cv2.imshow("Zoom Control", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    ZoomCamera().main()
