#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2020/10/7
__author__ = 'douzy'

"""
缩放图片
"""

from PIL import Image

file_path = "test9/11.png"
with Image.open(file_path) as image:
    image = image.resize((1440, 1440))
    image.save(file_path)
