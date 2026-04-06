import cv2

image = cv2.imread("OpenCV/Pi7_image.jpeg")

resized = cv2.resize(image,(300,300))

roi = image[50:200,100:250] # [y1:y2, x1:x2]

flipped = cv2.flip(image, -1)

cv2.imshow("Original",image)
cv2.imshow("Resized",resized)
cv2.imshow("ROI",roi)
cv2.imshow("Flipped",flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
