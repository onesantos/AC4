from flask import Flask, request, jsonify
from app.model.tables import User, db
from app.model.serializer import SerialUser

serial_user = SerialUser()


def get_user_by_username(username):
    user = (
        User.query.with_entities(User.username, User.id, User.email, User.name)
        .filter_by(username=username)
        .first()
    )
    return serial_user.dump(user)


def get_user_by_username_dict(username) -> User:
    user = (
        User.query.with_entities(User.username, User.id, User.email, User.name)
        .filter_by(username=username)
        .first()
    )
    return user


def create_user(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    db.session.flush()
    return {"message": "user created.", "user": serial_user.dump(user)}, 201