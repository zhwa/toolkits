#!/usr/bin/env python
"""
functioning blocks of neural networks

Z. Wang
wangzhe0543@gmail.com
"""
import numpy as np

def affine_forward(x, w, b):
    out = x.reshape(x.shape[0], -1).dot(w) + b
    cache = (x, w, b)
    return out, cache

def affine_backward(dout, cache):
    x, w, b = cache
    db = np.sum(dout, axis=0)
    dw = x.reshape(x.shape[0], -1).T.dot(dout)
    dx = dout.dot(w.T).reshape(x.shape)
    return dx, dw, db

def relu_forward(x):
    out = np.maximum(0, x)
    cache = x
    return out, cache

def relu_backward(dout, cache):
    dx = dout
    dx[dout<=0] = 0
    return dx


def batchnorm_forward(x, gamma, beta, bn_param):
    mode = bn_param['mode']
    eps = bn_param.get('eps', 1e-5)
    momentum = bn_param.get('momentum', 0.9)

    N, D = x.shape
    running_mean = bn_param.get('running_mean', np.zeros(D, dtype=x.dtype))

    if mode = 'train':
        sample_mean = np.mean(x, axis=0)
        sample_var = np.var(x, axis=0)

        running_mean = momentum * running_mean + (1 - momentum) * sample_mean
        running_var = momentum * running_var + (1 - momentum) * sample_var

        x_hat = (x - sample_mean) / np.sqrt(sample_var + eps)
        out = gamma * x_hat + beta
        cache = (x, gamma, beta)

    elif mode == 'test':
        x_hat = (x - running_mean) / np.sqrt(running_var + eps)
        out = gamma * x_hat + beta
        cache = (mode, x, gamma, beta)

    bn_param['running_mean'] = running_mean
    bn_param['running_var'] = running_var

    return out, cache


def batchnorm_backward(dout, cache):
    x, gamma, beta = cache
    dgamma = dout.dot(x_hat.T).sum()
    dbeta = dout.sum(axis=0)
    dx = dout * gamma
    return dx, dgamma, dbeta


def dropout_forward(x, dropout_param):
    p, mode = dropout_param['p'], dropout_param['mode']
    if 'seed' in dropout_param:
        np.random.seed(dropout_param['seed'])

    if mode == "train":
        mask = np.random.rand(*x.shape)
        mask[mask > p] = 1
        mask[mask <= p] = 0
        out = x * mask

    else:
        out = x

    cache = (dropout_param, mask)
    out = out.astype(x.dtype, copy=False)

    return out, cache


def dropout_backward(dout, cache):
    dropout_param, mask = cache
    mode = dropout_param['mode']

    if mode == "train":
        dx = dout * mask
    else:
        dx = dout

    return dx


def conv_forward(x, w, b, conv_param):
    N, C, H, W = x.shape
    F, HH, WW = w.shape[0], w.shape[2], w.shape[3]

    stride = conv_param["stride"]
    pad = conv_param["pad"]

    H1 = 1 + (H + 2*pad - HH) / stride
    W1 = 1 + (W + 2*pad - WW) / stride
    out = np.zeros((N, F, H1, W1))

    x_pad = np.pad(x, [(0, 0), (0, 0), (pad, pad), (pad, pad)], 'constant')
    for n in xrange(N):
        for f in xrange(F):
            for i in xrange(H1):
                for j in xrange(W1):
                    x_window = x_pad[n, :, i*stride: i*stride+HH, j*stride: j*stride+WW]
                    out[n, f, i, j] = np.sum(x_window * w[f]) + b[f]

    cache = (x, w, b, conv_param)
    return out, cache
