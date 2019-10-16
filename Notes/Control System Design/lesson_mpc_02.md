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


### Noiseless case

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
\hat{p}(k+j|k) =&\ C_p\hat{x}(k+j|k) + D_{p2}w(k+j) + D_{p3}v(k+j) \\
=&\ C_pA^jx(k) \\
&+ \sum_{i=1}^jC_pA^{i-1}B_2w(k+j-i) + \sum_{i=1}^jC_pA^{i-1}B_3v(k+j-i) \\
&+ D_{p2}w(k+j) + D_{p3}v(k+j)
\end{aligned}
$$

and so
$$
\begin{aligned}
\tilde{p} &= \tilde{C}_px(k) + \tilde{D}_{p2}\tilde{w}(k) + \tilde{D}_{p3}\tilde{v}(k) \\
&= \tilde{p}_0(k) + \tilde{D}_{p3}\tilde{v}(k)
\end{aligned}
$$
with free-response
$$
\tilde{p}_0(k) = \tilde{C}_px(k) + \tilde{D}_{p2}\tilde{w}(k)
$$
where
$$
\tilde{C}_p = \begin{bmatrix}
C_p \\ C_pA \\ C_pA^2 \\ \vdots \\ C_pA^{N-1}
\end{bmatrix}\quad \tilde{D}_{p2}= \begin{bmatrix}
D_{p2} & 0 & \cdots & 0 & 0 \\
C_pB_2 & D_{p2} & \cdots & 0 & 0 \\
C_pAB_2 & C_pB_2 & \ddots & \vdots & \vdots \\
\vdots & \ddots & \ddots & D_{p2}& 0 \\
C_pA^{N-2}B_2 & \cdots & C_pAB_2 & C_pB_2& D_{p2}
\end{bmatrix}
$$

$$
\tilde{D}_{p3} = \begin{bmatrix}
D_{p3} & 0 & \cdots & 0 & 0 \\ 
C_pB_3 & D_{p3} & \cdots & 0 & 0 \\
C_pAB_3 & C_pB_3 & \ddots & \vdots & \vdots \\
\vdots & \ddots & \ddots & D_{p3} & 0  \\
C_pA^{N-2}B_3 & \cdots & C_pAB_3 & C_pB_3 & D_{p3}
\end{bmatrix}
$$



### Noisy case

The model:
$$
\begin{aligned}
x(k+1) &= Ax(k) + B_1e(k) + B_2w(k) + B_3v(k) \\
y(k) &= C_1x(k) + D_{11}e(k) + D_{12}w(k) \\
p(k) &= C_px(k) + D_{p1}e(k) + D_{p2}w(k) + D_{p3} v(k)
\end{aligned}
$$
Successive substitution:
$$
\begin{aligned}
\hat{x}(k+j|k) =& A^jx(k) \\
&+ \sum_{i=1}^jA^{i-1}B_3v(k+j-i) \\
&+ \sum_{i=1}^jA^{i-1}B_1\hat{e}(k+j-i|k)\\
&+ \sum_{i=1}^j A^{i-1}B_2w(k+j-i)
\end{aligned}
$$
Prediction of noise: $\hat{e}(k+j|k)=0$ for $j > 0$ and $e(k) = D^{-1}_{11}\Big(y(k) - C_1x(k) - D_{12}w(k)\Big)$

and so
$$
\begin{aligned}
\hat p(k+j|k) =&\ C_p\hat x(k+j|k) + D_{p2}w(k+j) + D_{p3}v(k+j) \\
=&\ C_pA^jx(k) + C_pA^{j-1}B_1e(k) \\
&+ \sum_{i=1}^j C_pA^{i-1}B_pw(k+j-i) \\
&+ \sum_{i=1}^j C_pA^{i-1}B_3v(k+j-i) \\
&+ D_{p2}w(k+j) + D_{p3}v(k+j)
\end{aligned}
$$


