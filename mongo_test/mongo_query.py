from pymongo import MongoClient

client = MongoClient("mongodb://admin:123456@dreamatach.com:27017/")
collection = client['blog']['article']
pipeline = [
    {"$match": {"age": {"$gte": "25"}}}
]
ret = collection.aggregate(pipeline)
for x in ret:
    print(x)
