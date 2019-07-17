#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

a = 1
b = None


def fuc():
    a = 2
    # global b
    b = 3
    print(a, b)


fuc()
print(a)
print(b)
