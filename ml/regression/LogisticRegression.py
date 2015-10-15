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
import numpy as np



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
        """
        Gradient Decent
        """
        step = 100
        alpha = 0.01
        iters = 0
        while abs(sum(step)) > 0.01:
            iters += 1
            for k in range(self.K):
                step = np.sum(map(lambda (x, y): (1 - self.prb(x, y)) * x, zip(data, labels)), axis=0)
                self.beta[k,:] += alpha * step


