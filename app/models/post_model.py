import pymongo
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
mongodb_path = os.environ["MONGODB_PATH"]
client = pymongo.MongoClient(mongodb_path)
db = client["kenzie"]
collection = db["posts"]

class Post:
    def __init__(self, title, author, tags, content) -> None:
        self.title: str = title
        self.author: str = author
        self.tags: list[str] = tags
        self.content: str = content
        self.id = len(list(collection.find())) + 1
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def create_post(self):
        new_post = self.__dict__
        collection.insert_one(new_post)
        return new_post
    
    @staticmethod
    def get_all_posts():
        posts_list = collection.find()
        return posts_list
    
    @staticmethod
    def get_specific_post(id: int):
        specific_post = collection.find({"id": id})
        return specific_post
    
    @staticmethod
    def update_post(id: int, new_data: dict):
        new_data.update({"updated_at": datetime.utcnow()})
        return collection.find_one_and_update({"id": id}, {"$set": new_data})
    
    @staticmethod
    def delete_post(id: int):
        return collection.find_one_and_delete({"id": id})