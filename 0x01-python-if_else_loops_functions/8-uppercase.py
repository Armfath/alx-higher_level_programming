#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) >= 97 and ord(c) < 123):
            i = ord(c) - 32
        else:
            i = ord(c)
        print("{}".format(chr(i)), end='')
    print("")
