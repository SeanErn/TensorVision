import tornado.web
import tornado.websocket
import tornado.ioloop
import websocket.GET as wsGET
import websocket.SET as wsSET
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
            print(type)
        except:
            return wsStatus.failedParseRequest()
        # Use a case statement to handle different requests
        match type:
            case "getAllModelNames":
                return wsGET.getAllModelNamesFormatted()
            case "getAllPipelineNames":
                return wsGET.getAllPipelineNamesFormatted()
            case "getCurrentPipelineName":
                return wsGET.getCurrentPipelineNameFormatted()
            case "getCurrentPipelineData":
                return wsGET.getCurrentPipelineDataFormatted()
            case "setCurrentPipelineName":
                try:
                    wsSET.setCurrentPipelineName(json.loads(message)["data"]["pipelineName"])
                except:
                    return wsStatus.failedParseRequest()
                return wsStatus.ok()
            case _ :
                return wsStatus.failedParseType()

def make_app():
    return tornado.web.Application([
        (r"/", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
