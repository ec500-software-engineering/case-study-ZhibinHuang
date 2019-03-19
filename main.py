#!/usr/bin/env python
# encoding: utf-8
import tensorflow as tf
import os
import numpy as np
import pickle

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
a = np.abs([-1,2,-3])
print(a)

print('generate array')
data = [[1,2,3,9],[3,4,7,9],[5,6,8,9]]
x = np.array(data)
print(x) #print array
print(x.ndim) #print shape of array
print(x.shape) #print the length of every shape

w = tf.Variable([[1,2]])
x = tf.Variable([[2],[5]])
y = tf.matmul(w,x)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print(y.eval())
    sess.close()

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
