from multiprocessing import Queue, Process
from tensorflowObjectDetectorService import createObjectDetector
from mjpegService import createServerStream
from targetInfo import createInfoWsStream
    
if __name__ == '__main__':
    # Frame queues
    processed_frame_queue = Queue()
    raw_frame_queue = Queue()
    
    # Frame resolution queue
    res_queue = Queue()
    
    # targetInfo queue
    target_info_queue = Queue()
    
    # Processed stream
    processedStreamObjDetector = Process(target=createObjectDetector, args=(processed_frame_queue, raw_frame_queue, res_queue, target_info_queue, "UserData/Models/bill", 1, 0, 0.80, False))
    processedStreamObjDetector.start()
    
    # MJPEG stream
    streamMJPEG = Process(target=createServerStream, args=(processed_frame_queue, "processedstream", raw_frame_queue, "rawstream", res_queue.get(), 100, 30, 8080))
    streamMJPEG.start()
    
    # targetInfo stream
    targetInfoStream = Process(target=createInfoWsStream, args=(target_info_queue, 5000))
    targetInfoStream.start()