We assume that $D_{11}$ is an invertible matrix
$$
\begin{aligned}
\tilde{p}(k) &= \tilde{C}_px(k) +\tilde{D}_{p1}e(k) + \tilde{D}_{p2}\tilde{w}(k) + \tilde{D}_{p3}\tilde{v}(k) \\
&= \tilde{p}_0(k) + \tilde{D}_{p3}\tilde{v}(k)
\end{aligned}
$$
where
$$
\tilde{D}_{p1} = \begin{bmatrix}
D_{p1} \\ C_pB_1 \\ C_pAB_1 \\ \vdots \\ C_pA^{N-1}B_1
\end{bmatrix}
$$
and free-response signal
$$
\begin{aligned}
\tilde{p}_0(k) &= \tilde{C}_px(k) + \tilde{D}_{p1}e(k) + \tilde{D}_{p2}\tilde{w}(k) \\
&= \tilde{C}_px(k) + \tilde{D}_{p1}D^{-1}_{11}(y(k) - C_1x(k) - D_{12}w(k)) + \tilde{D}_{p2}\tilde{w} \\
&= (\tilde{C}_p-\tilde{D}_{p1}D^{-1}_{11}C_1)x(k) + \tilde{D}_{p1}D^{-1}_{11}y(k) + (\tilde{D}_{p2}-\tilde{D}_{p1}D^{-1}_{11}D_{12}E_w)\tilde{w}(k)
\end{aligned}
$$

### Summary

On basis of model:
$$
\begin{aligned}
x(k+1) &= Ax(k) + B_1e(k) + B_2w(k) + B_3v(k) \\
y(k) &= C_1x(k) + D_{11}e(k) + D_{12}w(k) \\
p(k) &= C_px(k) + D_{p1}e(k) + D_{p2}w(k) + D_{p3} v(k)
\end{aligned}
$$
we make prediction:
$$
\begin{aligned}
\tilde{p}(k) &= \tilde{C}_px(k) +\tilde{D}_{p1}e(k) + \tilde{D}_{p2}\tilde{w}(k) + \tilde{D}_{p3}\tilde{v}(k) \\
&= \tilde{p}_0(k) + \tilde{D}_{p3}\tilde{v}(k)
\end{aligned}
$$
where $e(k) = D^{-1}_{11}\Big(y(k) - C_1x(k) -D_{12}w(k)\Big)$ and where
$$
\tilde{C}_p = \begin{bmatrix}C_p \\ C_pA \\ C_pA^2 \\ \vdots \\ C_pA^{N-1}\end{bmatrix}\quad \tilde{D}_{p2}= \begin{bmatrix}D_{p2} & 0 & \cdots & 0 & 0 \\C_pB_2 & D_{p2} & \cdots & 0 & 0 \\C_pAB_2 & C_pB_2 & \ddots & \vdots & \vdots \\\vdots & \ddots & \ddots & D_{p2}& 0 \\C_pA^{N-2}B_2 & \cdots & C_pAB_2 & C_pB_2& D_{p2}\end{bmatrix}
$$

$$
\tilde{D}_{p1} = \begin{bmatrix}
D_{p1} \\ C_pB_1 \\ C_pAB_1 \\ \vdots \\ C_pA^{N-2}B_1
\end{bmatrix}\quad
\tilde{D}_{p3} = \begin{bmatrix}D_{p3} & 0 & \cdots & 0 & 0 \\ C_pB_3 & D_{p3} & \cdots & 0 & 0 \\C_pAB_3 & C_pB_3 & \ddots & \vdots & \vdots \\\vdots & \ddots & \ddots & D_{p3} & 0  \\C_pA^{N-2}B_3 & \cdots & C_pAB_3 & C_pB_3 & D_{p3}\end{bmatrix}
$$

## Standard formulation

### Performance index

Consider the system
$$
\begin{aligned}
x(k+1) &= Ax(k) + B_1e(k) + B_2w(k) + B_3v(k) \\
y(k) &= C_1x(k) + D_{11}e(k) + D_{12}w(k) \\
z(k) &= C_2x(k) + D_{21}e(k) + D_{22}w(k) + D_{23}v(k)
\end{aligned}
$$
Define performance index
$$
J(v,k) = \sum_{j=0}^{N-1}\hat{z}^T(k+j|k)\Gamma(j)\hat{z}(k+j|k)
$$
**LQPC**:
$$
J(u,k) = \sum_{j=N_m}^{N} \hat{x}^T(k+j|k)Q\hat{x}(k+j|k)+\sum_{j=1}^Nu^T(k+j-1)Ru(k+j-1)
$$

