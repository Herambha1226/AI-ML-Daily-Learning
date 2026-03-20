# Canny Edge Detection using Opnncv


import cv2
import numpy as np

image = cv2.imread("guptha.jpeg")

img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img_gray,20,150)
cv2.imshow("Original ",image)
cv2.imshow("Canny : ",canny)

cv2.waitKey()
cv2.destroyAllWindows()