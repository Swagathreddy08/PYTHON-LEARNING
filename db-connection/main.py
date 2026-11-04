from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
app=FastAPI()
username=quote_plus("swagathreddy08")
password=quote_plus("Swag@2004")
print(username)
uri = f"mongodb+srv://{username}:{password}@cluster0.ovw9rpo.mongodb.net/"
print(uri)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
