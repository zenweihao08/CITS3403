from datetime import datetime
from flaskpoll import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class MoviePoll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    movie_release_date = db.Column(db.DateTime, nullable=False)
    movie_director = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    movie_rank = db.Column(db.Integer)

class MusicPoll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_title = db.Column(db.String(100), nullable=False)
    music_debut_date = db.Column(db.DateTime, nullable=False)
    singer= db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    music_rank = db.Column(db.Integer)

class GamePoll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(100), nullable=False)
    game_release_date = db.Column(db.DateTime, nullable=False)
    production_company = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    game_rank = db.Column(db.Integer)
    



