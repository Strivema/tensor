# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/30 19:30
# @Software: PyCharm
import pymysql


def get_conn():
    conn = pymysql.connect(host='172.18.18.205', port=3306, user='root', password='root', db='demo',
                           charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return conn


def insert(sql):
    conn = get_conn()
    cur = conn.cursor()
    res = cur.execute(sql)
    print(res)
    conn.commit()
    cur.close()
    conn.close()


def query(sql):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall();
    print(type(res))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    find = 'select * from temp'
    query(find)
