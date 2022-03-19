import numpy as np

print(np.random.choice(5, 2))  # 等价于 np.random.randint(0,5,3)
# [3 2]

"""   从非均匀分布的np.arange(5)中生成 size 为 3 的随机样本，给定取值概率   """
print(np.random.choice(5, 4, p=[0.1, 0, 0.3, 0.6, 0]))
# [2 3 2 3]

"""   从np.arange(5)中生成一个 size=3 的随机均匀分布，replace=False   """
print(np.random.choice(5, 3, replace=False))  # 等价于 np.random.permutation(np.arange(5))[:3]
# [2 3 0]

"""   从np.arange(5)中生成一个 size=3 的随机非均匀分布，replace=False   """
print(np.random.choice(5, 2, replace=False, p=[0.1, 0, 0.3, 0.6, 0]))
# [2 3]

"""   非整数   """
aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
print(np.random.choice(aa_milne_arr, 6, p=[0.5, 0.1, 0.1, 0.3]))
# ['piglet' 'pooh' 'Christopher' 'pooh' 'Christopher' 'pooh']
