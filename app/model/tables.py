from app.model.database import db
from flask import Flask


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", foreign_keys=user_id)


class Follow(db.Model):
    __tablename__ = "follow"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", foreign_keys=user_id)
    follower = db.relationship("User", foreign_keys=follower_id)


def init_app(app: Flask):
    db.create_all(app=app)