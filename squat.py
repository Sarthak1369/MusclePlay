import cv2
import numpy as np
import PoseModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector(detectionCon=True, trackCon=True)
count = 0
dir = "DOWN"

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    #print(lmList)
    if len(lmList) != 0:
        angle = detector.findAngles(img, 28, 26, 24) #this is for the point and getting points
        per = np.interp(angle, (190, 340), (0, 100))
        print(angle,per)

        #check for the squat
        if per == 100:
            if dir == "DOWN":
                count += 0.5
                dir = "UP"
        if per == 0:
            if dir == "UP":
                count += 0.5
                dir = "DOWN"

        print(count)
        cv2.rectangle(img, (0, 0), (225, 73), (245, 117, 16), -1)
        cv2.putText(img, str(int(count)), (10, 60), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5, cv2.LINE_AA)
        #cv2.putText(img, dir, (100, 60), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2, cv2.LINE_AA)



    cv2.imshow("image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
