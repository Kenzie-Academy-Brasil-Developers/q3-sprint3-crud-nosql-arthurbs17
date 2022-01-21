from flask import jsonify, request
from http import HTTPStatus
from app.models.post_model import Post
from app.exc.document_not_found import DocumentNotFound
from app.exc.request_error import RequestError

def create_new_post():
    requisition_post = dict(request.get_json())
    try:
        new_post = Post(**requisition_post)
        save_post = new_post.create_post()
        save_post.update({"_id": str(save_post["_id"])})
        return jsonify(save_post), HTTPStatus.OK
    except RequestError as e:
        return jsonify({"message": e.message},{"expected": e.expected_requisition}), e.status_code

def get_all_posts():
    posts_list = list(Post.get_all_posts())
    
    for post in posts_list:
        post.update({"_id": str(post["_id"])})
    
    return jsonify(posts_list), HTTPStatus.OK

def get_specific_post(id: int):
    try:
        specific_post_list = list(Post.get_specific_post(id))
        if len(specific_post_list) == 0:
            raise DocumentNotFound
        specific_post = specific_post_list[0]
        specific_post.update({"_id": str(specific_post["_id"])})
        return jsonify(specific_post), HTTPStatus.OK
    
    except DocumentNotFound as e:
        return {"message": e.message}, e.status_code

def updated_post(id: int):
    new_data = dict(request.get_json())
    try:
        post_for_att = Post.update_post(id, new_data)
        if post_for_att == None:
            return {"message": "Falha na atualização, requisão está vazia!"}
        post_for_att.update({"_id": str(post_for_att["_id"])})
        return jsonify(post_for_att), HTTPStatus.OK
    except RequestError as e:
        return jsonify({"message": e.message}), e.status_code

def delete_post(id: int):
    try:
        post_for_del = Post.delete_post(id)
        if post_for_del == None:
            raise DocumentNotFound
        post_for_del.update({"_id": str(post_for_del["_id"])})
        return jsonify(post_for_del), HTTPStatus.OK
    except DocumentNotFound as e:
        return jsonify({"message": e.message}), e.status_code