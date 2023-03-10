import face_recognition
import cv2
import numpy as np
import os


def facecap():
    
    


def identify():
    path = 'images'
    images = []
    clasName = []
    mylist = os.listdir(path)
    faceEncodeList = []
    for cl in mylist:
        image = cv2.imread(f'{path}/{cl}')
        images.append(image)
        clasName.append(os.path.splitext(cl)[0])
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodefaces = face_recognition.face_encodings(img)[0]
        faceEncodeList.append(encodefaces)

    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        # Resize Image For Better Speed Search Image
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        # Current Image Capture Location
        faceCurFrame = face_recognition.face_locations(imgS)
        encodeCurrentFrame = face_recognition.face_encodings(
            imgS, faceCurFrame)
        for encodeFace, faceLoc in zip(encodeCurrentFrame, faceCurFrame):
            matches = face_recognition.compare_faces(
                faceEncodeList, encodeFace)
            faceDist = face_recognition.face_distance(
                faceEncodeList, encodeFace)
            matchindex = np.argmin(faceDist)

            if matches[matchindex]:
                name = clasName[matchindex]
                y1, x2, y2, x1 = faceLoc
                # Because Previous We sorts image 4 times
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            else:
                y1, x2, y2, x1 = faceLoc
                # Because Previous We sorts image 4 times
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2),
                              (0, 0, 255), cv2.FILLED)
                cv2.putText(img, "Unknown", (x1+6, y2-6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("webcam", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


identify()

# imagerafsan1 = face_recognition.load_image_file('images/rafsan.jpg')
# imagerafsan1 = cv2.cvtColor(imagerafsan1, cv2.COLOR_BGR2RGB)

# imagerafsan2 = face_recognition.load_image_file('images/test.jpg')
# imagerafsan2 = cv2.cvtColor(imagerafsan2, cv2.COLOR_BGR2RGB)

# faceloc = face_recognition.face_locations(imagerafsan1)[0]
# faceloc2 = face_recognition.face_locations(imagerafsan2)[0]


# encodeface = face_recognition.face_encodings(imagerafsan1)[0]
# encodeface2 = face_recognition.face_encodings(imagerafsan2)[0]


# cv2.rectangle(imagerafsan1, (faceloc[3],
#               faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 255), 6)
# cv2.rectangle(imagerafsan2, (faceloc2[3],
#               faceloc2[0]), (faceloc2[1], faceloc2[2]), (255, 0, 255), 6)


# results = face_recognition.compare_faces([encodeface], encodeface2)
# print(results)

# cv2.imshow('rafsan1', imagerafsan1)
# cv2.imshow('rafsan2', imagerafsan2)

# cv2.waitKey(0)