$$
z(k) = \begin{bmatrix}
Q^{1/2}x(k+1) \\R^{1/2}u(k)
\end{bmatrix}
$$

**GPC**:
$$
J(u,k)=\sum_{j=N_m}^N|\hat{y}_p(k+j|k)-r(k+j|k)|^2+\lambda^2\sum_{j=1}^{N_c}|\Delta u(k+j-1)|^2
$$

$$
z(k) = \begin{bmatrix}
\hat{y}_p(k+1)-r(k+1) \\ \lambda \Delta u(k)
\end{bmatrix}
$$

### LQCP performance index

Consider IO-model
$$
\begin{aligned}
x_o(k+1) &= A_ox_o(k)+K_oe_o(k) + L_od_o(k)+B_ou(k) \\
y(k) &= C_ox_o(k) + D_He_o(k) + D_Fd_o(k)
\end{aligned}
$$
Choose
$$
x(k) = x_o(k),\quad v(k)=u(k), \quad w(k)=d_o(k),\quad e(k)=e_o(k)
$$
then
$$
\begin{aligned}
x(k+1) &= A_ox(k) + K_oe(k)+L_od(k) + B_ov(k) \\
&= Ax(k) + B_1e(k) + B_2w(k) + B_3v(k) \\
y(k) &= C_1x(k) + D_{11}e(k) + D_{12}w(k)
\end{aligned}
$$

$$
\begin{aligned}
z(k) &= \begin{bmatrix}
Q^{1/2}x(k+1) \\ R^{1/2}v(k)
\end{bmatrix} \\
&= \begin{bmatrix}
Q^{1/2}A_ox(k) + Q^{1/2}K_oe(k) + Q^{1/2}L_ow(k) + Q^{1/2}B_ov(k) \\
R^{1/2}v(k)
\end{bmatrix} \\
&= \begin{bmatrix}
Q^{1/2}A_o \\0
\end{bmatrix}x(k) + \begin{bmatrix}
Q^{1/2}K_o \\ 0
\end{bmatrix}e(k) + \begin{bmatrix}
Q^{1/2}L_o \\ 0
\end{bmatrix}w(k) + \begin{bmatrix}
Q^{1/2}B_o \\ R^{1/2}
\end{bmatrix}v(k) \\
&= C_2x(k) + D_{21}e(k) + D_{22}w(k) + D_{23}v(k)
\end{aligned}
$$

### GPC performance index

Consider IIO-model
$$
\begin{aligned}x_i(k+1) &= A_ix_i(k)+K_ie_i(k) + L_id_i(k)+B_i\Delta u(k) \\y(k) &= C_ix_i(k) + D_He_i(k)\end{aligned}
$$
The realisation $y_p(k) = P(q)y(k)$ described by:
$$
\begin{aligned}
x_p(k+1) &= A_px_p(k) + B_py(k) \\
y_p(k) &= C_px_p(k) + D_py(k)
\end{aligned}
$$


Choose
$$
e(k) = e_i(k),\quad v(k) = \Delta u(k)
$$

$$
w(k) = \begin{bmatrix}
d_i(k) \\ r(k+1)
\end{bmatrix},\qquad x(k) = \begin{bmatrix}
x_p(k) \\ x_i(k)
\end{bmatrix}
$$



