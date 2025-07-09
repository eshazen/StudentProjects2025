from picamera2 import Picamera2
from picamera2.encoders import Encoder
import time

picam2 = Picamera2()
config = picam2.create_video_configuration(raw={}, encode="raw")
picam2.configure(config)

encoder = Encoder()
picam2.start_recording( encoder, "test.raw")
time.sleep(5)
picam2.stop_recording()

