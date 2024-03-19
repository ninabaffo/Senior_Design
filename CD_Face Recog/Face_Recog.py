import cv2
import numpy as np
from flask import Flask, Response

# Initialize Flask application
app = Flask(__name__)

# Load face cascade and face recognizer
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face-trainner.yml")

labels = ["Nina"]

# Capture video from camera
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # Read frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        # Draw rectangle around detected faces and recognize them
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 80:
                name = labels[id_]
                cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Encode frame as JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()

        # Yield frame bytes to generator
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='raspberrypi-nina', port=8000)
    
""" #Program to Detect the Face and Recognise the Person based on the data from face-trainner.yml

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
from PIL import Image #Pillow lib for handling images 
import subprocess
from flask import Flask, Response

# Make camera script executable
username = 'pizero2'
command = f'sudo /home/{username}/.rpi-uvc-gadget.sh &'

try:
    # Execute the shell command
    subprocess.run(command, shell=True, check=True)
    print("Command executed successfully.")
except subprocess.CalledProcessError as e:
    # Handle any errors that occur during command execution
    print(f"Error executing command: {e}")

labels = ["Nina"]

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face-trainner.yml")

cap = cv2.VideoCapture(0) #Get vidoe feed from the Camera

while(True):

	ret, img = cap.read() # Break video into frames 
	gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) #Recog. faces
	for (x, y, w, h) in faces:
		roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 

		id_, conf = recognizer.predict(roi_gray) #recognize the Face
	
		if conf>=80:
			font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name 
			name = labels[id_] #Get the name from the List using ID number 
			cv2.putText(img, name, (x,y), font, 1, (0,0,255), 2)
		
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

	cv2.imshow('Preview',img) #Display the Video
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

"""