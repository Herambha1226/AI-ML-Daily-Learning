import cv2
def basic_overlay():
    bg = cv2.imread("face.jpg")
    overlay = cv2.imread("glasses.png")

    overlay = cv2.resize(overlay,(200,100))

    x,y = 100,150

    h,w,_ = overlay.shape

    roi = bg[y:y+h,x:x+w]

    gray = cv2.cvtColor(overlay,cv2.COLOR_BGR2GRAY)
    _,mask = cv2.threshold(gray,25,255,cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    bg_part = cv2.bitwise_and(roi,roi,mask,mask_inv)
    fg_part = cv2.bitwise_and(overlay,overlay,mask=mask_inv)

    result = cv2.add(bg_part,fg_part)

    bg[y:y+h, x:x+w] = result

    cv2.imshow("Output",bg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import mediapipe as mp 
import math

def face_based_overlay():
    cap = cv2.VideoCapture(0)

    overlay = cv2.imread("glasses.png",cv2.IMREAD_UNCHANGED)

    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    LEFT_EYE = 33
    RIGHT_EYE = 263

    while True:
        ret,frame = cap.read()
        frame = cv2.flip(frame,1)
        if not ret:
            break
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        if result.multi_face_landmarks:
            for detection in result.multi_face_landmarks:
                h,w,_ = frame.shape

                left = detection.landmark[LEFT_EYE]
                right = detection.landmark[RIGHT_EYE]

                x1,x2 = int(left.x * w),int(left.y*h)
                y1,y2 = int(right.x*w),int(right.y*h)

                distance = int(math.hypot(x2 - x1,y2 - y1))

                glasses_width = int(distance * 2)
                glasses_height = int(glasses_width * 0.5)

                overlay_resized = cv2.resize(overlay,(glasses_width,glasses_height))

                x = int((x1+x2)/2 - glasses_width /2)
                y = int((y1+y2)/2 - glasses_height /2)

                if y < 0 or x < 0:
                    continue

                roi = frame[y:y+glasses_height,x:x+glasses_width]

                if roi.shape[0] != glasses_height or roi.shape[1] != glasses_width:
                    continue

                gray = cv2.cvtColor(overlay_resized,cv2.COLOR_BGR2GRAY)
                _,mask = cv2.threshold(gray,25,255,cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)

                bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
                fg = cv2.bitwise_and(overlay_resized,overlay_resized,mask=mask)

                frame[y:y+glasses_height,x:x+glasses_width] = cv2.add(bg,fg)
        cv2.imshow("Glasses Filter",frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

face_based_overlay()
    
# fdsks