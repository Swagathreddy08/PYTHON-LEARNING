from pymongo import MongoClient
from urllib.parse import quote_plus

username=quote_plus("swagathreddy08")
password=quote_plus("Swag@2004")
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ovw9rpo.mongodb.net/")
db=client.todo_db
collection_name=db["todo_collection"]