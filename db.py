import uuid

from flask import Flask

#from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app import app

#app =  Flask(__name__)
#socket_app = SocketIO(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password@localhost/users_info'
db = SQLAlchemy(app)


class Info(db.Model):
    __tablename__ = 'info'
    
    id = db.Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4)
    login = db.Column(db.Text, nullable = False)
    password = db.Column(db.Text, nullable = False)
    img = db.Column(db.Text, nullable = False)

    
    def __init__(self, login, password, img):
        self.login = login
        self.password = generate_password_hash(password)
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

        return user_login

    def add_user(self, login, password, img):
        new_user = Info(login, password, img)
        db.session.add(new_user)
        db.session.commit()

    def check_user(self, login, password):
        user = Info.query.filter_by(login = login).first()

        if (user): 
            print('login: {}'.format(user.login))
            print('password: {}'.format(user.password))
            print('check_password: {}'.format(check_password_hash(user.password, password)))
            
            return check_password_hash(user.password, password), user.img

        else:
            return False, None
