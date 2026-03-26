from typing import Tuple,Optional
import numpy as np 
import cv2
import pyautogui 

def takeScreenShot(region: Tuple[int,int,int,int] | None = None) -> None:
    """
    **Capture ScreenShot.**

    Args:
        region (tuple): **[left, top, width, height]**
    """
    screenshot = pyautogui.screenshot(region=region)

    img = np.array(screenshot)

    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    cv2.imshow("ScreenShot",img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


drawing = False
ix,iy = -1,-1
fx,fy = -1,-1
snipping = False
def draw_rectangle(event,x,y,flags,param):
    global drawing,ix,iy,fx,fy,snipping

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
        snipping = False
        ix,iy = x,y
        fx,fy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            fx,fy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing=False
        fx,fy = x,y
        if ix != fx and iy != fy:
            snipping = True

screenshot = pyautogui.screenshot()
img = np.array(screenshot)
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
clone = img.copy()

cv2.namedWindow("Snipping Tool",cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Snipping Tool",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback("Snipping Tool",draw_rectangle)

while True:
    temp_img = clone.copy()

    overlay = temp_img.copy()
    cv2.rectangle(overlay,(0,0),(temp_img.shape[1],temp_img.shape[0]),(0,0,0),-1)
    cv2.addWeighted(overlay,0.4,temp_img,0.6,0,temp_img)

    if ix != -1 and iy != -1 and fx != -1 and fy !=-1:
        temp_img[min(iy,fy):max(iy,fy), min(ix,fx):max(ix,fx)] = \
            clone[min(iy,fy):max(iy,fy), min(ix,fx):max(ix,fx)]
        cv2.rectangle(temp_img,(ix,iy),(fx,fy),(0,255,0),2)
    cv2.imshow("Snipping Tool",temp_img)

    if snipping:
        roi = clone[min(iy,fy):max(iy,fy),min(ix,fx):max(ix,fx)]
        cv2.destroyWindow("Snipping Tool")
        cv2.imwrite("output/image.png",roi)
        print("Saved Successfully")
        cv2.imshow("Sinpping Tool",roi)
        cv2.waitKey(0)
        break

    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break
cv2.destroyAllWindows()
