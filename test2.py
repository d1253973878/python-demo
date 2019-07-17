#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

import cv2

# picture type 0:gray   1 color
img = cv2.imread("pil.png", 0)
cv2.imshow("image", img)
print(cv2.waitKey(0))
