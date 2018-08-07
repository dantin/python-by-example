# -*- coding: utf-8 -*-

import numpy as np

from numpy import newaxis


if __name__ == '__main__':
    a = np.floor(10*np.random.random( (2, 2) ))
    print('a =')
    print(a)
    b = np.floor(10*np.random.random( (2, 2) ))
    print('b =')
    print(b)

    print('np.vstack((a, b))')
    print(np.vstack((a,b)))        # stack array vertically

    print('np.hstack((a, b))')
    print(np.hstack((a, b)))       # stack array horizontally

    print('np.column_stack((a, b)) # only like hstack() in a 2D array')
    print(np.column_stack((a, b))) # only like hstack() in a 2D array

    a = np.array([4., 2.])
    print('a =')
    print(a)
    b = np.array([3., 8.])
    print('b =')
    print(b)

    print('np.column_stack((a, b)) and np.hstack((a,b)) is DIFFERENT!')
    print(np.column_stack((a, b)))
    print(np.hstack((a, b))) # the result is different

    print('a[:,newaxis]')
    print(a[:,newaxis]) # this allows to have a 2D columns vector

    print('ONLY same in 2D array')
    print('np.column_stack((a[:,newaxis], b[:,newaxis]))')
    print(np.column_stack((a[:,newaxis], b[:,newaxis])))
    print('np.hstack((a[:,newaxis], b[:,newaxis]))')
    print(np.hstack((a[:,newaxis], b[:,newaxis]))) # the result is the same

    # On the other hand, the function row_stack is equivalent to vstack for any input arrays.
    # create array by stacking numbers along one axis.
    print('np.r_[1:4,0,4]')
    print(np.r_[1:4,0,4])
    print('np.c_[1:4]')
    print(np.c_[1:4])
