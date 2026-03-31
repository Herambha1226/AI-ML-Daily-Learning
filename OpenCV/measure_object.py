import cv2

img = cv2.imread('object-image.jpeg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,0)

cv2.imshow("Thresh ",thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours,1,(0,255,0),3)

area = cv2.contourArea(contours[0])

scale_factor = 0.1
size = area * scale_factor ** 2

print("Size: ",size)

cv2.imshow('object.jpg',img)
cv2.waitKey(0)

