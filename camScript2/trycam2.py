import cv2  # library that allows us to interact with the camera
import time
import lzo
from picamera2 import Picamera2  # this library is how we grab the frame 
piCam = Picamera2() # create camera object 

# set camera settings 
piCam.preview_configuration.main.size=(640, 360)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.controls.FrameRate=30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()
fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_COMPLEX
height=1.5
myColor=(0,0,255)
weight=3
while True:
    # measure framerate 
    tStart=time.time()
    frame=piCam.capture_array() # grab the frame 
    
    # print frames per second on video 
    cv2.putText(frame,str(int(fps)), pos, font, 1.5, myColor, weight)

    # Compress the frame using LZO
    compressed_frame = lzo.compress(frame.tobytes())

    # Convert back to numpy array
    decompressed_frame = np.frombuffer(lzo.decompress(compressed_frame), dtype=np.uint8)
    decompressed_frame = decompressed_frame.reshape(frame.shape)

    # Display the decompressed frame
    cv2.imshow("piCam", decompressed_frame)  # display the frame

    if cv2.waitKey(1)==ord('q'):    # press 'q' to exit out of the camera preview
        break
    tEnd=time.time()
    loopTime=tStart-tEnd 
    fps=1/loopTime 
    #print(fps)

cv2.destroyAllWindows()
