#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    len = len(sys.argv)
    if (len == 1):
        print("{}".format(sum))
    else:
        for i in range(1, len):
            sum += int(sys.argv[i])
        print("{}".format(sum))
