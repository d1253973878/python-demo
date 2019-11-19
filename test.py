#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

import re
import time
import json
import requests
from lxml import etree

rex = "(http.*com).*"


def get_html(url, charset='utf-8'):
    try:
        time.sleep(1)

        matchObj = re.match(rex, url)
        if matchObj:
            referer = matchObj.group(1)

            headers = {"Referer": referer}

            res = requests.get(url, headers=headers)
            code = res.status_code
            if code == 200:
                encoding = requests.utils.get_encodings_from_content(res.text)
                if len(encoding) > 0:
                    charset = encoding[0]
                res.encoding = charset
                return res.text
            else:
                print("status_code: %s; URL=%s" % (code, url))
        else:
            print("Referer_error URL=%s" % url)
    except Exception as e:
        print(u"当前访问网络异常: %s; URL=%s" % (e.__class__, url))

    return ""


def get_all_text(node, text_list):
    if node.text is not None:
        text_list.append(node.text.strip())

    if node.tail is not None:
        text_list.append(node.tail.strip())

    if list(node):
        for child in node:
            get_all_text(child, text_list)


def get_urls(url):
    html = get_html(url)

    if html.strip():
        dom = etree.HTML(html)

        try:
            count = int(dom.xpath("//b[@class='findplotNum']/text()")[0])
        except Exception as e:
            print("################ " + url + " ################")
            count = -1

        if 0 < count <= 2000:
            return url
        elif count > 2000:
            url_list = list()

            a_eles = dom.xpath("//li[@id='houselist_B03_04']//a")
            for a_ele in a_eles:
                a_text = a_ele.text.strip()
                a_url = a_ele.attrib["href"]

                if a_text != "不限":
                    url_list.append(a_url)

            return url_list
        else:
            return "No"
    else:
        return ""


def start():
    all_list = list()

    single_list = list()
    price_list = list()

    with open("second.txt", "r", encoding="utf8") as f:
        for line in f.read().splitlines():
            url = line.strip()
            all_list.append(url)

    for url in all_list:
        result = get_urls(url)
        if result == "No":
            print("=========" + url + "==========")
            continue

        if isinstance(result, list) and len(result) > 0:
            for price_url in result:
                price_list.append(url.replace("/housing/", price_url))
        elif isinstance(result, str) and result.strip():
            single_list.append(url)
        else:
            print("未知错误 URL=%s" % url)

    with open("single.txt", 'w') as f:
        for url in single_list:
            f.write(url)
            f.write('\n')

    with open("price.txt", 'w') as f:
        for url in price_list:
            f.write(url)
            f.write('\n')


def download_url():
    base_url = "http://api.warchess.club/map/list.latest?page=%d&token=77t1SwIMRm4ukIIRGX0I8lZ2G6Ny0jL2"

    for i in range(8):
        url = base_url % (i + 1)
        r = requests.get(url)

        text = json.loads(r.text)
        if text["resultCode"] == 100:
            p_list = text["list"]
            for item in p_list:
                mapName = item["mapName"]
                imageUrl = item["imageUrl"]

                with open('./urls/url4.txt', 'a') as f:
                    try:
                        line = mapName + "@@@@@@@@@" + imageUrl
                        f.write(line)
                        f.write("\n")
                    except Exception as e:
                        print(e)
                        print(imageUrl)
        else:
            print(url)


def download_img():
    p_list = list()
    with open('./urls/url4.txt', 'r') as f:
        for line in f.readlines():
            lineArr = line.split("@@@@@@@@@")
            name = lineArr[0]
            url = lineArr[1]

            hero = dict()
            hero["name"] = name
            hero["url"] = url
            p_list.append(hero)

    print(len(p_list))

    index = 62
    for item in p_list:
        name = item["name"]
        url = item["url"].strip()

        r = requests.get(url)
        with open('./image/map/%s%d.jpg' % (name, index), 'wb') as f:
            f.write(r.content)

        index += 1


def test():
    url = "http://file.warchess.club/game/map/image/208.jpg"
    r = requests.get(url)
    with open('a.jpg', 'wb') as f:
        f.write(r.content)


if __name__ == "__main__":
    # start()
    # download_url()
    download_img()

    # test()
