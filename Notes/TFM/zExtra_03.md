# Precedence constraints pessimism

## The problem

When using precedence constraints and we are evaluating a low priority task $J_i$, we use $t_{high}$ to compute the time at which a high priority task can start. This works well for tasks without precedence constraints however, when such tasks exist as it can be possible that $J_i$ cannot start as the high priority task can start as soon as its predecessor finish. This is not contemplated in the current formulation.

Let's visualise this with an example. Let's suppose that we have the following system:

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ |
| ----- | ------------ | ------------ | ----- | ----- |
| $J_0$ | 15           | 25           | 1     | 0     |
| $J_1$ | 20           | 30           | 3     | 1     |
| $J_2$ | 10           | 10           | 1     | 2     |

![Example system scenario][precedence_single]

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

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$ |
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

Once we have $\mathcal{S}(v, J_i)$ we can compute the number of cores that are not taken by high-priority jobs with segments and thus are "free", let's call it $m^F$
$$
m^F = m - \sum_{J_k \in \mathcal{S}(v, J_i)} m_k^{\min}
$$

### New free availability

This will be the availability of the "free" cores.

## Examples

Examples to test the model that we are building

### Single precedence global

In this case the high-priority segment only has one precedence constraint

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$            |
| ----- | ------------ | ------------ | ----- | ----- | ---------------------- |
| $J_0$ | 15           | 25           | 1     | 0     | $\emptyset$            |
| $J_1$ | 20           | 30           | 3     | 0     | $\emptyset$            |
| $J_2$ | 10           | 10           | 1     | 1     | $\emptyset$            |
| $J_3$ | 10           | 10           | 1     | 0     | $\{J_0\}$ or $\{J_1\}$ |

We thus have the following state and we are wondering whether $J_2$ will be scheduled next or not: 

![System state before scheduling $J_2$][precedence_single]

- **Option A**: If $prec(J_3) = \{J_0\}$:
  - $EST_2^1 = 20$ and $LST_2^1 = 24$
- **Option B**: If $prec(J_3) = \{J_1\}$
  - $EST_2^1 = 15$ and $LST_2^1 = 25$

Which would produce the following options:

![System state with possible $J_2$ $EST_2^1$ and $LST_2^1$ for options A and B][precedence_single_AB]

**Extracted rule 1:** A segment $J_k$ with higher-priority than $J_i$ that can start as soon as its predecessor finishes acts as if $J_k$ reserves the core.

### Single precedence constraint gang

In this example the high-priority segment only has one precedence constraint but it needs 3 cores

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$            |
| ----- | ------------ | ------------ | ----- | ----- | ---------------------- |
| $J_0$ | 15           | 25           | 1     | 0     | $\emptyset$            |
| $J_1$ | 20           | 30           | 3     | 0     | $\emptyset$            |
| $J_2$ | 10           | 10           | 1     | 1     | $\emptyset$            |
| $J_3$ | 10           | 10           | 3     | 0     | $\{J_0\}$ or $\{J_1\}$ |

We continue to have the same initial state and we are wondering how can $J_2$ be scheduled next:

![System state before scheduling $J_2$][precedence_single]

In this case with the two options we obtain:

- **Option A**: If $prec(J_3) = \{J_0\}$:
  - $EST_2^1 = 15$ and $LST_2^1 = 25$ since $J_3$ could still be waiting for the necessary cores to run
- **Option B**: If $prec(J_3) = \{J_1\}$
  - $EST_2^1 = 15$ and $LST_2^1 = 25$

![Possible scheduling times of $J_2$ for options A and B][precedence_single_AB_gang]

**Extracted rule 2**: If a segment $J_k$ with higher-priority than $J_i$ requires more cores than $J_i$ (so $m_i^{\min} < m_k^{\min}$) then $J_i$ can possibly execute while $J_k$ is waiting for the cores

### Single precedence constraint global but lower job is gang

This example is very similar to the previous one but with the difference that the lower-priority job is a gang job while the high-priority segment is a single thread job.

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$            |
| ----- | ------------ | ------------ | ----- | ----- | ---------------------- |
| $J_0$ | 15           | 25           | 1     | 0     | $\emptyset$            |
| $J_1$ | 20           | 30           | 3     | 0     | $\emptyset$            |
| $J_2$ | 10           | 10           | 3     | 1     | $\emptyset$            |
| $J_3$ | 10           | 10           | 1     | 0     | $\{J_0\}$ or $\{J_1\}$ |



![System state before scheduling $J_2$][precedence_single]

- **Option A**: If $prec(J_3) = \{J_0\}$:
  - $EST_2^1 = 20$ and $LST_2^1 = 24$ since $J_3$ could still be waiting for its precedence to finish
- **Option B**: If $prec(J_3) = \{J_1\}$
  - $EST_2^1 = 25$ and $LST_2^1 = 24$ and thus scheduling is not possible

