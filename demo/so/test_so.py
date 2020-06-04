#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2020/5/1
__author__ = 'douzy'

from ctypes import cdll

cur = cdll.LoadLibrary('./libMyGame.so')

a = cur.getDataFromFile('./1.png')

print(a)
