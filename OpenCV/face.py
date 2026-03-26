import cv2
from deepface import DeepFace

# 1. Setup Camera and Reference Photo
cap = cv2.VideoCapture(0)
reference_img_path = "me.jpeg" # Make sure this file exists in your folder
is_me = False
counter = 0

while True:
    ret, frame = cap.read()
    if not ret: break

    # 2. Only check every 30 frames to keep it fast
    if counter % 30 == 0:
        try:
            # result is a dictionary with a 'verified' key
            result = DeepFace.verify(frame, reference_img_path, enforce_detection=False)
            is_me = result['verified']
        except Exception as e:
            print("Error during verification:", e)

    counter += 1

    # 3. Show the result on the screen
    color = (0, 255, 0) if is_me else (0, 0, 255)
    label = "MATCH!" if is_me else "NO MATCH"
    cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
