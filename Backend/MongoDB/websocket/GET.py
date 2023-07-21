import pymongo
import json
import websocket.status as status
from websocket.constants import *

# -----------------------------------------------------------------------------------------------------------------------------------------

# cameraSettings
def getCameraDevice(data: json):
    pipelineName = data["pipelineName"]
    return pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.device': 1, '_id': 0})["cameraSettings"]

def getCameraExposure(data: json):
    pipelineName = data["pipelineName"]
    return pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.exposure': 1})

def getCameraBrightness(data: json):
    pipelineName = data["pipelineName"]
    return pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.brightness': 1})

def getCameraAutoExposure(data: json):
    pipelineName = data["pipelineName"]
    return pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.autoExposure': 1})

def getInputImageRotationMode(data: json):
    pipelineName = data["pipelineName"]
    return pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.inputImageRotationMode': 1})

# -----------------------------------------------------------------------------------------------------------------------------------------

# pipelineSettings
def getModel(data: json):
    pipelineName = data["pipelineName"]
    return pipelines.find_one({"pipelineName": pipelineName}, {'model': 1})

def getMinimumConfidence(data: json):
    pipelineName = data["pipelineName"]
    return pipelines.find_one({"pipelineName": pipelineName}, {'minimumConfidence': 1})

# -----------------------------------------------------------------------------------------------------------------------------------------

# targetingOffsets
def getYaw(data: json):
    pipelineName = data["pipelineName"]
    return pipelines.find_one({"pipelineName": pipelineName}, {'yaw': 1})

def getPitch(data: json):
    pipelineName = data.pipelineName
    return pipelines.find_one({"pipelineName": pipelineName}, {'pitch': 1})

# -----------------------------------------------------------------------------------------------------------------------------------------
