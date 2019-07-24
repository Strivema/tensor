# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/24 10:38
# @Software: PyCharm
import tensorflow as tf


def main():
    w1 = tf.Variable(tf.random.normal([2, 3], stddev=1))
    w2 = tf.Variable(tf.random.normal([3, 1], stddev=1))
    x = tf.placeholder(tf.float32, shape=(3, 2), name="input")
    a = tf.matmul(x, w1)
    y = tf.matmul(a, w2)
    sess = tf.Session()

    init_op = tf.initialize_all_variables()
    sess.run(init_op)
    # print(sess.run(y))
    print(sess.run(y, feed_dict={x: [[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]}))


if __name__ == '__main__':
    main()
