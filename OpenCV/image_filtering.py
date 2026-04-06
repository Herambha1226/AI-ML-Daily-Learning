import cv2
import numpy as np 

image = cv2.imread("OpenCV/Pi7_image.jpeg")
if image is None:
    print("Error : Could not read image.")
    exit()

blurred = cv2.GaussianBlur(image,(7,7),0)

sharpen_kernal = np.array([[-1,-1,-1],
                           [-1,9,-1],
                           [-1,-1,-1]])
sharpended = cv2.filter2D(image,-1,sharpen_kernal)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

sepia_kernal = np.array([[0.272,0.534,0.131],
                         [0.349,0.686,0.168],
                         [0.393,0.769,0.189]])
sepia = cv2.transform(image,sepia_kernal)
sepia = np.clip(sepia,0,255)

edges = cv2.Canny(image,100,200)

cv2.imshow("Original",image)
cv2.imshow("Blurred",blurred)
cv2.imshow("Sharpend",sharpended)
cv2.imshow("Grayscale",gray)
cv2.imshow("Sepia",sepia.astype(np.uint8))
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

