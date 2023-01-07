#!/usr/bin/python3
# 6-print_matrix_integer.py
# Daniel Chahul  <funniyou@gmail.com>

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            if column == row[-1]:
                print('{:d}'.format(column), end='')
            else:
                print('{:d}'.format(column), end=' ')
        print()
