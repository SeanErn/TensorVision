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
    # rename copied pipeline to pipelineName
    # switch current pipeline in global config
    
# -----------------------------------------------------------------------------------------------------------------------------------------

# createNewModel
def createNewModel(data: json):
    modelName = data["modelName"]
    # THINGS TO DO
    # create new collection in files db named to model nickname
    # encode and upload detect.tflite and label.pbtxt to collection