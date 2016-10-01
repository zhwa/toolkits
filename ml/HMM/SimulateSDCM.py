# -*- coding: utf-8 -*-
"""
Simulate Simplified Friston DCM

x(k+1) = Ax(k) + Bu + w1
y(k) = h (*) x + Du + w2

Try to be Pythonic
"""

import numpy as np
from matplotlib import pyplot as plt
import time
import re
from itertools import imap
import pdb
import os

class LinearSys(object):
    '''
    elegant implementation, matrix A, B, D are provided for initialization
    P: D{w1}; Q: D{w2}
    Dimentionality: 2
    '''
    def __init__(self,A,B,D,P,Q,x0=np.ones((2,1))):
        self._A = A
        self._B = B
        self._D = D
        self.X = np.reshape(x0,(2,1))
        self._P = P
        self._Q = Q
        self.history = np.empty((2,0))
        self.observe = []
    
    def forward(self,u):
        # one step forward
        self.X = np.dot(self._A,self.X) + np.dot(self._B,u)
        Noise = np.reshape(np.random.multivariate_normal((0,0),self._P),(2,1))
        return self.X + Noise
    
    def run(self,u=0.0):
        '''
        u should be a list or iterator
        '''
        steps = imap(self.forward, u)
        while True:
            try:
                self.history = np.append(self.history,steps.next(),axis=1)
            except StopIteration:
                break
        return self.history
    
    def reset(self):
        self.X = np.ones((2,1))
        self.history = np.empty((2,0))
        self.observe = [0,0]
    
    def output(self,h=None):
        if h==None:
            h1 = np.array([0,0.82,3.31,1.12,0.13,0])
            h2 = np.array([0,0.82,3.31,1.12,0.13,0])
        else:
            h1 = h[0,:]
            h2 = h[1,:]
        self.observe[0] = np.convolve(self.history[0],h1,mode='same') + np.random.normal(0,self._Q[0,0],len(self.history[0]))
        self.observe[1] = np.convolve(self.history[1],h2,mode='same') + np.random.normal(0,self._Q[1,1],len(self.history[0]))    
        return self.observe
    
    def write(self,file_dir=None):
        #file_name = re.sub('\s|:','-',time.asctime(time.localtime(time.time())))
        file_name = 'SimFMRI'
        if file_dir is None:
            np.savetxt(file_name + ' output_1.1D',self.observe[0],fmt='%.4f',delimiter='\n')
            np.savetxt(file_name + ' output_2.1D',self.observe[1],fmt='%.4f',delimiter='\n')
        else:
            np.savetxt(file_dir + '/' + file_name + ' output_1.1D',self.observe[0],fmt='%.4f',delimiter='\n')
            np.savetxt(file_dir + '/' + file_name + ' output_2.1D',self.observe[1],fmt='%.4f',delimiter='\n')
    
    def states(self,file_dir=None):
        # print out the history
        file_name = 'SimStates'
        if file_dir is None:
            np.savetxt(file_name + ' states_1.1D',self.history[0],fmt='%.4f',delimiter='\n')
            np.savetxt(file_name + ' states_2.1D',self.history[1],fmt='%.4f',delimiter='\n')
        else:
            np.savetxt(file_dir + '/' + file_name + ' states_1.1D',self.history[0],fmt='%.4f',delimiter='\n')
            np.savetxt(file_dir + '/' + file_name + ' states_2.1D',self.history[1],fmt='%.4f',delimiter='\n')
    


class stimuli(object):
    '''
    generate the input signal
    '''
    def __init__(self,T,on,off):
        self._T = T                 # The total length of the input
        self._on = on               # The length of each stimulus [...0, 1,1,...,1,0...]
        self._off = off             # The length of silence between two stimulus [1,0,...,0,1...]
        self.signal = []

    def generate_signal(self):
        if self._T % (self._on + self._off) is not 0:
            self._T -= self._T % (self._on + self._off)
            print 'The length of the signal has been cut to %d' % self._T
        for kk in xrange(self._T / (self._on + self._off)):
            self.signal += list(np.ones(self._on)) + list(np.zeros(self._off))
        return iter(self.signal)


# ---------- simulation --------------------

def Main():
    # Parameter setting
    A = np.array([[0.6,-0.1],[-0.3,0.75]])
    B = np.array([[2],[1]])
    D = np.array([[1,3],[0,6]])
    P = np.array([[0.5,0],[0,0.5]])
    Q = np.array([[0.6,0],[0,0.6]])
    x0 = np.zeros((2,1))
    
    S = LinearSys(A,B,D,P,Q,x0)
    S.reset()
    
    sti = stimuli(160,6,10)
    u = sti.generate_signal()
    #pdb.set_trace()
    
    states = S.run(u)
    
    #pdb.set_trace()
    
    S.output()
    directory = '/Users/wangzh34/Desktop/sim_data'
    if not os.path.exists(directory):
            os.makedirs(directory)
    S.write(directory)
    S.states(directory)
    #print S.observe
    
    plt.figure(0)
    plt.plot(S.observe[0],'bo-',label='region 1')
    plt.hold(True)
    plt.plot(S.observe[1],'g*-',label='region 2')
    plt.hold(False)
    plt.legend()
    plt.grid()
    
    
    plt.figure(1)
    plt.plot(S.history[0],'bo-',label='region 1')
    plt.hold(True)
    plt.plot(S.history[1],'g*-',label='region 2')
    plt.hold(False)
    plt.legend()
    plt.grid()    
    
    plt.show()


def group_simulation(num):
    # Parameter setting
    A = np.array([[0.6,-0.1],[-0.3,0.75]])
    B = np.array([[2],[1]])
    D = np.array([[1,3],[0,6]])
    P = np.array([[0.5,0],[0,0.5]])
    Q = np.array([[0.6,0],[0,0.6]])
    x0 = np.zeros((2,1))
    
    S = LinearSys(A,B,D,P,Q,x0)
    
    for kk in xrange(num):
        S.reset() 
        sti = stimuli(160,6,10)
        u = sti.generate_signal()
        states = S.run(u)
        S.output()
        directory = '/Users/wangzh34/Desktop/sim_data/sub'+str(kk)
        if not os.path.exists(directory):
            os.makedirs(directory)
        S.write(directory)
        S.states(directory)


if __name__ == '__main__':
    #pdb.set_trace()
    group_simulation(20)
    #Main()
