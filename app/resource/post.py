from flask import Flask, request
from app.controller.post import get_posts
from app.controller.post import create_post_by_username
from app.controller.post import get_post
from app.controller.post import update_post_by_username
from app.controller.post import delete_post_by_username

def init_app(app: Flask):


    @app.route("/post/<username>", methods=["GET"])
    def get_all_posts(username):
        return get_posts(username=username)

    @app.route("/post/<username>/<int:post_id>", methods=["GET"])
    def get_one_post(username, post_id):
       return get_post(username=username, post_id=post_id)

    @app.route("/post/<username>", methods=["POST"])
    def create_post(username):
        data = request.json
        if not data:
            return {"message": "Ops, error user not missing."}, 400
        return create_post_by_username(username=username, data=data)

    @app.route("/post/<username>/<int:post_id>", methods=["PUT"])
    def update_post(username, post_id):
        data= request.json
        return update_post_by_username(username=username, post_id=post_id, data=data)

    @app.route("/post/<username>/<int:post_id>", methods=["DELETE"])
    def delete_post(username, post_id):
        return delete_post_by_username(username=username, post_id=post_id)

