import cv2
#import base64
#import numpy as np

from flask import Flask
from flask import render_template

from flask_socketio import SocketIO
from flask_socketio import emit

from utils.img_preprocess import Img
from utils.predict import Predict

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


class App():
    
    def __init__(self):
        pass

    @app.route('/')
    def index():
        return render_template('index.html')
    
    '''
    @socketio.on('login', namespace = '/test')
    def handle_message(login, password):
        print(login, password)
    '''

    @socketio.on('input', namespace = '/test')
    def handle_message(image_b64, login, password):
        img = Img().decode_img(image_b64)

        print('login: {}'.format(login))
        print('password: {}'.format(password))
        
        
        pred = Predict('/home/nat/Documents/model/bin_face.h5', img).predict()
        
        if (pred):
            emit('responce', ('Вы успешно зарегистрированы!', 1))
        else:
            emit('responce', ('Биометрические данные некорректны!', 0))
        
         

if __name__ == '__main__':
    App().socketio.run(debug = True)
    #socketio.run(debug = True)
    #app.run(debug = True)
