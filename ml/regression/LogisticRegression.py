#!/usr/bin/env python
"""
Several implementation of Logistic Regression

Z. Wang
wangzhe0543@gmail.com
"""
from __future__ import division
import numpy as np

# The sigmoid function
sigmoid = lambda x: 1.0 / (1.0 + np.e ** (-1.0 * x))


# cost function
