# Image Pyramids in opencv

import cv2
import numpy as np 
image = cv2.imread("guptha.jpeg")
image = cv2.resize(image,(300,400))

img1 = image.copy()
data= [img1]

for i in range(4):
    img1 = cv2.pyrDown(img1)

    data.append(img1)

    cv2.imshow("res"+str(i),img1)

cv2.imshow("Original : ",image)
cv2.waitKey()
cv2.destroyAllWindows()