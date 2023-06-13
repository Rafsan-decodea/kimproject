import cv2
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db
from io import BytesIO
import os
import requests

firebasepath = os.getcwd() + "/lib/firebase.json"
fireStorageCredit = credentials.Certificate(firebasepath)
firebase_admin.initialize_app(fireStorageCredit,{'databaseURL':'https://kimsirproject-default-rtdb.firebaseio.com'})


def handle_new_data(event):
    # Get the newly added data
    new_data = event.data

    # Process the new data
    # For example, download the image and use it with OpenCV
    ref = db.reference('/knownperson')
    data = ref.get()
    for key, value in data.items():
       image_url = value['image_url']
       image_name = value['name']+'_'+key+'.jpg'
       download_image(image_url,image_name)
       
    # Perform any additional processing or analysis as needed
    
    # Delete the data from the database (optional)
def handle_deleted_data(event):
    # Get the deleted data
    deleted_key = event.path.strip('/-')
    print (deleted_key)
    
    # Process the deleted data
    # For example, delete the local image file
    # image_name = deleted_data['name'] + '_' + deleted_data.key + '.jpg'
    

def download_image(image_url,image_name):
    
    response = requests.get(image_url)
    path = 'images/known/'+image_name
    with open(path, "wb") as f:
        f.write(response.content)

def delete_image(filename):
    path =  os.getcwd()+"/images/known/"+filename
    # Delete the local image file
    os.remove(path)



data_ref = db.reference('/knownperson')

# data_ref.listen(handle_new_data)
data_ref.listen(handle_deleted_data)