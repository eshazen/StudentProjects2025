import time
import numpy as np
from picamera2 import Picamera2
from threading import Event

def capture_fast_video(duration_sec=10, max_frames=1000):
    """
    Captures raw video frames as fast as possible using Picamera2 and measures actual FPS.
    
    Args:
        duration_sec (int): Duration to capture in seconds.
        max_frames (int): Optional max number of frames to store.
    
    Returns:
        Tuple[List[np.ndarray], float]: List of captured frames and the actual FPS.
    """
    picam2 = Picamera2()

    # Use fast format and lower resolution for speed
    config = picam2.create_video_configuration(
        main={"size": (320, 240), "format": "YUV420"}
    )
    picam2.configure(config)

    frames = []
    stop_event = Event()
    start_time = None
    end_time = None

    def handle_frame(request):
        nonlocal start_time, end_time
        if stop_event.is_set():
            return
        if start_time is None:
            start_time = time.time()
        frame = request.make_array("main")
        frames.append(frame)
        if len(frames) >= max_frames:
            end_time = time.time()
            stop_event.set()

    picam2.post_callback = handle_frame
    picam2.start()

    # Wait for the duration or until max_frames reached
    stop_event.wait(timeout=duration_sec)
    if end_time is None:
        end_time = time.time()

    picam2.stop()

    elapsed_time = end_time - start_time if start_time and end_time else duration_sec
    actual_fps = len(frames) / elapsed_time if elapsed_time > 0 else 0.0

    print(f"Captured {len(frames)} frames in {elapsed_time:.2f} seconds ({actual_fps:.2f} FPS)")
    return frames, actual_fps

data = capture_fast_video()
