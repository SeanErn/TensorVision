import tornado.web
import tornado.websocket
import tornado.ioloop
import websocket.GET as wsGET
import websocket.UPDATE as wsUPDATE
import json
import websocket.status as wsStatus

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True # allow all origins
    
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print(message)
        response = self.handle_request(message)
        self.write_message(response)
        
    def on_close(self):
        print("WebSocket closed")

    def handle_request(self, message):
        try:
            type = json.loads(message)["type"]
            data = json.loads(message)["data"]
            print(type)
            print(data)
        except:
            return wsStatus.failedParseRequest()
        # Use a case statement to handle different requests
        if type == "updateCameraExposure":
            return wsUPDATE.updateCameraExposure(data)
        elif type == "getCameraDevice":
            return wsGET.getCameraDevice(data)
        else:
            return wsStatus.failedParseType()

def make_app():
    return tornado.web.Application([
        (r"/", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5803)
    tornado.ioloop.IOLoop.current().start()
