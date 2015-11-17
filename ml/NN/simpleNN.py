#!/usr/bin/env python
"""
simple demo of neural network. example by:
http://www.hankcs.com/ml/back-propagation-neural-network.html

Z. Wang
wangzhe0543@gmail.com
"""
from __future__ import division
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def dSigmoid(x):
    y = sigmoid(x)
    return y * (1 - y)


class NN(object):
    def __init__(self, layer1, layer2, output):
        self.l1 = layer1
        self.l2 = layer2
        self.no = output

        self.a1 = [1.0] * self.l1
        self.a2 = [1.0] * self.l2
        self.ao = [1.0] * self.no

        self.w1 = np.random.rand(self.l1, self.l2)
        self.w2 = np.random.rand(self.l2, self.no)

        self.g1 = np.zeros((self.l1, self.l2))
        self.g2 = np.zeros((self.l2, self.no))


    def forward(self, vec):
        if 
