import face_recognition
import cv2
import numpy as np
import os


def test():
    path = 'images'
    images = []
    clasName = []
    mylist = os.listdir(path)
    for cl in mylist:
        image = cv2.imread(f'{path}/{cl}')
        images.append(image)
        clasName.append(os.path.splitext(cl)[0])

    print(clasName)


test()

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
