import random
import numpy as np


def load_data(file):
    """处理数据"""
    data = np.fromfile(file, sep=' ')
    print(data.shape)

    data1 = np.genfromtxt(file, delimiter=' ')
    print(data1.shape)


class Model():
    def __init__(self, trian_x, trian_y):
        """初始化参数"""
        self.w = round(random.random(), 3)  # 随机初始化的参数w
        self.b = round(random.random(), 3)  # 随机初始化的参数b
        self.partial_w = 0
        self.partial_b = 0
        self.lr = 0.0001  # learning rate
        self.iteration = 100  # 训练的批次
        self.epoch = 50  # 训练的轮次
        self.train_x = trian_x
        self.train_y = trian_y

    def relation_x_y(self, x):
        """预设x、y之间的关系"""
        hat_y = self.w * x + self.b
        return hat_y


    def update_param(self):
        """计算w和b的偏导数，并更新参数"""
        self.partial_w = np.average(self.train_y - (self.w * self.train_x - self.b) * self.train_x)
        self.partial_b = np.average(self.train_y - (self.w * self.train_x - self.b))
        self.w = self.w - self.lr * self.partial_w
        self.b = self.b - self.lr * self.partial_b


def main(file):
    train_x, train_y = load_data(file)
    model = Model(train_x, train_y)


if __name__ == '__main__':
    data_file = 'housing.data'
    main(data_file)
