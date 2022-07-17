import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:<password>@cluster0.lsd5b.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

results = collection.find({})

for x in results: 
    print(x)