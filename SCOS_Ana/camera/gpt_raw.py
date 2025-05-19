import time
import numpy as np
from picamera2 import Picamera2, Preview
from picamera2.encoders import Quality
from picamera2.outputs import FileOutput

def capture_video_frames(duration_sec=10, fps=100):
    """
    Captures raw video frames using Picamera2 for the given duration at specified FPS.
    
    Args:
        duration_sec (int): Duration of capture in seconds.
        fps (int): Frame rate in frames per second.
    
    Returns:
        List[np.ndarray]: List of captured frames as NumPy arrays.
    """
    picam2 = Picamera2()
    
    # Configure the camera with a suitable mode for high frame rate
    video_config = picam2.create_video_configuration(
        main={"size": (640, 480), "format": "RGB888"},
        controls={"FrameDurationLimits": (10000, 10000)}  # 100 Hz = 10,000 µs per frame
    )
    picam2.configure(video_config)

    frames = []
    picam2.start()
    
    start_time = time.time()
    frame_interval = 1.0 / fps
    
    while (time.time() - start_time) < duration_sec:
        frame = picam2.capture_array()
        frames.append(frame)
        time.sleep(frame_interval)  # Regulate frame capture rate
    
    picam2.stop()
    return frames

data = capture_video_frames( duration_sec=2, fps=100)
print( data)
