# -*- coding: utf-8 -*-

import numpy as np

from numpy import pi
from example import print_dtype


if __name__ == '__main__':
    # NOTE: For operation, a new array is created and filled with the result.
    #
    # Arithmetic operation
    print('# Arithmetic operatiors on arrays apply elementwise.')
    a = np.array( [20, 30, 40, 50] )
    b = np.arange( 4 )

    # subtract
    print('a =', a)
    print('b =', b)
    print('a-b =', a-b)

    # square
    print('b**2 =', b**2)

    # trigonometric function
    print('10*np.sin(a) =', 10*np.sin(a))

    # compare with scalar
    print('a<35 =', a<35)

    print()
    # Matrix operation
    print('# Matrix operation')
    A = np.array( [[1, 1], [0, 1]] )
    B = np.array( [[2, 0], [3, 4]] )
    print('A =')
    print(A)
    print('B =')
    print(B)

    print('elementwise product:')
    p = A * B    # elementwise product
    print('A*B =')
    print(p)

    print('matrix product')
    p = A @ B    # matrix product
    print('A@B =')
    print(p)

    print('another matrix product')
    p = A.dot(B) # another matrix product
    print('A.dot(B) =')
    print(p)

    print()

    print('# Inplace modify')
    # operations that act in place to modify an existing array rather than create a new one
    a = np.ones( (2, 3), dtype=int )
    b = np.random.random( (2, 3) )
    print('a =')
    print(a)
    print('b =')
    print(b)

    print('a *= 3, a =')
    a *= 3
    print(a)

    print('b += a, b =')
    b += a
    print(b)

    try:
        a += b # b is not automatically converted to integer type
    except TypeError as e:
        print('a += b raise exception')
        print(e)
        print(' b is not automatically converted to integer type')

    print()

    # When operating with arrays of different type, the resulting array is more general or precise one(AKA. upcasting)
    print('# When operating with arrays of different type, the resulting array is more general or precise one(AKA. upcasting)')
    a = np.ones(3, dtype=np.int32)
    print('a =', a)
    b = np.linspace(0, pi, 3)
    print('b =', b)

    c = a+b
    print('c =', c)
    print('dtype of c:')
    print_dtype(c)

    d = np.exp(c*1j)
    print('np.exp(c*1j) =')
    print(d)
    print('dtype of d:')
    print_dtype(d)

    # methods of ndarray
    print()
    print('# Methods of ndarray')
    a = np.random.random( (2, 3) )
    print('a =')
    print(a)

    print('a.sum()')
    print(a.sum())

    print('a.min()')
    print(a.min())

    print('a.max()')
    print(a.max())

    # specify with axis parameter
    print()
    print('# Specify with `axis` parameter')
    b = np.arange(12).reshape(3, 4)
    print('b =')
    print(b)

    print('b.sum(axis=0)')    # sum of each column
    print(b.sum(axis=0))

    print('b.min(axis=1)')    # min of each row
    print(b.min(axis=1))

    print('b.cumsum(axis=1)') # cumulative sum along each row
    print(b.cumsum(axis=1))
