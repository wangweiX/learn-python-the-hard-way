#!/usr/bin/env python
# coding: UTF-8
import os

import mysql.connector

directory = '/Users/wangwei/Documents/002-Tech/0012-安全/SecLists/Passwords/'
dir_path = os.path.normpath(os.path.abspath(directory))

# 数据集
datas = set()

# 获取子文件及子目录
for name in os.listdir(dir_path):
    # 获取文件路径
    if not name.endswith("wordpress_attacks_july2014.txt"):
        continue
    file_path = os.path.join(dir_path, name)

    # 判断是否是文件
    if not os.path.isfile(file_path):
        continue

    # 按行读取文件
    for line in open(file_path):
        value = line.strip()
        if value == "":
            continue
        # strip 去除左右空格
        datas.add(value)
    print "file name:", name

print "datas size:", len(datas)

# 打开数据库连接
config = {
    'user': 'develop',
    'password': 'BzAZ123R2V20PUJy',
    'host': 'rds03gt58c24i5k3w913public.mysql.rds.aliyuncs.com',
    'database': 'base',
    'raise_on_warnings': True,
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

sql = "INSERT INTO t_cfg_worst_value (`value`) VALUES (%s);"

# 转成列表
datas = list(datas)

# 每次写入 1000 条数据
for i in xrange(0, len(datas), 1000):
    cursor.executemany(
        sql,
        [[value] for value in datas[i:i + 1000]]
    )
    conn.commit()

cursor.close()
conn.close()

# 存储数据进文件
# with io.open('./datas.txt', 'w+') as f:
#     f.writelines(datas)
