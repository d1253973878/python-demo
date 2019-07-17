#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

''' 通过PIL库来进行图片处理
    用到的图片 img/pil.png
'''

from PIL import Image


# 将图片转换为灰度图像后保存起来
def test_l():
    # 读取一个图片，pil_im是一个PIL的图片对象
    pil_im = Image.open('img/pil.png')

    pil_im_l = pil_im.convert('L')
    pil_im_l.save('img/dest/pil_l.png')


# 将图片进行缩放后保存起来
# 一般来说，thumbnail接收的元组的两个元素的值要相等，因为该方法会通过计算后以得到图片较小的“宽/高”为准，
# pil_im.thumbnail((200, 200))，
# 即分别以元组的第“一/二”个元素作为缩放后图片的“宽/高”，并以原图片的“宽高比例”进行缩放，得到两张图片，最终取较小的那张图片。
# 如果原图片的“宽高比”为“二比一”，大小为200*100。缩放的元组参数为(100, 60),即pil_im.thumbnail((100, 60))，
# 我们可以知道缩放有两种情况：1.新图片100*50；2.新图片120*60；则最终结果是得到一张100*50的新图片
# thumbnail方法直接缩放原图片，方法没有返回值
def test_thumbnail():
    # 读取一个图片，pil_im是一个PIL的图片对象
    pil_im = Image.open('img/pil.png')

    # 以下三种情况分别尝试一下
    pil_im.thumbnail((500, 500))
    # pil_im.thumbnail((500, 250))
    # pil_im.thumbnail((500, 249))
    pil_im.save('img/dest/pil_t.png')


# 调整图片的大小并生成新的图片
# resize方法不对原图片进行修改，而是生成一个新的图片并返回
# resize的宽高可以随意设置，不会受到原图片的“宽高比”影响
def test_resize():
    img = Image.open('img/pil.png')
    print("resize前的尺寸", img.size)
    img2 = img.resize((500, 500))
    img2.save("img/dest/pil_r.png")
    print("resize后的尺寸", img2.size)
    img2.show()


if __name__ == '__main__':
    test_l()
    test_thumbnail()
    test_resize()
