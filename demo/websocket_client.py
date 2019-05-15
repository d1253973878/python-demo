#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

""" 运用websocket_client模块实现WebSocket服务端
    pip install websocket_client
"""

import websocket


# 最简单的单次连接发送接收消息
def single_connect():
    ws = None
    try:
        ws = websocket.create_connection("ws://localhost:8080/test/ws/bitcoinServer")
        print("Sending 'Hello, World'...")
        ws.send("Hello, World")
        print("Sent")
        print("Receiving...")

        # 该方法会阻塞，一直等到接收到消息为止
        result = ws.recv()
        print("Received '%s'" % result)
    except Exception as e:
        print(e)
    finally:
        if ws:
            ws.close()


def forever_connect():
    def on_open(ws):
        ws.send("test123")

    def on_message(ws, message):
        print(message)

    def on_error(ws, error):
        print(error)

    def on_close(ws):
        print("### closed ###")

    websocket_client = websocket.WebSocketApp("ws://localhost:8000",
                                              on_open=on_open,
                                              on_message=on_message,
                                              on_error=on_error,
                                              on_close=on_close)
    websocket_client.run_forever()


if __name__ == "__main__":
    # single_connect()
    forever_connect()
