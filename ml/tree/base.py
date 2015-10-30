#!/usr/bin/env python
"""
Basic decision tree structure

Z. Wang
wangzhe0543@gmail.com
"""
from __future__ import division
import operator
import numpy as np
from utils import *
import pdb


def splitDataSet(dataSet, feat, val):
    ext = np.array(filter(lambda vec: vec[feat] == val, dataSet))
    return np.hstack((ext[:,:feat], ext[:,feat+1:]))


def featSelect(dataSet):
    numFeat = len(dataSet[0]) - 1
    bestGain = 0.0
    bestFeat = -1
    
    for feat in range(numFeat):
        feats = [s[feat] for s in dataSet]
        vals = set(feats)
        subSets = map(lambda val: splitDataSet(dataSet, feat, val), vals)
        subEnts = map(ent, subSets)
        subPrbs = map(lambda subSet: len(subSet) / len(subSets), subSets)
        newEnt = sum(map(lambda i: subPrbs[i] * subEnts[i], range(len(subSets))))
        if -1 * newEnt < bestGain:
            bestGain = -1 * newEnt
            bestFeat = feat

    return bestFeat


def majorityVote(classList):
    votes = {}
    for vote in classList:
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
    return max(votes.keys(), key=(lambda key: votes[key]))


def createTree(dataSet, labels):
    classList = [e[-1] for e in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset[0]) == 1:
        return majorityVote(classList)
    bestFeat = featSelect(dataSet)
    bestLabel = labels[bestFeat]
    myTree = {bestLabel: {}}
    labels.remove(labels[bestFeat])
    featValues = [e[bestFeat] for e in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueValues:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree
