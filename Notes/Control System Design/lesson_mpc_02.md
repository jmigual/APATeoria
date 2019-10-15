# Model Predictive Control 2 - Prediction

Discussed the fives ingredients of MPC:

1. Proces + disturbance model (IO and IIO)
2. Performance index (GPC and LQPC)
3. Constraint handling (equality and inequality)
4. Optimization (QP)
5. Receding horizon principle 

## Prediction model

Prediction on basis of model:
$$
\begin{aligned}
x(k+1) &= Ax(k) + B_1e(k) + B_2w(k) + B_3v(k) \\
y(k) &= C_1x(k) + D_{11}e(k) + D_{12}w(k) \\
p(k) &= C_px(k) + D_{p1}e(k) + D_{p2}w(k) + D_{p3}v(k)
\end{aligned}
$$

- $x(k)$ is the state
- $v(k)$ is the control signal ($u$ / $\Delta u$)
- $e(k)$ is ZMWN
- $w(k)$ consists of all known signals ($r$ / $d_i$ / $d_o$)
- $p(k)$ is a signal to be predicted

- At time instant $k$:
  - Make a set of $j$-step ahead predictions of $p(k+j)$
- Prediction, denoted as $\hat{p}(k+j|k)$
  - Using information given at time $k$
  - Future values of the control signal $v(k+j)$

$$
p(k) = C_px(k) + D_{p1}e(k) + D_{p2}w(k) + D_{p3}v(k)
$$

Define
$$
\tilde{p}(k) = \begin{bmatrix}
\hat{p}(k|k) \\ \hat{p}(k+1|k) \\ \vdots \\ \hat{p}(k+N-1|k) \\ 
\end{bmatrix}\quad 
\tilde{v}(k) = \begin{bmatrix}
v(k) \\ v(k+1) \\ \vdots \\ v(k+N-1)
\end{bmatrix}\quad 
\tilde{w}(k) = \begin{bmatrix}
w(k) \\ w(k+1) \\ \vdots \\ w(k+N-1)
\end{bmatrix}
$$
Goal: find $\tilde{p}_0(k)$ and $\tilde{D}_{p3}$ such that
$$
\tilde{p}(k) = \tilde{p}_0(k) + \tilde{D}_{p3}
$$
with free-response signal:
$$
\tilde{p}_0(k) = \tilde{C}_px(k) + \tilde{D}_{p1}e(k) + \tilde{D}_{p2}\tilde{w}
$$


### Noseless case

$$
\begin{aligned}
x(k+1) &= Ax(k) + B_2w(k) + B_3v(k) \\
p(k) &= C_px(k) + D_{p2}w(k) + D_{p3} v(k)
\end{aligned}
$$

Successive substitution:
$$
\begin{aligned}
\hat{x}(k+j|k) &= Ax(k+j-1|k) + B_2w(k+j-1) + B_3v(k+j-1) \\
&= A^2 x(k+j-2|k) + AB_2w(k+j-2) + AB_3v(k+j-2) \\
&+ B_2w(k+j-1) + B_3v(k+j-1) \\
& \qquad \vdots \\
&= A^jx(k) + \sum_{i=1}^jA^{i-1}B_2w(k+j-i) + \sum_{i=1}^jA^{i-1}B_3v(k+j-i)
\end{aligned}
$$

$$
\begin{aligned}
\hat{p}(k+j|k) &= C_p\hat{x}(k+j|k) + D_{p2}w(k+j) + D_{p3}v(k+j) \\
&= C_pA^jx(k) + \sum_{i=1}^j\left(C_pA^{i-1}B_2w(k+j-i) + C_pA^{i-1}B_3v(k+j-i)\right) \\
&+ D_{p2}w(k+j) + D_{p3}v(k+j)
\end{aligned}
$$



