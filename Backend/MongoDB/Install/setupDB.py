import pymongo

localClient = pymongo.MongoClient("mongodb://localhost:27017/")

# Setup config database and collections
configDB = localClient["config"]
print("Setup config database")

# Setup global collection
globalConfigs = configDB["global"]
print("Setup global collection")

# Setup pipelines collection
pipelines = configDB["pipelines"]
print("Setup pipelines collection")

# Setup defaults collection
defaults = configDB["defaults"]
print("Setup defaults collection")

# Import global config from JSON
globalConfig = {
    "currentPipeline": "default",
    "networkConfig": {
        "teamNumber": 0,
        "hostname": "tensorflow",
        "useStaticIP": False,
        "staticIP": ""
    }
}

globalConfigs.insert_one(globalConfig)
print("Imported global config")

# Import 2024 pretrained pipeline from JSON
pretrainedPipeline = {
    "pipelineName": "default",
    "cameraSettings": {
        "device": 0,
        "exposure": 1,
        "brightness": 1,
        "autoExposure": True,
        "inputImageRotationMode": 0
    },

    "pipelineSettings": {
        "model": "default",
        "minimumConfidence": 0.8,

        "targetingOffsets": {
            "yaw": 0,
            "pitch": 0
        }
    }
}

pipelines.insert_one(pretrainedPipeline)
print("Imported pretrained pipeline")

# Import default pipeline example from JSON
defaultPipelineConfig = {
    "pipelineName": "defaultPipelineConfig",
    "cameraSettings": {
        "device": 0,
        "exposure": 1,
        "brightness": 1,
        "autoExposure": True,
        "inputImageRotationMode": 0
    },

    "pipelineSettings": {
        "model": "detect",
        "minimumConfidence": 0.8,

        "targetingOffsets": {
            "yaw": 0,
            "pitch": 0
        }
    }
}

defaults.insert_one(defaultPipelineConfig)
print("Imported default pipeline config")