#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2020/6/4
__author__ = 'douzy'

import pandas as pd
import numpy as np

cities = {'Beijing': 55000, 'Shanghai': 60000, 'shenzhen': 50000, 'Hangzhou': 20000, 'Guangzhou': 45000, 'Suzhou': None}
apts = pd.Series(cities, name='income')
apts['shenzhen'] = 70000
print('New income of shenzhen:{}'.format(apts['shenzhen']))
less_than_50000 = (apts < 50000)
apts[less_than_50000] = 40000
print(apts)

print(apts / 2)  ###
print(apts ** 1.5)  ###
print(np.log(apts))  ###
apts2 = pd.Series(
    {'Beijing': 10000, 'Shanghai': 8000, 'shenzhen': 6000, 'Tianjin': 40000, 'Guangzhou': 7000, 'Chongqing': 30000})
print(apts2)
print(apts + apts2)  ###
