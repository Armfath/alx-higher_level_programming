#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        str = '0'
    else:
        str = ''
    if (i != 99):
        end = ', '
    else:
        end = ''
    print("{}{}{}".format(str, i, end), end='')
print("")
