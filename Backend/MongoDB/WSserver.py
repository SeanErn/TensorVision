# TODO:
# ✓ Finish postman api docs
# Finish CREATE functions
# Files DB
# Add notifications from server to client when the data on backend is updated
# Attach to frontend

import tornado.web
import tornado.websocket
import tornado.ioloop
from websocket.GET import *
from websocket.UPDATE import *
from websocket.CREATE import *
import websocket.status as wsStatus

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True # allow all origins
    
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print("[Client → Server] "+ message)
        response = self.handle_request(message)
        self.write_message(response)
        
    def on_close(self):
        print("WebSocket closed")

    def handle_request(self, message):
        try:
            type = json.loads(message)["type"]
            data = json.loads(message)["data"]
        except:
            return wsStatus.failedParseRequest()
        # Use a case statement to handle different requests
        
        #                    __ _       
        #                   / _(_)      
        #    ___ ___  _ __ | |_ _  __ _ 
        #   / __/ _ \| '_ \|  _| |/ _` |
        #  | (_| (_) | | | | | | | (_| |
        #   \___\___/|_| |_|_| |_|\__, |
        #                          __/ |
        #                         |___/ 

        # GET
        # pipelines
        if type == "getCameraDevice":
            return getCameraDevice(data)
        elif type == "getCameraExposure":
            return getCameraExposure(data)
        elif type == "getCameraBrightness":
            return getCameraBrightness(data)
        elif type == "getCameraAutoExposure":
            return getCameraAutoExposure(data)
        elif type == "getInputImageRotationMode":
            return getInputImageRotationMode(data)
        elif type == "getModel":
            return getModel(data)
        elif type == "getMinimumConfidence":
            return getMinimumConfidence(data)
        elif type == "getYaw":
            return getYaw(data)
        elif type == "getPitch":
            return getPitch(data)
        elif type == "getPipelineConfig":
            return getPipelineConfig(data)
        # globalConfigs
        elif type == "getCurrentPipeline":
            return getCurrentPipeline()
        elif type == "getTeamNumber":
            return getTeamNumber()
        elif type == "getHostname":
            return getHostname()
        elif type == "getUseStaticIP":
            return getUseStaticIP()
        elif type == "getStaticIP":
            return getStaticIP()
        elif type == "getGlobalConfig":
            return getGlobalConfig()
        # bulk
        elif type == "getAllPipelineNames":
            return getAllPipelineNames()
        elif type == "getAllPipelineConfigs":
            return getAllPipelineConfigs()
            
        # UPDATE
        # pipelines
        elif type == "updatePipelineName":
            return updatePipelineName(data)
        elif type == "updateCameraDevice":
            return updateCameraDevice(data)
        elif type == "updateCameraExposure":
            return updateCameraExposure(data)
        elif type == "updateCameraBrightness":
            return updateCameraBrightness(data)
        elif type == "updateCameraAutoExposure":
            return updateCameraAutoExposure(data)
        elif type == "updateInputImageRotationMode":
            return updateInputImageRotationMode(data)
        elif type == "updateModel":
            return updateModel(data)
        elif type == "updateMinimumConfidence":
            return updateMinimumConfidence(data)
        elif type == "updateYaw":
            return updateYaw(data)
        elif type == "updatePitch":
            return updatePitch(data)
        # globalConfigs
        elif type == "updateCurrentPipeline":
            return updateCurrentPipeline(data)
        elif type == "updateTeamNumber":
            return updateTeamNumber(data)
        elif type == "updateHostname":
            return updateHostname(data)
        elif type == "updateUseStaticIP":
            return updateUseStaticIP(data)
        elif type == "updateStaticIP":
            return updateStaticIP(data)
        
        # CREATE
        elif type == "createNewPipeline":
            return createNewPipeline(data)
            
        # errors
        else:
            return status.failedParseType()

def make_app():
    return tornado.web.Application([
        (r"/", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5803)
    tornado.ioloop.IOLoop.current().start()
