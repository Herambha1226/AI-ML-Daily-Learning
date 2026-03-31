import cv2
import webbrowser
import pyautogui
import numpy as np


def detect_qr_Code():
    cap = cv2.VideoCapture(0)

    detector = cv2.QRCodeDetector()

    link = None
    while True:
        ret,frame = cap.read()

        if not ret:
            print("There is No Frame !")
            break

        frame = cv2.flip(frame,1)

        data,bbox,_ = detector.detectAndDecode(frame)

        if data:
            link = data
            break

        cv2.imshow("QRCode Scanner",frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    b = webbrowser.open(link)
    cv2.destroyAllWindows() 


ix,iy = -1,-1
fx,fy = -1,-1
drawing = False
roi_selected = False

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,fx,fy,drawing,roi_selected

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        fx,fy = x,y 
        roi_selected = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            fx,fy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx,fy = x,y 
        if ix != fx and iy != fy:
            roi_selected = True


def detect_qrcode_screenshot():
    global ix,iy,fx,fy,drawing,roi_selected


    screenshot = pyautogui.screenshot()
    img = np.array(screenshot)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    clone = img.copy()

    cv2.namedWindow("Detect QR",cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Detect QR",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN )
    cv2.setMouseCallback("Detect QR",draw_rectangle)
    link = None

    detector = cv2.QRCodeDetector()

    while True:
        temp_img = clone.copy()

        if drawing or (ix != -1 and iy != -1):
            cv2.rectangle(temp_img,(ix,iy),(fx,fy),(0,255,0),2)

        cv2.imshow("Detect QR",temp_img)

        key = cv2.waitKey(1) & 0xff

        if roi_selected:

            y1,y2 = min(iy,fy),max(iy,fy)
            x1,x2 = min(ix,fx),max(ix,fx)

            if y2 - y1 > 10 and x2 - x1 > 10:
                roi = clone[y1:y2,x1:x2]

                data,bbox,_ = detector.detectAndDecode(roi)

                if data:
                    print(f"QR Code data: ",data)
                    webbrowser.open(data)
                    break
                else:
                    print("No QR Code Deteted in region")
                    roi_selected = False
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_qrcode_screenshot()
