# coding:utf-8
import MySQLdb
import MySQLdb.cursors
# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
mysql_info = {"host": '192.168.1.221',
              "port": 3306,
              "user": 'root',
              "passwd": 'root',
              "db": 'test',
              "charset": 'utf8'}

class MysqlUtil():

    '''
     mysql 数据库相关操作
     连接数据库信息：mysql_info
     创建游标：mysql_execute
     查询某个字段对应的字符串：mysql_getstring
     查询一组数据：mysql_getrows
     关闭 mysql 连接：mysql_close
     '''

    def __init__(self):
        self.db_info = mysql_info
        u'''连接池方式'''
        self.conn = MysqlUtil.__getConnect(self.db_info)
    @staticmethod
    def __getConnect(db_info):
        '''静态方法，从连接池中取出连接'''
        try:
            conn = MySQLdb.connect(host=db_info['host'],
                                   port=db_info['port'],
                                   user=db_info['user'],
                                   passwd=db_info['passwd'],
                                   db=db_info['db'],
                                   charset=db_info['charset']
                                   )
            return conn
        except Exception as a:
            print("数据库连接异常：%s"%a)

    def mysql_execute(self, sql):
        '''执行 sql 语句'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            self.conn.rollback() # sql 执行异常后回滚
            print("执行 SQL 语句出现异常：%s"%a)
        else:
            cur.close()
            self.conn.commit() # sql 无异常时提交

    def mysql_getrows(self, sql):
        ''' 返回查询结果'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            print("执行 SQL 语句出现异常：%s"%a)
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    def mysql_getdict(self, sql):
        '''返回字典查询结果'''
        cur = self.conn.cursor(cursorclass= MySQLdb.cursors.DictCursor)
        try:
            cur.execute(sql)
        except Exception as a:
            print("执行 SQL 语句出现异常：%s"%a)
        else:
            rows = list(cur.fetchall())
            cur.close()
            return rows


    def mysql_getstring(self, sql):
        '''查询某个字段的对应值'''
        rows = self.mysql_getrows(sql)
        if rows != None:
            for row in rows:
                for i in row:
                    return i

    def mysql_close(self):
        ''' 关闭 close mysql'''
        try:
            self.conn.close()
        except Exception as a:
            print("数据库关闭时异常：%s"%a)
            # MySQLdb.connect() 建立数据库连接
            # cur = conn.cursor() #通过获取到的数据库连接 conn 下的 cursor()方法来创建游标。
            # cur.execute() #过游标 cur 操作 execute()方法可以写入纯 sql 语句。通过 execute()方法中写如 sql 语句来对数据进行操作。
            # cur.close() # cur.close() 关闭游标
            # conn.commit() # conn.commit()方法在提交事物，在向数据库插入(或update)一条数据时必须要有这个方法，否则数据不会被真正的插入。
            # conn.rollback() # 发生错误时候回滚
            # conn.close() # Conn.close()关闭数据库连接

if __name__ == "__main__":
    mysql = MysqlUtil()
    # sql = "SELECT * FROM qr_pool WHERE id = '3' and '5'"
    sql = "select * FROM test_data"
    mysql.mysql_execute(sql)
    # print (mysql.mysql_getrows(sql))
    print(mysql.mysql_getdict(sql))
    # print (mysql.mysql_getstring(sql))
    # mysql.mysql_close()