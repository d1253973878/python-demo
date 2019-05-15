#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

""" 运用simple-websocket-server模块实现WebSocket服务端
    pip install simple-websocket-server
"""

from simple_websocket_server import WebSocketServer, WebSocket


class SimpleEcho(WebSocket):
    def handle(self):
        print(self.data)
        self.send_message(self.data)

    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')


server = WebSocketServer('', 8000, SimpleEcho)
server.serve_forever()
