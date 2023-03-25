import cv2
import face_recognition

# Open the video capture device
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a frame from the video
    ret, frame = video_capture.read()

    # Resize the frame for faster face detection
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the frame from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all the faces and face landmarks in the current frame
    face_landmarks_list = face_recognition.face_landmarks(rgb_small_frame)

    # Draw the face landmarks and connect them
    for face_landmarks in face_landmarks_list:
        # Draw the facial landmarks
        for name, points in face_landmarks.items():
            for point in points:
                cv2.circle(
                    frame, (point[0] * 4, point[1] * 4), 2, (0, 0, 255), -1)

        # Connect the facial landmarks
        draw_points = [face_landmarks['chin'],
                       face_landmarks['left_eyebrow'],
                       face_landmarks['right_eyebrow'],
                       face_landmarks['nose_bridge'] +
                       face_landmarks['nose_tip'],
                       face_landmarks['left_eye'] +
                       [face_landmarks['left_eye'][0]],
                       face_landmarks['right_eye'] +
                       [face_landmarks['right_eye'][0]],
                       face_landmarks['top_lip'] + face_landmarks['bottom_lip'][::-1] + [face_landmarks['top_lip'][0]]]

        for points in draw_points:
            for i in range(len(points)-1):
                cv2.line(frame, (points[i][0] * 4, points[i][1] * 4),
                         (points[i+1][0] * 4, points[i+1][1] * 4), (0, 255, 0), 1)

    # Display the resulting image
    cv2.imshow("Video", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture device and close all windows
video_capture.release()
cv2.destroyAllWindows()
