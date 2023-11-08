#Use Multi-camera-Adapter v2.2
from picamera2 import Picamera2, Preview
import time
from datetime import datetime
import os

picam2 = Picamera2()
os.system("v4l2-ctl --set-ctrl wide_dynamic_range=1 -d /dev/v4l-subdev0")
camera_config = picam2.create_preview_configuration({"size": (1920, 1080)})
picam2.configure(camera_config)
picam2.start_preview(True)
picam2.start()
time.sleep(2)
image_name = f"image{datetime.now():%Y%m%d%H%M%S}.jpg"
picam2.capture_file(image_name)
print("end")
