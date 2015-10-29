#!/usr/bin/env python
"""
Useful algorithms and data structures for decision trees

Z. Wang
wangzhe0543@gmail.com
"""
from __future__ import division
import numpy as np


def ent(dataSet):
    """
    calculate the Shannon Enropy of a given data set
    Arguments:
        dataSet: labeled data, the last volume should be the labels
        return: entropy in real values
    """
    N = len(dataSet)
    cates = {}
    for vector in dataSet:
        label = vector[-1]
        if label in cates:
            cates[label] += 1
        else:
            cates[label] = 1
    ent = 0
    for lable in cates:
        prob = cates[label] / N
        ent -= prob * np.log2(prob)
    return ent


def createDataSet():
    dataSet = [[1, 1, "yes"],
               [1, 1, "yes"],
               [1, 0, "no"],
               [0, 1, "no"],
               [0, 1, "no"]]
    labels = ["no surfacing", "flippers"]
    return np.array(dataSet), np.array(labels)
