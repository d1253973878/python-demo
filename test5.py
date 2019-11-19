#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Mysprite(Sprite):
    def __init__(self):
        super().__init__()
        self.mast_image = pygame.image.load('2233.jpg')  # 读取图像
        self.rect = self.mast_image.get_rect()  # 获取图像矩形参数
        self.frame_rect = self.rect.copy()  # 声明框架参数
        self.rect.x, self.rect.y = 400, 300  # 这里是我实验的动画坐标绘制,如果把这两个参数放在第12行之前,那么就会报错,显示子表面绘制超出了范围 .
        self.frame_rect.width /= 4
        self.frame_rect.height /= 4
        self.frame = 0
        self.last_frame = (self.rect.width // self.frame_rect.width) * (self.rect.height // self.frame_rect.height) - 1
        self.old_frame = 1
        self.last_time = 0

    def update(self):
        self.current_time = pygame.time.get_ticks()
        rate = 100  # 因为这个属性在别的地方不会有调用,所以这里我就写成了方法的局部变量
        if self.current_time >= self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = 0
            self.last_time = self.current_time

        if self.old_frame != self.frame:
            self.frame_rect.x = (self.frame % 4) * self.frame_rect.width
            self.frame_rect.y = (self.frame // 4) * self.frame_rect.height
            self.old_frame = self.frame

        self.image = self.mast_image.subsurface(self.frame_rect)  # 这里就是在生成子表面


pygame.init()
screen = pygame.display.set_mode((800, 600))
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

    group.update()
    group.draw(screen)
    pygame.display.update()
