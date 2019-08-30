import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.1.99", "root", "zolbon@2018.1", "project")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
sql = "INSERT INTO emp(name,age)VALUES ('%s', %d),('%s', %d)" % ('站山峰来啦', 15, '王文', 25)
try:
    # 执行sql语句
    rest = cursor.execute(sql)
    # 执行sql语句
    print(cursor.lastrowid)
    print(rest)
    db.commit()
except Exception as e:
    print(e)
    # 发生错误时回滚
    db.rollback()
    # 关闭数据库连接
db.close()
