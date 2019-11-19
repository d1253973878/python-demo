#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'douzy'

import cv2

img = cv2.imread("pil.png", cv2.IMREAD_COLOR)
b, g, r = cv2.split(img)

merged = cv2.merge([g, b, r])
img[100:200, 100:200] = (0, 0, 0)

cv2.imshow("Blue", b)
# cv2.imshow("Green", 、.3











# cv2.imshow("Red", r)

cv2.imshow("Merged", merged)
cv2.imshow("Merged", img)
cv2.waitKey()
