from pymongo import MongoClient

client = MongoClient("mongodb://admin:123456@dreamatach.com:27017/")
db = client.get_database("blog")
collection = client['blog']['article']
# ret = collection.update_many({"sex": 0}, {"$set": {"name": "无名氏"}})
ret = collection.update_one({"age": "20"}, {"$set": {"name": "哈哈嘻嘻"}})
print(ret.raw_result)
