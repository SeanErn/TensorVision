import pymongo
import json
import websocket.status as status
from websocket.constants import *

# -----------------------------------------------------------------------------------------------------------------------------------------

# cameraSettings
def updateCameraDevice(data: json):
    pipelineName = data["pipelineName"]
    device = data["device"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.device': device}})
    return status.ok()

def updateCameraExposure(data: json):
    pipelineName = data["pipelineName"]
    exposure = data["exposure"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.exposure': exposure}})
    return status.ok()

def updateCameraBrightness(data: json):
    pipelineName = data["pipelineName"]
    brightness = data["brightness"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.brightness': brightness}})
    return status.ok()

def updateCameraAutoExposure(data: json):
    pipelineName = data["pipelineName"]
    autoExposure = data["autoExposure"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.autoExposure': autoExposure}})
    return status.ok()

def updateInputImageRotationMode(data: json):
    pipelineName = data["pipelineName"]
    inputImageRotationMode = data["inputImageRotationMode"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.inputImageRotationMode': inputImageRotationMode}})
    return status.ok()

# -----------------------------------------------------------------------------------------------------------------------------------------

# pipelineSettings
def updateModel(data: json):
    pipelineName = data["pipelineName"]
    model = data["model"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'pipelineSettings.model': model}})
    return status.ok()

def updateMinimumConfidence(data: json):
    pipelineName = data["pipelineName"]
    minimumConfidence = data["minimumConfidence"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'pipelineSettings.minimumConfidence': minimumConfidence}})
    return status.ok()

# -----------------------------------------------------------------------------------------------------------------------------------------

# pipelineSettings.targetingOffsets
def updateYaw(data: json):
    pipelineName = data["pipelineName"]
    yaw = data["yaw"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'pipelineSettings.targetingOffsets.yaw': yaw}})
    return status.ok()

def updatePitch(data: json):
    pipelineName = data.pipelineName
    pitch = data["pitch"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'pipelineSettings.targetingOffsets.pitch': pitch}})
    return status.ok()

# -----------------------------------------------------------------------------------------------------------------------------------------
