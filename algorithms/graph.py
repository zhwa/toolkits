#!/usr/bin/env python
"""
Grpah algorithm

Z. Wang
wangzhe0543@gmail.com
"""
import sys

class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.status = "new"
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        slef.fin = 0

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def setDiscovery(self, dtime):
        self.disc = dtime

    def getDiscovery(self):
        return self.disc

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def setDistance(self, d):
        self.dist = d

    def getDistance(self):
        return self.dist
    
    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    

class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.num = 0
        self.time = 0

    def addVert(self, key):
        self.num += 1
        newVert = Vertex(key)
        self.vertList[key] = newVert
        return newVert

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            newVert = self.addVert(f)
        if t not in self.vertList:
            newVert = self.addVert(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)



def gBuild(adr):
    g = Graph()
    with open(adr) as fid:
        while True:
            try:
                nodePair = fid.next().split()
                g.addEdge(int(nodePair[0]), int(nodePair[1]))
            except StopIteration:
                break
    return g



def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    start.setStatus("front")
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.status() == "new":
                nbr.setStatus("front")
                nbr.setPred(currentVert)
                nbr.setDistance(currentVert.getDistance() + 1)
                vertQueue.enqueue(nbr)
        currentVert.setStatus("old")




def dfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertStack = Stack()
    vertStack.push(start)
    while VertStack.size() > 0:
        currentVert = VertStack.peak()
        final = True
        for nbr in currentVert.getConnections():
            if nbr.getStatus() == "new":
                final = False
                nbr.setStatus("front")
                nbr.setPred(currentVert)
                nbr.setDistance(currentVert.getDistance() + 1)
                vertStack.push(nbr)
                break
        if final:
            currentVert.setStatus("old")
            vertStack.pop()
        
        















































