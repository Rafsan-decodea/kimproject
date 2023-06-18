import cv2
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db
from io import BytesIO
import os
import requests
from plyer import notification


firebasepath = os.getcwd() + "/lib/firebase.json"
fireStorageCredit = credentials.Certificate(firebasepath)
firebase_admin.initialize_app(
    fireStorageCredit,
    {"databaseURL": "https://kimsirproject-default-rtdb.firebaseio.com"},
)


def handle_new_data(event):
    new_data = event.data
    ref = db.reference("/knownperson")
    data = ref.get()
    for key, value in data.items():
        image_url = value["image_url"]
        image_name = value["name"] + "_" + key + ".jpg"
        download_image(image_url, image_name)


def handle_deleted_data(event):
    # Get the deleted data
    snapshot = event.data
    if snapshot is None:
        delete_image(event.path.strip("/"))


def download_image(image_url, image_name):
    notification.notify(title="From Server", message="Image Adding to path")
    response = requests.get(image_url)
    path = "images/known/" + image_name
    with open(path, "wb") as f:
        f.write(response.content)


def delete_image(filename):
    imagelist = os.listdir("images/known")
    print(filename)
    # input all image path to list
    for image in imagelist:
        if filename in image:
            mess = "A image Called " + image + " is Delete From Storage"
            notification.notify(title="From Server", message=mess)
            path = os.getcwd() + "/images/known/" + image
            os.remove(path)


data_ref = db.reference("/knownperson")

data_ref.listen(handle_new_data)
data_ref.listen(handle_deleted_data)
