# Precedence constraints pessimism

## The problem

When using precedence constraints and we are evaluating a low priority task $J_i$, we use $t_{high}$ to compute the time at which a high priority job can start. This works well for jobs without precedence constraints however, when such jobs exist as it can be possible that $J_i$ cannot start as a high priority segment could always start as soon as its predecessor finishes. The current formulation provides a pessimist answer to this problem.

Let's visualise this with an example. Let's suppose that we have the following system:

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ |
| ----- | ------------ | ------------ | ----- | ----- |
| $J_0$ | 15           | 25           | 1     | 0     |
| $J_1$ | 20           | 30           | 3     | 0     |
| $J_2$ | 10           | 10           | 1     | 1     |

![Example system scenario](images/extra_03/precedence_single.png){width=70%}

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

## Examples of expected results

Some examples are shown with the expected values that we would like to have when using precedence constraints. The new version of the model should provide the same response as the created examples. 

The job in **bold** is the next one that we are trying to see if it can be scheduled. Note that in the figures the orange blocks represent possible start time intervals given the current scenario, they don't mean execution times.

### Single precedence global

In this case the high-priority segment only has one precedence constraint

- | $J_i$              | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$            |
  | ------------------ | ------------ | ------------ | ----- | ----- | ---------------------- |
  | $J_0$              | 15           | 25           | 1     | 0     | $\emptyset$            |
  | $J_1$              | 20           | 30           | 3     | 0     | $\emptyset$            |
  | $\boldsymbol{J_2}$ | 10           | 10           | 1     | 1     | $\emptyset$            |
  | $J_3$              | 10           | 10           | 1     | 0     | $\{J_0\}$ or $\{J_1\}$ |


- We thus have the following state and we are wondering whether $\boldsymbol{J_2}$ will be scheduled next or not: 


![System state before scheduling $J_2$](images/extra_03/precedence_single.png){width=70%}

- **Option A**: If $prec(J_3) = \{J_0\}$:
  - $EST_2^1 = 20$ and $LST_2^1 = 24$
- **Option B**: If $prec(J_3) = \{J_1\}$
  - $EST_2^1 = 15$ and $LST_2^1 = 25$

Which would produce the following options:

![System state with possible $J_2$ $EST_2^1$ and $LST_2^1$ for options A and B](images/extra_03/precedence_single_job.png){width=70%}

### Single precedence constraint gang

In this example the high-priority segment only has one precedence constraint but it needs 3 cores

| $J_i$              | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$            |
| ------------------ | ------------ | ------------ | ----- | ----- | ---------------------- |
| $J_0$              | 15           | 25           | 1     | 0     | $\emptyset$            |
| $J_1$              | 20           | 30           | 3     | 0     | $\emptyset$            |
| $\boldsymbol{J_2}$ | 10           | 10           | 1     | 1     | $\emptyset$            |
| $J_3$              | 10           | 10           | 3     | 0     | $\{J_0\}$ or $\{J_1\}$ |

- We continue to have the same initial state and we are wondering how can $\boldsymbol{J_2}$ be scheduled next:


![System state before scheduling $J_2$](images/extra_03/precedence_single.png){width=70%}

In this case with the two options we obtain:

- **Option A**: If $prec(J_3) = \{J_0\}$:
  - $EST_2^1 = 15$ and $LST_2^1 = 25$ since $J_3$ could still be waiting for the necessary cores to run
- **Option B**: If $prec(J_3) = \{J_1\}$
  - $EST_2^1 = 15$ and $LST_2^1 = 25$

![Possible scheduling times of $J_2$ for options A and B](images/extra_03/precedence_single_gang_job.png){width=70%}

### Single precedence constraint global but lower job is gang

This example is very similar to the previous one but with the difference that the lower-priority job is a gang job while the high-priority segment is a single thread job.

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$            |
| ----- | ------------ | ------------ | ----- | ----- | ---------------------- |
| $J_0$ | 15           | 25           | 1     | 0     | $\emptyset$            |
| $J_1$ | 20           | 30           | 3     | 0     | $\emptyset$            |
| $J_2$ | 10           | 10           | 3     | 1     | $\emptyset$            |
| $J_3$ | 10           | 10           | 1     | 0     | $\{J_0\}$ or $\{J_1\}$ |



![System state before scheduling $J_2$](images/extra_03/precedence_single.png){width=70%}

- **Option A**: If $prec(J_3) = \{J_0\}$:
  - $EST_2^1 = 20$ and $LST_2^1 = 24$ since $J_3$ could still be waiting for its precedence to finish
- **Option B**: If $prec(J_3) = \{J_1\}$
  - $EST_2^1 = 25$ and $LST_2^1 = 24$ and thus scheduling is not possible

![Possible scheduling times of $J_2$ for options A and B](images/extra_03/precedence_single_lower_gang_job.png){width=70%}

### Single precedence constraint gang and lower job is gang

