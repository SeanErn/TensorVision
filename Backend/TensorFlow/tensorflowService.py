import tornado.ioloop
from multiprocessing import Queue, Process
from tensorflowObjectDetectorService import createObjectDetector
from mjpegService import createServerStream
    
if __name__ == '__main__':
    frame_queue = Queue()
    res_queue = Queue()
    processedStreamObjDetector = Process(target=createObjectDetector, args=(frame_queue, res_queue, "UserData/Models/bill", 1, 0, 0.97, True))
    processedStreamObjDetector.start()
    processedStreamMJPEG = Process(target=createServerStream, args=("processedStream", res_queue.get(), 50, 30, 8080, frame_queue))
    processedStreamMJPEG.start()