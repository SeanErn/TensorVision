import pymongo

# setup db connection
localClient = pymongo.MongoClient("localhost", 27017)

# client databases
configDB = localClient["config"]
filesDB = localClient["files"]

# client collections
globalConfigs = configDB["global"]
pipelines = configDB["pipelines"]
defaults = configDB["defaults"]

