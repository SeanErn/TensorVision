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
        response = self.handle_request(message)
        print(message)
        self.write_message(response)

    def on_close(self):
        print("WebSocket closed")

    def handle_request(self, message):
        # Use a case statement to handle different requests
        match message:
            case "getAllModelNames":
                return pipelineGET.getAllModelNamesFormatted()
            case "getAllPipelineData":
                return pipelineGET.getAllPipelineDataFormatted()
            case "getAllPipelineNames":
                return pipelineGET.getAllPipelineNamesFormatted()
            case _ :
                data = {
                    "type": "error",
                    "data": {
                        "code": "404",
                        "message": "Invalid request"
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
