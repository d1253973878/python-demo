#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2019/10/28
__author__ = 'douzy'

''' 通过OpenCV库来进行图片处理
    用到的图片 img/cv2.png   img/index.png
'''

import cv2
import numpy as np


# 读取并展示图片
def test_open():
    # 第二个参数是读取模式（不传参默认彩色），cv2.IMREAD_COLOR：彩色图；cv2.IMREAD_GRAYSCALE：灰度图。
    # img = cv2.imread("img/cv2.png")
    img = cv2.imread("img/cv2.png", cv2.IMREAD_GRAYSCALE)

    # 展示图片
    cv2.imshow("image", img)

    # 为了让图片窗口一直显示，这里要等待一下
    cv2.waitKey(0)


# 打印图片的基本信息
def test_info():
    img = cv2.imread("img/index.png")
    # 图片的维度
    print(img.shape)
    # 图片的大小
    print(img.size)
    # 图片的数据类型
    print(img.dtype)


# 通过修改图片字节的方式修改图片
def test_modify():
    img = cv2.imread("img/index1.png")
    b_channel, g_channel, r_channel = cv2.split(img)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255

    sp = b_channel.shape
    print(sp)
    height = sp[0]
    width = sp[1]
    for yh in range(height):
        for xw in range(width):
            color_b = b_channel[yh, xw]
            color_g = g_channel[yh, xw]
            color_r = r_channel[yh, xw]
            if color_b == color_g == color_r == 0:
                # 最小值为0
                alpha_channel[yh, xw] = 0

    img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    cv2.imwrite("lena.png", img_BGRA)
    np.arange()


if __name__ == '__main__':
    # test_open()
    test_modify()
