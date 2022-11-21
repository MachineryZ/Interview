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
\tau_t = min_n\{x_1+...+x_{n-1}<=t,x_1+...+x_n>t\}
$$

那么我们考虑第一个独立变量 $x_1$ 的取值，如果
