#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2020/10/7
__author__ = 'douzy'

"""
以图片左上角颜色为基准，去掉图片背景色
"""

from PIL import Image


# 以第一个像素为准，相同色改为透明
def transparent_back(img_in):
    img_in = img_in.convert('RGBA')
    L, H = img_in.size
    color_0 = img_in.getpixel((0, 0))
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img_in.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img_in.putpixel(dot, color_1)
    return img_in


if __name__ == '__main__':
    img = Image.open('18-1.png')
    img = transparent_back(img)
    img = img.resize((75, 75))
    img.save('snowfield.png')
