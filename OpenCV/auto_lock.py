import cv2
import pyautogui
pyautogui.FAILSAFE = False
import ctypes

casade = cv2.CascadeClassifier(r"OpenCV//haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while True:
    ret,frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame,1)

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = casade.detectMultiScale(frame,1.3,5)

    if len(result) == 0:
        ctypes.windll.user32.LockWorkStation()
        break

    cv2.imshow("Auto Lock Screen",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
