import subprocess
import threading
import numpy as np

class RTMPIngest:
    def __init__(self, input_url, scaled_width, scaled_height):
        self.input_url = input_url
        self.width = scaled_width
        self.height = scaled_height
        self.channels = 3
        self.frame_size = self.width * self.height * self.channels
        self._latest = None
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._reader = None
        self.process = None

    def start(self):
        ffmpeg_cmd = [
            "ffmpeg",
            "-i", self.input_url,
            "-f", "rawvideo",
            "-pix_fmt", "bgr24",
            "-vf", f"scale={self.width}:{self.height},fps=10",
            "-"
        ]
        self.process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        self._reader = threading.Thread(target=self._read_loop, daemon=True)
        self._reader.start()

    def _read_loop(self):
        while not self._stop.is_set():
            raw = self.process.stdout.read(self.frame_size)
            if len(raw) != self.frame_size:
                break
            with self._lock:
                self._latest = raw

    def get_frame_as_array(self):
        with self._lock:
            raw = self._latest
            self._latest = None
        if raw is None:
            return None
        return np.frombuffer(raw, np.uint8).reshape((self.height, self.width, self.channels))

    def stop(self):
        self._stop.set()
        if self.process:
            self.process.kill()
            self.process = None
