# -*- coding: utf-8 -*-

import numpy as np


if __name__ == '__main__':
    a = np.floor(10*np.random.random( (2,12) ))
    print('a =')
    print(a)

    # specifying the number of equally shaped arrays to return
    s = np.hsplit(a, 3) # Split 'a' into 3
    print('# specifying the number of equally shaped arrays to return')
    print('np.hsplit(a, 3)')
    print(s)

    # specify the columns after which the division should occur
    print('# specify the columns after which the division should occur')
    s = np.hsplit(a, (3,4))
    print('np.hsplit(a, (3,4))')
    print(s)
