#!/usr/bin/python3
n = 0
m = 1
for i in range(n, 10):
    for j in range(m, 10):
        if (i == 8 and j == 9):
            str = ''
        else:
            str = ', '
        print("{}{}{}".format(i, j, str), end='')
    m += 1
print("")
