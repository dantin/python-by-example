# -*- coding: utf-8 -*-

import numpy as np


if __name__ == '__main__':
    a = np.arange(12)
    a.shape = 3,4
    print('a =')
    print(a)

    d = a.copy() # a new array object with new data is created
    print('d = a.copy()')
    t = d is a
    print('d is a:', t)
    t = d.base is a # d doesn't share anything with a
    print('d.base is a:', t)
    d[0,0] = 9999
    print('d[0,0] = 9999')
    print('a =')
    print(a)
    print('d =')
    print(d)
