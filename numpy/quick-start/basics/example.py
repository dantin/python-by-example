# -*- coding: utf-8 -*-

import numpy as np


def print_ndim(ndarray):
    """print the number of axes(dimensions) of the array."""
    print(ndarray.ndim)


def print_shape(ndarray):
    """print the dimensions of the array.

    That is a tuple of integers indicating the size of the array in each dimension."""
    print(ndarray.shape)


def print_dtype(ndarray):
    """print the object describing the type of the elements in the array."""
    print(ndarray.dtype)
    # alternative way
    # print(ndarray.dtype.name)


def print_size(ndarray):
    """print the total number of elements of the array."""
    print(ndarray.size)


def print_itemsize(ndarray):
    """print the size in bytes of eache element of the array."""
    print(ndarray.itemsize)
    # alternative way
    # print(ndarray.dtype.itemsize)


if __name__ == '__main__':
    # generate a ndarray
    a = np.arange(15).reshape(3, 5)

    print('# ndarray:')
    print(a)

    print('# ndarray.ndim:')
    print_ndim(a)

    print('# ndarray.shape:')
    print_shape(a)

    print('# ndarray.dtype')
    print_dtype(a)

    print('# ndarray.size: it is equal to the production of the elements of `shape`')
    print_size(a)

    print('# ndarray.itemsize:')
    print_itemsize(a)

    # type of a numpy's ndarray.
    print('type of numpy\'s ndarray:', type(a))

    # convert Python's list to ndarray
    l = [6, 7, 8]
    print('list b:', l)
    b = np.array(l)
    print('convert b to ndarray:', b)
    print('type of b:', type(b))
