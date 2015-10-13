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



class LR(object):
    def __init__(self, d, K):
        self.K = int(K)
        self.d = int(d)
        self.beta = np.random.rand(K,d)

    def prb(self, x, k):
        return  np.exp(self.beta[k].dot(x)) / sum(map(lambda kk: np.exp(self.beta[kk].dot(x)), range(self.K)))

    def predict(self, x):
        prob = map(lambda k: self.prb(x, k), range(self.K))
        return prob.index(max(prob))

    def train(self, data, labels):
        """ data should be in d dimension """
        step = 100
        alpha = 0.01
        iters = 0
        while abs(sum(step)) > 0.01:
            iters += 1
            for k in range(self.K):
                step = np.sum(map(lambda (x, y): (1 - self.prb(x, y)) * x, zip(data, labels)), axis=0)
                self.beta[k,:] += alpha * step


    





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



    
