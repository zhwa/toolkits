#!/usr/bin/env python
"""
implementation of Logistic Regression

Arguments:

    w: weight vector
    g: gradient function

Z. Wang
wangzhe0543@gmail.com
"""
from __future__ import division
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import pdb
import warnings

#warnings.filterwarnings('error')


class LR(object):
    def __init__(self, d, K):
        self.K = int(K)
        self.d = int(d)
        self.beta = np.random.rand(K,d)

    def prb(self, x, k):
        return np.exp(self.beta[k,:].dot(x)) / sum(map(lambda kk: np.exp(self.beta[kk,:].dot(x)), range(self.K)))

    def predict(self, x):
        prob = map(lambda k: self.prb(x, k), range(self.K))
        return prob.index(max(prob))

    def judge(self, y, k):
        if int(y) == int(k):
            return 1
        else:
            return 0

    def score(self, data, labels):
        err = 0
        for (x,y) in zip(data, labels):
            err += self.judge(x, y)
        return 1 - err / len(data)

    def train(self, data, labels, sgd=False):
        """
        Gradient Decent
        """
        alpha = 1e-3
        iters = 0
        while iters < 500:
            iters += 1
            for k in range(self.K):
                if not sgd:
                    s = map(lambda (x, y): self.judge(y, k) * (1 - self.prb(x, y)) * x, zip(data, labels))
                    step = np.sum(s, axis=0)
                    self.beta[k,:] += alpha * step
                else:
                    for (x,y) in zip(data, labels):
                        step = self.judge(x,y) * (1 - self.prb(x, y)) * x
                        alpha = 0.1
                        self.beta[k,:] += alpha * step


def test():
    data = datasets.load_iris()
    X = data.data[:100,:2]
    X = np.hstack((X, np.ones((100,1))))
    y = data.target[:100]
    """ raw data plot """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(X[:50,0], X[:50,1], color="black", marker="*", label="Setosa")
    ax.scatter(X[50:,0], X[50:,1], color="red", marker="*", label="Versicolor")
    """ classifier """
    clf = LR(d=3, K=2)
    clf.train(X, y)
    """ decision region """
    for ix in np.arange(4.0, 7.5, 0.05):
        for iy in np.arange(1.5, 5.0, 0.05):
            pred = clf.predict(np.array([ix,iy,1]))
            if pred == y[0]:
                ax.scatter(ix, iy, color="green", alpha=0.2)
            else:
                ax.scatter(ix, iy, color="blue", alpha=0.2)
    ax.set_xlim(4.0, 7.5)
    ax.set_ylim(1.5, 5.0)
    ax.set_xlabel("Sepal Length")
    ax.set_ylabel("Sepal Width")
    ax.legend()
    ax.grid()
    plt.show()



if __name__ == "__main__":
    test()
