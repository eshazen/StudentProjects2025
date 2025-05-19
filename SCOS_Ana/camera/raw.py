#!/usr/bin/python3
import sys
from picamera2 import Picamera2, Preview
from picamera2.sensor_format import SensorFormat
from pprint import *
import time
import numpy as np

picam2 = Picamera2()
# create a configuration for the first sensor mode, which is 640x480
mode = picam2.sensor_modes[0]
raw_format = SensorFormat(picam2.sensor_format)
config = picam2.create_video_configuration(
   raw={"format": raw_format.format},
   sensor={'output_size': mode['size'], 'bit_depth': mode['bit_depth']})
picam2.configure(config)

pprint( picam2.camera_configuration())

picam2.start()
time.sleep(2)
# raw1 = picam2.capture_array("raw").view(np.uint16)
raw1 = picam2.capture_array("raw")
print("--- shape ---")
print(raw1.shape)
np.save( "raw1", raw1)
# print("--- data ---")
# np.set_printoptions(threshold=sys.maxsize)
# np.set_printoptions(linewidth=sys.maxsize)
# print(raw1)

