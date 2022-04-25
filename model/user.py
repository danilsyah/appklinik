from app import app, db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    password = db.Column(db.Text)
    level = db.Column(db.String(100))
    
    def __init__(self, username, password, level):
        self.username = username
        if password != '':
            self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.level = level