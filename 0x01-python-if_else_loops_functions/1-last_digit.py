#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    lastDigit = -((number * -1) % 10)
else:
    lastDigit = number % 10
if (lastDigit > 5):
    str = "greater than 5"
elif (lastDigit == 0):
    str = "0"
else:
    str = "less than 6 and not 0"

print("Last digit of {} is {} and is {}".format(number, lastDigit, str))
