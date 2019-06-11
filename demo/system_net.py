#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

# 获取本机网络相关信息

import socket
import uuid

# 获取主机名
hostname = socket.gethostname()
# 获取IP
ip = socket.gethostbyname(hostname)


# 获取Mac地址
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


ipList = socket.gethostbyname_ex(hostname)
print('IP地址列表', ipList)
print("主机名：", hostname)
print("IP：", ip)
print("Mac地址：", get_mac_address())
