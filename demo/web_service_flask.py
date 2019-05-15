#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

""" 使用flask框架做web服务器端
    参考：https://blog.csdn.net/luanpeng825485697/article/details/80934185
"""

import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/get/str', methods=['GET'])
def get_str():
    # 获取get请求参数
    name = request.args["name"]
    return "Hello %s" % name


@app.route('/post/info', methods=['POST'])
def post_info():
    # 获取post请求参数
    params = request.form.to_dict()
    print(params)
    print(request)

    return "success"


@app.route('/upload/file', methods=['POST'])
def upload_file():
    # 获取上传的文件
    f = request.files['code']

    save_path = os.path.join("code", f.filename)
    print(save_path)
    f.save(save_path)

    return "success"


if __name__ == '__main__':
    app.run(port=8080, debug=True)
