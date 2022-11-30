#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i != 100):
            str = " "
        else:
            str = ""
        if ((i % 15) == 0):
            print("FizzBuzz{}".format(str), end='')
        elif ((i % 3) == 0):
            print("Fizz{}".format(str), end='')
        elif ((i % 5) == 0):
            print("Buzz{}".format(str), end='')
        else:
            print("{}{}".format(i, str), end='')
