import math

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