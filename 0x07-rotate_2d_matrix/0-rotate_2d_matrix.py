#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list[int]]): The input 2D matrix to be rotated.
    """
    n = m = t = 0
    mat_len = len(matrix)
    while n + m < mat_len - 1:
        while n + m < mat_len - 1:
            o, p = n, m
            curr_val = matrix[n][m]
            for i in range(4):
                next_val = matrix[p][(mat_len - 1) - o]
                matrix[p][(mat_len - 1) - o] = curr_val
                curr_val = next_val
                temp = o
                o = p
                p = (mat_len - 1) - temp
            n += 1
        t += 1
        n = m = t