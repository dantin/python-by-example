# -*- coding: utf-8 -*-

import numpy as np


if __name__ == '__main__':
    print('# 1d array')
    a = np.arange(6)                   # 1d array
    print(a)

    print('# 2d array')
    b = np.arange(12).reshape(4, 3)    # 2d array
    print(b)

    print('# 3d array')
    c = np.arange(24).reshape(2, 3, 4) # 3d array
    print(c)

    print('# For large array, NumPy automatically skips the central part of the array and only prints the corners')
    print('LARGE 1D array')
    la = np.arange(10000)
    print(la)

    print('LARGE 2D array')
    lb = np.arange(10000).reshape(100, 100)
    print(lb)

    print('# disable default behaviour and print entire array')
    np.set_printoptions(threshold=np.nan)
    print(la)
