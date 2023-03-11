import face_recognition
import cv2
import numpy as np
import os
import time


def facecap():
    # Male And Femail Detected Mechanijm
    male_image = face_recognition.load_image_file(
        "images/male-femail/male.jpg")
    female_image = face_recognition.load_image_file(
        "images/male-femail/femail.jpg")
    male_encoding = face_recognition.face_encodings(male_image)[0]
    female_encoding = face_recognition.face_encodings(female_image)[0]
    labels = ['Female', 'Male']
    # Make and Femail Detect Mechanizm finished

    cap = cv2.VideoCapture(0)
    #cv2.namedWindow('Video', cv2.WINDOW_FREERATIO)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Set BackGroud and resize
    imageBackground = cv2.imread('sifi.png', cv2.IMREAD_UNCHANGED)
    opacity = 0.9
    imageBackground = cv2.addWeighted(
        imageBackground, opacity, imageBackground, 1 - opacity, 0)
    background = cv2.resize(imageBackground, (width, height))

    while True:
        success, imgWithBG = cap.read()
        imgWithBG = cv2.cvtColor(imgWithBG, cv2.COLOR_BGR2BGRA)
        # Set Image Backgroud
        imgWithBG = cv2.addWeighted(background, 0.5, imgWithBG, 0.5, 0)
        # CV2 Decoration
        if time.time() % 1 < 0.3:
            text = "Face Scanning Mode"
        else:
            text = ""
        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        img_center = (imgWithBG.shape[1] // 2, imgWithBG.shape[0] // 2)
        text_pos = (img_center[0] - (text_size[0] // 2),
                    img_center[1] - text_size[1])

        cv2.putText(imgWithBG, text, text_pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 155, 255), 2)

        # Decoration Finished

        # Resize Image For Better Speed Search Image 4 times Smaller 100/4=> 25
        imgS = cv2.resize(imgWithBG, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        # Current Image Capture Location
        faceCurFrame = face_recognition.face_locations(imgS)
        # Current Image encoding's
        encodeCurrentFrame = face_recognition.face_encodings(
            imgS, faceCurFrame)
        for encodeFace, faceLoc in zip(encodeCurrentFrame, faceCurFrame):
            print("reading")
            y1, x2, y2, x1 = faceLoc
            results = face_recognition.face_distance(
                [female_encoding, male_encoding], encodeFace)
            label = labels[results.argmin()]

            # Because Previous We reside  image 4 times so now we Multyply that
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(imgWithBG, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imgWithBG, (x1, y2-35), (x2, y2),
                          (255, 20, 0), cv2.FILLED)
            cv2.putText(imgWithBG, f"Reading({label})", (x1+6, y2-6),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            # cv2.imwrite(f"train/{name}-1.jpg", )

        cv2.imshow("Video", imgWithBG)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


facecap()


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
    for imgWithBG in images:
        imgWithBG = cv2.cvtColor(imgWithBG, cv2.COLOR_BGR2RGB)
        encodefaces = face_recognition.face_encodings(imgWithBG)[0]
        faceEncodeList.append(encodefaces)

    cap = cv2.VideoCapture(0)
    #cv2.namedWindow('Video', cv2.WINDOW_FREERATIO)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Set BackGroud and resize
    imageBackground = cv2.imread('sifi.png', cv2.IMREAD_UNCHANGED)
    opacity = 0.9
    imageBackground = cv2.addWeighted(
        imageBackground, opacity, imageBackground, 1 - opacity, 0)

    background = cv2.resize(imageBackground, (width, height))

    while True:
        success, imgWithBG = cap.read()
        imgWithBG = cv2.cvtColor(imgWithBG, cv2.COLOR_BGR2BGRA)
        # Set Image Backgroud
        imgWithBG = cv2.addWeighted(background, 0.5, imgWithBG, 0.5, 0)
        # CV2 Decoration
        if time.time() % 1 < 0.3:
            text = "Face Detecting Mode"
        else:
            text = ""
        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        img_center = (imgWithBG.shape[1] // 2, imgWithBG.shape[0] // 2)
        text_pos = (img_center[0] - (text_size[0] // 2),
                    img_center[1] - text_size[1])

        cv2.putText(imgWithBG, text, text_pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 155, 255), 2)

        # Decoration Finished

        # Resize Image For Better Speed Search Image 4 times Smaller 100/4=> 25
        imgS = cv2.resize(imgWithBG, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        # Current Image Capture Location
        faceCurFrame = face_recognition.face_locations(imgS)
        # Current Image encoding's
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
                # Because Previous We reside  image 4 times so now we Multyply that
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(imgWithBG, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(imgWithBG, (x1, y2-35), (x2, y2),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(imgWithBG, name, (x1+6, y2-6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            else:
                y1, x2, y2, x1 = faceLoc
                # Because Previous We reside  image 4 times so now we Multyply that
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(imgWithBG, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(imgWithBG, (x1, y2-35), (x2, y2),
                              (0, 0, 255), cv2.FILLED)
                cv2.putText(imgWithBG, "Unknown", (x1+6, y2-6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Video", imgWithBG)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# identify()

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
