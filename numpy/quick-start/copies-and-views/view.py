# -*- coding: utf-8 -*-

import numpy as np


if __name__ == '__main__':
    a = np.arange(12)
    print('a =')
    a.shape = 3,4 # changes the shape of a
    print(a)

    c = a.view()
    t = c is a
    print('c = a.view()')
    print('c is a:', t)

    t = c.base is a # c is a view of the data owned by a
    print('c.base is a:', t)

    t = c.flags.owndata
    print('c.flags.owndata:', t)

    c.shape = 2, 6 # a's shape doesn't change
    print('c.shape = 2, 6')
    print(c)
    print('a.shape:', a.shape)

    c[0,4] = 1234 # a's data changes
    print('c[0,4] = 1234')
    print('a =')
    print(a)
    print('c =')
    print(c)

    # slicing an array returns a view of it
    s = a[:, 1:3] # choose 2nd, 3rd column
    s[:] = 10 # s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
    print('a[:, 1,3] = 10')
    print(a)
