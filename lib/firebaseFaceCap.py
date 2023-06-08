import cv2
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from io import BytesIO
import os

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

def get_bucket(bucket_name):
    if bucket_name is None:
        raise ValueError("ValueError: Storage bucket name not specified. Specify the bucket name via the \"storageBucket\" option when initializing the App, or specify the bucket name explicitly when calling the storage.bucket() function.")

    bucket = storage.bucket(bucket_name)
    return bucket

def get_images_from_directory(bucket_name, directory):
    bucket = get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=directory)
    images = []

    for blob in blobs:
        image_name = blob.name
    
        image = get_image(bucket_name, image_name)
        images.append(image)

    return images

def get_image(bucket_name, image_name):
    bucket = get_bucket(bucket_name)
    blob = bucket.blob(image_name)
    image_data = blob.download_as_bytes()
    image_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image

#bucket_name = "kimsirproject.appspot.com"
#directory = ""  # Specify the directory path within the bucket

# images = get_images_from_directory(bucket_name, directory)

# for image in images:

#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
