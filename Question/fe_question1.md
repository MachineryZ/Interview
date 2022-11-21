# Financial Engineering Question 1

一个均匀分布的随机变量，累加到第一次大于1的时候就停下来，求累加次数的期望

~~~c++
float sum = 0;
while(sum <= 1.0) {
    sum += randomUniform(0, 1);
}
return sum;
~~~

~~~c++
int num_event = 0;
int tot_num_event = 10000;
int sum_x = 0;
while(num_event < tot_num_event) {
    float sum = 0;

    while(sum <= 1.0) {
        sum += randomUniform(0, 1);
        sum_x++;
    }
    num_event++;
}
cout << sum_x / num_event;
~~~

自定义一个函数 
$$
\tau = min_n\{x_1+...+x_{n-1}<=1,x_1+...+x_n>1\} \\
\tau_t = min_n\{x_1+...+x_{n-1}<=t,x_1+...+x_n>t\} = f(t)
$$

那么我们考虑第一个独立变量 $x_1$ 的取值
$$
x_1 = s > t\\
E[x_1;x_1 > t] = \frac{1 + t}{2} * (1 - t)=(1 - t^2)/2
$$
另外一种情况：
$$
x_1 = s < t \\
E[x_1 ; x_1 < t] = (t)/2 * (t) = t^2/2
$$
然后考虑 x_2 到 x_n 的情况
$$
f(t) = (1 - t^2)/2 + t^2 / 2 + \int_0^t f(t - s) ds
$$
从积分方程转化为微分方程得到最后的
$$
f(t) = e^t/2
$$