from flask import Flask, request
from app.controller.follow import get_followers
from app.controller.follow import create_follow_by_username
from app.controller.follow import unfollow_by_username


def init_app(app: Flask):
    @app.route("/followers/<username>", methods=["GET"])
    def get_all_followers(username):
        return get_followers(username=username)

    @app.route("/followers/<username>", methods=["POST"])
    def create_follow(username):
        data = request.json
        if not data:
            return {
                "message": "Ops, error followers not missing.",
                "example": [{"username": "john"}],
            }, 400
        return create_follow_by_username(username=username, data=data)

    @app.route("/followers/<username>", methods=["DELETE"])
    def delete_follow(username):
        data = request.json
        if not data or "username" not in data:
            return {
                "message": "Ops, error followers not missing.",
                "example": {"username": "john"},
            }, 400
        return unfollow_by_username(username=username, follow_username=data["username"])
