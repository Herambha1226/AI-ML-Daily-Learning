# Contours

import cv2 

img = cv2.imread("guptha.jpeg")

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,127,255,0)

cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img,cnts,-1,(176,0,171),4)

cv2.imshow("Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()