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
        # 获取屏幕大小
        size = pag.size()
        print(size)

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


# 鼠标事件
def test_mouse():
    # 鼠标移动到坐标点(300, 200)
    pag.moveTo(300, 200)  # 绝对移动

    # 例行休息
    time.sleep(1)

    # 鼠标相对当前位置横向移动100，纵向移动200
    pag.moveRel(100, 200)  # 相对移动

    # 例行休息
    time.sleep(1)

    # 鼠标拖拽
    # 为了看到效果，设置过程时间为2s，如果不设置是瞬间执行，看不到效果
    # 绝对移动
    pag.dragTo(100, 200, 2, button='left')  # 左键拖拽
    # 相对当前坐标点移动
    pag.dragRel(100, 100, 2, button='right')  # 右键拖拽

    # 例行休息
    time.sleep(1)

    # 鼠标移动时的渐变效果
    pag.moveTo(100, 100, 2, pag.easeInQuad)  # 开始慢, 最后快
    pag.moveTo(600, 600, 2, pag.easeOutQuad)  # 开始快，最后慢
    pag.moveTo(100, 100, 2, pag.easeInOutQuad)  # 开始和结束都快, 中间过程慢
    pag.moveTo(600, 600, 2, pag.easeInBounce)  # 额，不好描述，自己看效果
    pag.moveTo(100, 100, 2, pag.easeInElastic)  # 额，不好描述，自己看效果

    # 例行休息
    time.sleep(1)

    # 鼠标点击，默认鼠标左键
    pag.click(x=100, y=200)  # 鼠标移动到某坐标并点击
    pag.click(clicks=2)  # 鼠标点击两次
    pag.doubleClick(buttton='right')  # 鼠标右键点击两次

    # 例行休息
    time.sleep(1)

    # 鼠标按下和弹起
    pag.mouseDown()
    pag.mouseUp()

    # 例行休息
    time.sleep(1)

    # 鼠标滚轮
    pag.scroll(500)  # 数字太小会看不出效果


# 键盘事件
def test_key():
    # 模拟输入信息,在当前光标位置输入字符串 Hello world!
    pag.typewrite(message='Hello world!', interval=0.5)

    # 点击ESC
    pag.press('esc')

    # 按住shift键
    pag.keyDown('shift')

    # 放开shift键
    pag.keyUp('shift')
    
    # 模拟组合热键
    pag.hotkey('ctrl', 'c')


if __name__ == "__main__":
    # getJob()
    # test_mouse()
    test_key()
