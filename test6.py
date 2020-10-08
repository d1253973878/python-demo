#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2020/10/7
__author__ = 'douzy'

"""
切分并缩放英雄资源图片
"""

import os
from PIL import Image

name_list_l = ["attack_down_1", "attack_down_2", "attack_down_3", "attack_down_4", "attack_up_1", "attack_up_2",
               "attack_up_3", "attack_up_4", "attack_left_1", "attack_left_2", "attack_left_3", "attack_left_4"]

name_list_r = ["move_down_1", "move_down_2", "move_up_1", "move_up_2", "move_left_1", "move_left_2", "stand_down_1",
               "stand_up_1", "stand_left_1", "weak_down_1", "weak_down_2", "block_down_1", "block_up_1", "block_left_1",
               "beaten_down_1", "beaten_up_1", "beaten_left_1"]


# 切分图片
def cut_image(image_in):
    box_list1 = []
    for i in range(12):
        box = (0, i * 120, 120, (i + 1) * 120)
        box_list1.append(box)

    image_list1 = [image_in.crop(box) for box in box_list1]

    box_list2 = []
    for i in range(16):
        box = (120, i * 90, 210, (i + 1) * 90)
        box_list2.append(box)

    image_list2 = [image_in.crop(box) for box in box_list2]

    return image_list1, image_list2


# 缩放图片
def scal_image(image_in, sign):
    if sign == "L":
        return image_in.resize((96, 96))
    else:
        return image_in.resize((72, 72))


# 保存图片
def save_images(image_list_in, sign, num):
    result_path = "test6/" + num
    if not os.path.exists(result_path):
        os.mkdir(result_path)

    if sign == "L":
        name_list = name_list_l
    else:
        name_list = name_list_r

    index = 0
    for img in image_list_in:
        img = scal_image(img, sign)

        name = name_list[index]
        img.save("%s/%s_%s%s" % (result_path, num, name, '.png'), 'PNG')
        index += 1


if __name__ == '__main__':
    file_path = "image/hero1/甘宁.png"
    hero_num = "h1"

    image = Image.open(file_path)
    image_list_l, image_list_r = cut_image(image)
    save_images(image_list_l, "L", hero_num)
    save_images(image_list_r, "R", hero_num)
