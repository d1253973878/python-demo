#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

""" 将图片转换为字符串，并还原
    用到图片 img/back.png
"""

import base64

# 用二进制的方式读取图片文件并通过base64编码后转成字符串
img_str = None
with open('img/back.png', 'rb') as f:
    img_str = base64.b64encode(f.read())
    print(img_str)

# 将图片转换成的字符串通过base64解码后用二进制的方式写入图片文件
file_str = open('img/dest/back.png', 'wb')
file_str.write(base64.b64decode(img_str))
file_str.close()
