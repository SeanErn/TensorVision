import tornado.ioloop
from multiprocessing import Queue, Process
from tensorflowObjectDetectorService import createObjectDetector
from mjpegService import createServerStream
    
if __name__ == '__main__':
    processed_frame_queue = Queue()
    raw_frame_queue = Queue()
    res_queue = Queue()
    # Processed stream
    processedStreamObjDetector = Process(target=createObjectDetector, args=(processed_frame_queue, raw_frame_queue, res_queue, "UserData/Models/bill", 1, 0, 0.80, True))
    processedStreamObjDetector.start()
    
    streamMJPEG = Process(target=createServerStream, args=(processed_frame_queue, "processedstream", raw_frame_queue, "rawstream", res_queue.get(), 50, 30, 8080))
    streamMJPEG.start()