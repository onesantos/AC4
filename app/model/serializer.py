from flask import Flask
from flask_marshmallow import Marshmallow
from app.model.tables import User
from app.model.tables import Post
from app.model.tables import Follow

ms = Marshmallow()


def init_app(app: Flask):
    ms.init_app(app=app)


class SerialUser(ms.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class SerialPost(ms.SQLAlchemyAutoSchema):
    class Meta:
        model = Post

class SerialFollow(ms.SQLAlchemyAutoSchema):
    class Meta:
        model = Follow
