# Functions for setting data on the backend about pipelines
import glob
import os
import json
import constants as const

# Set the current pipeline in globalConfig.json
def setCurrentPipeline(pipeline_name):
    """
    Sets the current pipeline in globalConfig.json

    Args:
        pipeline_name (str): The name of the pipeline to set as the current pipeline.
    """
    with open(const.GLOBAL_CONFIG_FILE, "r") as global_config_file:
        global_config = json.load(global_config_file)
        global_config["currentPipeline"] = pipeline_name
    with open(const.GLOBAL_CONFIG_FILE, "w") as global_config_file:
        json.dump(global_config, global_config_file, indent=4)