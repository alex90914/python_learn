from pymongo import MongoClient

client = MongoClient("mongodb://admin:123456@dreamatach.com:27017/")
db = client.get_database("blog")
client.drop_database("blog")
collection = client['blog']['article']
item_list = [{"age": "2{}".format(i), "sex": i % 2, "name": "张三{}".format(i)} for i in range(10)]
item = {"name": "王二麻子", "age": "15"}
ret = collection.insert_one(item)
print(ret.inserted_id)
print("*" * 100)
ret = collection.insert_many(item_list)
for inserted_id in ret.inserted_ids:
    print(inserted_id)
