import pymongo
import json
import websocket.status as status
from websocket.constants import *

# -----------------------------------------------------------------------------------------------------------------------------------------

# createPipeline
def getCameraDevice(data: json):
    pipelineName = data["pipelineName"]
    dataFormatted = pipelines.find_one({"pipelineName": pipelineName}, {'cameraSettings.device': 1, '_id': 0})["cameraSettings"]
    return status.ok_send_data(dataFormatted)
    
# -----------------------------------------------------------------------------------------------------------------------------------------