# -*- coding: utf-8 -*-

import numpy as np


if __name__ == '__main__':
    a = np.floor(10*np.random.random( (3, 4) ))
    print('a =')
    print(a)
    print('shape of a:', a.shape)

    # change the shape of an array
    print()
    print('# Change the shape of an array')
    t = a.ravel()       # returns the array, flattened
    print('a.ravel()')
    print(t)

    t = a.reshape(6, 2) # returns the array with a modified shape
    print('a.reshape(6, 2)')
    print(t)

    t = a.T             # returns the array, transposed
    print('a.T')
    print(t)
    print('shape of a.T:', a.T.shape)
    print('shape of a:', a.shape)

    # resize() do a in-place modify, whereas reshape() return a new array.
    print()
    print('# resize() do a in-place modify')
    print('a =')
    print(a)

    a.resize( (2, 6) )
    print('a.resize((2,6))')
    print('a =')
    print(a)

    # if a dimension is given as '-1' in a reshaping operation, the other dimensions are automatically calculated.
    print('a.reshape(3, -1)')
    print(a.reshape(3, -1))
