
import time
import numpy as np
import naoqi as n
import sys
import argparse
import sys

nao_ip = "192.168.0.48"
port = 9559
# Get the service ALVideoRecorder.
VR = n.ALProxy("ALVideoRecorder", nao_ip, port)

# This records a 320*240 MJPG video at 10 fps.
# Note MJPG can't be recorded with a framerate lower than 3 fps.
VR.setResolution(2)
VR.setFrameRate(10)
VR.setVideoFormat("MJPG")
VR.setCameraID(1)

VR.startRecording("images/", "video")

time.sleep(5)

# Video file is saved on the robot in the
# /home/nao/recordings/cameras/ folder.
videoInfo = VR.stopRecording()

print "Video was saved on the robot: ", videoInfo[1]
print "Num frames: ", videoInfo[0]
    
