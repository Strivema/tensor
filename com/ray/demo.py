# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/23 9:58
# @Software: PyCharm
import tensorflow as tf

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
res = a + b
sess = tf.compat.v1.Session()
print(sess.run(res))
print(a.graph is tf.get_default_graph())
