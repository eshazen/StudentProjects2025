#!/usr/bin/python3
from picamera2 import Picamera2
from pprint import *
picam2 = Picamera2()
print("--- modes ---")
pprint(picam2.sensor_modes)
print("---")
