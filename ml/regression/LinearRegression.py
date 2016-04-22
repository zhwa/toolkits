#!/usr/bin/env python
"""
Tensorflow Implementation of Linear Regression

Credits: cs224d@Stanford
"""
import numpy as np
import tensorflow as tf

# define input data
X_data = np.arange(100, step=.1)
y_data = X_data + 20 * np.sin(X_data/10)


# define data size and batch size
n_samples = 1000
batch_size = 100


# Tensorflow adjustment
X_data = np.reshape(X_data, (n_samples, 1))
y_data = np.reshape(y_data, (n_samples, 1))


# define placeholders for input
X = tf.placeholder(tf.float32, shape=(batch_size, 1))
y = tf.placeholder(tf.float32, shape=(batch_size, 1))


# define variables to be learned
with tf.variable_scope("linear-regression"):
    W = tf.get_variable("weight", (1, 1), initializer=tf.random_normal_initializer())
    b = tf.get_variable("bias", (1,), initializer=tf.constant_initializer(0.0))
    y_pred = tf.matmul(x, W) + b
    loss = tf.reduce_sum((y - y_pred) ** 2) / n_samples



# sample code to run one step of gradient descent
opt = tf.train.AdamOptimizer()
opt_operation = opt.minimize(loss)
with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    sess.run([opt_operation], feed_dict={X: X_data, y: y_data})



# run full gradient descent
opt_operation = tf.train.AdamOptimizer().minimize(loss)
with tf.Session() as sess:
    # initialize
    sess.run(tf.initialize_all_variables())
    # gradient descent loop
    for _ in range(500):
        # select random minibatch
        indices = np.random.choice(n_samples, batch_size)
        X_batch, y_batch = X_data[indices], y_data[indices]
        # gradient descent
        _, loss_val = sess.run([opt_operation, loss], feed_dict={X: X_batch, y: y_batch})
        











