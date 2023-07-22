import pymongo
import json
import websocket.status as status
from websocket.constants import *

# -----------------------------------------------------------------------------------------------------------------------------------------

# cameraSettings
def getCameraDevice(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.device': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)
    

def getCameraExposure(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.exposure': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)

def getCameraBrightness(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.brightness': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)

def getCameraAutoExposure(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.autoExposure': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)

def getInputImageRotationMode(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.inputImageRotationMode': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)

# -----------------------------------------------------------------------------------------------------------------------------------------

# pipelineSettings
def getModel(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'pipelineSettings.model': 1, '_id': 0})["pipelineSettings"]
    return status.ok_send_data(dataFormatted)

def getMinimumConfidence(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'pipelineSettings.minimumConfidence': 1, '_id': 0})["pipelineSettings"]
    return status.ok_send_data(dataFormatted)

# -----------------------------------------------------------------------------------------------------------------------------------------

# pipelineSettings.targetingOffsets
def getYaw(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'pipelineSettings.targetingOffsets.yaw': 1, '_id': 0})["pipelineSettings"]["targetingOffsets"]
    return status.ok_send_data(dataFormatted)

def getPitch(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'pipelineSettings.targetingOffsets.pitch': 1, '_id': 0})["pipelineSettings"]["targetingOffsets"]
    return status.ok_send_data(dataFormatted)

def getAll(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'_id': 0})
    return status.ok_send_data(dataFormatted)

# -----------------------------------------------------------------------------------------------------------------------------------------
