import pymysql


class DBUtil:
    conn = None
    @classmethod
    def __get_conn(cls):
        if cls.conn is None:
            cls.conn = pymysql.connect(host="192.168.222.131", port=3306, user='root',
                                       password='123456', database='ihrm', charset='utf8')
        return cls.conn

    @classmethod
    def __close_conn(cls):
        if cls.conn is not None:
            cls.conn.close()
            cls.conn = None

    @classmethod
    def select_one(cls, sql):
        cursor = None
        res = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
        except Exception as err:
            print("查询sql错误：", str(err))
        finally:
            cursor.close()
            cls.__close_conn()
            return res

    @classmethod
    def uid_util(cls, sql):
        cursor = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            print("影响的行数：", cls.conn.affected_rows())
            cls.conn.commit()
        except Exception as err:
            print("增删改语句错误：", str(err))
            cls.conn.rollback()
        finally:
            cursor.close()
            cls.__close_conn()

