from flask import Flask
from app.routes.posts_routes import posts_routes

def init_app(app: Flask):
    posts_routes(app)