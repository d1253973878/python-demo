#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

''' 通过PIL库来进行图片处理
    用到的图片 img/pil.png
'''

from PIL import Image

# 读取一个图片，pil_im是一个PIL的图片对象
pil_im = Image.open('img/pil.png')

# 将图片转换为灰度图像后保存起来
pil_im_l = pil_im.convert('L')
pil_im_l.save('img/dest/pil_l.png')

# 将图片进行缩放后保存起来
# 一般来说，thumbnail接收的元组的两个元素的值要相等，因为该方法会通过计算后以得到图片较小的“宽/高”为准，
# pil_im.thumbnail((200, 200))，
# 即分别以元组的第“一/二”个元素作为缩放后图片的“宽/高”，并以原图片的“宽高比例”进行缩放，得到两张图片，最终取较小的那张图片。
# 如果原图片的“宽高比”为“二比一”，大小为200*100。缩放的元组参数为(100, 60),即pil_im.thumbnail((100, 60))，
# 我们可以知道缩放有两种情况：1.新图片100*50；2.新图片120*60；则最终结果是得到一张100*50的新图片

# 以下三种情况分别尝试一下
pil_im.thumbnail((500, 500))
# pil_im.thumbnail((500, 250))
# pil_im.thumbnail((500, 249))
pil_im.save('img/dest/pil_t.png')
