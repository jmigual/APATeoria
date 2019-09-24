# Lecture 4

If you want a system and you should be able to know where you are (know the state of your system). Thus, the observability of a system is really important

- If you can observe your system then it's important that you can control it
- Do we have enough freedom to control our system?1

## Reachability

_Book 6.1_

- Consider

$$
\frac{d}{dt}x(t) = Ax(t) + Bu(t),\quad x(0) = x_0 \in \R^n
$$

- with known solution

$$
x(t) = e^{At}x_0 + \int_0^t e^{A(t - \tau)}Bu(\tau)d\tau
$$

- **Definition**: System is reachable if for any $x_0 \in \R^n, x_t \in \R^t$, there exists input $u(\tau)$, with $\tau\in[0,t],0<t<\infty$, such that $x(t) = x_t$
- Reachability is equivalent to Controllability

### Algebraic Conditions for Reachability

- Reachability depends on the form $e^{At}B$, i.e. on matrices $A$ and $B$
- Assume initial state $x(0) =0$
- For input $u(t) = \delta(t)$ we find the state

$$
x(t) = \int_0^t e^{A(t - \tau)}B\delta(\tau)d\tau = e^{At}B
$$

- For input $u(t) = \dot{\delta}(t)$ we find the  state $x(t) = Ae^{At}B$
- For input $u(t) = \ddot{d}(t)$ we find the state $x(t) = A^2e^{At}B$
- For input $u(t) = d^{(k)}(t)$ we find the state $x(t) = A^ke^{At}B$
- For input $u(t) = \alpha_1\delta(t) + \alpha_2\dot{\delta}(t) + \alpha_3\ddot{\delta}(t) + \dotsb + \alpha_n \delta^{(n-1)}(t)$ we find the state

$$
\begin{aligned}
x(t) &= \alpha_1 e^{At} B + \alpha_2 A e^{At} B + \alpha_3 A^2 e^{At} B + \dotsb + \alpha_1 A^{n-1}e^{At} B \\
&= \underbrace{\begin{bmatrix}
B & AB & A^2B& \cdots & A^{n-1}B
\end{bmatrix}}_{W_r}\begin{bmatrix}
\alpha_1 \\ \alpha_2 \\ \alpha_3 \\ \vdots \\ \alpha_n
\end{bmatrix} e^{At} \\
\begin{bmatrix}
\alpha_1 \\ \alpha_2 \\ \alpha_3 \\ \vdots \\ \alpha_n
\end{bmatrix} = e^{-At}W_r^{-1}x(t)
\end{aligned}
$$

- Reachability means that Reachability matrix $W_r$ must have full rank

$$
W_r = \begin{bmatrix}
B & AB & A^2B & \cdots A^{n-1}B
\end{bmatrix}
$$

- **Theorem**: $(A, B)$ reachable if and only if

$$
\operatorname{rank} \begin{bmatrix}
B & AB & A^2B & \cdots A^{n-1}B
\end{bmatrix} = n (= \text{ number of rows})
$$

- The test

$$
\operatorname{rank} W_r = n
$$

is known as Kalman rank condition

- Extensions to time-varying, non-linear case through notion of state-transition matrix $\Phi$ (also mentioned in Lec 2)
- In MATLAB use command `ctrb over ss` structure to obtain Reachability matrix

> ***
>
> **EXAMPLE**
>
> - Consider
>
> $$
> A = \left[\begin{array}{rrr}
> -5 & -4 & 4 \\ 1 & 0 & -2 \\ -1 & -1 & -1
> \end{array}\right]\quad B = \left[\begin{array}{r}
> 3 \\ -1 \\ 1
> \end{array}\right]
> $$
>
> - Compute
>
> $$
> W_r = \begin{bmatrix}
> B & AB & A^2 B
> \end{bmatrix} = \left[\begin{array}{rrr}
> 3 & -7 & 19 \\ -1 & 1 & -1 \\
> 1 & -3 & 9
> \end{array}\right]
> $$
>
> - Perform elementary column operations $(2^{\circ} + 1^{\circ},3^{\circ} - 1^{\circ})$
>
> $$
> \operatorname{rank} \left[\begin{array}{rrr}
> 3 & -7 & 19 \\
> -1 & 1 & -1 \\
> 1 & -3 & 9
> \end{array}\right] = \operatorname{rank} \left[\begin{array}{rrr}
> 3 & -4 & 16 \\ -1 & 0 & 0 \\ 1 & -2 & 8
> \end{array}\right] = 2 < n = 3 \implies (A,B) \text{ not reachable}
> $$
>
> ***

## Observability

_Book 7.1_

- Consider autonomous (no control) system:

$$
\frac{d}{dx}x(t) = Ax(t),\quad x(0) = x_0 \in \R^n;\quad y(t) = Cx(t)
$$

