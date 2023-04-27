import glob
import os

def getModels(directory):
    """
    Gets all the files in a directory and removes the .tflite file extension.

    Args:
        directory (str): The directory to search for files.

    Returns:
        A list of file names for all the files in the directory without the .tflite extension.
    """
    tflite_files = glob.glob(f"{directory}/*.tflite")
    files_without_tflite_extension = []
    for tflite_file in tflite_files:
        filename = os.path.basename(tflite_file)
        file_without_extension = os.path.splitext(filename)[0]
        files_without_tflite_extension.append(file_without_extension)
    return files_without_tflite_extension
