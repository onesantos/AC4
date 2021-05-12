from flask import abort, request
from app.model.tables import Follow
from app.model.serializer import SerialUser
from app.model.database import db
from app.controller.user import get_user_by_username_dict

serial_user = SerialUser()


def get_followers(username):
    user = get_user_by_username_dict(username=username)
    if not user:
        return abort(404, "Usuário não encontrado.")
    followers = Follow.query.filter_by(user_id=user.id).all()
    if not followers:
        return abort(404, "Nenhum seguidor encontrado.")

    list_follewers = []
    for follow in followers:
        follow_dump = serial_user.dump(follow.follower)
        follow_dump.pop("password")
        follow_dump.pop("email")
        list_follewers.append(follow_dump)
    user_dump = serial_user.dump(user)
    return {**user_dump, "followers": list_follewers}


def create_follow_by_username(username, data):
    user = get_user_by_username_dict(username=username)
    if not user:
        return abort(404, "Usuário não encontrado")
    id = user.id
    for follow in data:
        user = get_user_by_username_dict(username=follow["username"])
        if user and user.username != username:
            follower = Follow(user_id=id, follower_id=user.id)
            db.session.add(follower)
    db.session.commit()
    return {"message": "followers added"}, 201


def unfollow_by_username(username, follow_username):
    user = get_user_by_username_dict(username=username)
    follow = get_user_by_username_dict(username=follow_username)
    if not user or not follow:
        return abort(404, "Usuário ou Seguidor Inválido.")
    data = Follow.query.filter_by(user_id=user["id"], follower_id=follow["id"]).first()
    db.session.delete(data)
    db.session.commit()
    return {"message": "Deixou de seguir."}