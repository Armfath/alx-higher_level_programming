#!/usr/bin/python3
def max_integer(my_list=[]):
    my_len = len(my_list)
    if (my_len == 0):
        return (None)
    temp = my_list[0]
    for x in my_list:
        if (x > temp):
            temp = x
    return (temp)
