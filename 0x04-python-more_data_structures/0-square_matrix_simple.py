#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[i**2 for i in matrix[i]] for i in range(len(matrix))]
