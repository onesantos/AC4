from flask import abort, request
from app.model.tables import Follow
from app.model.serializer import SerialFollow
from app.model.database import db
from app.controller.user import get_user_by_username_dict

serial_follow = SerialFollow()
serial_follow_list = SerialFollow(many=True)

def get_followers(username):
    user = get_user_by_username_dict(username=username)
    if not user:
        return abort(404, "Usuário não encontrado")
    follower = Follow.query.filter_by(user_id=user.id).all()
    return {"posts": serial_follow_list.dump(follower)}

def create_follow_by_id(username, user_id, data):
    user = get_user_by_username_dict(username=username)
    if not user:
        return abort(404, "Usuário não encontrado")
    follower = Follow(user_id=user.id)
    db.session.add(follower)
    db.session.commit()
    db.session.flush()
    return {"message": "followed", "follow": serial_follow.dump(follower)}, 201
