from flask import Flask
from app.config import config
from app.model import database
from app.model import serializer
from app.resource import user
from app.resource import post
from app.resource import follow
from app.errors import error


app = Flask(__name__)


def create_app():
    config.init_app(app=app)
    database.init_app(app=app)
    serializer.init_app(app=app)
    user.init_app(app=app)
    post.init_app(app=app)
    follow.init_app(app=app)
    error.init_app(app=app)
    return app