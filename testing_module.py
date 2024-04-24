import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
ptime = 0
detector = pm.poseDetector(detectionCon=True , trackCon=True)
while True:
    success, img = cap.read()
    if not success:  # Check if frame was successfully captured
        print("Failed to capture frame. Exiting...")
        break

    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[20])  # This number shows which point we are tracking
        cv2.circle(img, (lmList[20][1], lmList[20][2]), 15, (0, 0, 255), cv2.FILLED)  # It circles the point we are tracking

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
