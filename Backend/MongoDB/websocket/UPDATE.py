import pymongo
import json
import websocket.status as status
from websocket.constants import *

# -----------------------------------------------------------------------------------------------------------------------------------------

def updatePipelineName(data: json):
    """Update the pipeline name set in the pipeline config 

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    newPipelineName = data["newPipelineName"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'pipelineName': newPipelineName}})
    return status.ok()

# cameraSettings
def updateCameraDevice(data: json):
    """Update the camera device set in the pipeline config 

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    device = data["device"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.device': device}})
    return status.ok()

def updateCameraExposure(data: json):
    """Update the camera exposure set in the pipeline config 

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    exposure = data["exposure"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.exposure': exposure}})
    return status.ok()

def updateCameraBrightness(data: json):
    """Update the camera brightness set in the pipeline config 

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    brightness = data["brightness"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.brightness': brightness}})
    return status.ok()

def updateCameraAutoExposure(data: json):
    """Update if the camera is using auto exposure set in the pipeline config 

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    autoExposure = data["autoExposure"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.autoExposure': autoExposure}})
    return status.ok()

def updateInputImageRotationMode(data: json):
    """Set the image rotation set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        status: ok (see postman for example)
        
    ```
   -1: 90deg counter clockwise
    0: 0deg
    1: 90deg clockwise
    2: 180deg
    ```
    """
    pipelineName = data["pipelineName"]
    inputImageRotationMode = data["inputImageRotationMode"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'cameraSettings.inputImageRotationMode': inputImageRotationMode}})
    return status.ok()

# -----------------------------------------------------------------------------------------------------------------------------------------

# pipelineSettings
def updateModel(data: json):
    """Update the model set in the pipeline config 

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    model = data["model"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'pipelineSettings.model': model}})
    return status.ok()

def updateMinimumConfidence(data: json):
    """Update the minimum confidence set in the pipeline config 

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    minimumConfidence = data["minimumConfidence"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'pipelineSettings.minimumConfidence': minimumConfidence}})
    return status.ok()

# -----------------------------------------------------------------------------------------------------------------------------------------

# pipelineSettings.targetingOffsets
def updateYaw(data: json):
    """Update the targeting offset for yaw set in the pipeline config 

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    yaw = data["yaw"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'pipelineSettings.targetingOffsets.yaw': yaw}})
    return status.ok()

def updatePitch(data: json):
    """Update the targeting offset for pitch set in the pipeline config 

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    pitch = data["pitch"]
    pipelines.find_one_and_update({"pipelineName": pipelineName}, {'$set': {'pipelineSettings.targetingOffsets.pitch': pitch}})
    return status.ok()

# -----------------------------------------------------------------------------------------------------------------------------------------

# global
def updateCurrentPipeline(data: json):
    """Update the current pipeline in the global config

    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    pipelineName = data["pipelineName"]
    globalConfigs.find_one_and_update({}, {'$set': {'currentPipeline': pipelineName}})
    return status.ok()

# -----------------------------------------------------------------------------------------------------------------------------------------

# networkConfig
def updateTeamNumber(data: json):
    """Update the current team number in the global config
    
    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    teamNumber = data["teamNumber"]
    globalConfigs.find_one_and_update({}, {'$set': {'teamNumber': teamNumber}})
    return status.ok()

def updateHostname(data: json):
    """Update the current team number in the global config
    
    Args:
        data (json): The data from the websocket request
        
    Returns:
        status: ok (see postman for example)
    """
    hostname = data["hostname"]
    globalConfigs.find_one_and_update({}, {'$set': {'hostname': hostname}})
    return status.ok()

def updateUseStaticIP(data: json):
    """Update the current setting for using static ip in the global config

    Args:
        data (json): The data from the websocket request

    Returns:
        status: ok (see postman for example)
    """
    useStaticIP = data["useStaticIP"]
    globalConfigs.find_one_and_update({}, {'$set': {'useStaticIP': useStaticIP}})
    return status.ok()

def updateStaticIP(data: json):
    """Update the current static ip in the global config

    Args:
        data (json): The data from the websocket request

    Returns:
        status: ok (see postman for example)
    """
    staticIP = data["staticIP"]
    globalConfigs.find_one_and_update({}, {'$set': {'staticIP': staticIP}})
    return status.ok()

# -----------------------------------------------------------------------------------------------------------------------------------------