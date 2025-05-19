import time
import numpy as np
from picamera2 import Picamera2
from threading import Event

def capture_fast_video(duration_sec=10, max_frames=1000):
    """
    Captures raw video frames as fast as possible using Picamera2.
    
    Args:
        duration_sec (int): Duration to capture in seconds.
        max_frames (int): Optional max number of frames to store.
    
    Returns:
        List[np.ndarray]: Captured video frames.
    """
    picam2 = Picamera2()

    # Use low resolution and fast format (YUV420 for speed)
    config = picam2.create_video_configuration(
        main={"size": (320, 240), "format": "YUV420"}
    )
    picam2.configure(config)

    frames = []
    stop_event = Event()

    def handle_frame(request):
        if stop_event.is_set():
            return
        frame = request.make_array("main")
        frames.append(frame)
        if len(frames) >= max_frames:
            stop_event.set()

    picam2.post_callback = handle_frame
    picam2.start()

    time.sleep(duration_sec)
    stop_event.set()
    picam2.stop()
    return frames
