# -*- coding: utf-8 -*-

import numpy as np


def f(x):
    """Python passes mutable objects as references, so function calls make no copy"""
    print(id(x))


if __name__ == '__main__':
    a = np.arange(12)
    print('a =')
    print(a)

    b = a      # no new object is created
    t = b is a # a and b are two names for the same ndarray object
    print('b = a')
    print('b is a:', t)

    b.shape = 3, 4 # change the shape of a
    print(b)
    print(a.shape)

    i = id(a) # id is an unique identifier of an object
    print('id(a) =', i)
    print('id in function')
    f(a)
