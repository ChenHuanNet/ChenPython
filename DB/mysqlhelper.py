#使用pymysql包
import pymysql

host = ''
port = 3306
user = 'root'
password = 'root'
dbname = ''


# 执行sql语句
def ExecuteSql(sql):
    # 打开数据库连接
    db = pymysql.connect(host=host, port=port, user=user, password=password, database=dbname, charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()



