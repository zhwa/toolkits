#!/usr/bin/env python
"""
Helper functions for the SMO algorithm
"""
from __future__ import division
import random
import numpy as np


def loadDataSet(fileName):
    whole = np.loadtxt(fileName)
    return whole[:,:-1], whole[:,-1]


def selectJrand(i, m):
    j = i
    while j==i:
        j = int(random.uniform(0, m))
    return j


def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = dataMatIn
    labelMat = classLabels.reshape((-1,1))
    b = 0
    m, n = dataMatrix.shape
    alphas = np.zeros((m, 1))
    iters = 0
    while iters < maxIter:
        alphaPairsChanged = 0
        for i in range(m):
            fXi = np.dot(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T) + b
