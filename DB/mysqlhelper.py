# 使用pymysql包
import pymysql
from django.conf import settings

host = settings.APPSETTING.get('mysql').get('host')
port = settings.APPSETTING.get('mysql').get('port')
user = settings.APPSETTING.get('mysql').get('user')
password = settings.APPSETTING.get('mysql').get('password')
dbname = settings.APPSETTING.get('mysql').get('dbname')


# 执行sql语句
def ExecuteSql(sql):
    # 打开数据库连接
    db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbname, charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    rows = 0
    try:
        # 执行SQL语句
        rows = cursor.execute(sql)
        print(rows)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        rows = -1
        db.rollback()

    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()

    return rows


# 执行sql语句
def ExecuteSql(sql, args):
    # 打开数据库连接
    db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbname, charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    rows = 0
    try:
        # 执行SQL语句 args 是指sql中的 %s部分  mysql会自动格式化
        # cursor.execute('select * from userinfo where username=%s and password=%s',[user,pwd])
        rows = cursor.execute(sql, args)
        print(rows)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        rows = -1
        db.rollback()

    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()

    return rows


# 获取第一条数据  只有value 没有 key
def Get(sql):
    # 打开数据库连接
    db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbname, charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行SQL语句
        v = cursor.execute(sql)
        result = cursor.fetchone()
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return

        # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()

    return result


# 获取第一条数据字典类型有 JSON 数据格式 有key value
def GetDict(sql):
    # 打开数据库连接
    db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbname, charset="utf8")
    # 默认获取的数据是元祖类型，如果想要或者字典类型的数据
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        # 执行SQL语句
        v = cursor.execute(sql)
        result = cursor.fetchone()
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return

        # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()

    return result


# 获取所有数据
def Gets(sql):
    # 打开数据库连接
    db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbname, charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 默认获取的数据是元祖类型，如果想要或者字典类型的数据
    # cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        # 执行SQL语句
        v = cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return

        # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()

    return result


# 获取所有数据 返回JSON格式
def GetsDict(sql):
    # 打开数据库连接
    db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbname, charset="utf8")
    # 使用cursor()方法获取操作游标
    # 默认获取的数据是元祖类型，如果想要或者字典类型的数据
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        # 执行SQL语句
        v = cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return

        # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()

    return result


# 新增数据,主键是自增长的时候使用
def Insert(sql):
    # 打开数据库连接
    db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbname, charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行SQL语句
        rows = cursor.execute(sql)
        newid = cursor.lastrowid
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()

    return newid
