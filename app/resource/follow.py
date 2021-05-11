from flask import Flask, request
from app.controller.follow import get_followers
from app.controller.follow import create_follow_by_id


def init_app(app: Flask):

    @app.route("/user/<followers>", methods=["GET"])
    def get_all_followers(username):
        return get_followers(username=username)

    @app.route("/user/<followers>", methods=["POST"])
    def create_follow(username, user_id):
        data= request.json
        return create_follow_by_id(username=username, user_id=user_id ,data=data)