# Functions for getting data from the backend about pipelines
import glob
import os
import json

# Constants
PIPELINE_CONFIGS_DIR = "../UserData/Config/Pipelines"
MODELS_DIR = "../UserData/Models"

# Gets all models that will be used for the pipeline
def getAllModelNames():
    """
    Gets all the files in a directory and removes the .tflite file extension.

    Args:
        directory (str): The directory to search for files.

    Returns:
        A list of file names for all the files in the directory without the .tflite extension.
    """
    tflite_files = glob.glob(f"{MODELS_DIR}/*.tflite")
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
        "data": {
            "code": "200",
            "models": getAllModelNames()
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
    pipeline_config_files = [x for x in os.listdir(PIPELINE_CONFIGS_DIR) if x.endswith(".json")]
    pipeline_config_data = []
    
    # If there are no files, return an empty array
    if len(pipeline_config_files) == 0:
        print("No JSON file found in directory")
        return pipeline_config_data
    else:
        # Otherwise, read each file and append it to the array
        for pipeline_config in pipeline_config_files:
            pipeline_config_path = os.path.join(PIPELINE_CONFIGS_DIR, pipeline_config)
        with open(pipeline_config_path, "r") as f:
            pipeline_config_data.append(json.load(f))
    return pipeline_config_data

def getAllPipelineDataFormatted():
    """
    Gets all pipelines in the UserData/Pipelines directory

    Returns:
        JSON payload for websocket with the type, code, and pipelines array
    """
    return json.dumps({
        "type": "getAllPipelineData",
        "data": {
            "code": "200",
            "models": getAllPipelineData()
        }
    })

