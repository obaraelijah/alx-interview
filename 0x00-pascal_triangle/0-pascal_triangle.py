#!/usr/bin/python3
"""Create a list of lists of integers representing
the Pascal's triangle of `n`
"""

def pascal_triangle(n):
    """Returns pascal triangle as a list of lists
    of integers
    """
    if n <= 0:
        return []
    
    array = [[1]]
    
    for i in range(n - 1):
        temp = [0] + array[-1] + [0]
        row = []
        for j in range(len(array[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        array.append(row)
        
    return array