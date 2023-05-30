import pyrebase
from google.cloud import storage
import os 
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
base_dir = os.getcwd()
storage_client = storage.Client.from_service_account_json(base_dir+"/firebase.json")

def fetch_all_images():
    bucket = storage_client.get_bucket("known")
    blobs = bucket.list_blobs()

    for blob in blobs:
        if blob.name.endswith('.jpg') or blob.name.endswith('.jpeg') or blob.name.endswith('.png'):
            print('Image URL:', blob.public_url)  # Print the download URL
            # Perform any further processing or display the images as needed

fetch_all_images()