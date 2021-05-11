from flask import abort, request
from app.model.tables import Post
from app.model.serializer import SerialPost
from app.controller.user import get_user_by_username_dict
from app.model.database import db


serial_post = SerialPost()
serial_post_list = SerialPost(many=True)

def get_posts(username):
    user = get_user_by_username_dict(username=username)
    if not user:
        return abort(404, "Usuário não encontrado")
    post = Post.query.filter_by(user_id=user.id).all()
    return {"posts": serial_post_list.dump(post)}

def get_post(username, post_id):
    user = get_user_by_username_dict(username=username)
    if not user:
        return abort(404, "Usuário não encontrado")
    post = Post.query.filter_by(user_id=user.id, id=post_id).first()
    return serial_post.dump(post)

def create_post_by_username(username, data):
    user = get_user_by_username_dict(username=username)
    if not user:
        return abort(404, "Usuário não encontrado")
    post = Post(user_id=user.id, content=data["content"])
    db.session.add(post)
    db.session.commit()
    db.session.flush()
    return {"message": "post created.", "post": serial_post.dump(post)}, 201


def update_post_by_username(username, post_id, data):
    user = get_user_by_username_dict(username=username)
    if not user:
        return abort(404, "Usuário não encontrado")
    post = Post.query.filter_by(user_id=user.id, id=post_id).first()
    if not post:
        return abort(404, "Publicação não encontrada")
    db.session.query(Post).filter_by(user_id=user.id, id=post_id).update(data)
    db.session.commit()
    return {"messege": "post updated"}



def delete_post_by_username(username, post_id):
    user = get_user_by_username_dict(username=username)
    if not user:
        return abort(404, "Usuário não encontrado")
    post = Post.query.filter_by(user_id=user.id, id=post_id).first()
    if not post:
        return abort(404, "Publicação não encontrada")
    db.session.delete(post)
    db.session.commit()
    return {"message": "post deleted."}



