from flask import Flask

#from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
#socket_app = SocketIO(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password@localhost/users_info'
db = SQLAlchemy(app)


class Info(db.Model):
    __tablename__ = 'info'
    
    id = db.Column(db.Text, primary_key = True, nullable = False)
    login = db.Column(db.Text, nullable = False)
    password = db.Column(db.Text, nullable = False)
    img = db.Column(db.Text, nullable = False)

    
    def __init__(self, login, password, img):
        self.login = login
        self.password = password
        self.img = img
    
    '''
    def __repr__(self):
        return '<Info %r,%r>' % self.user_id, self.user_name
    '''

class DB_interact():

    def __init__(self):
        pass

    def check_login(self, login):
        user_login = Info.query.filter_by(login = login).first()
        print('user_login: {}'.format(user_login))
