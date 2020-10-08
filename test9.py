#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2020/10/7
__author__ = 'douzy'

"""
瓦片地图处理 
根据背景图制作前景图
"""

import sys
import math
import numpy as np
from PIL import Image
from xml.dom.minidom import parse
import xml.dom.minidom

type_list = ["river", "snowfield", "steppe", "wood"]

type_map = dict()


def get_lattice(tile_type):
    path = "test9/{}.png".format(tile_type)
    type_image = Image.open(path).convert('L')
    return np.asarray(type_image)


# 根据行列数和tile_id确定当前瓦片在大地图中的位置
def get_position(tile_id):
    y = math.floor(tile_id / columns)
    x = tile_id - (y * columns)

    return x * tilewidth, y * tileheight


def deal_image(image_in, tile_id, tile_type):
    # 现根据瓦片类型获取点阵信息
    if tile_type not in type_map.keys():
        type_map[tile_type] = get_lattice(tile_type)

    data = type_map[tile_type]
    # 确定基准像素点坐标
    dot = get_position(tile_id)
    for i in range(data.shape[1]):
        for j in range(data.shape[0]):
            if data[j][i] == 0:
                new_dot = (dot[0] + i, dot[1] + j)
                color_1 = image_in.getpixel(new_dot)
                color_1 = color_1[:-1] + (0,)
                image_in.putpixel(new_dot, color_1)

    return image_in


def clear_image(image_in, tile_id):
    # 确定基准像素点坐标
    dot = get_position(tile_id)
    for i in range(tilewidth):
        for j in range(tileheight):
            new_dot = (dot[0] + i, dot[1] + j)
            color_1 = image_in.getpixel(new_dot)
            color_1 = color_1[:-1] + (0,)
            image_in.putpixel(new_dot, color_1)

    return image_in


if __name__ == "__main__":
    # 读取背景图片
    image = Image.open('test9/11.png').copy()
    image = image.convert('RGBA')

    # 读取瓦片信息
    DOMTree = xml.dom.minidom.parse("test9/map.tsx")
    collection = DOMTree.documentElement

    # 瓦片宽
    if collection.hasAttribute("tilewidth"):
        global tilewidth
        tilewidth = int(collection.getAttribute("tilewidth"))
    else:
        print("No tilewidth, exit!")
        sys.exit(-1)

    # 瓦片高
    if collection.hasAttribute("tileheight"):
        global tileheight
        tileheight = int(collection.getAttribute("tileheight"))
    else:
        print("No tileheight, exit!")
        sys.exit(-1)

    # 瓦片行数
    if collection.hasAttribute("columns"):
        global columns
        columns = int(collection.getAttribute("columns"))
    else:
        print("No columns, exit!")
        sys.exit(-1)

    # 瓦片总数
    if collection.hasAttribute("tilecount"):
        global tilecount
        tilecount = int(collection.getAttribute("tilecount"))
    else:
        print("No tilecount, exit!")
        sys.exit(-1)

    # 获取所有的瓦片，并遍历处理
    tiles = collection.getElementsByTagName("tile")
    for tile in tiles:
        # 瓦片ID
        if tile.hasAttribute("id"):
            tileId = int(tile.getAttribute("id"))
        else:
            print("No id, exit!")
            sys.exit(-1)

        # 瓦片类型
        if tile.hasAttribute("type"):
            tileType = tile.getAttribute("type")
        else:
            print("No type, exit!")
            sys.exit(-1)

        if tileType in type_list:
            image = deal_image(image, tileId, tileType)
        else:
            image = clear_image(image, tileId)

    image.save("test9/force.png")
