from flask import Flask
from app.controllers import posts_controller

def posts_routes(app: Flask):

    @app.get("/posts")
    def read_all_posts():
        return posts_controller.get_all_posts()
    
    @app.get("/posts/<int:id>")
    def read_specific_post(id: int):
        return posts_controller.get_specific_post(id)
    
    @app.post("/posts")
    def create_new_post():
        return posts_controller.create_new_post()
    
    @app.patch("/posts/<int:id>")
    def to_update_post(id: int):
        return posts_controller.updated_post(id)

    @app.delete("/posts/<int:id>")
    def delete_post(id: int):
        return posts_controller.delete_post(id)