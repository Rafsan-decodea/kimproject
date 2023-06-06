


import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("../firebase.json")
firebase_admin.initialize_app(cred)

def get_bucket(bucket_name):
    if bucket_name is None:
        raise ValueError("ValueError: Storage bucket name not specified. Specify the bucket name via the \"storageBucket\" option when initializing the App, or specify the bucket name explicitly when calling the storage.bucket() function.")


    bucket = storage.bucket(bucket_name)
    return bucket

bucket = get_bucket("kimsirproject.appspot.com")

images = bucket.list_blobs()

for image in images:
    print(image.name)