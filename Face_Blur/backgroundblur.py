import cv2
import numpy as np
import face_recognition
import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.preview_configuration.main.size = (800,800)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

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
    while True:
        im= picam2.capture_array()
        cv2.imshow("Camera", im)
        blur_except_faces(im)
        if cv2.waitKey(1)==ord('q'):
            break

cv2.destroyAllWindows()

'''
import cv2
import numpy as np
import face_recognition
import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.preview_configuration.main.size = (800, 800)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

while True:
    frame = picam2.capture_array()

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

    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
'''

''' 
import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.preview_configuration.main.size = (800,800)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

while True:
    im= picam2.capture_array()
    cv2.imshow("Camera", im)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
'''