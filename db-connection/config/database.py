from pymango import MongoClient
from urllib.parse import quote_plus

username=quote_plus("swagathreddy08")
password=quote_plus("Swag@2004")
client = f"mongodb+srv://{username}:{password}@cluster0.ovw9rpo.mongodb.net/"