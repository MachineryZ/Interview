令 $W_t$ 为标准布朗运动，定义随机变量：

$X = \int_0^T W_t dt$，$Y = \int_0^T tdW_t$

求 $Cor(X, Y) $

解：

先分别计算 X 和 Y 的方差、期望：
$$
E(x) = \int_0^T E(W_t)dt = 0 (\text{brown movement}) \\
$$

$$
E(Y) = E(\int_0^T t dW_t) = E(\lim \Sigma_{i=0}^{n-1}t_i(W_{t_i+1} - W_{t_i}))=\\
\lim \Sigma_{i=0}^{n-1}E(t_i(W_{t_i+1} - W_{t_i})) = 0
$$

方差：
$$
E(X^2) = E(\int_0^TW_tdt *\int_0^TW_tdt)=E(\int_0^TW_tdt\int_0^TW_sds)\\
= E(\int_0^T\int_0^TW_tW_sdtds) \\
= \int_0^T\int_0^T E(W_t W_s)dtds \\

E(W_t*W_s) = min(t,s)\quad\text{theorem }\\ 
=\int_0^T(\int_0^st dt + \int_s^Tsdt)ds \\
=T^3/3
$$

$$

$$

$$
E(Y^2) = \int_0^TtdW_t =\int_0^T t^2dt \quad \text{ito asymmetric theorem}\\
=T^3/3
$$

协方差：
$$
Y = \int_0^TtdW_t = tW_t|_0^T - \int_0^TW_tdt = TW_t - X \\
X+Y = TW_T
$$

$$
Cov(X, Y) = Cov(X, TW_T - X) \\
= Cov(X, TW_T) - COV(X, X) \\
Cov(X, TW_T) = E(TW_TX) = TE(W_T\int_0^TW_tdt) = T\int_0^TE(W_TW_t)dt \\
= T\int_0^Ttdt = T^3/2
$$

$$
Cov(X, Y) = T^3/2 - T^3/3 = T^3/6
$$

$$
cor(X, Y) = Cov(X, Y) / Std(X) / Std(Y) = T^3/6 / T^3/3=1/2
$$

