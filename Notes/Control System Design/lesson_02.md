# Lesson 2

## Solving differential equations

Consider a system with feedback:
$$
\left.
\begin{aligned}
\dot{x} &= f(x, u) \\
u &= \alpha(x)
\end{aligned}
\right\} \quad
\dot{x} = f(x, \alpha(x)) = F(x)
$$
Problems:

- Existence: maybe there's not a signal that satisfies all the conditions
- Uniqueness: sometimes there's not a unique solution but many to them

> ***
>
> **EXAMPLE 1**: 
>
> In this case there's no solution here. The system would have exploded disintegrated or something else
>
> ***

>***
>
>**EXAMPLE 2**:
>
>You don't know what to expect at some point is just going to start. There are an infinite number of solutions.
>
>***

They can be guaranteed by Lipschitz continuity:
$$
\exists c : ||F(x) - F(y)|| < c||x - y||
$$
_It's just a sufficient condition_

- If you look at $F(x)$ the derivative of this function is bounded, although sometimes the derivative does not exist
- If the derivative is not bounded this condition does not hold

### Qualitative analysis of ODE: phase portraits

_Book 4.2_

- Consider planar case, $x \in \mathbb{R}^2$ 
- Plot with the two states on the axis
- By studying properties of vector field, build _phase portrait_

Let's suppose that we have:
$$
x(t) = 
\begin{bmatrix}
x_1(t) \\ x_2(t)
\end{bmatrix} \qquad
\dot{x}(t) = f(x(t)) = 
\begin{bmatrix}
f_1(x(t)) \\ f_2(x(t))
\end{bmatrix} = 
\begin{bmatrix}
1 \\ 1.2
\end{bmatrix}
$$
Then we can compute for every point in $t$ the values for $f(x(t))$ 

> ***
>
> **EXAMPLES**
>
> 1. This system is marginally stable since it does not go to infinity or zero and just oscillates
> 2. This system is stable because the points go to zero even if it is slowly
> 3. This system is unstable because it goes to infinity
>
> ***

#### Limit cycle

All trajectories will end up in the limit cycle

## Stability

_Book (4.3)_

- Consider autonomous system:

$$
\dot{x} = f(x)
$$

with initial state $x_0$ and trajectory $x(t, x_0)\ \forall t$

- Many different "kinds". Most relevant for this class
  - BIBO (bounded-input-bounded-output stability)

- $x_e$ is an _equilibrium point_ for $\dot{x} = f(x)$ if $f(x_e) = 0$ (Note that for linear ODE the origin is an equilibrium point)
- An equilibrium point $x_e$ is Lyapunov stable if:

$$
\forall \varepsilon > 0, \exists\delta>0: ||x_0 - x_e|| < \delta \rightarrow
||x(t, x_0) - x_e|| < \varepsilon, \forall t \ge 0
$$

- If my system is Lyapunov stable and I draw a circle of radius $\varepsilon$ around the equilibrium point, my system will remain bounded inside the circle and probably converge in the $x_e$ point
- An equilibrium point $x_e$ is asymptotically stable if
  - Is Lyapunov stable
  - $x(t, x_0) \rightarrow x_e$, as $t \rightarrow \infty$ 
- There's a difference between **local** and **global** validity  of the above notions

## Lyapunov Stability Analysis

_Book (4.4)_

- Let $x \in \mathbb{R}^n$. A function $V(x)$ is called **positive (semi)definite** in $\mathbb{R}^n$ if $V(x) > 0\ (V(x) \ge 0)$ for all $x \in \mathbb{R}^n$ with $x \ne 0$ and $V(0) = 0$
- Special case: $V(x) := x^TPx$, where $P=P^T \in \mathbb{R}^{n \times n}$ ($P$ is symmetric). Then $V > 0 \iff P > 0$ (pos. def.) $\iff$ all eigenvalues $\lambda_i(P) > 0$ 
- Look at the level sets for a positive definite function

$$
V(x) = \text{constant}
$$

- The vectors defined by $\nabla V(x)$ are orthogonal to the level sets. Proof: pick a curve $c(t)$ such that

$$
\begin{aligned}
V(c(t)) &= \text{constant} \iff \\
\frac{d}{dt}(V(c(t))) &= 0 \iff \\
\left.\frac{\partial V(x)}{\partial x}\right|_{x=c(t)} \cdot \frac{dc(t)}{dt} &= 0 \iff \\
\nabla V \cdot \dot{c}(t) = 0
\end{aligned}
$$

- **Lyapunov stability**:
  - Consider system $\dot{x}(t) = f(x(t)),\ x(0) = x_0$.
  - $V(x)$ be scalar function having continuous first derivatives, satisfying:
    1. $V(x)$ is positive definite
    2. $\dot{V}(x) = \frac{d V(x)}{dx} \dot{x}$ is negative definite
  - Then the system is **asymptotically stable**
- $V(x)$ is called **Lyapunov function**
- $V(x)$ can be a measure 

### Lyapunov Stability Analysis of linear systems

Consider system
$$
\dot{x} = Ax
$$
and a function
$$
V(x) = x^T Px
$$
Derivative:
$$
\begin{aligned}
\dot{V}(x) &= \dot{x}^T Px + x^TP\dot{x} \\
&= x^TA^TPx + x^TPAx \\
&= x^T(A^TP + PA)x
\end{aligned}
$$
For Lyapunov stability there must hold:
$$
A^TP + PA < 0
$$
If $A^TP + PA < 0$ the function $V(x)$ is a Lyapunov function

### Lyapunov Stability Analysis of non-linear systems

> ***
>
> **EXAMPLE**: regular pendulum with damping
> $$
> ml^2 \ddot{\theta} + k\dot{\theta} + mgl \sin\theta = 0 \quad \text{pick} x= 
> \begin{bmatrix}
> \theta \\ \dot{\theta}
> \end{bmatrix}
> $$
>
> - Select $V(x)$ the sum of kinetic energy
>
> $$
> V(x) = mgl(1 - \cos\theta) + \frac{1}{2}ml^2\dot{\theta}^2
> $$
>
> 
>
> - Compute time derivative of $V(x)$ along trajectory
> - Observe that:
>   - $V(x) > 0,\ V(0) = 0$
>   - $\dot{V}(x) < 0 \implies$ the system is asymptotically stable 
> - Consider now the case with no damping, $k=0 \implies$ the system is **not** stable
>
> ***

