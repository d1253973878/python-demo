#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time 2020/7/10
__author__ = 'douzy'

import matplotlib.pyplot as plt

import numpy as np

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

n_angles = 36

n_radii = 8

radii = np.linspace(0.125, 1.0, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)

angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

x = np.append(0, (radii * np.cos(angles)).flatten())

y = np.append(0, (radii * np.sin(angles)).flatten())

z = np.sin(-x * y)

ax.plot_trisurf(x, y, z, cmap=cm.jet, lw=0.2)

plt.show()
