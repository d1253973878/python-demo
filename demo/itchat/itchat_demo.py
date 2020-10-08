#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2020/9/8
__author__ = 'douzy'

import time
import itchat


# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == '':
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        # 回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n'  % (msg['Text'])


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)

    # # 获取好友的UserName
    # friends = itchat.get_friends(update=True)[0:]
    #
    # for friend in friends:
    #     print(friend)
    #     NickName = friend["NickName"]
    #     if NickName == "奇杰":
    #         itchat.send_msg("你好", toUserName=friend["UserName"])
    #
    # print(NickName)
    itchat.run()

    # friend = itchat.search_friends(name='祁洁')
    # print(friend)