then
$$
\begin{aligned}
\begin{bmatrix}
x_p(k+1) \\ x_i(k+1)
\end{bmatrix} = & \begin{bmatrix}
A_p & B_pC_i \\ 0 & A_i
\end{bmatrix}\begin{bmatrix}
x_p(k) \\ x_i(k)
\end{bmatrix} + \begin{bmatrix}
B_pD_H \\ K_i
\end{bmatrix}e_i(k) + \\
&\begin{bmatrix}
0 & 0 \\ L_i & 0
\end{bmatrix}\begin{bmatrix}
d_i(k) \\ r(k+1)
\end{bmatrix} + \begin{bmatrix}
0 \\ B_i
\end{bmatrix}\Delta u(k) \\
= & Ax(k) + B_1e(k) + B_2w(k) + B_3v(k) \\
y(k) =& C_ix(k) + D_He(k) \\
=& C_1x(k) + D_{11}e(k) + D_{12}w(k)
\end{aligned}
$$
For $y_p(k)$ we find
$$
y_p(k) = \begin{bmatrix}
C_p & D_pC_i
\end{bmatrix}x(k) + D_pD_He(k)
$$
and we obtain the estimate $y_p(k+1)$
$$
\begin{aligned}
y_p(k+1) =& \begin{bmatrix}
C_pA_p & C_pB_pC_i + D_pC_iA_i
\end{bmatrix}\begin{bmatrix}
x_p(k) \\ x_i(k)
\end{bmatrix} + \\
&\begin{bmatrix}
C_pB_pD_H+D_pC_iK_i
\end{bmatrix}\hat{e}(k) + \\
&\begin{bmatrix}
D_pC_iL_i & 0
\end{bmatrix}\begin{bmatrix}
d_i(k) \\ r(k+1)
\end{bmatrix} + \begin{bmatrix}
D_pC_iB_i
\end{bmatrix}v(k)
\end{aligned}
$$
where we used the fact that $\hat{e}_i(k+1|k)=0$

Now we find:
$$
\begin{aligned}
z(k) =& \begin{bmatrix}
y_p(k+1) - r(k+1) \\
\lambda \Delta u(k)
\end{bmatrix} \\
=& \begin{bmatrix}
C_pA_p & C_pB_pC_i + D_pC_iA_i \\
0 & 0
\end{bmatrix}\begin{bmatrix}
x_p(k) \\x_i(k)
\end{bmatrix} + \\
& \begin{bmatrix}
C_pB_pD_H+D_pC_iK_i \\ 0
\end{bmatrix}\hat{e}_i(k) + \\
& \begin{bmatrix}
D_pC_iL_i & -I \\ 0 & 0
\end{bmatrix}\begin{bmatrix}
d_i(k) \\ r(k+1)
\end{bmatrix} + \begin{bmatrix}
D_pC_iB_i \\ \lambda I
\end{bmatrix}v(k) \\
=& C_2x(k) + D_{21}e(k) + D_{22}w(k) + D_{23}v(k)
\end{aligned}
$$


### Standard performance index

Define vector $\tilde{z}(k)$ with predictions of $\hat{z}(k+j|k)$:
$$
\tilde{z}(k) = \begin{bmatrix}
\hat{z}(k|k) \\ \hat{z}(k+1|k) \\ \vdots \\ \hat{z}(k+N-1|k)
\end{bmatrix}
$$
Then using the formulas of chapter 3 we obtain:
$$
\tilde{z}(k) = \tilde{C}_2x(k) + \tilde{D}_{21}e(k) + \tilde{D}_{22}\tilde{w}(k) + \tilde{D}_{23}\tilde{v}(k)
$$


$$
\tilde{C}_2 = \begin{bmatrix}
C_2 \\ C_2A \\ C_2A^2 \\ \vdots \\ C_2A^{N-1}
\end{bmatrix}\quad \tilde{D}_{22}= \begin{bmatrix}
D_{22} & 0 & \cdots & 0 & 0 \\
C_2B_2 & D_{22} & \cdots & 0 & 0 \\
C_2AB_2 & C_2B_2 & \ddots & \vdots & \vdots \\
\vdots & \ddots & \ddots & D_{22}& 0 \\
C_2A^{N-2}B_2 & \cdots & C_2AB_2 & C_2B_2& D_{22}
\end{bmatrix}
$$

$$
\tilde{D}_{21} = \begin{bmatrix}
D_{21} \\ C_2B_1 \\ C_2AB_1 \\ \vdots \\ C_2A^{N-2}B_1
\end{bmatrix}\quad
\tilde{D}_{23} = \begin{bmatrix}
D_{23} & 0 & \cdots & 0 & 0 \\ 
C_2B_3 & D_{23} & \cdots & 0 & 0 \\
C_2AB_3 & C_2B_3 & \ddots & \vdots & \vdots \\
\vdots & \ddots & \ddots & D_{23} & 0  \\
C_2A^{N-2}B_3 & \cdots & C_2AB_3 & C_2B_3 & D_{23}
\end{bmatrix}
$$

