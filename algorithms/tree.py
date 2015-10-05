#!/usr/bin/env python
"""
Basic Tree types.

Z. Wang
wangzhe0543@gmail.com
"""
class PriorityQueue(object):
    """
    data format: (key, value) pair
    """
    def __init__(self):
        self.heap = [(0,0)]
        self.size = 0

    def build(self, rawList):
        self.size = len(rawList)
        self.heap = [(0,None)]
        for element in rawList:
            self.heap.append(element)
        mid = self.size // 2
        while mid > 0:
            self.percDown(i)
            i -= 1

    def percDown(self, idx):
        while idx * 2 <= self.size:
            mChild = self.minChild(idx)
            if self.heap[idx][1] > self.heap[mChild][1]:
                self.heap[idx], self.heap[mChild] = self.heap[mChild], self.heap[idx]
            idx = mChild

    def minChild(self, idx):
        if idx * 2 > self.size:
            return -1
        else:
            if idx * 2 + 1 > self.size:
                return idx * 2
            else:
                if self.heap[idx*2][1] < self.heap[idx*2+1][1]:
                    return idx * 2
                else:
                    return idx * 2 + 1

    def percUp(self, idx):
        while idx // 2 > 0:
            if self.heap[idx][1] < self.heap[idx//2][1]:
                self.heap[idx], self.heap[idx//2] = self.heap[idx//2], self.heap[idx]
            idx = idx // 2

    def add(self, k):
        self.heap.append(k)
        self.size += 1
        self.percUp(self.size)

    def delMin(self):
        retval = self.heap[1][0]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        return self.size == 0

    def modifyKey(self, old, new):
        idx = 0
        while idx <= self.size:
            if selfheap[idx][1] == old:
                break
            else:
                idx += 1
        if idx > 0:
            self.heap[idx] = (self.heap[idx][0], new)
            if new < old:
                self.percUp(idx)
            else:
                self.percDown(idx)
        else:
            raise ValueError("Key not found!")

    def __contains__(self, vertex):
        for pair in self.heap:
            if pair[1] == vertex:
                return True
        return False
        
            
