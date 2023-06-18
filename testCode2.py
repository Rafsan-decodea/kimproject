import face_recognition
import cv2
import numpy as np
import os
import time
import pyrebase
import datetime
# from datetime import datetime
import threading
import glob
from cvzone.FaceMeshModule import FaceMeshDetector
from lib.firebaseFaceCap import *
now = datetime.datetime.now()




def KnownImages():
    config = {
        "apiKey": "AIzaSyBiP96UgQNqzcblfcNqmp8arneThFH7SQI",
        "authDomain": "kimsirproject.firebaseapp.com",
        "databaseURL": "https://kimsirproject-default-rtdb.firebaseio.com",
        "projectId": "kimsirproject",
        "storageBucket": "kimsirproject.appspot.com",
        "messagingSenderId": "186797081014",
        "appId": "1:186797081014:web:d9d08d73bacdd7feb30117",
        "measurementId": "G-Q268WWQZPN"
    }
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    path_on_cloud="/knownperson"
    url = storage.child(path_on_cloud).get_url("AIzaSyBiP96UgQNqzcblfcNqmp8arneThFH7SQI")
    print (url)
    



def IntruderUpload():
    config = {
        "apiKey": "AIzaSyBiP96UgQNqzcblfcNqmp8arneThFH7SQI",
        "authDomain": "kimsirproject.firebaseapp.com",
        "databaseURL": "https://kimsirproject-default-rtdb.firebaseio.com",
        "projectId": "kimsirproject",
        "storageBucket": "kimsirproject.appspot.com",
        "messagingSenderId": "186797081014",
        "appId": "1:186797081014:web:d9d08d73bacdd7feb30117",
        "measurementId": "G-Q268WWQZPN"
    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    mylist = os.listdir("images/unknown")
    images = []
    # input all image path to list
    for image in mylist:
        images.append(image)

    # Image upload from directory
    url = ''
    for image in images:
        path_on_local = "images/unknown"
        filess = "images/unknown/"+image
        storage.child(path_on_local+image).put(filess)
        url = storage.child(
            path_on_local+image).get_url("AIzaSyBiP96UgQNqzcblfcNqmp8arneThFH7SQI")

        # storage.child("").delete("images/rafsan.jpg",
        #                          "AIzaSyBiP96UgQNqzcblfcNqmp8arneThFH7SQI")

    # delete Files After Upload
    jpg_files = glob.glob(os.path.join("images/unknown", "*.jpg"))
    for file_path in jpg_files:
        os.remove(file_path)

    # Upload all data
    date = now.strftime("%Y-%m-%d")
    timee = time.strftime("%H:%M:%S", time.localtime())
    dateetimee = date+" "+timee
    db = firebase.database()
    data = {
        "type": "intruder",
        "date": dateetimee,
        "image": url

    }
    db.child("intruder").child().push(data)
    url = ''


def facecap():
    imagename = input("Enter name of person : ")
    ids = input("Enter Face Id :")
    # Male And Femail Detected Mechanijm
    male_image = face_recognition.load_image_file(
        "male-femail/male.jpg")
    female_image = face_recognition.load_image_file(
        "male-femail/femail.jpg")
    male_encoding = face_recognition.face_encodings(male_image)[0]
    female_encoding = face_recognition.face_encodings(female_image)[0]
    labels = ['Female', 'Male']
    # Make and Femail Detect Mechanizm finished

    cap = cv2.VideoCapture(0)
    # cv2.namedWindow('Video', cv2.WINDOW_FREERATIO)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # Set BackGroud and resize
    imageBackground = cv2.imread('sifi.png', cv2.IMREAD_UNCHANGED)
    opacity = 0.9
    imageBackground = cv2.addWeighted(
        imageBackground, opacity, imageBackground, 1 - opacity, 0)
    background = cv2.resize(imageBackground, (width, height))
    detector = FaceMeshDetector()
    while True:
        success, imgWithBG = cap.read()
        success, img = cap.read()
        #success, FaceDetector = cap.read()
        img, faces = detector.findFaceMesh(img, draw=False)
        #FaceDetector, MeshFace = detector.findFaceMesh(FaceDetector, draw=True)
        imgWithBG = cv2.cvtColor(imgWithBG, cv2.COLOR_BGR2BGRA)
        # Set Image Backgroud
        imgWithBG = cv2.addWeighted(background, 0.5, imgWithBG, 0.5, 0)
        # CV2 Decoration
        if time.time() % 2 < 1:
            text = "Face Scanning Mode"
        else:
            text = ""

        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        text_size2, __ = cv2.getTextSize(
            "Press Q For Capture", cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

        img_center = (imgWithBG.shape[1] // 2, imgWithBG.shape[0] // 2)

        text_pos = (img_center[0] - (text_size[0] // 2),
                    100 - text_size[1])
        text_pos2 = (img_center[0] - (text_size2[0] // 2),
                     120 - text_size2[1])

        cv2.putText(imgWithBG, text, text_pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

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
            # For Calculate Face Distance
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]
            w, _ = detector.findDistance(pointLeft, pointRight)
            W = 6.3
            f = 840
            d = (W*f)/w
            d = int(d)

            # Captrure Signals
            cv2.putText(imgWithBG, "Press 'Q' For Capture", text_pos2,
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (244, 100, 0), 1)
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
            cv2.putText(imgWithBG, f"Distance({d}).CM", (x1+6, y2+50),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)
            #cv2.imshow("image", FaceDetector)
            # cv2.imwrite(f"train/{name}-1.jpg", )

        cv2.imshow("Video", imgWithBG)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # img = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            cv2.imwrite(f"images/known/{imagename}-{ids}.jpg", img)
            break
    cap.release()
    cv2.destroyAllWindows()


def identify():

    path = 'images/known'
    
    images = []
    ids = []
    clasName = []
    faceEncodeList = []
    def imgcheck():
        while True:
            mylist = os.listdir(path)
            
            for cl in mylist:
                image = cv2.imread(f'{path}/{cl}')
                # That is for Substract Name and Ids
                if cl.endswith('.jpg'):
                    parts = cl.split('-')
                    images.append(image)
                    clasName.append(parts[0])
                    ids.append(parts[1].split('.')[0])
         
    
    imgchk = threading.Thread(target=imgcheck)
    imgchk.start()
    for imgWithBG in images:
                imgWithBG = cv2.cvtColor(imgWithBG, cv2.COLOR_BGR2RGB)
                encodefaces = face_recognition.face_encodings(imgWithBG)[0]
                faceEncodeList.append(encodefaces) 

    cap = cv2.VideoCapture(0)
    # cv2.namedWindow('Video', cv2.WINDOW_FREERATIO)
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
        success, imgWithOutBg = cap.read()
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
                    100 - text_size[1])

        cv2.putText(imgWithBG, text, text_pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

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
                Id = ids[matchindex]
                y1, x2, y2, x1 = faceLoc
                # Because Previous We reside  image 4 times so now we Multyply that
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(imgWithBG, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(imgWithBG, (x1, y2-35), (x2, y2),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(imgWithBG, f"{name}", (x1+6, y2-6),
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
                date = now.strftime("%Y-%m-%d %H:%M:%S")
                timee = time.strftime("%H:%M:%S", time.localtime())
                dateetimee = date+timee
                cv2.imwrite(f"images/unknown/{dateetimee}.jpg",  imgWithOutBg)
                # ------- if image Write then Run that Firebase update Code ----------

                my_thread = threading.Thread(target=IntruderUpload)
                my_thread.start()

        cv2.imshow("Video", imgWithBG)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# db  = db.reference('/')
# db.listen(identify)

identify()
#facecap()
# KnownImages()

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
