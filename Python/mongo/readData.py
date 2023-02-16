from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost:27017")
db = mongoClient["mongoDB"]
collection = db["testCollection"]

results = collection.find({"data2": "B2"})

for result in results:
    print(result)
