import tensorflow as tf

X = (tf.reshape(tf.constant(range(12)), (3, 4)))
print(X)
# tf.Tensor(
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]], shape=(3, 4), dtype=int32)

"""   2.2.4 索引   """
print(X[1:3])  # 张量切片
print(X[:, :1])  # 张量切片
print(X[1, 1])  # 张量取值

########################
# 指定位置重新赋值
########################
X = tf.Variable(X)
X[1, 2].assign(9)
print(X)
# <tf.Variable 'Variable:0' shape=(3, 4) dtype=int32, numpy=
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  9,  7],
#        [ 8,  9, 10, 11]])>