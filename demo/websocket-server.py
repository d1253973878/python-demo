#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

""" 运用websocket-server模块实现WebSocket服务端
    pip install websocket-server
"""

from websocket_server import WebsocketServer


# 当新的客户端连接时触发
def new_client(client, server):
    print("当新的客户端连接时会提示:%s" % client['id'])
    server.send_message_to_all("Hey all, a new client has joined us")


# 当客户端离开时触发
def client_left(client, server):
    print("客户端%s断开" % client['id'])


# 接收客户端的信息时触发
def message_received(client, server, message):
    print("Client(%d) said: %s" % (client['id'], message))
    server.send_message(client, message)


if __name__ == '__main__':
    websocketServer = WebsocketServer(8000)
    websocketServer.set_fn_new_client(new_client)
    websocketServer.set_fn_client_left(client_left)
    websocketServer.set_fn_message_received(message_received)

    websocketServer.run_forever()
