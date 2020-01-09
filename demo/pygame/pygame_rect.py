#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2019/12/10
__author__ = 'douzy'

import sys
import pygame

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
color = (255, 255, 255)

redLine = pygame.image.load("./resource/mark/1-1.bmp")
rect1 = redLine.get_rect()

tick = pygame.time.Clock()
while True:
    tick.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(color)

    for i in range(100):
        screen.blit(redLine, (100 + i, 100))

    # 将屏幕更新为最新的状态
    pygame.display.update()
