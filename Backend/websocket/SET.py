# Functions for setting data on the backend about pipelines
import glob
import os
import json
import constants as const
import websocket.GET as wsGET

# Set the current pipeline in globalConfig.json
def setCurrentPipelineName(pipeline_name):
    """
    Sets the current pipeline in globalConfig.json
    (Ex: "currentPipeline": "pipeline1")
    pipeline1.json is the current pipeline
    Args:
        pipeline_name (str): The name of the pipeline file (minus .json) to set as the current pipeline.
    """
    with open(const.GLOBAL_CONFIG_FILE, "r") as global_config_file:
        global_config = json.load(global_config_file)
        global_config["currentPipeline"] = pipeline_name
    with open(const.GLOBAL_CONFIG_FILE, "w") as global_config_file:
        json.dump(global_config, global_config_file, indent=4)

def setCurrentPipelineMinConfidence(confidence_value):
    """
    Sets the current pipeline's minimum confidence level for the model selected.

    Args:
        confidence_value (float): The minimum confidence for it to be counted as a detection
    """
    