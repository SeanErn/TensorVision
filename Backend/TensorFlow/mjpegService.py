from mjpeg_streamer import MjpegServer, Stream
from multiprocessing import Queue

# Start the server
def createServerStream(PROCESSED_FRAME_QUEUE: Queue, PROCESSED_CAMERA_URL: str, RAW_FRAME_QUEUE: Queue, RAW_CAMERA_URL: str, CAMERA_RES: tuple, CAMERA_QUALITY: int, MAX_FPS: int, PORT: int):

    # Create an MJPEG server
    server = MjpegServer("localhost", PORT)
    
    processedStream = Stream(PROCESSED_CAMERA_URL, CAMERA_RES, CAMERA_QUALITY, MAX_FPS)
    rawStream = Stream(RAW_CAMERA_URL, CAMERA_RES, CAMERA_QUALITY, MAX_FPS)
    
    # Add the stream to the server
    server.add_stream(processedStream)
    server.add_stream(rawStream)
    
    server.start()

    while True:
        processedStream.set_frame(PROCESSED_FRAME_QUEUE.get())
        rawStream.set_frame(RAW_FRAME_QUEUE.get())
        


