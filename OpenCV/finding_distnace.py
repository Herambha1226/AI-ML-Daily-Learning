import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

KOWN_WIDTH = 7.6
KOWN_PIXELS = 210
KOWN_DISTANCE = 30
FOCAL_LENGTH = (KOWN_PIXELS * KOWN_DISTANCE) / KOWN_WIDTH

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    result = model(frame,verbose=False)

    for r in result:
        boxes = r.boxes

        for box in boxes:
            x1,y1,x2,y2 = map(int,box.xyxy[0])
            width = x2 - x1

            distance = (KOWN_WIDTH * FOCAL_LENGTH) / width
            

            label = model.names[int(box.cls[0])]

            if label != "cell phone":
                continue

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)

            cv2.putText(frame,f"{label} {distance:.2f} cm",
                        (x1,y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,255,0),
                        2)
    cv2.imshow("Object Distance Detection",frame)

    if cv2.waitKey(1) & 0xff ==27:
        break

cap.release()
cv2.destroyAllWindows()
