# 线性回归
1. 给定一个一次函数$y=1.57x+0.058$
2. 自己生成一些带有漂移的数据
3. 利用这些数据再拟合出这个一次函数，以验证结果。

- 损失函数
$$
loss = \frac{1}{N}\sum\limits_i(w*x_i+b-y_i)^2
$$
  
- 更新参数
$$
  w'=w-lr*\frac{\partial loss}{\partial w} 
$$
$$ 
  b'=b-lr*\frac{\partial loss}{\partial b}
$$
  
- 参数更新后有
$$
y = w'*x+b'
$$


