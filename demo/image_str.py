#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

""" 将图片转换为字符串，并还原
"""

import base64

img_str = None
with open('img/back.png', 'rb') as f:
    img_str = base64.b64encode(f.read())
    print(img_str)

file_str = open('img/dest/back.png', 'wb')
file_str.write(base64.b64decode(img_str))
file_str.close()
