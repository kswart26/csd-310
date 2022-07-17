import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:<password>@cluster0.lsd5b.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

post1 = {"_id": 1007, "First Name": "Fred", "Last Name": "Hyde"}
post2 = {"_id": 1008, "First Name": "Minato", "Last Name": "Namikaze"}
post3 = {"_id": 1009, "First Name": "Jeff", "Last Name": "Teague"}

#collection.insert_one(post1)

collection.insert_many([post1, post2, post3])