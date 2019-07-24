# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/24 15:27
# @Software: PyCharm
import tensorflow as tf


def main():
    v = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    # tf.nn.softmax_cross_entropy_with_logits

    print(tf.reduce_mean(v))


def select_greater():
    v1 = tf.constant([1.0, 2.0, 3.0, 4.0])
    v2 = tf.constant([4.0, 3.0, 2.0, 1.0])
    sess = tf.InteractiveSession
    print(tf.greater(v1, v2))
    print(tf.select(tf.greater(v1, v2), v1, v2))
    sess.close()


if __name__ == '__main__':
    # main()
    select_greater()