Now define
$$
\bar{\Gamma} = \begin{bmatrix}
\Gamma(0) & 0 & \cdots & 0 \\
0 & \Gamma(1) & & 0 \\
\vdots & \ddots & \ddots & \vdots \\
0 & \cdots & 0 & \Gamma(N-1)
\end{bmatrix}
$$
then
$$
\begin{aligned}
J(v,k) &= \sum_{j=0}^{N-1} \hat{z}^T (k+j|k)\Gamma(j)\hat{z}(k+j|k) \\
&= \tilde{z}^T(k)\Gamma\tilde{z}(k)
\end{aligned}
$$




## Handling constraints

Equality constraints
$$
E_j\hat{\phi}(k+j|k)=0
$$
Stack all constraints at time $k$ on predicted $\phi$ in one vector:
$$
\tilde{\phi} = \begin{bmatrix}
E_1\hat\phi(k+1|k) \\
E_2\hat\phi(k+2|k) \\
\vdots \\ E_N\hat\phi(k+N)
\end{bmatrix}
$$
In standard framework, we can express the equality constraints in the form
$$
\tilde\phi(k) = \tilde C_3x(k) + \tilde D_{31}e(k) + \tilde D_{32}\tilde w(k) + \tilde D_{33}\tilde v(k) = 0
$$

### State end-point constraint

$$
\begin{aligned}
x(k+N|k) =&\ A^Nx(k) + \begin{bmatrix}
A^{N-1}B_2 & A^{N-2}B_2 & \cdots B_2
\end{bmatrix}\tilde w(k) + \\
&+ A^{N-1}B_1e(k) + \begin{bmatrix}
A^{N-1}B_3 & A^{N-2}B_3 & \cdots & B_3
\end{bmatrix}\tilde v(k) \\
=&\ 0
\end{aligned}
$$

by defining
$$
\begin{aligned}
\tilde C_3 &= A^N \\ 
\tilde D_{31}&=A^{N-1}B_1 \\ 
\tilde D_{32}&=\begin{bmatrix}A^{N-1}B_2& A^{N-2}B_2 & \cdots & B_2\end{bmatrix} \\
\tilde D_{33} &= \begin{bmatrix}A^{N-1}B_3 & A^{N-2}B_3 & \cdots & B_3\end{bmatrix}
\end{aligned}
$$
we obtain
$$
\tilde \phi(k) = \tilde C_3x(k) + \tilde D_{31}e(k) + \tilde D_{32}\tilde w(k) + \tilde D_{33}\tilde v(k) = 0 
$$

### Inequality constraints

$$
\psi(k) \le \Psi(k)
$$

where $\psi$ reflects states, inputs, outputs and $\Psi$ reflects limitations

> ***
>
> **EXAMPLE**:
> $$
> \begin{array}{rcccl}
> x_{1,min} &\le& x_1(k) &\le & x_{1,max} \\
> & & v(k) &\le & v_{max} \\
> y_{min} & \le & y(k)
> \end{array}
> $$
> result in:
> $$
> \psi(k) = \left[\begin{array}{r}
> x_1(k) \\ -x_1(k) \\ v(k) \\ -y(k)
> \end{array}\right]\quad \Psi(k) = \left[\begin{array}{r}
> x_{1,max} \\ -x_{1,min} \\ v_{max} \\ -y_{min}
> \end{array}\right]
> $$
> So:
> $$
> \begin{aligned}
> \psi(k) &= \left[\begin{array}{r}
> E_1 \\ -E_1 \\ 0 \\ -C_1
> \end{array}\right]x(k) + 
> \left[\begin{array}{r}
> 0 \\ 0 \\ 0 \\ -D_{11}
> \end{array}\right]e(k) + \left[\begin{array}{r}
> 0 \\ 0 \\ 0 \\ -D_{12}
> \end{array}\right]w(k) + \left[\begin{array}{r}
> 0 \\ 0 \\ I \\ 0
> \end{array}\right]v(k) \\
> &= C_4x(k) + D_{41}e(k) + D_{42}w(k) + D_{43}v(k)
> \end{aligned}
> $$
> where $E_1 = \begin{bmatrix}1 & 0 & \cdots & 0\end{bmatrix}$. 
>
> ***

