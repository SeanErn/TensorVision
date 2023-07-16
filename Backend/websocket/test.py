import os
from glob import glob

def getAllModelNames():
    """
    Gets all the folders in a directory

    Args:
        directory (str): The directory to search for folders.

    Returns:
        A list of file names for all the folders
    """
    subfolders = [ f.name for f in os.scandir("UserData/Models/") if f.is_dir() ]
    return subfolders
