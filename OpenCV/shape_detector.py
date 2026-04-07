import cv2

img = cv2.imread("OpenCV/Pi7_image.jpeg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(5,5),0)

edges = cv2.Canny(blur,50,150)

contours,_ = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    epsilon = 0.02 * cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    corners = len(approx)

    if corners == 3:
        shape = "Traingle"
    elif corners == 4:
        shape = "Rectangle"
    else:
        shape = "Circle"
    
    cv2.drawContours(img,[approx],-1,(0,255,0),2)

    x,y = approx[0][0]
    cv2.putText(img,shape,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

cv2.imshow("Shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
