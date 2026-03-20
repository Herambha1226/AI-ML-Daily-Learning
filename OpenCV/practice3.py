# image blending 
# blending means addition of two images

import cv2 
import numpy as np 

image1 = cv2.imread("guptha.jpeg")
image1 = cv2.resize(image1,(300,400))
image2 = cv2.imread("guptha.jpeg")
image2 = cv2.resize(image2,(300,400))


result = image1 + image2

result1 = cv2.add(image1,image2)

result2 = cv2.addWeighted(image1,0.7,image2,0.3,0)

#cv2.imshow("Blending",result)
#cv2.imshow("Blending",result1)
cv2.imshow("Blending",result2)

cv2.waitKey(0)
cv2.destroyAllWindows()