#Use Multi-camera-Adapter v2.2
import socket
import time 
import RPi.GPIO as gp
import numpy as np
import os

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput

address = ('198.168.11.2', 8888)
#65530 is already used to connect in ssh.

#Connecting to camera A
gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)
i2c = "i2cset -y 1 0x70 0x00 0x04"
os.system(i2c)
gp.output(7, False)
gp.output(11, False)
gp.output(12, True)

#Setting camera
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration({"size": (1920, 1080)})
picam2.configure(camera_config)
encoder = H264Encoder(1000000)


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(address)
    stream = sock.makefile("wb")
    picam2.start_recording(encoder, FileOutput(stream))
    time.sleep(20)
    picam2.stop_recording()

