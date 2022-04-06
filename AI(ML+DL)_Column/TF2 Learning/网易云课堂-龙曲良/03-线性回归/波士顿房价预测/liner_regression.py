import random
import numpy as np
import matplotlib.pyplot as plt


def load_data(file):
    # 从文件导入数据
    data = np.fromfile(file, sep=' ')

    # 每条数据包括14项，其中前面13项是影响因素，第14项是相应的房屋价格中位数
    feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                     'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    feature_num = len(feature_names)

    # 将原始数据进行Reshape，变成[N, 14]这样的形状
    data = data.reshape([data.shape[0] // feature_num, feature_num])

    # 将原数据集拆分成训练集和测试集
    # 这里使用80%的数据做训练，20%的数据做测试
    # 测试集和训练集必须是没有交集的
    ratio = 0.8
    offset = int(data.shape[0] * ratio)
    training_data = data[:offset]

    # 计算训练集的最大值，最小值，平均值
    maximums, minimums, avgs = training_data.max(axis=0), training_data.min(axis=0), \
                               training_data.sum(axis=0) / training_data.shape[0]

    # 对数据进行归一化处理
    for i in range(feature_num):
        # 归一化公式：x_i = \frac{x_i - min}{max - min}
        data[:, i] = (data[:, i] - minimums[i]) / (maximums[i] - minimums[i])

    # 训练集和测试集的划分比例
    training_data = data[:offset]
    test_data = data[offset:]
    return training_data, test_data


class Network(object):
    def __init__(self, num_of_weights):
        """初始化参数"""
        self.w = np.random.randn(num_of_weights, 1)
        self.b = random.random()
        self.iteration = 100
        self.eta = 0.01  # η 学习率

    def forward(self, x):
        """前向传播"""
        z = np.dot(x, self.w) + self.b
        return z

    def loss(self, z, y):
        """计算损失值"""
        error = z - y
        num_samples = error.shape[0]
        cost = error * error
        cost = np.sum(cost) / num_samples
        return cost

    def gradient(self, x, y):
        """计算梯度"""
        z = self.forward(x)
        gradient_w = (z - y) * x
        gradient_w = np.mean(gradient_w, axis=0)
        gradient_w = gradient_w[:, np.newaxis]
        gradient_b = (z - y)
        gradient_b = np.mean(gradient_b)
        return gradient_w, gradient_b

    def update(self, gradient_w, gradient_b):
        """更新梯度"""
        self.w = self.w - self.eta * gradient_w
        self.b = self.b - self.eta * gradient_b

    def train(self, x, y, ):
        """训练模型"""
        losses = []
        for i in range(self.iteration):
            z = self.forward(x)
            L = self.loss(z, y)
            gradient_w, gradient_b = self.gradient(x, y)
            self.update(gradient_w, gradient_b)
            losses.append(L)
            if (i + 1) % 10 == 0:
                print('iter {}, loss {}'.format(i, L))
        return losses


if __name__ == '__main__':
    file = 'housing.data'
    # 获取数据
    train_data, test_data = load_data(file)
    x = train_data[:, :-1]
    y = train_data[:, -1:]
    # 创建网络
    net = Network(x.shape[1])
    # 启动训练
    losses = net.train(x, y)

    # 画出损失函数的变化趋势
    plot_x = np.arange(net.iteration)
    plot_y = np.array(losses)
    plt.plot(plot_x, plot_y)
    plt.show()
