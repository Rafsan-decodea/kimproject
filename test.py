import cv2
import face_recognition

video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Convert the image to grayscale and apply the Canny edge detection algorithm
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 100)

    # Find the face landmarks using the face recognition library
    face_landmarks = face_recognition.face_landmarks(frame)

    # Draw the face landmarks on the image
    for landmark in face_landmarks:
        for key, value in landmark.items():
            for point in value:
                cv2.circle(edges, point, 1, (0, 255, 0), 1)

    # Write the frame to the output video

    # Show the frame in a window
    cv2.imshow("Video", edges)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
