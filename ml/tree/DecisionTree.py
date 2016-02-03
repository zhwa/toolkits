#!/usr/bin/env python
"""
Naive Decesion Tree
"""
from __future__ import division
import numpy as np
import operator
from utils import sampleData, entropy, split, stats



class node(object):
    """
    Arguments:
        feature: the index of the column in the data set
        threshold: boundary for binary split
        results: dict to store the statics of category corresponding to the current node
        left: child node for the data item when feature value < threshold
        right: child node
    """
    def __init__(slef, feature=0, threshold=None, results=None, left=None, right=None):
        self.feature = feature
        self.threshold = threshold
        self.results = results
        self.left = left
        self.right = right


def buildTree(data):
    if len(data) <= 0: return node()

    currentEnt = entropy(data)
    bestGain = 0.0
    bestCriteria = None
    bestSets = None

    dimension = len(data[0]) - 1

    for feature in range(dimension):
        feature_values = {}
        for item in data:
            feature_values[data[feature]] = 1
        for value in feature_values.keys():
            set1, set2 = split(data, feature, value)
            p = len(set1) / len(set2)
            infoGain = currentEnt - p * entropy(set1) - (1 - p) * entropy(set2)
            if infoGain > bestGain and len(set1) > 0 and len(set2) > 0:
                bestGain = infoGain
                bestCriteria = (feature, value)
                bestSets = (set1, set2)

    if bestGain > 0:
        leftBranch = buildTree(bestSet[0])
        rightBranch = buildTree(bestSet[1])
        return node(feature=bestCriteria[0], threshold=bestCriteria[1], left=leftBranch, right=rightBranch)
    else:
        return node(results=stats(data))
