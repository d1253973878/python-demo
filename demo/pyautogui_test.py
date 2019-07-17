#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

""" 使用模块pyautogui实现鼠标和键盘操作，找图找色
    图片img/screen.png是我当时的桌面。大家可以根据自己的桌面来更换img目录下的1.png、2.png、3.png之后再测试
"""

import time
import pyautogui as pag


# 执行测试任务
def getJob():
    try:
        # 在当前屏幕中找到图片 1.png，并返回该图片在当前屏幕的位置，返回的是 左-上-宽-高
        pos = pag.locateOnScreen('img/1.png')
        print(pos)

        # 根据pos找到位置的中心点
        x, y = pag.center(pos)
        print(x, y)
    except Exception as e:
        # 如果在当前屏幕中没有找到如片 1.png，就会抛出一个异常
        print(e)

    # locateCenterOnScreen等同于locateOnScreen 和 center的组合
    try:
        # 在当前屏幕中找到图片 1.png，并返回该图片在当前屏幕的位置，返回的x, y是所在位置的中心点的坐标
        x, y = pag.locateCenterOnScreen('img/1.png')
        print(x, y)

        # 鼠标左键点击一下该坐标点
        pag.click(x, y)
    except Exception as e:
        # 如果在当前屏幕中没有找到如片 1.png，就会抛出一个异常
        print(e)

    # 例行休息
    time.sleep(2)

    # 找到当前屏幕中图片 3.png 出现的所有位置
    try:
        pos = pag.locateAllOnScreen('img/3.png')
        print(pos)

        pos_list = list(pos)
        print(pos_list)

        # 遍历结果集合，并去中间坐标
        for p in pos_list:
            x, y = pag.center(p)
            print(x, y)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    getJob()
