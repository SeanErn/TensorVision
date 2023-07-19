# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from multiprocessing import Queue

def createObjectDetector(FRAME_QUEUE: Queue, RES_QUEUE: Queue, MODEL_DIR: str, NUMBER_CLASSES: int, VIDEO_DEVICE_NUMBER: int, MIN_CONF: float, GUI_ENABLED: bool):
    
    MODEL_NAME = MODEL_DIR # MODEL_DIR
    GRAPH_NAME = "detect.tflite"
    LABELMAP_NAME = "label.pbtxt"
    NUM_CLASSES = NUMBER_CLASSES # NUMBER_CLASSES
    VIDEO_PATH = VIDEO_DEVICE_NUMBER # VIDEO_DEVICE_NUMBER
    min_conf_threshold = MIN_CONF # MIN_CONF

    # Get path to current working directory
    CWD_PATH = os.getcwd()

    # Path to video file

    # Path to .tflite file, which contains the model that is used for object detection
    PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, GRAPH_NAME)

    # Path to label map file
    PATH_TO_LABELS = os.path.join(CWD_PATH, MODEL_NAME, LABELMAP_NAME)


    # Load the label map
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                                use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    # Load the Tensorflow Lite model.
    interpreter = tf.lite.Interpreter(model_path=PATH_TO_CKPT)

    interpreter.allocate_tensors()

    # Get model details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]
    print(height)
    print(width)
    floating_model = (input_details[0]['dtype'] == np.float32)

    input_mean = 128
    input_std = 128

    # Open video file
    try:
        video = cv2.VideoCapture(VIDEO_PATH)
        imW = video.get(cv2.CAP_PROP_FRAME_WIDTH)
        imH = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        RES_QUEUE.put((int(imW), int(imH)))
    except:
        print("Error while opening video capture...")
        exit()

    while video.isOpened():

        # Acquire frame and resize to expected shape [1xHxWx3]
        ret, frame = video.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (width, height))
        input_data = np.expand_dims(frame_resized, axis=0)

        # Normalize pixel values if using a floating model (i.e. if model is non-quantized)
        if floating_model:
            input_data = (np.float32(input_data) - input_mean) / input_std

        # Perform the actual detection by running the model with the image as input
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        # Retrieve detection results
        boxes = interpreter.get_tensor(output_details[0]['index'])[0]  # Bounding box coordinates of detected objects
        classes = interpreter.get_tensor(output_details[1]['index'])[0]  # Class index of detected objects
        scores = interpreter.get_tensor(output_details[2]['index'])[0]  # Confidence of detected objects
        num = interpreter.get_tensor(output_details[3]['index'])[0]  # Total number of detected objects (inaccurate and
        # not needed)

        # Loop over all detections and draw detection box if confidence is above minimum threshold
        for i in range(len(scores)):
            if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):
                # Get bounding box coordinates and draw box Interpreter can return coordinates that are outside of image
                # dimensions, need to force them to be within image using max() and min()
                ymin = int(max(1, (boxes[i][0] * imH)))
                xmin = int(max(1, (boxes[i][1] * imW)))
                ymax = int(min(imH, (boxes[i][2] * imH)))
                xmax = int(min(imW, (boxes[i][3] * imW)))

                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (10, 255, 0), 4)

                # Draw label
                object_name = categories[int(classes[i])]['name']
                label = '%s: %d%%' % (object_name, int(scores[i] * 100))  # Make Label
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)  # Get font size
                label_ymin = max(ymin, labelSize[1] + 10)  # Make sure not to draw label too close to top of window
                cv2.rectangle(frame, (xmin, label_ymin - labelSize[1] - 10),
                              (xmin + labelSize[0], label_ymin + baseLine - 10), (255, 255, 255),
                              cv2.FILLED)  # Draw white box to put label text in
                cv2.putText(frame, label, (xmin, label_ymin - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0),
                            2)  # Draw label text
        # stream frame to pipe      
        FRAME_QUEUE.put(frame)
        
        if GUI_ENABLED:
            # All the results have been drawn on the frame, so it's time to display it.
            cv2.imshow('Object detector(TFLite)', frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break
            
        # Clean up
        # video.release()
        # cv2.destroyAllWindows()
    
    return frame, boxes, classes, scores