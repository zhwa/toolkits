#!/usr/bin/env python
"""
Useful algorithms and data structures for decision trees

Z. Wang
wangzhe0543@gmail.com
"""
from __future__ import division
import numpy as np

def simpleData():
    data = [['slashdot','USA','yes',18,'None'],
        ['google','France','yes',23,'Premium'],
        ['digg','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['digg','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['digg','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]
    return data


def split(data, feature, threshold):
    if isinstance(threshold, str):
        judge = lambda row: row[feature] == threshold
    else:
        judge = lambda row: row[feature] >= threshold
    set1 = filter(judge, data)
    set2 = filter(lambda row: row not in set1, data)
    return set1, set2



def stats(data):
    cnt = {}
    s = 0
    for item in data:
        s += 1
        if item in cnt:
            cnt[item] += 1
        else:
            cnt[item] = 1
    cnt['s'] = s
    return cnt


def entropy(data):
    categories = np.asarray(data)[:,-1]
    cnt = stats(categories)
    h = 0
    N = cnt['s']
    for item in cnt:
        p = cnt[item] / N
        h -= p * np.log2(p)
    return h



if __name__ == "__main__":
    data = simpleData()
    set1, set2 = split(data, 3, 20)
    print entropy(set1)
    print entropy(set2)
