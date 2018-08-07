# -*- coding: utf-8 -*-

import numpy as np

from example import print_shape


def one_dimension_demo():
    """One-dimensional arrays can be indexed, sliced and iterated over, much like `lists` and other Python sequence."""
    a = np.arange(10)**3
    print('a =')
    print(a)

    print('indexing')
    print('a[2] =', a[2])

    print('slicing')
    print('a[2:5] =', a[2:5])

    print('a[:6:2] = -1000')
    a[:6:2] = -1000 # equivalent to `a[0:6:2] = -1000`; from start to position 6, exclusive, set every 2nd element to '-1000'
    print(a)

    print('a[::-1], reverse order')
    print(a[::-1])

    print('iterating')
    for i in a:
        print('i**(1/3.) =', (i**(1/3.)))


def multi_dimension_demo():
    def f(x, y):
        """x, y means `(row, col)`."""
        return 10*x + y

    b = np.fromfunction(f, (5, 4), dtype=int)
    print('b =')
    print(b)

    print('indexing multi-dimensional array')
    print('b[2,3] =', b[2, 3])

    col = b[0:5, 1]  # each row in the second column of b
    print('b[0:5, 1] =', col)

    col = b[:, 1]    # equivalent to the previous example
    print('b[:, 1]   =', col)

    rows = b[1:3, :] # each column in the second and third row
    print('b[1:3, :] =')
    print(rows)

    row = b[-1]      # the last row. Equivalent to b[-1,:]
    print('b[-1] =')
    print(row)

    print('`dot(...)` represent as many colons as needed to produce a complete indexing tuple.')
    c = np.array( [[[  0,   1,   2 ],  # a 3D array (two stacked 2D arrays)
                    [ 10,  12,  13]],
                   [[100, 101, 102],
                    [110, 112, 113]]] )
    print(c)
    print_shape(c)

    e = c[1,...]   # same as c[1,:,:] or c[1]
    print('c[1,...] =')
    print(e)

    e = c[...,2]   # same as c[:,:,2]
    print('c[...,2]')
    print(e)

    print()
    print('iterating')
    for row in b:
        print(row)

    print('iterating one by one')
    for element in b.flat:
        print(element)


if __name__ == '__main__':
    one_dimension_demo()
    print()
    multi_dimension_demo()
