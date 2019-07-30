# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/30 16:44
# @Software: PyCharm
import pymysql
import requests
import random


def sql1():
    db = pymysql.connect(host='172.18.18.205', port=3306, user='root', password='root', db='demo',
                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()

    for i in range(6, 17):
        sql = """insert into netmanage.property_system_KPI values(NULL,1,'经开区','2019/7/{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{});""" \
            .format(i, random.uniform(0.90, 0.9899), random.uniform(0.98, 0.9999), random.uniform(0.020, 0.0699),
                    random.uniform(0.0190, 0.03999), random.uniform(0.030, 0.059999),
                    random.uniform(0.90, 0.9999), random.uniform(0.00050, 0.009999), random.uniform(0.020, 0.079999),
                    random.uniform(0.0190, 0.03999), random.uniform(10.0, 50),
                    random.randint(-75, 80), random.uniform(0.96, 0.9999), random.randint(0, 5), random.randint(0, 50),
                    random.uniform(0.90, 0.9999), \
                    random.randint(-180, -80), random.uniform(-100, -70), random.uniform(0.98, 0.9999))

        cursor.execute(sql)

    db.commit()
