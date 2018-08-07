# -*-: coding: utf-8 -*-

import numpy as np

from numpy import pi

from example import print_dtype


if __name__ == '__main__':
    indarray = np.array([2, 3, 4])
    # NOTE: np.array(1, 2, 3, 4) # WRONG!!!
    print_dtype(indarray)

    dndarray = np.array([1.2, 3.5, 5.1])
    print_dtype(dndarray)

    # transform sequences of sequences into two-dimensional arrays
    print('# Transform sequences of sequences into two-dimensional arrays:')
    b = np.array([(1.5, 2, 3), (4, 5, 6)])
    print(b)

    # specify type at creation time
    print('# Specify type at creation time')
    c = np.array([ [1, 2], [3, 4] ], dtype=complex)
    print(c)

    # create when elements of an array is unknown, but its size is known
    print('# Create when elements of an array is unknown, but its size is known')
    print('# By default, the dtype of the created array is `float64`')

    print('np.zeros((3, 4)) # array full of zeros')
    zeros = np.zeros( (3, 4) )
    print(zeros)

    print('np.ones(..) # array full of ones')
    ones = np.ones( (2, 3, 4), dtype=np.int16 ) # dtype can also be specified
    print(ones)

    print('np.empty(..) # uninitialized array')
    empty = np.empty( (2, 3) ) # uninitialized, output my vary
    print(empty)

    # create sequences of numbers, NumPy provides a function analogous to `range` that returns arrays
    # instead of lists.
    print('# Create sequences of numbers')
    print('np.arange(..)')
    ia = np.arange( 10, 30, 5)
    print(ia)
    print_dtype(ia)

    da = np.arange( 0, 2, 0.3) # it accepts float arguments
    print(da)
    print_dtype(da)

    print('np.linspace(..) # better for floating point number')
    da2 = np.linspace( 0, 2, 9) # 9 numbers from 0 to 2
    print(da2)

    x = np.linspace( 0, 2*pi, 100) # useful to evaluate function at lots of points
    print('x =', x)

    f = np.sin(x)
    print('f = sin(x)', f)


