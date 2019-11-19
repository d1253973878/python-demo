#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

import os
from PIL import Image

path = "./image/hero1"
dest = "./dest/hero"
for filename in os.listdir(path):
    imgPath = os.path.join(path, filename)

    img = Image.open(imgPath)  # 打开图像

    left2 = 120
    upper2 = 0
    right2 = 210
    lower2 = 90

    (prefix, extension) = os.path.splitext(filename)
    for i in range(16):
        prefix1 = prefix + "-R" + str(i) + ".png"
        destPath = os.path.join(dest, prefix1)
        roi = img.crop((left2, upper2, right2, lower2))
        roi.save(destPath)

        upper2 += 90
        lower2 += 90

    break
