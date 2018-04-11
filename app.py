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

    

if __name__ == '__main__':
    App().socketio.run(debug = True)
    #socketio.run(debug = True)
    #app.run(debug = True)
