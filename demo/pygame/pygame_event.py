#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

"""
pygame用于处理事件的模块
pygame.event.get() 一次从队列中获取当前的所有事件，通过遍历的方式处理全部事件
pygame.event.poll() 一次从队列中获取一个事件，如果队列中没有待处理事件，就返回一个“空”事件
"""

import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()


def deal_get_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("pygame.QUIT")
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pressed()
            print(pressed)
            pos = pygame.mouse.get_pos()
            print(pos)


def deal_poll_event():
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        print("pygame.QUIT")
        sys.exit()

    if event.type == pygame.MOUSEMOTION:
        pos = pygame.mouse.get_pos()
        print(pos)


# 为了让窗口一直存在下去，这里加个无限循环来保持程序一直运行
while True:
    clock.tick(60)
    # deal_poll_event()
    deal_get_event()