Now we obtain the inequality constraint
$$
\psi(k) = C_4x(k) + D_{41}e(k) + D_{42}w(k) + D_{43}v(k) \le \Psi(k)
$$
Stack all constraints at time $k$ on predicted $\psi$ in one vector:
$$
\tilde \psi(k) = \begin{bmatrix}
\hat\psi(k+1|k) \\ \hat\psi(k+2|k) \\ \vdots \\ \hat\psi(k+N|k)
\end{bmatrix} \le \begin{bmatrix}
\Psi(k+1|k) \\ \Psi(k+2|k) \\ \vdots \\ \Psi(k+N|k)
\end{bmatrix} = \tilde\Psi(k)
$$
Using the formulas of chapter 3, the inequality constraints can be written in the form
$$
\tilde\psi(k) = \tilde C_4x(k) + \tilde D_{41}e(k) + \tilde D_{42}\tilde w(k) + \tilde D_{43}\tilde v(k) \le \tilde\Psi(k)
$$
where

$$
\tilde{C}_4 = \begin{bmatrix}
C_4 \\ C_4A \\ C_4A^2 \\ \vdots \\ C_4A^{N-1}
\end{bmatrix}\quad \tilde{D}_{42}= \begin{bmatrix}
D_{42} & 0 & \cdots & 0 & 0 \\C_4B_2 & D_{42} & \cdots & 0 & 0 \\
C_4AB_2 & C_4B_2 & \ddots & \vdots & \vdots \\
\vdots & \ddots & \ddots & D_{42}& 0 \\
C_4A^{N-2}B_2 & \cdots & C_4AB_2 & C_4B_2& D_{42}
\end{bmatrix}
$$

$$
\tilde{D}_{41} = \begin{bmatrix}
D_{41} \\ C_4B_1 \\ C_4AB_1 \\ \vdots \\ C_4A^{N-2}B_1
\end{bmatrix}\quad
\tilde{D}_{43} = \begin{bmatrix}
D_{43} & 0 & \cdots & 0 & 0 \\ 
C_4B_3 & D_{43} & \cdots & 0 & 0 \\
C_4AB_3 & C_4B_3 & \ddots & \vdots & \vdots \\
\vdots & \ddots & \ddots & D_{43} & 0  \\
C_4A^{N-2}B_3 & \cdots & C_4AB_3 & C_4B_3 & D_{43}
\end{bmatrix}
$$

### Standard formulation

Consider the system
$$
\begin{aligned}
x(k+1) &= Ax(k) + B_1e(k) + B_2w(k) + B_3v(k) \\
y(k) &= C_1x(k) + D_{11}e(k) + D_{12}w(k) \\
\tilde z(k) &= \tilde C_2x(k) + \tilde D_{21}e(k) + \tilde D_{22}\tilde w(k) + \tilde D_{23}\tilde v(k) \\
\tilde\phi(k) &= \tilde C_3x(k) + \tilde D_{31}e(k) + \tilde D_{32}\tilde w(k) + \tilde D_{33}\tilde v(k) \\
\tilde\psi(k) &= \tilde C_4x(k) + \tilde D_{41}e(k) + \tilde D_{42}\tilde w(k) + \tilde D_{43}\tilde v(k) \\
\end{aligned}
$$
Minimise performance index:
$$
\begin{aligned}
J(v,k) &= \sum_{j=0}^{N-1}\hat z^T (k+j|k)\Gamma(j)\hat z(k+j|k) \\
&= \tilde z^T(k)\bar\Gamma\tilde z(k)
\end{aligned}
$$
subject to the constraints $\tilde\phi(k) = 0$ and $\tilde\psi(k) \le \tilde\Psi(k)$

