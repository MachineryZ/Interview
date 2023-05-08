# Financial Engineering Equation 6

平值看涨期权的定价用波动率和时间表示出来

1. 看涨期权：
    1. 行权价 K strike
    2. 到期时间 t maturity time
    3. 利率 r risk free rate 
    4. 分红率 q dividend
    5. 现价 s spot
    6. 波动率 volatility
2. 当 strike = s 是平值；当 strike > s 是虚值；当 strike < s 是实值
3. 定价 $C = SN(d_1) - e^{-rT}KN(d_2)$，$N(x) =\frac{1}{\sqrt{2\pi}}\int^x_{\infty}e^{-t^2/2}dt$，$d_1 = log(s/k) + rT + \frac{1}{2}\sigma^2$