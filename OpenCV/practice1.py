# ROI means Reagion Of Intrest practice

import numpy as np 
import cv2

image = cv2.imread("guptha.jpeg")
cv2.imshow('Original Image',image)

height,width = image.shape[:2]

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ROI = np.array([[(120,height),(120,220),(750,220),(750,height)]],dtype=np.int32)

blank = np.zeros_like(image_gray)

ROI2 = cv2.fillPoly(blank,ROI,255)
ROI_Image = cv2.bitwise_and(image_gray,ROI2)

cv2.imshow('Region Of Interest',ROI_Image)

cv2.waitKey()
cv2.destroyAllWindows()
