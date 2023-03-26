import cv2
import face_recognition
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        #cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
       # cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
       # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        # Finding The Distance
        #Wide in Cm
        W = 6.3
        f = 840
        d = (W*f)/w
        d = int(d)
        print(d)
        cvzone.putTextRect(
            img, f'Depth: {d} cm', (face[5][0], face[5][1]), scale=2)

    cv2.imshow("image", img)
    cv2.waitKey(1)
# https://www.youtube.com/watch?v=jsoe1M2AjFk
