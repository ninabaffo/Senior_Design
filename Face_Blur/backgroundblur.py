import cv2
import numpy as np
import face_recognition

# Function to blur everything except faces
def blur_except_faces(frame):
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    for (top, right, bottom, left) in face_locations:
        # Blur everything except faces
        frame[0:top, :] = cv2.blur(frame[0:top, :], (23, 23))  # Blur top region
        frame[bottom:, :] = cv2.blur(frame[bottom:, :], (23, 23))  # Blur bottom region
        frame[:, 0:left] = cv2.blur(frame[:, 0:left], (23, 23))  # Blur left region
        frame[:, right:] = cv2.blur(frame[:, right:], (23, 23))  # Blur right region

    return frame

# Function to run the photobooth application
def run_photobooth():
    # Get a reference to the webcam (0 is usually the default webcam on MacBook)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture a photo
        ret, frame = video_capture.read()

        # Apply blurring except on faces
        frame = blur_except_faces(frame)

        # Display the resulting image
        cv2.imshow('Photobooth', frame)

        # Check for user input to capture the photo or exit the application
        key = cv2.waitKey(1)
        if key == ord('c'):  # Example: 'c' to capture photo
            # Save the photo or process it further
            # ...
            pass
        elif key == ord('q'):  # Example: 'q' to quit
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

# Run the photobooth application
run_photobooth()