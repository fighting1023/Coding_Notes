import numpy as np


if __name__ == '__main__':
    data_file = '../00-深度学习与TensorFlow入门实战-源码和PPT/lesson04-回归问题实战/data.csv'
    points = np.genfromtxt(data_file, delimiter=',')  # delimiter: 用于分隔数据的字符

    learning_rate = 0.0001
    initial_b = 0
    initial_w = 0
    num_iterations = 1000

    print("Starting gradient descent at b = {0}, w = {1}, error = {2}"
          .format(initial_b, initial_w, compute_error_for_line_given_points(initial_b, initial_w, points)))
    print("Running...")
    [b, w] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, w = {2}, error = {3}".
          format(num_iterations, b, w, compute_error_for_line_given_points(b, w, points)))


