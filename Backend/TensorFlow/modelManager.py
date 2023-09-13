import tornado.web
import tornado.ioloop
import tornado.websocket
from pymongo import MongoClient
from gridfs import GridFS

# MongoDB configuration
mongo_uri = 'mongodb://localhost:27017/'
database_name = 'files'
collection_name = 'models'
client = MongoClient(mongo_uri)
db = client[database_name]
fs = GridFS(db, collection=collection_name)

class UploadHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        # 'message' contains the binary data of the file
        # Create a writable stream to MongoDB GridFS
        file_id = fs.put(message, filename='uploaded_file', metadata={
            # You can add any additional metadata about the file here
            # For example, the user who uploaded it, date, description, etc.
        })

        self.write_message({'file_id': str(file_id), 'message': 'File uploaded successfully'})

    def on_close(self):
        print("WebSocket closed")

def make_app():
    return tornado.web.Application([
        (r'/api/upload', UploadHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)  # Replace 8888 with your desired port number
    tornado.ioloop.IOLoop.current().start()
