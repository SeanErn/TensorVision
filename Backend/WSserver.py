import tornado.web
import tornado.websocket
import tornado.ioloop
import pipelines.pipelineGET as pipelineGET
import pipelines.pipelineSET as pipelineSET
import json

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
            data = {
                "type": "error",
                "code": "400",
                "data": {
                    "message": "Invalid JSON"
                }
            }
            payload = json.dumps(data)
            return payload
        # Use a case statement to handle different requests
        match type:
            case "getAllModelNames":
                return pipelineGET.getAllModelNamesFormatted()
            case "getAllPipelineData":
                return pipelineGET.getAllPipelineDataFormatted()
            case "getAllPipelineNames":
                return pipelineGET.getAllPipelineNamesFormatted()
            case "getCurrentPipeline":
                return pipelineGET.getCurrentPipelineFormatted()
            case _ :
                data = {
                    "type": "error",
                    "code": "404",
                    "data": {
                        "message": "Invalid type"
                    }
                }
                payload = json.dumps(data)
                return payload

def make_app():
    return tornado.web.Application([
        (r"/", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
