#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'douzy'

# 获取本机系统信息

import platform


def get_system_Platform():
    print('system and bit'.center(40, '-'))
    print(platform.architecture())
    print('\n')

    print('system and deatial'.center(40, '-'))
    print(platform.platform())
    print('\n')

    print('uname'.center(40, '-'))
    print(platform.uname())
    print('\n')

    print('system'.center(40, '-'))
    print(platform.system())
    print('\n')

    print("release".center(40, '-'))
    print(platform.release())
    print('\n')

    print("version".center(40, '-'))
    print(platform.version())
    print('\n')

    print("python Version".center(40, '-'))
    print(platform.python_version())
    print('\n')


get_system_Platform()
