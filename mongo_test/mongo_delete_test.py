from pymongo import MongoClient

client = MongoClient("mongodb://admin:123456@dreamatach.com:27017/")
db = client.get_database("blog")
collection = client['blog']['article']
ret = collection.delete_one({"_id": "5d6e152c1114ea73a872de2a"})
print(ret.raw_result)
