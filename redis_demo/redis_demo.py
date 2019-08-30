import redis

if __name__ == '__main__':
    host = '118.25.212.23'
    port = 6379
    db = 4
    password = ""
    redis_client = redis.Redis(host=host, port=port, db=db)
    rest = redis_client.get("name")
    print("请求结果:%s" % rest.decode())
