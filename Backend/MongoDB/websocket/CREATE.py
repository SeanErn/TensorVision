import pymongo
import json
import websocket.status as status
from websocket.constants import *

# -----------------------------------------------------------------------------------------------------------------------------------------

# createNewPipeline
def createNewPipeline(data: json):
    pipelineName = data["pipelineName"]
    # THINGS TO DO
    # copy pipeline from defaults to pipelines
    default = defaults.find_one({}, {'_id': 0})
    pipelines.insert_one(default)
    # rename copied pipeline to pipelineName
    pipelines.find_one_and_update({"pipelineName": "defaultPipelineConfig"}, {'$set': {'pipelineName': pipelineName}})
    # switch current pipeline in global config
    globalConfigs.find_one_and_update({}, {'$set': {'currentPipeline': pipelineName}})
    return status.ok()
    
# -----------------------------------------------------------------------------------------------------------------------------------------

# createNewModel
def createNewModel(data: json):
    modelName = data["modelName"]
    # THINGS TO DO
    # create new collection in files db named to model nickname
    # encode and upload detect.tflite and label.pbtxt to collection