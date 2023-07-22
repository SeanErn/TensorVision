import pymongo
import json
import websocket.status as status
from websocket.constants import *

# -----------------------------------------------------------------------------------------------------------------------------------------

# cameraSettings
def getCameraDevice(data: json):
    """Get the current camera device set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (int): the current camera device (see postman for example)
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.device': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)
    

def getCameraExposure(data: json):
    """Get the current camera exposure set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (int): the current camera exposure (see postman for example)
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.exposure': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)

def getCameraBrightness(data: json):
    """Get the current camera brightness set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (int): the current camera brightness (see postman for example)
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.brightness': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)

def getCameraAutoExposure(data: json):
    """Get if the camera is using auto exposure set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (bool): if the camera uses auto exposure or not (see postman for example)
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.autoExposure': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)

def getInputImageRotationMode(data: json):
    """Get the image rotation set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (int): the image rotation (see postman for example)
        
    ```
   -1: 90deg counter clockwise
    0: 0deg
    1: 90deg clockwise
    2: 180deg
    ```
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.inputImageRotationMode': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)

# -----------------------------------------------------------------------------------------------------------------------------------------

# pipelineSettings
def getModel(data: json):
    """Get the model set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (str): the model name (see postman for example)
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'pipelineSettings.model': 1, '_id': 0})["pipelineSettings"]
    return status.ok_send_data(dataFormatted)

def getMinimumConfidence(data: json):
    """Get the minimum confidence set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (float): the minimum confidence (see postman for example)
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'pipelineSettings.minimumConfidence': 1, '_id': 0})["pipelineSettings"]
    return status.ok_send_data(dataFormatted)

# -----------------------------------------------------------------------------------------------------------------------------------------

# pipelineSettings.targetingOffsets
def getYaw(data: json):
    """Get the yaw offset set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (float): the yaw offset (see postman for example)
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'pipelineSettings.targetingOffsets.yaw': 1, '_id': 0})["pipelineSettings"]["targetingOffsets"]
    return status.ok_send_data(dataFormatted)

def getPitch(data: json):
    """Get the pitch offset set in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (float): the pitch offset (see postman for example)
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'pipelineSettings.targetingOffsets.pitch': 1, '_id': 0})["pipelineSettings"]["targetingOffsets"]
    return status.ok_send_data(dataFormatted)

# -----------------------------------------------------------------------------------------------------------------------------------------

# other
def getPipelineConfig(data: json):
    """Get all the settings in the pipeline config

    Args:
        data (json): The data from the websocket request

    Returns:
        response (object): the settings (see postman for example)
    """
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'_id': 0})
    return status.ok_send_data(dataFormatted)

# -----------------------------------------------------------------------------------------------------------------------------------------

# global
def getCurrentPipeline():
    """Get the current pipeline set in the global config

    Returns:
        response (str): the current pipeline (see postman for example)
    """
    dataFormatted = globalConfigs.find_one({}, {'_id': 0, 'currentPipeline': 1})
    return status.ok_send_data(dataFormatted)

# -----------------------------------------------------------------------------------------------------------------------------------------

# networkConfig
def getTeamNumber():
    """Get the team number set in the global config

    Returns:
        response (int): the team number (see postman for example)
    """
    dataFormatted = globalConfigs.find_one({}, {'_id': 0, 'networkConfig.teamNumber': 1})
    return status.ok_send_data(dataFormatted)

def getHostname():
    """Get the hostname set in the global config

    Returns:
        response (str): the hostname (see postman for example)
    """
    dataFormatted = globalConfigs.find_one({}, {'_id': 0, 'networkConfig.hostname': 1})
    return status.ok_send_data(dataFormatted)

def getUseStaticIP():
    """Get if the static ip is set in the global config

    Returns:
        response (bool): if static ip is enabled (see postman for example)
    """
    dataFormatted = globalConfigs.find_one({}, {'_id': 0, 'networkConfig.useStaticIP': 1})
    return status.ok_send_data(dataFormatted)

def getStaticIP():
    """Get the static ip set in the global config

    Returns:
        response (str): the static ip (see postman for example)
    """
    dataFormatted = globalConfigs.find_one({}, {'_id': 0, 'networkConfig.staticIP': 1})
    return status.ok_send_data(dataFormatted)

# -----------------------------------------------------------------------------------------------------------------------------------------

# other
def getGlobalConfig():
    """Get the global config

    Returns:
        response (object): the global config (see postman for example)
    """
    dataFormatted = globalConfigs.find_one({}, {'_id': 0, 'currentPipeline': 1})
    return status.ok_send_data(dataFormatted)