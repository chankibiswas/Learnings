from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost:27017")
db = mongoClient["mongoDB"]
collection = db["testCollection"]

data1 = {"data1": "A1", "data2": "B1"}
data2 = {"data1": "A2", "data2": "B2"}

collection.insert_many([data1, data2])
# collection.insert_one(data1)