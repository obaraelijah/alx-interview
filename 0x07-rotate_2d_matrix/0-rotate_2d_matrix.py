#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list[int]]): The input 2D matrix to be rotated.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(i, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for row in matrix:
        row.reverse()