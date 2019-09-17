# Lecture 3

## Linearization

_Book 5.4_

An _equilibrium point_ or _steady-state_ is a point where the system comes to a rest.
$$
\dot{x}(t) = 0
$$
Consider the system $\dot{x} = f(x, y)$. For a steady-state or equilibrium point $(x_0, u_0, y_0)$ there holds
$$
f(x_0, u_0) = 0
$$
The corresponding output $y_0$ can be computed by
$$
y_0 = g(x_0, u_0)
$$
Look at small variations $\tilde{x}$, $\tilde{u}$, and $\tilde{y}$ about the equilibrium $(x_0, u_0, y_0)$:
$$
\begin{aligned}
x(t) &= x_0 + \tilde{x}(t) \\
u(t) &= u_0 + \tilde{u}(t) \\
y(t) &= y_0 + \tilde{y}(t)
\end{aligned}
$$
First of all, note that $\dot{\tilde{x}}(t) = \dot{x} - \dot{x}_0$, and so
$$
\begin{aligned}
\dot{\tilde{x}}(t) &= f(x_0 + \tilde{x}(t), u_0 + \tilde{u}(t)) \\
y_0 + \tilde{y}(t) &= g(x_0 + \tilde{x}(t), u_0 + \tilde{u}(t))
\end{aligned}
$$
Use Taylor expansion to describe nonlinear equations in terms of $\tilde{x}$ and $\tilde{u}$:
$$
\begin{aligned}
\dot{\tilde{x}}(t) &= f(x_0, u_0) + A\tilde{x}(t) + B\tilde{u}(t) \\
\tilde{y} &= g(x_0, u_0) + C\tilde{x}(t) + D\tilde{u}(t) - y_0
\end{aligned}
$$
where $A$, $B$, $C$, and $D$ are computed as
$$
A = \left.\frac{\partial f}{\partial x}\right|_{\substack{x = x_0 \\ u=u_0}} \quad,\quad 
B = \left.\frac{\partial f}{\partial u}\right|_{\substack{x = x_0 \\ u=u_0}} \quad,\quad 
C = \left.\frac{\partial g}{\partial x}\right|_{\substack{x = x_0 \\ u=u_0}} \quad,\quad 
D = \left.\frac{\partial g}{\partial u}\right|_{\substack{x = x_0 \\ u=u_0}}
$$
With $f(x_0, u_0) = 0$ and $y_0 = g(x_0, u_0)$, this reduces to:
$$
\begin{aligned}
\dot{\tilde{x}}(t) &= A\tilde{x}(t) + B\tilde{u}(t) \\
\tilde{y}(t) &= C\tilde{x}(t) + D\tilde{u}(t)
\end{aligned}
$$

## From state-space models to frequency domain

_Book 8.1 and 8.2_

- Start with a state-space representation

$$
\begin{aligned}
\dot{x} &= Ax + Bu \\
y &= Cx + Du
\end{aligned}
$$

- Consider inputs of the form $u(t) = e^{st}, s = \sigma+iw \implies u(t) = e^{\sigma t}(\cos wt + i\sin wt)$ 
- Solution is $x(t) = e^{At}x_0 + \int_0^t e^{A(t - \tau)} Be^{st} d\tau = e^{At}x_0 + e^{At}\int_0^t e^{(sI - A)\tau} Bd\tau$
- If $s\ne \lambda(A) \implies x(t) = e^{At}x_0 + e^{At}(sI - A)^{-1}(e^{(sI-A)t} - I)B$
- Thus $y(t) = Ce^{At}(x_0 - (sI - A)^{-1}B) + (C(sI-A)^{-1}B + D)e^{st}$
  - (closely related to the frequency response (see Lecture 2) - transient plus steady-state term)
- Consider steady-state term. Let us define the transfer function as follows:

$$
G_{yu}(s) = C(sI - A)^{-1}B + D
$$

then we obtain:
$$
y(t) = G_{yu}(s)(t),\quad \text{for } u(t) = e^{st}
$$

### Transfer functions

> ***
>
> **EXAMPLE**: Consider the system
> $$
> \ddot{q} + 2 \zeta\omega_o\dot{q} + \omega_o^2q = k\omega_o^2u,\quad y = q
> $$
>
> - Can be written as (note: $x_1 = q$ and $x_2 = \dot{q}$)
>
> $$
> \frac{dx}{dt} = \begin{bmatrix}
> 0 & 1 \\ -\omega_0^2 & 2 \zeta\omega_o
> \end{bmatrix} \boldsymbol{x} + \begin{bmatrix}
> 0 \\ k\omega_o^2
> \end{bmatrix} u, \quad y = \begin{bmatrix}
> 1 & 0
> \end{bmatrix}x
> $$
>
> - Model has eigenvalues $\lambda = -\zeta\omega_o \pm \sqrt{\omega_o^2(\zeta^2 - 1)}$
> - For $\zeta,\omega_o > 0 \rightarrow$ model is stable
> - Transfer function
>
> $$
> \begin{aligned}
> G(s) &= C(sI - A)^{-1}B \\
> &= \begin{bmatrix}
> 1 & 0
> \end{bmatrix}\left(
> sI - \begin{bmatrix}
> 0 & 1 \\ -\omega_o^2 & -2\zeta\omega_o
> \end{bmatrix}
> \right)^{-1} \begin{bmatrix}
> 0 \\ k\omega_o^2
> \end{bmatrix} \\
> &= \frac{k\omega_o^2}{s^2 + 2\zeta\omega_os + \omega_o^2}
> \end{aligned} 
> $$
>
> 
>
> ***

