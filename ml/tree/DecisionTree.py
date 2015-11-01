#!/usr/bin/env python
"""
Naive Decesion Tree
"""
from __future__ import division
import numpy as np
import operator
from utils import ent, createDataSet


class node(object):
    def __init__(self, key, func, level, data):
        self.key = key
        self.func = func
        self.level = level
        self.data = data
        self.next = []

    def _classify(self):
        labels = {}
        for e in self.data:
            if e[-1] in labels:
                labels[e[-1]] += 1
            else:
                labels[e[-1]] = 1
        return max(labels.keys(), key=(lambda k: labels[k]))

    def classify(self, vec):
        if self.next == []:
            return _classify()
        else:
            check = [n.func(vec) for n in self.next]
            return self.next[check.index(True)].classify(vec)


    def train(self, mxLevel):
        if self.level >= mxLevel:
            self.next = []
        else:
            """ create children nodes """
            pass

    
        

    


class tree(object):
    def __init__(self, data, depth):
        self.data = data
        self.root = node(0, None, None)
        self.depth = depth

    def train(self):
        """ BFS for training """
        pass

    
