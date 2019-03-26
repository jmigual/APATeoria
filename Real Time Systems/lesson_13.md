# Lesson 13 - Jitter analysis

What do we call Jitter?

A variation in the system. If you don't know where the variation is coming from we call it random.

## Motivation
- Multi-processor analysis
- **Finalization**: variation in finalization times
- **Activation**: variation in activation times
- When there's some dependence between two tasks

**Example**: multimedia in a networked environment

**Example multiprocessor**:
1. A strictly periodic system event activates task $\tau_1$
2. Task $\tau_1$ sends message $\mu_j$
   - $FJ_j$ causes $AJ_j$
3. Message $\mu_j$ triggers task $\tau_k$
   - $FJ_j$ causes $AJ_k$
4. Task $\tau_k$ generates a system response

### Goal jitter analysis
- Determine schedulability in the context of jitter
- Determine end-to-end response times

## Motivation for Fixed Priority Preemptive Scheduling (FPPS)

- De-facto standard
- Supported by commercial RTOS
- ...


**EXAMPLE**
Task | Period $T$ | computation time $C$ | Utilization $U$
-|-|-|-
$\tau_1$ | 10 | 3 | 0.3
$\tau_2$ | 19 | 11 | 0.58
$\tau_3$ | 56 | 5 | 0.09

- RM priority assignment, with $WD_i = T_i$ and $BD_i = 0$
- Schedulable?
$$
\sum U_i = 0.97 \le 1
$$

$$
HB(n) = \prod_i (U_i + 1) \le 2
$$

$$
HB(3) = 2.05
$$

Therefore $HB(3)$ does not hold

It can be seen that this task is feasible but just exactly.

---

## Response times

**EXAMPLE**: airbag
- If the airbag releases too soon or too early it can be fatal
---

- Schedulability condition:
  - all jobs of all tasks must meet their deadline constraints

$$
\forall_{i, k, \varphi} BD_i \le R_{i,k}(\varphi) \le WD_i
$$


## Worst-case response times of FPPS

_Book chapter 4_

Recursive equation for task $\tau_i$:
$$
\begin{aligned}
WR_i^{(0)} &= C_i \\
WR_i^{(0)} &= WR_{i - 1} \longrightarrow \text{Optimization} \\
WR_i^{(n)} &= C_i + \sum_{j < i} \left\lceil \frac{WR_i^{(n-1)}}{T_j} \right\rceil \cdot C_j
\end{aligned}
$$

- Intuition
  - LHS: amount of time available
  - RHS: max amount of time requested
- Observation
  - Best-case and worst-case notions are duals

## Best-case response times of FPPS

- Formalization
  - Best-case response time $BR_i$ of a periodic task $\tau_i$, where $\varphi$ is the phasing of the task set

$$
BR_i \equiv \inf_{\varphi, k} R_{i, k}(\varphi)
$$

 - Hence:

$$
\forall_{i, k, \varphi} BR_i \le R_{i, k}(\varphi)
$$

### Introduction
- Optimal instant of task $\tau_i : \tau_i$ "assumes" its $BR_i$
  - Incurs the lowest amount of preemption by higher priority tasks

$$
\begin{aligned}
    BR_i^{(0)} &= WR_i \\
    BR_i^{(l + 1)} &= C_i + \sum_{j < i} \left( \left\lceil \frac{BR_i^{(l)}}{T_j} \right\rceil - 1 \right) \cdot C_j
\end{aligned}
$$
