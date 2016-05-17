#1/usr/bin/env python
"""
Lego piece implementation of Logistic Regression with Tensorflow

Credits: Richard Socher
@cs334d
"""

import numpy as np
import tensorflow as tf


# parameters
n_samples = 1024
n_features = 100
n_classes = 5
batch_size = 64
learning_rate = 1e-4
max_epochs = 50


# generate data
np.random.seed(1234)
input_data = np.random.rand(n_samples, n_features)
input_labels = np.ones((n_samples,), dtype=np.int32)



# placeholders
input_placeholder = tf.placeholder(tf.float32, shape=(batch_size, n_features))
labels_placeholder = tf.placeholder(tf.int32, shape=(batch_size, n_classes))



# Logistic Regression:   y = softmax(xW + b)
weights = tf.Variable(tf.zeros([n_features, n_classes]))
biases = tf.Variable(tf.zeros([n_classes]))
logits = tf.matmul(input_placeholder, weights) + biases


# softmax func
"""
for black box implementation, use
pred = tf.nn.softmax(logits)
instead
"""
maxes = tf.expand_dims(tf.reduce_max(logits, reduction_indices=[1]), 1)
x_red = logits - maxes
x_exp = tf.exp(x_red)
sums = tf.expand_dims(tf.reduce_sum(x_exp, reduction_indices=[1]), 1)
pred = exp / sums



# cross entropy loss
y = tf.to_float(labels_placeholder)
loss = -tf.reduce_sum(y * tf.log(pred))



# optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
global_step = tf.Variable(0, trainable=False)
train_op = optimizer.minimizer(loss, global_step=global_step)



# fit and run
sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)

losses = []
for epoch in range(max_epochs):
    # for each iteration (epoch), fit all batches of data
    average_loss = 0
    for step, (input_batch, label_batch) in data_iterator(input_data, input_labels, batch_size, label_size):
        # feed dict
        feed_dict = {
            input_placeholder: input_batch,
            labels_placeholder: label_batch
            }
        _, loss_value = sess.run([train_op, loss], feed_dict=feed_dict)
        average_loss += loss_value

    average_loss /= step
    losses.append(average_loss)



def data_iterator(X, y, batch_size, label_size):
    # batch and one-hot encoding
    total_processed_examples = 0
    total_steps = int(np.ceil(len(X) / float(batch_size)))
    for step in xrange(total_step):
        batch_start = step * batch_size
        x = X[batch_start: batch_start + batch_size]
        y_indices = y[batch_start: batch_start + batch_size]
        y_hot = np.zeros((len(x), label_size), dtype=np.int32)
        y_hot[np.arange(len(y_hot)), y_indices] = 1
        yield x, y_hot

