#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    end = ''
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if (j == len(matrix[0]) - 1):
                end = ''
            else:
                end = ' '
            print("{:d}{}".format(matrix[i][j], end), end='')
        print("")
