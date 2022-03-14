1. 数据集中有100组数据

2. 给定预测的目标式 
   - 一次式：$\hat y = w_0x+b$
   - 二次式：$\hat y=w_1x^2+w_2x+b$
   
3. 设置损失函数并求梯度

    给定损失函数为$loss = \frac{1}{N}\sum\limits_{i=0}^{N}(y-\hat y)^2$

    -   对于一次式：$loss = \frac{1}{N}\sum\limits_{i=0}^{N}(y_i-(w_0x_i+b))^2$
        -   计算w的偏导数：
        -   $$\begin{aligned}\frac{\partial loss}{\partial w}&=\frac{\partial loss}{\partial \hat y}\frac{\partial \hat y}{\partial w}\\ &=\frac{1}{N}\sum\limits_{i=1}^{N}(y_i-(w_0x_i+b))x_i \end{aligned}$$
        -   $$\begin{aligned}\frac{\partial loss}{\partial b}&=\frac{\partial loss}{\partial \hat y}\frac{\partial \hat y}{\partial b}\\ &=\frac{1}{N}\sum\limits_{i=1}^{N}(y_i-(w_0x_i+b)) \end{aligned}$$
    -   对于二次式：$loss = \frac{1}{N}\sum\limits_{i=0}^{N}(y-(w_1x^2+w_2x+b))^2$
        -   

