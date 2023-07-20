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
    "name": "default",
    "cameraSettings": {
        "cameraDevice": 0,
        "cameraExposure": 1,
        "cameraBrightness": 1,
        "cameraAutoExposure": True,
        "cameraRedGain": 3,
        "cameraBlueGain": 4,
        "inputImageRotationMode": 0
    },

    "pipelineSettings": {
        "model": "default",
        "minimumConfidence": "0.8",

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
    "name": "defaultPipelineConfig",
    "cameraSettings": {
        "cameraDevice": 0,
        "cameraExposure": 1,
        "cameraBrightness": 1,
        "cameraAutoExposure": True,
        "cameraRedGain": 3,
        "cameraBlueGain": 4,
        "inputImageRotationMode": 0
    },

    "pipelineSettings": {
        "model": "model1",
        "minimumConfidence": "0.8",

        "targetingOffsets": {
            "yaw": 0,
            "pitch": 0
        }
    }
}

defaults.insert_one(defaultPipelineConfig)
print("Imported default pipeline config")