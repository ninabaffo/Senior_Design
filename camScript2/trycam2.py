import cv2  # library that allows us to interact with the camera
from picamera2 import Picamera2  # this library is how we grab the frame 
piCam = Picamera2() # create camera object 

# set camera settings 
piCam.preview_configuration.main.size=(1280,720)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.controls.FrameRate=60
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

while True:
    # measure framerate 
    tStart=time.time()
    frame=piCam.capture_array() # grab the frame 
    cv2.imshow("piCam", frame)  # display the frame

    if cv2.waitKey(1)==ord('q'):    # press 'q' to exit out of the camera preview
        break
    tEnd=time.time()
    loopTime=tStart-tEnd 
    fps=1/loopTime 
    print(fps)
cv2.destroyAllWindows()
