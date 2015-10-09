#!/usr/bin/env python
"""
Several implementation of Logistic Regression

Arguments:

    w: weight vector
    g: gradient function

Z. Wang
wangzhe0543@gmail.com
"""
from __future__ import division
from operator import add
import numpy as np
from ..regression import bfgs




# The sigmoid function
sigmoid = lambda z: 1.0 / (1.0 + np.e ** (-1.0 * z))


# gradient function
def g(w, x, y):
    """
    x: n * d, each rwo corresponds to one sample
    y: n * 1, lable
    w: 1 * d
    """
    yx = np.array(map(lambda vec: vec[:-1] * vec[-1], np.hstack((x,y.reshape((-1,1))))))
    gradient = reduce(add, map(lambda vec: (sigmoid(w.dot(vec)) - 1) * vec, yx))
    return gradient


def train(labeledData, alpha):
    raws = labeledData[:,:-1]
    labels = labeledData[:,-1]
    samples = np.hstack(np.ones((-1, raw.shape[0])), raws)

    # loop
    w = np.random.rand(samples.shape[1])
    for i in range(100):
        w = w - alpha * g(w, samples, labels)

    return w


def predict(rawVec, w):
    vec = np.hstack((1, rawVec))
    score = sigmoid(w.dot(vec))
    if score > 0.5:
        return 1
    else:
        return 0




    
