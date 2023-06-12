import cv2
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db
from io import BytesIO
import os

firebasepath = os.getcwd() + "/lib/firebase.json"
fireStorageCredit = credentials.Certificate(firebasepath)
firebase_admin.initialize_app(fireStorageCredit,{'databaseURL':'https://kimsirproject-default-rtdb.firebaseio.com'})


def handle_new_data(event):
    # Get the newly added data
    new_data = event.data

    # Process the new data
    # For example, download the image and use it with OpenCV
    image_url = new_data['image_url']
    image = download_image(image_url)
    # Perform any additional processing or analysis as needed
    
    # Delete the data from the database (optional)
    # event.ref.delete()

def download_image():
    ref = db.reference('/knownperson')
    data = ref.get()
    for key, value in data.items():
       print(key, value)




# data_ref = db.reference('/data')

# data_ref.listen(handle_new_data)