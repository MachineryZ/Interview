# Financial Engineering Question 4

[0, 1] 上均匀独立分布随机变量相加刚大于1的个数期望是多少？

也就是说，$E(n|x_1+...+x_{n-1}<1, x_1+...+x_n>1)$，递推：

1. $F(x) = E(\tau|\sum_{i=1}^{\tau x_i > x$，$\tau$ 是 stopping time，现在开始建立 F(x) 的递推公式或者递推方程。首先要理解这个函数 F 的含义，他是对于固定个数的变量之和大于x的期望
2. $P(x_1 > x) = 1 - x$, $P(x_1 < x) = x$
3. $F(x) = 1 - x + \int_0^x (F(x - t) + 1)dt$，这个式子的含义是：我们考察 $x_1$，