import face_recognition
import cv2
import numpy as np

# Load pre-trained Haar cascades for face detection
face_cascade = cv2.CascadeClassifier("../xml/haarcascade_frontalface_default.xml")

# Load pre-trained emotion detection model
model = cv2.ml.SVM_load("svm_model.xml")

# Define dictionary to map predicted labels to emotions
emotions = {
    0: "Angry",
    1: "Disgust",
    2: "Fear",
    3: "Happy",
    4: "Neutral",
    5: "Sad",
    6: "Surprise",
}

# Load sample image
img = cv2.imread("sample_image.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in image using Haar cascades
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Loop over detected faces
for x, y, w, h in faces:
    # Extract face ROI
    roi = gray[y : y + h, x : x + w]
    # Resize ROI to match model input size
    roi = cv2.resize(roi, (48, 48), interpolation=cv2.INTER_AREA)
    # Flatten ROI into 1D numpy array
    roi = np.reshape(roi, (1, -1))
    # Normalize ROI pixel values to range [0, 1]
    roi = roi.astype(float) / 255.0
    # Predict emotion label using model
    label = int(model.predict(roi)[1][0])
    # Map predicted label to emotion string
    emotion = emotions[label]
    # Draw bounding box and label on original image
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(
        img, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2
    )

# Display resulting image
cv2.imshow("Emotion detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
