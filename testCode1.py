import cv2
import os
import numpy as np
import tkinter as tk
import tkinter.font as font
import datetime
from datetime import datetime
import pyrebase

# python3 -m pip install pycryptodome
# python3 -m pip install pyrebase4
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


def databasetest():
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
    data = {
        "name": "John",
        "age": 10000,
        "email": "john@example.com",

    }
    db = firebase.database()
    data = {
        "type": "intruder",
        "date": datetime.now().strftime("%D-%H-%M-%S"),
        "image": "hi"

    }

    db.child("intruder").child().push(data)
    # d = db.child("users").child("-NP8H_eT066j_tWJK6n4").get()
    # res = d.val()
    # for x, y in res.items():
    #     print(x, '==>', y)

    # storage = firebase.storage()
    # filename = "rafsan.jpg"
    # path_on_cloud = "images/" + filename
    # storage.child(path_on_cloud).put(
    #     "rafsan.jpg", "AIzaSyBiP96UgQNqzcblfcNqmp8arneThFH7SQI")
    # storage.child("").delete("images/rafsan.jpg",
    #                          "AIzaSyBiP96UgQNqzcblfcNqmp8arneThFH7SQI")

    # # Get the download URL of the image
    # url = storage.child(path_on_cloud).get_url(None)
    # print(url)


def collect_data():
    name = input("Enter name of person : ")

    count = 1
    ids = input("Enter ID: ")

    cap = cv2.VideoCapture(0)

    filename = "xml/haarcascade_frontalface_default.xml"

    cascade = cv2.CascadeClassifier(filename)

    while True:
        _, frm = cap.read()

        gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

        faces = cascade.detectMultiScale(gray, 1.4, 1)

        for x, y, w, h in faces:
            cv2.rectangle(frm, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi = gray[y:y+h, x:x+w]

            cv2.imwrite(f"train/{name}-{count}-{ids}.jpg", roi)
            count = count + 1
            cv2.putText(frm, f"{count}", (20, 20),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
            # cv2.imshow("new", roi)

        cv2.imshow("identify", frm)

        if cv2.waitKey(1) == 27 or count > 300:
            cv2.destroyAllWindows()
            cap.release()
            train()
            break


def train():
    print("training part initiated !")

    recog = cv2.face.LBPHFaceRecognizer_create()

    dataset = 'train'

    paths = [os.path.join(dataset, im) for im in os.listdir(dataset)]

    faces = []
    ids = []
    labels = []
    for path in paths:
        labels.append(path.split('/')[-1].split('-')[0])

        ids.append(int(path.split('/')[-1].split('-')[2].split('.')[0]))

        faces.append(cv2.imread(path, 0))

    recog.train(faces, np.array(ids))

    recog.save('model.yml')
    print("Finished")

    return


def identify():
    cap = cv2.VideoCapture(0)
    count = 1
    filename = "xml/haarcascade_frontalface_default.xml"

    paths = [os.path.join("train", im) for im in os.listdir("train")]
    labelslist = {}
    for path in paths:
        labelslist[path.split('/')[-1].split('-')[2].split('.')
                   [0]] = path.split('/')[-1].split('-')[0]

    print(labelslist)
    recog = cv2.face.LBPHFaceRecognizer_create()

    recog.read('model.yml')

    cascade = cv2.CascadeClassifier(filename)

    while True:
        _, frm = cap.read()

        gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

        faces = cascade.detectMultiScale(gray, 1.3, 2)
        cv2.putText(frm, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                    0.6, (255, 255, 255), 2)

        for x, y, w, h in faces:
            cv2.rectangle(frm, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi = gray[y:y+h, x:x+w]

            label = recog.predict(roi)

            if label[1] < 100:
                print("Found")
                cv2.putText(frm, f"{labelslist[str(label[0])]}",
                            (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            else:
                print("Not Found")
                cv2.putText(frm, "unkown", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime('%Y-%m-%d')
                imagename = f'intruder/{formatted_datetime}.jpg'
                cv2.imwrite(imagename, roi)

                path_on_cloud = "images/" + imagename
                storage.child(path_on_cloud).put(
                    imagename, "AIzaSyBiP96UgQNqzcblfcNqmp8arneThFH7SQI")
                url = storage.child(path_on_cloud).get_url(None)
                print(url)
                data = {
                    "type": "intruder",
                    "date": datetime.now().strftime("%D-%H-%M-%S"),
                    "image": url

                }
                db = firebase.database()
                db.child("users").child().push(data)

        cv2.imshow("identify", frm)

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            cap.release()
            break


def maincall():

    root = tk.Tk()

    root.geometry("480x100")
    root.title("identify")

    label = tk.Label(root, text="Select below buttons ")
    label.grid(row=0, columnspan=2)
    label_font = font.Font(size=10, weight='bold', family='Helvetica')
    label['font'] = label_font

    btn_font = font.Font(size=10)

    button1 = tk.Button(root, text="Add Member ",
                        command=collect_data, height=2, width=20)
    button1.grid(row=1, column=0, pady=(10, 10), padx=(5, 5))
    button1['font'] = btn_font

    button2 = tk.Button(root, text="Start with known ",
                        command=identify, height=2, width=20)
    button2.grid(row=1, column=1, pady=(10, 10), padx=(5, 5))
    button2['font'] = btn_font
    root.mainloop()

    return


databasetest()