This example is very similar to the previous one but with the difference that both the lower and higher priority jobs are gang tasks. In this case $m=2$

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$            |
| ----- | ------------ | ------------ | ----- | ----- | ---------------------- |
| $J_0$ | 15           | 25           | 1     | 0     | $\emptyset$            |
| $J_1$ | 20           | 30           | 1     | 0     | $\emptyset$            |
| $J_2$ | 10           | 10           | 2     | 1     | $\emptyset$            |
| $J_3$ | 10           | 10           | 2     | 0     | $\{J_0\}$ or $\{J_1\}$ |



![System state before scheduling $J_2$](images/extra_03/precedence_single_gang_gang.png){width=70%}

- **Option A**: If $prec(J_3) = \{J_0\}$:
  - $EST_2^1 = 30$ and $LST_2^1 = 29$ and thus scheduling is not possible
- **Option B**: If $prec(J_3) = \{J_1\}$
  - $EST_2^1 = 30$ and $LST_2^1 = 29$ and thus scheduling is not possible

![Possible scheduling times of $J_2$ for options A and B](images/extra_03/precedence_single_gang_gang_job.png){width=70%}

### Multiple precedence constraints global

In this example the high-priority segment has more than one precedence constraint but it only needs 1 core. In this case $m = 2$.

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$     |
| ----- | ------------ | ------------ | ----- | ----- | --------------- |
| $J_0$ | 10           | 20           | 1     | 0     | $\emptyset$     |
| $J_1$ | 10           | 20           | 1     | 0     | $\emptyset$     |
| $J_2$ | 10           | 10           | 1     | 1     | $\emptyset$     |
| $J_3$ | 10           | 10           | 1     | 0     | $\{J_0 , J_1\}$ |

![System state before scheduling $J_2$](images/extra_03/precedence_multi.png){width=70%}

In this case $J_3$ has to wait for both its parents to finish execution so $J_2$ can be scheduled with:

- $EST_2^1 = 10$
- $LST_2^1 = 19$

![Possible scheduling times of $J_2$](images/extra_03/precedence_multi_job.png){width=70%}

### Multiple precedence constraints gang

In this example the high-priority segment has more than one precedence constraint but it only needs 1 core. In this case $m = 4$.

| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$                 | $P_i$ | $prec(J_i)$     |
| ----- | ------------ | ------------ | --------------------- | ----- | --------------- |
| $J_0$ | 10           | 20           | 1                     | 0     | $\emptyset$     |
| $J_1$ | 15           | 25           | 1                     | 0     | $\emptyset$     |
| $J_2$ | 20           | 25           | 2                     | 0     | $\emptyset$     |
| $J_3$ | 10           | 10           | 1 (A), 2 (B) or 3 (C) | 1     | $\emptyset$     |
| $J_4$ | 10           | 10           | 2                     | 0     | $\{J_0 , J_1\}$ |

![System state before scheduling $J_2$](images/extra_03/precedence_multi_gang.png){width=70%}

In this case there are three different scenarios depending in the number of cores that $J_3$ is assigned. Also, $J_4$ has to wait for both its parents to finish execution. So:

- **Option A**: $m_3 = 1$:
  - $EST_2^1 = 10$
  - $LST_2^1 = 20$
- **Option B**: $m_3 = 2$:
  - $EST_2^1 = 20$
  - $LST_2^1 = 24$
- **Option C**: $m_3 = 3$
  - $EST_2^1 = 20$
  - $LST_2^1 = 24$

![Possible scheduling times of $J_2$](images/extra_03/precedence_multi_gang_job.png){width=70%}

## The solution

### Rules found

For a job $J_i$ if there is a segment with higher priority $J_k$ with predecessors $J_j$ (so $pred(J_k) = \{J_{j,1}, J_{j,2}, ...\}$):

- We have to look at the cores that will always be "taken" by $J_k$ and set $A^{\min}$ to the value of $A^{\max}$ for those cores **only when computing** $EST_{\boldsymbol{i}}^p(v)$
- One or more cores will be always "taken" by $J_k$ if:
  - $m_i^{\min} \ge m_k^{\min}$
  - and $p_i < p_k$
  - and scheduling of $J_i$ would use all the cores currently in use by $pred(J_k) \cap \mathcal{X}(v)$ in a first instance

### New availability

To solve the issue a new availability **only used to compute** $EST_i^p(v)$ is created. In this availability all the $A^{\min}$ values matching the $EFT_j(v)$ for all $J_j \in pred(J_k) \cap \mathcal{X}(v)$  such that $J_k$ that matches the previous conditions, are increased until not all the $EFT_j(v)$ are required.

### Example



| $J_i$ | $C_i^{\min}$ | $C_i^{\max}$ | $m_i$ | $P_i$ | $prec(J_i)$     |
| ----- | ------------ | ------------ | ----- | ----- | --------------- |
| $J_0$ | 5            | 20           | 1     | 0     | $\emptyset$     |
| $J_1$ | 10           | 25           | 1     | 0     | $\emptyset$     |
| $J_2$ | 15           | 30           | 1     | 0     | $\emptyset$     |
| $J_3$ | 20           | 35           | 1     | 0     | $\emptyset$     |
| $J_4$ | 10           | 10           | 2     | 0     | $\{J_0 , J_1\}$ |
| $J_5$ | 10           | 10           | 2     | 1     | $\emptyset$     |