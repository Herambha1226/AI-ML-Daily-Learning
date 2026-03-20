# Adaptive Threshold

import cv2

img = cv2.imread("guptha.jpeg")
img = cv2.resize(img,(400,400))

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,th1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Original",img)
cv2.imshow("normal thresh",th1)
cv2.imshow("Thresh mean",th2)
cv2.imshow("Thresh gaussian",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()