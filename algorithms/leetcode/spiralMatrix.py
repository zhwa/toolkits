#!/usr/bin/env python
"""
traverse a matrix in a spiral order

version 0.1: works only on square matrix

Z. Wang
wangzhe0543@gmail.com
"""
def spiralOrder(matrix):
    if matrix == [] or matrix == [[]]: return []
    
    result = []
    m, n = len(matrix), len(matrix[0])
    bottomLeft, bottomRight, topLeft, topRight = (m-1, 0), (m-1, n-1), (0, 0), (0, n-1)
    i, j = 0, 0

    while bottomLeft[0] < bottomRight[0] and bottomLeft[1] < topLeft[1]:
        for j in xrange(topLeft[1], topRight[1]+1):
            result.append(matrix[i][j])
        for i in xrange(topRight[0], bottomRight[0]+1):
            result.append(matrix[i][j])
        for j in xrange(bottomRight[1], bottomLeft[1]-1, -1):
            result.append(matrix[i][j])
        for i in xrange(bottomLeft[0], topLeft[0]-1, -1):
            result.append(matrix[i][j])

        bottomLeft, bottomRight, topLeft, topRight = (bottomLeft[0]-1, bottomLeft[1]+1), \
                                                 (bottomRight[0]-1, bottomRight[1]-1),\
                                                 (topLeft[0]+1, topLeft[1]+1),\
                                                 (topRight[0]+1, topRight[1]-1)
    return result
    
