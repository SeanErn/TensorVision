# Handle errors
import json

def failedParseRequest():
    return json.dumps({
    "type": "error",
    "code": "400",
    "data": {
            "message": "Invalid JSON"
        }
    })

def failedParseType():
    return json.dumps({
    "type": "error",
    "code": "404",
    "data": {
            "message": "Invalid type"
        }
    })

def pipelineConfigNotFound():
    return json.dumps({
    "type": "error",
    "code": "404",
    "data": {
            "message": "Pipeline config not found"
        }
    })

def ok():
    return json.dumps({
    "type": "ok",
    "code": "200",
    "data": {
            "message": "OK"
        }
    })

