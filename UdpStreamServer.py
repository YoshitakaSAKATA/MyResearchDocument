import socket
import time 
import RPi.GPIO as gp
import numpy as np
import os

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput

