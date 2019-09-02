from pymongo import MongoClient

client = MongoClient("mongodb://admin:123456@node01:27017/")
db = client.get_database("blog")
print(db)
collection = client['blog']['artic']
# 插入一条数据
ret = collection.insert({"name": "沾上乾"})
print(type(ret))
print("插入结果" + str(ret))
print(client)
