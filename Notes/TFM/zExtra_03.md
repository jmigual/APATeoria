# Precedence constraints pessimism

## The problem

When using precedence constraints and we are evaluating a low priority task $J_i$, we use $t_{high}$ to compute the time at which a high priority task can start. This works well for tasks without precedence constraints however, when such tasks exist as it can be possible that $J_i$ cannot start as the high priority task can start as soon as its predecessor finish. This is not contemplated in the current formulation.

Let's visualize this with an example. Let's suppose that we have the following system:

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $s_i$ | $P_i$ |
| ----- | ------------ | ------------ | ----- | ----- |
| $J_0$ | 15           | 25           | 1     | 0     |
| $J_1$ | 20           | 30           | 3     | 1     |
| $J_2$ | 10           | 10           | 1     | 2     |

![Precedences example image][precedence_single]

With this state we have three options:

- **Option A**: Both $J_0$ and $J_1$ have successors. In this case $J_2$ will never be able to execute. 
  - However using the current formulation we have
    - $EST_2^1 (v) = 15$
    - $LST_2^1(v) = \min\{t_{wc}, t_{avail}, t_{high} - 1\} = \min\{25, 24, +\infty\} = 24$
  - While we should not have this scenario
- **Option B**: Only $J_0$ has a successor. In this case $J_2$ should only be able to start after $J_1$ completes as it does not have a successor. 
  - However using the current formulation we have:
    - $EST_2^1(v) = 15$
    - $LST_2^1(v) = \min\{t_{wc}, t_{avail}, t_{high} - 1\} = \min\{25, 24, +\infty\} = 24$
  - While we should have:
    - $EST_2^1(v) = 20$
    - $LST_2^1(v) = 24$
- **Option C**: Only $J_1$ has a successor. In this case $J_2$ should be able to start as soon as $J_0$ completes as it does not have a successor. We can see that here the formulation matches what we expect:
  - $EST_2^1(v) = 15$
  - $LST_2^1(v) = \min\{t_{wc}, t_{avail}, t_{high} - 1\} = \min\{25, 29, +\infty\}$

## The solution

Now that we have identified the problem we will attempt to fix it in a way that it also works for gang scheduling (as this is the focus of our work). Let's extend the previous example with gang scheduling.

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $s_i$ | $P_i$ | $prec(J_i)$ |
| ----- | ------------ | ------------ | ----- | ----- | ----------- |
| $J_0$ | 15           | 25           | 1     | 0     | $\emptyset$ |
| $J_1$ | 20           | 30           | 3     | 1     | $\emptyset$ |
| $J_2$ | 10           | 20           | 1     | 2     | $\emptyset$ |
| $J_3$ | 10           | 20           | 2     | 0     | $\{ J_0\}$  |

Now in this case there is a job with a higher priority than $J_2$  however, this job now requires 2 cores so it cannot immediately start executing.

### Set of segments that have a higher priority and that can always start before $J_i$

The idea of this set is to search for all the higher-priority segments that can always start before $J_i$ and thus "steal" the processors. It can be defined as follows:
$$
\mathcal{S}(v, J_i) = \Big\{ J_k | \underbrace{(\exists J_j | J_k \in succ(J_j) \land J_j \in \mathcal{X}(v))}_{\substack{\text{is successor of a} \\ \text{certainly running job}}} \land \underbrace{J_k \in hp_i}_{\substack{\text{has higher} \\ \text{priority}}}  \land \underbrace{t_{pred}(J_k) \le A_{m_k^{\min}}^{\min}(v)}_{\text{is ready}} \land \underbrace{A^{\min}_{m_k^{\min}} \le A^{\min}_{m_i^{\min}}}_{\substack{\text{enough cores available} \\ \text{to execute segment}}}\Big\}
$$
Where $t_{pred}(v, J_i)$ represents the earliest time at which we certainly know that a job will only wait for 1 predecessor. It can be computed as follows:
$$
t_{pred}(J_i) = \max\{ EFT_j, \{LFT_k | J_k \in pred(J_i) \setminus \{J_j\}\} \} \text{ where } \underbrace{J_j = J_k : LFT_k = \max_{J_k \in pred(J_i)}\{LFT_k\}\}}_{\text{job with largest LFT}}
$$

### Free cores for low-priority job

Once we have $\mathcal{S}(v, J_i)$ we can compute the number of cores that are not taken by high-priority jobs with segments and thus are "free" $m^F$
$$
m^F = m - \sum_{J_k \in \mathcal{S}(v, J_i)} m_k^{\min}
$$

### New free availability

This will be the availability of the "free" cores.

## Examples

Examples to test the model that we are building

### Single precedence single core

In this case the high-priority segment only has one precedence constraint

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $s_i$ | $P_i$ | $prec(J_i)$            |
| ----- | ------------ | ------------ | ----- | ----- | ---------------------- |
| $J_0$ | 15           | 25           | 1     | 0     | $\emptyset$            |
| $J_1$ | 20           | 30           | 3     | 0     | $\emptyset$            |
| $J_2$ | 10           | 10           | 1     | 1     | $\emptyset$            |
| $J_3$ | 10           | 10           | 1     | 0     | $\{J_0\}$ or $\{J_1\}$ |

We thus have the following state and we are wondering whether $J_2$ will be scheduled next or not: 

![Precedences example image][precedence_single]

- **Option A**: If $prec(J_3) = \{J_0\}$:
  - $EST_2^1 = 20$ and $LST_2^1 = 24$
- **Option B**: If $prec(J_3) = \{J_1\}$
  - $EST_2^1 = 15$ and $LST_2^1 = 25$

Which would produce the following options:
![Precedences example image][precedence_single_AB]




[precedence_single_AB]: images/extra_03/precedence_single_AB.png "Example single core" {width=70%}
[precedence_single]: images/extra_03/precedence_single_AB.png "Example single core" {width=70%}