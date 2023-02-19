import cv2


def open(camindex, camname):
    cap = cv2.VideoCapture(camindex)
    if not cap.isOpened():
        print("Error opening the webcam.")
        exit()
    while True:
        ret, frame = cap.read()
        cv2.imshow(camname, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def capimage(camindex, imagepath):
    cap = cv2.VideoCapture(camindex)
    if not cap.isOpened():
        print("Error opening the webcam.")
        exit()
    ret, frame = cap.read()
    cv2.imwrite(imagepath, frame)
    cap.release()
    cv2.imshow("Captured Image", frame)
    cv2.destroyAllWindows()


def DetectFace(camindex, camname):
    eye_cap = cv2.CascadeClassifier("xml/eye.xml")
    face_cap = cv2.CascadeClassifier("xml/face.xml")
    video_cap = cv2.VideoCapture(camindex)
    while True:
        ret, video_data = video_cap.read()
        color = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
        eye = eye_cap.detectMultiScale(
            color,
            # The smaller this value, the finer the scale and the slower the detection
            scaleFactor=1.0485258,
            minNeighbors=6,  # A higher value will result in fewer detections but with higher accuracy. The default value is 3
            minSize=(40, 40),  # Hight Width
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # print("Found {0} faces!".format(len(eye)))  # Find face
        for (x, y, w, h) in eye:
            cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 255), 2)
        face = face_cap.detectMultiScale(
            color,
            # The smaller this value, the finer the scale and the slower the detection
            scaleFactor=1.0485258,
            minNeighbors=6,  # A higher value will result in fewer detections but with higher accuracy. The default value is 3
            minSize=(200, 100),  # Hight Width
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (fx, fy, fw, fh) in face:
            cv2.rectangle(video_data, (fx, fy),
                          (fx+fw, fy+fh), (127, 0, 255), 2)

        cv2.imshow(camname, video_data)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_cap.release()
    cv2.destroyAllWindows()


DetectFace(0, "Capture")
