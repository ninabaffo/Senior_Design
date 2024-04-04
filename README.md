### Mac OS users
The preview window uses XQuartz, download it on your local machine before running the code here: https://www.xquartz.org/

### ** Important **
- When you SSH into your pi, do 'ssh username@hostname.local -X' 
- If you SSH into your RPi without -x argument and try to display a frame (eg. cv2.imshow()), you will likely get an error. 
- The solution is to use X11 forwarding when SSHing to the RPi.
- If you want to read more about it, see here: https://docs.luxonis.com/projects/hardware/en/latest/pages/guides/raspberrypi/?highlight=x11#ssh-ing-without-x11-forwarding

##### Pi OS
- Bullseye, 32-bit, no desktop
- sudo apt update                    // do not upgrade 

##### Git
- sudo apt install -y git

##### Pip
- sudo apt install python3-pip

##### Opencv
- sudo apt install -y python3-opencv
- sudo apt install -y opencv-data
- sudo apt install libopencv-dev

##### libcamera / rpicam
- sudo apt install -y libcamera-dev libjpeg-dev libpng-dev
- sudo apt install libavdevice-dev libavformat-dev libswresample-dev
- sudo apt install -y libboost-dev libgnutls28-dev openssl libtiff5-dev pybind11-dev
- sudo apt install -y meson cmake
- sudo apt install -y python3-yaml python3-ply
- sudo apt install libjasper-dev libwebp-dev
- sudo apt install libhdf5-dev libhdf5-103
- sudo apt install libgtk-3-dev       // dont know if we need this or not, i think no
- sudo apt install libatlas-base-dev liblapacke-dev gfortran
- sudo apt-get install libopenblas-dev

##### Picamera2 
- sudo apt install -y python3-picamera2
- sudo apt install -y python3-opengl

##### codeblocks 
- sudo apt install codeblocks

#####  v4l2-utils 
- sudo apt install v4l2loopback-dkms v4l2loopback-utils ffmpeg

##### Gstreamer for pipeline
- sudo apt-get install gstreamer1.0-plugins-good
- sudo apt-get install gstreamer1.0-tools
- sudo apt install python3-pip python3-yaml libyaml-dev python3-ply python3-jinja2
- sudo apt install libx264-dev libjpeg-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-ugly gstreamer1.0-tools gstreamer1.0-gl gstreamer1.0-gtk3

### Face_Recognition libraries 

- sudo apt-get install build-essential \ cmake \ gfortran \ git \ wget \ curl \ graphicsmagick \ libgraphicsmagick1-dev \ libatlas-base-dev \ liblapack-dev \ libatlas3-base \ libavcodec-dev \ libavformat-dev \ libboost-all-dev \ libgtk2.0-dev \ libjpeg-dev \ liblapack-dev \ libswscale-dev \ pkg-config \ python3-dev \ python3-numpy \ python3-pip \ zip

