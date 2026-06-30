import subprocess

class RTMPEgress:
    def __init__(self, output_url, scaled_width, scaled_height):
        self.output_url = output_url
        self.width = scaled_width
        self.height = scaled_height
        self.channels = 3
        self.frame_size = self.width * self.height * self.channels

    def start(self):
        """FFmpeg command to pipe frames back to RTMP"""
        # FFmpeg command to pipe frames back to RTMP
        ffmpeg_cmd = [
            "ffmpeg",
            "-y",
            "-f", "rawvideo",
            "-vcodec", "rawvideo",
            "-pix_fmt", "bgr24",
            "-s", f"{self.width}x{self.height}",
            "-r", "10",
            "-use_wallclock_as_timestamps", "1",
            "-i", "-",
            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-tune", "zerolatency",
            "-pix_fmt", "yuv420p",
            "-g", "20",
            "-f", "flv",
            self.output_url
        ]
        self.process = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

    def write_frame(self, new_frame):
        self.process.stdin.write(new_frame.tobytes())

    def stop(self):
        """Stop FFmpeg process"""
        if self.process:
            self.process.kill()
            self.process = None
