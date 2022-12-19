#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a) - 1
    len_b = len(tuple_b) - 1
    if (len_a < 1):
        for i in range(len_a, 1):
            tuple_a += (0,)
    if (len_b < 1):
        for i in range(len_b, 1):
            tuple_b += (0,)
    return ((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))
