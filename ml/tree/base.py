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
    pass
