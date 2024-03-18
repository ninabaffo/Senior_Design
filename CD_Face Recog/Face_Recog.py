#Program to Detect the Face and Recognise the Person based on the data from face-trainner.yml

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
from PIL import Image #Pillow lib for handling images 
import subprocess

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

# Function to display camera feed
def display_camera_feed():
    cap = cv2.VideoCapture(0, cv2.CAP_V4L)

    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Camera Feed", 640, 480)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture frame.")
            break

        cv2.imshow("Camera Feed", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

labels = ["Nina"]

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face-trainner.yml")

cap = cv2.VideoCapture(0) #Get vidoe feed from the Camera

while(True):

	ret, img = cap.read() # Break video into frames 
	print(img.shape)
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
