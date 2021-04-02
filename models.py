from flask_ReadingList_app import db, login_manager, create_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    readinglist = db.relationship('Readinglist', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Readinglist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listname = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    books = db.relationship('Booklist', backref='book', lazy=True)

    def __repr__(self):
        return f"ReadingList('{self.listname}')"

class Booklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(100), nullable=False)
    readinglist_id = db.Column(db.Integer, db.ForeignKey('readinglist.id'), nullable=False)

    def __repr__(self):
        return f"BookList('{self.bookname}')"
