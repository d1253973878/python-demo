#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

import sys
import pygame

pygame.init()

backgroud = pygame.image.load("./pil.png")

screen = pygame.display.set_mode((672, 480))
surface2 = pygame.Surface((672, 480)).convert_alpha()

tick = pygame.time.Clock()

pygame.draw.rect(surface2, (0, 0, 192, 50), (100, 100, 48, 48), 0)

screen.blit(surface2, (0, 0))

while True:
    tick.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
