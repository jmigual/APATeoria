# Precedence constraints pessimism

## The problem

When using precedence constraints and we are evaluating a low priority task $J_i$, we use $t_{high}$ to compute the time at which a high priority task can start. This works well for tasks without precedence constraints however, when such tasks exist as it can be possible that $J_i$ cannot start as the high priority task can start as soon as its predecessor finish. This is not contemplated in the current formulation.

Let's visualize this with an example. Let's suppose that we have the following system:

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $s_i$ | $P_i$ |
| ----- | ------------ | ------------ | ----- | ----- |
| $J_0$ | 15           | 25           | 1     | 0     |
| $J_1$ | 20           | 30           | 3     | 1     |
| $J_2$ | 10           | 10           | 1     | 2     |

![Precedences example image](images/extra_03/precedence-JLFP.png){width=50%}

## The solution

### Set of 