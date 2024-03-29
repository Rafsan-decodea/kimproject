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


def get_bucket(bucket_name):
    if bucket_name is None:
        raise ValueError(
            'ValueError: Storage bucket name not specified. Specify the bucket name via the "storageBucket" option when initializing the App, or specify the bucket name explicitly when calling the storage.bucket() function.'
        )

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


def download_images_from_directory(bucket_name, directory, save_directory):
    ref = db.reference('/knownperson')
    data = ref.get()
    for key, value in data.items():
       print(key, value)
    bucket = get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=directory)

    # for blob in blobs:
    #     image_name = blob.name + ".jpg"
    #     save_path = os.path.join(save_directory, image_name)

    #     # Create directory if it doesn't exist
    #     os.makedirs(os.path.dirname(save_path), exist_ok=True)

    #     # Download image data
    #     blob.download_to_filename(save_path)

        # Optionally, decode and display the image using OpenCV
        # image = cv2.imread(save_path)
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


# bucket_name = "kimsirproject.appspot.com"
# directory = ""  # Specify the directory path within the bucket

# images = get_images_from_directory(bucket_name, directory)

# for image in images:

#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
