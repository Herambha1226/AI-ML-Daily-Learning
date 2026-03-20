# Create a bordr for a image using cv2.copyMakeBorder()

import cv2 

image = cv2.imread("guptha.jpeg")

image = cv2.copyMakeBorder(image,10,10,5,5,cv2.BORDER_CONSTANT,value=[255,0,214])

cv2.imshow("Border Image",image)

cv2.waitKey()
cv2.destroyAllWindows()
