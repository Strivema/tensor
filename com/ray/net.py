# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/23 17:24
# @Software: PyCharm
import tensorflow as tf


def main():
    res = tf.Variable(tf.random.normal([2, 3], stddev=2))
    weights = tf.Variable(tf.random.truncated_normal([2, 3], stddev=2))
    a = tf.Variable(tf.random.uniform([2, 3], minval=1, maxval=10))
    b = tf.Variable(tf.random.gamma([2, 3], alpha=1, beta=2))

    c = tf.zeros([2, 3])
    d = tf.ones([2, 3])
    f = tf.fill([2,3],6)
    e = tf.constant([1,2,3])
    print(res)
    print(weights)
    print(a)
    print(b)
    print(c)
    print(d)
    print(f)
    print(e)


if __name__ == '__main__':
    main()
