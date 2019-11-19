#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

"""
pygame用于创建窗口的模块
需要了解的前置知识：屏幕的坐标系，屏幕左上角为坐标原点(0, 0)，向右横向为 X轴，向下纵向为 Y轴；
游戏窗口也是同理，游戏窗口的左上角为坐标原点(0, 0)，向右横向为 X轴，向下纵向为 Y轴；
"""

import os
import sys
import pygame

"""
调整游戏窗口在屏幕上的位置
pygame没有提供接口设置窗口在屏幕上的位置的API
由于pygame的窗口位置依赖于环境变量：SDL_VIDEO_WINDOW_POS，
所以可以通过修改环境变量的方式来设置窗口位置
"""
os.environ["SDL_VIDEO_WINDOW_POS"] = "10,100"

# 初始化整个游戏模块，必须要做，不然pygame的模块都无法使用
pygame.init()

# 设置窗口左上角的小图标
icon = pygame.image.load("./resource/ico/ico.png")
pygame.display.set_icon(icon)

# 设置窗口的标题
pygame.display.set_caption("我是窗口标题")

# 初始化得到一个准备显示的特定大小的窗口
screen_size = (720, 480)
screen = pygame.display.set_mode(screen_size)
# screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN) # 全屏模式
# screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)  # 窗口大小可调整

# 加载一个图片
backgroud = pygame.image.load("./resource/screen/screen.png")

# 将图片画到窗口的特定位置上
backgroud_pos = (0, 0)

tick = pygame.time.Clock()
while True:
    tick.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(backgroud, backgroud_pos)

    # 将屏幕更新为最新的状态
    pygame.display.update()
