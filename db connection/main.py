from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

app = FastAPI()

username = quote_plus("Swagath08")
password = quote_plus("Swag@2004")

uri = f"mongodb+srv://{username}:{password}@cluster0.ocrvdba.mongodb.net/"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. Successfully connected to MongoDB!")
except Exception as e:
    print("MongoDB connection failed:", e)