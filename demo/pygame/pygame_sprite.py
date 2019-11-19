#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

"""
“精灵”的使用
"""

import pygame, sys
from pygame.sprite import Sprite
from pygame.sprite import Group

indexs = [(0, 0), (100, 0), (0, 100), (100, 100), (200, 0), (200, 100), (300, 0), (400, 0), (300, 100), (400, 100)]


class Mysprite(Sprite):
    def __init__(self):
        super().__init__()
        self.mast_image = pygame.image.load('resource/img/skill_20.png')  # 读取图像

        self.image = None
        self.rect = self.mast_image.get_rect()  # 获取图像矩形参数
        self.frame_rect = self.rect.copy()  # 声明框架参数
        self.rect.x, self.rect.y = 400, 300
        self.frame_rect.width = 100
        self.frame_rect.height = 100

        self.frame = 0
        self.old_frame = 1
        self.last_frame = 9
        self.rate = 150
        self.current_time = 0
        self.last_time = 0

    def update(self):
        self.current_time = pygame.time.get_ticks()

        if self.current_time >= self.last_time + self.rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = 0
            self.last_time = self.current_time

        if self.old_frame != self.frame:
            self.frame_rect.x = indexs[self.frame][0]
            self.frame_rect.y = indexs[self.frame][1]
            self.old_frame = self.frame

        self.image = self.mast_image.subsurface(self.frame_rect)  # 这里就是在生成子表面


pygame.init()
screen = pygame.display.set_mode((900, 600))
color = (255, 255, 255)
screen.fill(color)

mysprite = Mysprite()
group = Group()
group.add(mysprite)
tick = pygame.time.Clock()

while True:
    tick.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(color)
    group.update()
    group.draw(screen)
    pygame.display.update()
