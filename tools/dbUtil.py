import pymysql


class DBUtil:
    def __init__(self, host, port, user, passport, db):
        self.db = pymysql.connect(host=host, port=port, user=user, passwd=passport, db=db, charset="utf8",
                                 autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def re_connect(self):
        try:
            self.db.ping()
        except:
            self.db()
        return self.cursor

    def get_db(self):
        return self.db

    def close(self):
        # 关闭游标连接
        self.cursor.close()
        # 关闭数据库连接
        self.db.close()