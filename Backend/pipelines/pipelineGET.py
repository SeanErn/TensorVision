# Functions for getting data from the backend about pipelines
import glob
import os
import json
import constants as const

# Gets all models that will be used for the pipeline
def getAllModelNames():
    """
    Gets all the files in a directory and removes the .tflite file extension.

    Args:
        directory (str): The directory to search for files.

    Returns:
        A list of file names for all the files in the directory without the .tflite extension.
    """
    tflite_files = glob.glob(f"{const.MODELS_DIR}/*.tflite")
    files_without_tflite_extension = []
    for tflite_file in tflite_files:
        filename = os.path.basename(tflite_file)
        file_without_extension = os.path.splitext(filename)[0]
        files_without_tflite_extension.append(file_without_extension)
    return files_without_tflite_extension

# Same as get all models but returns a JSON object
def getAllModelNamesFormatted():
    """
    Gets all the files in a directory and removes the .tflite file extension.

    Returns:
        JSON payload for websocket with the type, code, and models
    """
    return json.dumps({
        "type": "getAllModelNames",
        "code": 200,
        "data": {
            "models": getAllModelNames()
        }
    })


# ------------------- #

# Gets all models that will be used for the pipeline
def getAllPipelineNames():
    """
    Gets all the files in a directory and removes the .tflite file extension.

    Args:
        directory (str): The directory to search for files.

    Returns:
        A list of file names for all the files in the directory without the .tflite extension.
    """
    pipeline_files = glob.glob(f"{const.PIPELINE_CONFIGS_DIR}/*.json")
    files_without_json_extension = []
    for pipeline_file in pipeline_files:
        filename = os.path.basename(pipeline_file)
        file_without_extension = os.path.splitext(filename)[0]
        files_without_json_extension.append(file_without_extension)
    return files_without_json_extension

# Same as get all models but returns a JSON object
def getAllPipelineNamesFormatted():
    """
    Gets all the files in a directory and removes the .tflite file extension.

    Returns:
        JSON payload for websocket with the type, code, and models
    """
    return json.dumps({
        "type": "getAllPipelineNames",
        "code": 200,
        "data": {
            "pipelines": getAllPipelineNames()
        }
    })

# ------------------- #


# Gets all pipelines raw JSON data
def getAllPipelineData():
    """
    Gets all pipelines in the UserData/Pipelines directory
    
    Returns:
        An array of JSON objects of each pipeline
    """
    pipeline_config_files = [x for x in os.listdir(const.PIPELINE_CONFIGS_DIR) if x.endswith(".json")]
    pipeline_config_data = []
    
    # If there are no files, return an empty array
    if len(pipeline_config_files) == 0:
        print("No JSON file found in directory")
        return pipeline_config_data
    else:
        # Otherwise, read each file and append it to the array
        for pipeline_config in pipeline_config_files:
            pipeline_config_path = os.path.join(const.PIPELINE_CONFIGS_DIR, pipeline_config)
            with open(pipeline_config_path, "r") as f:
                pipeline_config_data.append({
                    "pipeline": pipeline_config,
                    "data": json.load(f)
                    })
    return pipeline_config_data

def getAllPipelineDataFormatted():
    """
    Gets all pipelines in the UserData/Pipelines directory

    Returns:
        JSON payload for websocket with the type, code, and pipelines array
    """
    return json.dumps({
        "type": "getAllPipelineData",
        "code": 200,
        "data": {
            "pipelineData": getAllPipelineData()
        }
    })

# ------------------- #

# Gets the current pipeline
def getCurrentPipeline():
    """
    Gets the current pipeline from globalConfig.json

    Returns:
        The current pipeline
    """
    with open(const.GLOBAL_CONFIG_FILE, "r") as global_config_file:
        global_config = json.load(global_config_file)
        return global_config["currentPipeline"]

# Same as get current pipeline but returns a JSON object
def getCurrentPipelineFormatted():
    """
    Gets the current pipeline from globalConfig.json
    
    Returns:
        JSON payload for websocket with the type, code, and current pipeline
    """
    return json.dumps({
        "type": "getCurrentPipeline",
        "code": 200,
        "data": {
            "currentPipeline": getCurrentPipeline()
        }
    })