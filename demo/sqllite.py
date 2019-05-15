#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

""" 使用内置模块sqlite3实现数据库操作
    sqllite的语句和mysql的语句非常相似，绝大多数可以照搬
"""

import sqlite3


# 创建表
def create_table():
    connection = None
    cu = None
    try:
        # 创建数据库连接
        connection = sqlite3.connect("data\\test.db")
        # 获取游标
        cu = connection.cursor()

        # 执行建表语句
        cu.execute('''create table if not exists user_info (
                            id integer primary key autoincrement,
                            username varchar(50),
                            password varchar(50)
                      )''')

        print("创建表成功")
    except Exception as e:
        print(e)
    finally:
        # 关闭游标
        if cu:
            cu.close()

        # 关闭连接
        if connection:
            connection.close()


# 插入信息
def insert_info():
    item = ("username", "123")

    connection = None
    cu = None
    try:
        # 创建数据库连接
        connection = sqlite3.connect("data\\test.db")
        # 获取游标
        cu = connection.cursor()

        # 插入数据需要commit。如果同时插入多条数据，建议先执行多次插入操作，最后执行一次commit
        cu.execute("insert into user_info(username,password) values (?,?)", item)
        # cu.execute("insert into user_info(username,password) values (?,?)", item1)
        # cu.execute("insert into user_info(username,password) values (?,?)", item2)

        # 插入数据后，执行commmit
        connection.commit()

        print("插入了一条数据")
    except Exception as e:
        print(e)
    finally:
        # 关闭游标
        if cu:
            cu.close()

        # 关闭连接
        if connection:
            connection.close()


# 删除信息
def delete_info():
    item = (1,)

    connection = None
    cu = None
    try:
        # 创建数据库连接
        connection = sqlite3.connect("data\\test.db")
        # 获取游标
        cu = connection.cursor()

        # 删除数据需要commit。如果同时删除多条数据，建议先执行多次删除操作，最后执行一次commit
        cu.execute("delete from user_info where id=?", item)
        # cu.execute("delete from user_info where id=?", item1)
        # cu.execute("delete from user_info where id=?", item2)

        # 删除数据后，执行commmit
        connection.commit()

        print("删除了一条数据")
    except Exception as e:
        print(e)
    finally:
        # 关闭游标
        if cu:
            cu.close()

        # 关闭连接
        if connection:
            connection.close()


# 修改数据
def update_info():
    item = ("456", 1)

    connection = None
    cu = None
    try:
        # 创建数据库连接
        connection = sqlite3.connect("data\\test.db")
        # 获取游标
        cu = connection.cursor()

        # 修改数据需要commit。如果同修改除多条数据，建议先执行多次修改操作，最后执行一次commit
        cu.execute("update user_info set password=? where id=?", item)
        # cu.execute("update user_info set password=? where id=?", item1)
        # cu.execute("update user_info set password=? where id=?", item2)

        # 修改数据后，执行commmit
        connection.commit()

        print("修改了一条数据")
    except Exception as e:
        print(e)
    finally:
        # 关闭游标
        if cu:
            cu.close()

        # 关闭连接
        if connection:
            connection.close()


# 查找信息
def select_info():
    item = (1,)
    results = []

    connection = None
    cu = None
    try:
        # 创建数据库连接
        connection = sqlite3.connect("data\\test.db")
        # 获取游标
        cu = connection.cursor()

        # 执行查找语句,fetchall会将全部结果都返回，其他方法请参照官方文档
        results = cu.execute("select * from user_info where id=?", item).fetchall()
    except Exception as e:
        print(e)
    finally:
        # 关闭游标
        if cu:
            cu.close()

        # 关闭连接
        if connection:
            connection.close()

    print(results)


if __name__ == "__main__":
    create_table()

    # insert_info()
    # select_info()

    # update_info()
    # select_info()

    # delete_info()
    # select_info()
