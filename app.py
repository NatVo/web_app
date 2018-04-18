import cv2
import base64
import numpy as np

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


class App():
    
    def __init__(self):
        pass

    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('my event', namespace = '/test')
    def handle_message(message):
        print(message)

    @socketio.on('my img', namespace = '/test')
    def handle_message(image_b64):
        print(image_b64)
        body = base64.b64decode(image_b64)
        #nparr = np.fromstring(body, np.uint8)
        #img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        

if __name__ == '__main__':
    App().socketio.run(debug = True)
    #socketio.run(debug = True)
    #app.run(debug = True)
