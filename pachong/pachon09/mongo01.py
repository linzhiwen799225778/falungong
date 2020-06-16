import pymongo
#创建数据库连接对象
conn=pymongo.MongoClient('mongodb://127.0.0.1:27017')
#选择数据库集合
mydb=conn['lin']
myset=mydb['like']