- with solution

$$
y(t) = Ce^{At}x_0
$$

- **Definition**: System is observable if any $x_0\in \R^n$ can be derived from observation $y(\tau)$ within the interval $\tau \in [0, t], t> 0$
- Observability follows from $Ce^{At}$, hence it depends on matrices $A, C$
- Output is given by $y(t) = Ce^{At}x_0$
- Derivative Output is given by $\dot{y}(t) = C\frac{d}{dt}e^{At}x_0 = CAe^{At}x_0$
- And so:

$$
\begin{bmatrix}
y(t) \\ \dot{y}(t) \\ \ddot{y}(t) \\ \vdots \\ y^{(n-1)}(t)
\end{bmatrix} = \begin{bmatrix}
C \\ CA \\ CA^2 \\ \vdots \\ CA^{n-1}
\end{bmatrix} e^{At}x_0
$$

- Observability matrix $W_o$:

$$
W_o = \begin{bmatrix}
C \\ CA \\ CA^2 \\ \vdots \\ CA^{n-1}
\end{bmatrix}
$$

- **Theorem**: $(A,C)$ is observable if and only if

$$
\operatorname{rank} W_o = n (= \text{ number of columns})
$$

- In MATLAB, use `obsv over ss` structure to obtain observability matrix

> ***
>
> **EXAMPLE**: Consider the following model
> $$
> \begin{cases}
> \dot{x}_1 &= x_2 \\
> \dot{x}_2 &= 2x_2 \\
> y  &= \alpha x_1 + x_2
> \end{cases}
> $$
>
> $$
> \begin{aligned}
> A &= \begin{bmatrix}
> 0 & 1 \\ 0 & 2
> \end{bmatrix},\quad C=\begin{bmatrix}
> \alpha & 1
> \end{bmatrix} \\
> W_o &= \left[\begin{array}{rl}
> \alpha & 1 \\ 0 & 2 + \alpha
> \end{array}\right]
> \end{aligned}
> $$
>
> - $(A,C)$ is observable for $\alpha \ne 0$ and $\alpha \ne -2$
>
> ***

### Reachability and Observability: Alternative Test by Hautus

- Rationale: $\lambda I - A$ has rank $n$ for all $\lambda$ not equal to an eigenvalue of $A \implies$ rank check  needs only to be evaluated when $\lambda$ is equal to an eigenvalue of $A$

- Finding unreachable or unobservable _eigenvalues_ can be done using:

  - **Hautus reachability condition**: $(A,B)$ is reachable iff:

  $$
  \operatorname{rank}\begin{bmatrix}
  \lambda I - A & B
  \end{bmatrix} = n, \forall \lambda \in \mathbb{C}
  $$
  - **Hautus observability condition**: $(A,C)$ is observable iff:
  $$
  \operatorname{rank}\begin{bmatrix}
  \lambda I - A \\ C
  \end{bmatrix} = n, \forall \lambda \in C
  $$

> ***
>
> **EXAMPLE**: Consider $(A,B)$:
> $$
> A = \left[\begin{array}{rrr}
> -5 & -4 & 4 \\ 1 & 0 & -2 \\ -1 & -1 & -1
> \end{array}\right]\quad
> \left[\begin{array}{r}
> 3 \\ -1 \\ 1
> \end{array}\right]
> $$
>
> - Matrix $A$ has eigenvalues in the set $\{-1, -2, -3\}$
> - Perform following computations
>
> $$
> \operatorname{rank} \left[\begin{array}{c|c}
> (\lambda I - A)|_{\lambda=-1} & B
> \end{array}\right] = \operatorname{rank} \left[\begin{array}{rrr|r}
> 4 & 4 & -4 & 3 \\
> -1 & -1 & 2 & -1 \\
> 1 & 1 & 0 & 1 
> \end{array}\right] = 3
> $$
>
> - Eigenvalue $-1$ is reachable
>
> $$
> \operatorname{rank} \left[\begin{array}{c|c}
> (\lambda I - A)|_{\lambda=-2} & B
> \end{array}\right] = \operatorname{rank} \left[\begin{array}{rrr|r}
> 3 & 4 & -4 & 3 \\
> -1 & -2 & 2 & -1 \\
> 1 & 1 & -1 & 1 
> \end{array}\right] = 2
> $$
>
> - Eigenvalue $-2$ is unreachable
>
> $$
> \operatorname{rank} \left[\begin{array}{c|c}
> (\lambda I - A)|_{\lambda=-1} & B
> \end{array}\right] = \operatorname{rank} \left[\begin{array}{rrr|r}
> 2 & 4 & -4 & 3 \\
> -1 & -3 & 2 & -1 \\
> 1 & 1 & -2 & 1 
> \end{array}\right] = 3
> $$
>
> - Eigenvalue $-3$ is reachable

