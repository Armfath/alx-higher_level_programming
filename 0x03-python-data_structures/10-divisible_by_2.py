#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listy = []
    for x in my_list:
        if (x % 2 == 0):
            listy.append(True)
        else:
            listy.append(False)
    return (listy)
