import pymysql
'''
class MysqlUtils():
    # shared by all exampls
    db = pymysql.connect("localhost", "root", "071007", "mydb")
    
    @classmethod
    def get_connection(cls):
        return cls.db
'''
# 连接数据库
db = pymysql.connect(host = "localhost", user = "root", password = "071007", database = "socket_lab")

def realse_db(db):
    db.close()