![Possible scheduling times of $J_2$ for options A and B][precedence_single_AB_lower_gang]

**Extracted rule 3**: If a segment $J_k$ with higher-priority than $J_i$ requires less cores than $J_i$ (so $m_i^{\min} > m_k^{\min}$) then $J_k$ will be able to "steal cores from the system".

### Single precedence constraint gang and lower job is gang

This example is very similar to the previous one but with the difference that both the lower and higher priority jobs are gang tasks. In this case $m=2$

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$            |
| ----- | ------------ | ------------ | ----- | ----- | ---------------------- |
| $J_0$ | 15           | 25           | 1     | 0     | $\emptyset$            |
| $J_1$ | 20           | 30           | 1     | 0     | $\emptyset$            |
| $J_2$ | 10           | 10           | 2     | 1     | $\emptyset$            |
| $J_3$ | 10           | 10           | 2     | 0     | $\{J_0\}$ or $\{J_1\}$ |



![System state before scheduling $J_2$][precedence_single_gang_gang]

- **Option A**: If $prec(J_3) = \{J_0\}$:
  - $EST_2^1 = 30$ and $LST_2^1 = 29$ and thus scheduling is not possible
- **Option B**: If $prec(J_3) = \{J_1\}$
  - $EST_2^1 = 30$ and $LST_2^1 = 29$ and thus scheduling is not possible

### Multiple precedence constraints global

In this example the high-priority segment has more than one precedence constraint but it only needs 1 core. In this case $m = 2$.

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$     |
| ----- | ------------ | ------------ | ----- | ----- | --------------- |
| $J_0$ | 10           | 20           | 1     | 0     | $\emptyset$     |
| $J_1$ | 10           | 20           | 1     | 0     | $\emptyset$     |
| $J_2$ | 10           | 10           | 1     | 1     | $\emptyset$     |
| $J_3$ | 10           | 10           | 1     | 0     | $\{J_0 , J_1\}$ |

![System state before scheduling $J_2$][precedence_multi]

In this case $J_3$ has to wait for both its parents to finish execution so $J_2$ can be scheduled with:

- $EST_2^1 = 10$
- $LST_2^1 = 19$

![Possible scheduling times of $J_2$][precedence_multi_job]

**Extracted rule** 4: When trying to schedule a lower-priority job $J_i$. If there are multiple precedence constraints waiting at the same time only the smallest $m_j$ for all the certainly running predecessors of a ready successor.

### Multiple precedence constraints gang

In this example the high-priority segment has more than one precedence constraint but it only needs 1 core. In this case $m = 4$.

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$                 | $P_i$ | $prec(J_i)$     |
| ----- | ------------ | ------------ | --------------------- | ----- | --------------- |
| $J_0$ | 10           | 20           | 1                     | 0     | $\emptyset$     |
| $J_1$ | 15           | 25           | 1                     | 0     | $\emptyset$     |
| $J_2$ | 20           | 25           | 2                     | 0     | $\emptyset$     |
| $J_3$ | 10           | 10           | 1 (A), 2 (B) or 3 (C) | 1     | $\emptyset$     |
| $J_4$ | 10           | 10           | 2                     | 0     | $\{J_0 , J_1\}$ |

![System state before scheduling $J_2$][precedence_multi_gang]

In this case there are three different scenarios depending in the number of cores that $J_3$ is assigned. Also, $J_4$ has to wait for both its parents to finish execution. So:

- **Option A**: $m_3 = 1$:
  - $EST_2^1 = 10$
  - $LST_2^1 = 19$
- **Option B**: $m_3 = 2$:
  - $EST_2^1 = 20$
  - $LST_2^1 = 24$
- **Option C**: $m_3 = 3$
  - $EST_2^1 = 20$
  - $LST_2^1 = 24$

![Possible scheduling times of $J_2$][precedence_multi_gang_job]

[precedence_single]: images/extra_03/precedence_single.png "Example single core" {width=70%}

[precedence_single_AB]: images/extra_03/precedence_single_AB.png "Example single core" {width=70%}

[precedence_single_AB_gang]: images/extra_03/precedence_single_AB_gang.png "Example single core" {width=70%}

[precedence_single_AB_lower_gang]: images/extra_03/precedence_single_AB_lower_gang.png "Example single core" {width=70%}

[precedence_single_gang_gang]: images/extra_03/precedence_single_gang_gang.png "Example single core" {width=70%}

[precedence_multi]: images/extra_03/precedence_multi.png "Example multiple precedence constraints" {width=70%}

[precedence_multi_job]: images/extra_03/precedence_multi_job.png "Example multiple precedence constraints" {width=70%}

[precedence_multi_gang]: images/extra_03/precedence_multi_gang.png "Example multiple precedence constraints" {width=70%}

[precedence_multi_gang_job]: images/extra_03/precedence_multi_gang_job.png "Example multiple precedence constraints" {width=70%}