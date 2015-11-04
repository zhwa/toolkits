#!/usr/bin/env python
"""
SVM with SMO training. Implementation of a special case:

1. only two classes, y_i = +1 / -1
2. no outlier -- the data is linearly separable
3. no kernel

Z. Wang
wangzhe0543@gmail.com
"""
from __future__ import division
import numpy as np



def objective(alpha, data, label):
    (n, d) = data.shape
    locSum = lambda i, j: alpha[i] * alpha[j] * label[i] * label[j] * np.dot(data[i,:], data[j,:])
    grids = [(i,j) for i in range(n) for j in range(n)]
    first = np.sum(alpha)
    second = np.sum(map(locSum, grids))
    return first - 0.5 * second
    


def CoordinateDecent(alpha, data, label, C):
    """
    Args:
        alpha: alpha_i for i in [1,n]
        data: n data vectors, in d-dimension
        labels: y_i = +1 / -1
    return:
        updated alpha
    """
    (n, d) = data.shape
    
    
        
