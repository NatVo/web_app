import cv2
#import base64
#import numpy as np

from flask import Flask, render_template
from flask_socketio import SocketIO

from utils.img_preprocess import Img

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


class App():
    
    def __init__(self):
        pass

    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('login', namespace = '/test')
    def handle_message(login, password):
        print(login, password)

    @socketio.on('my img', namespace = '/test')
    def handle_message(image_b64):
        img = Img().decode_img(image_b64)

         

if __name__ == '__main__':
    App().socketio.run(debug = True)
    #socketio.run(debug = True)
    #app.run(debug = True)
