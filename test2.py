#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

import cv2

# picture type 0:gray   1 color
img = cv2.imread("pil.png", 1)
cv2.imshow("image", img)

print(img.shape)
print(img.size)
print(img.dtype)

print(img[507:, 1015:, 0:3])
print(cv2.waitKey(0))
