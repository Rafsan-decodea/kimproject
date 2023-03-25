import cv2
import face_recognition

# Open the default video capture device
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture device
    success, img = cap.read()
    if not success:
        continue

    # Resize the image for faster face detection
    small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_img = small_img[:, :, ::-1]

    # Find all the faces and facial landmarks in the current frame
    face_locations = face_recognition.face_locations(rgb_small_img)
    face_landmarks = face_recognition.face_landmarks(
        rgb_small_img, face_locations)

    # Draw the face landmarks and face boundary box on the frame
    for (top, right, bottom, left) in face_locations:
        # Scale the face location coordinates back up by 4x to get the original image size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw the face boundary box on the frame
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

    # Draw the facial landmarks on the frame
    for landmarks in face_landmarks:
        for name, points in landmarks.items():
            for point in points:
                # Scale the facial landmark coordinates back up by 4x to get the original image size
                x = point[0] * 4
                y = point[1] * 4
                cv2.circle(img, (x, y), 2, (0, 0, 255), -1)

    # Display the resulting image
    cv2.imshow("Video", img)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
