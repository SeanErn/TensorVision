from mjpeg_streamer import MjpegServer, Stream
from multiprocessing import Queue

# Start the server
def createServerStream(CAMERA_URL: str, CAMERA_RES: tuple, CAMERA_QUALITY: int, MAX_FPS: int, PORT: int, FRAME_QUEUE: Queue):
    # Create a stream with desired settings
    stream = Stream(CAMERA_URL, CAMERA_RES, CAMERA_QUALITY, MAX_FPS)

    # Create an MJPEG server
    server = MjpegServer("localhost", PORT)

    # Add the stream to the server
    server.add_stream(stream)

    server.start()

    while True:
        stream.set_frame(FRAME_QUEUE.get())  # Set the frame for the stream

