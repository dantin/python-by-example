# -*- coding: utf-8 -*-

import numpy as np


if __name__ == '__main__':
    B = np.arange(3)
    print('B =')
    print(B)

    print('np.exp(B)')
    print(np.exp(B))

    print('np.sqrt(B)')
    print(np.sqrt(B))

    C = np.array([2., -1., 4.])
    print('C =')
    print(C)

    print('np.add(B, C)')
    print(np.add(B, C))
