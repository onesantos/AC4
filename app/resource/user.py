from flask import Flask, request, jsonify
from app.model.tables import User, db
from app.model.serializer import SerialUser
from app.controller.user import get_user_by_username
from app.controller.user import create_user


def init_app(app: Flask):
    serial_user = SerialUser()

    @app.route("/user/<username>", methods=["GET"])
    def get_users(username):
        return get_user_by_username(username=username)

    @app.route("/user", methods=["POST"])
    def create_users():
        data = request.json
        if not data:
            return {"message": "Ops, error user not missing."}, 400
        return create_user(data=data)

    @app.route("/user/<username>", methods=["PUT"])
    def update_user(username):
        user = db.session.query(User).filter_by(username=username).first()
        if not user:
            return {"message": "user not exists."}, 400
        data = request.json
        if not data:
            return {"message": "Ops, error data not missing."}, 400
        db.session.query(User).filter_by(username=username).update(data)
        db.session.commit()
        return serial_user.dump(user)

    @app.route("/user/<username>", methods=["DELETE"])
    def delete_user(username):
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        return {"message": "user deleted."}