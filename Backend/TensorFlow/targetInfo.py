import math
from multiprocessing import Queue

def calculateMidpoint(target_top_left_xy: tuple, target_bottom_right_xy: tuple):
    tl = target_top_left_xy
    br = target_bottom_right_xy
    
    x_center = int((tl[0] + br[0])/2)
    y_center = int((tl[1] + br[1])/2)
    midpoint = (x_center, y_center)
    
    return midpoint

def calculateYaw(image_wh: tuple, fov: int, target_xy: tuple):
    # calculate the center of the image
    cx, cy = image_wh[0] / 2, image_wh[1] / 2

    # calculate the yaw
    yaw = math.atan2((target_xy[0] - cx), cx)
    yaw = math.degrees(yaw)  # convert to degrees
    # yaw = yaw * (fov / 2)  # scale by the field of view
    
    return yaw

def calculatePitch(image_wh: tuple, fov: int, target_xy: tuple):
    # calculate the center of the image
    cx, cy = image_wh[0] / 2, image_wh[1] / 2
    
        # calculate the pitch
    pitch = math.atan2((cy - target_xy[1]), cy)
    pitch = math.degrees(pitch)  # convert to degrees
    # pitch = pitch * (fov / 2)  # scale by the field of view
    
    return pitch

def calculateArea(image_wh: tuple, target_top_left_xy: tuple, target_bottom_right_xy: tuple):
    tl = target_top_left_xy
    br = target_bottom_right_xy
    
    # calculate the area of the bounding box
    box_width = br[0] - tl[0]
    box_height = br[1] - tl[1]
    box_area = box_width * box_height
    
    # calculate the total area of the frame
    frame_area = image_wh[0] * image_wh[1]

    # calculate the percentage of frame area that the box covers
    box_percentage = (box_area / frame_area) * 100
    
    return box_percentage

import asyncio
import websockets
import json

def createInfoWsStream(TARGET_INFO_QUEUE: Queue,  PORT: int):
    """Create a websocket server to stream detection info to the server.

    Args:
        DETECTION_INFO (Queue): The queue containing the array of json with each target's info
        PORT (int): The port to run the server on
    """
    # This set will store all connected clients
    connected_clients = set()

    async def handle_client(websocket, path):
        # When a client connects, we add it to the set
        connected_clients.add(websocket)
    
        try:
            # Main loop for each connection
            while True:
                message = json.dumps({
                    "type": "targetInfo",
                    "code": 200,
                    "data": TARGET_INFO_QUEUE.get()})
                
                # The main logic of the server:
                # send the message to the client
                print(str(message))
                await websocket.send(message)
                # Wait for 1 second before sending the next message
                await asyncio.sleep(1)
        except websockets.exceptions.ConnectionClosed:
            # If the client disconnects, we remove it from the set
            connected_clients.remove(websocket)

    start_server = websockets.serve(handle_client, 'localhost', PORT)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
