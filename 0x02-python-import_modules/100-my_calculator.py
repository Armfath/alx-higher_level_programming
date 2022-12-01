#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len = len(sys.argv)
    operators = ['+', '-', '*', '/']
    if (len != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if operator in operators:
        if (operator == '+'):
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif (operator == '-'):
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif (operator == '*'):
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        else:
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
