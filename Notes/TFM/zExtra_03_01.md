# Reducing precedence constraints pessimism

## Problem

When considering the execution of a low-priority job $J_i$, the current formulation does not consider the case where a higher-priority job $J_k$ is waiting for its predecessors ($J_j$) jobs to finish their execution. This allows $J_i$ to be scheduled before $J_k$. While this scenario may be possible, there's a case where $J_i$ ends up replacing $J_k$'s valid execution. This happens when we are **certain** that at dispatch time $t$, job $J_i$ will use the cores just freed by the completion of $J_j$. If $J_j$ just finished this means that $J_k$ would have been scheduled first instead of $J_i$. 

The solution to this problem is to find a lower bound $t_{pred}$ such that if $J_i$ starts at this time we are not certain that $J_k$ may have started. The explanation that follows is how to find such lower bound.

## Original formulation

$$
R_i^{\min} = \max\big\{r_i^{\min}, \max^{0}\{EFT_x^*(v) | J_x \in pred(J_i)\}\big\}
$$

$$
R_i^{\max} = \max\big\{r_i^{\max}, \max^0 \{LFT_x^*(v) | J_x \in pred(J_i)\}\big\}
$$

$$
\mathcal{R}(v) = \{ J_i, | J_i \in \mathcal{J} \setminus \mathcal{S}(v) \land pred(J_i) \subseteq \mathcal{S}(v) \}
$$

#### Earliest Start Time


$$
EST^p_i = \max\{R_i^{\min}(v), t_{gang}(v)\}
$$

$$
t^p_{gang}(v) = \begin{cases}
A_p^{\min}(v) & \text{if } p = m_i^{\max} \\
A_p^{exact}(v) & \text{otherwise}
\end{cases}
$$

#### Latest Start Time

$$
LST_i^p = \min\{t^p_{avail}(v), t_{wc}(v), t_{high}(v) - 1\}
$$

$$
t^p_{avail}(v) = \begin{cases}
A_{p+1}^{\max}(v) - 1 & \text{if } p < m_i^{\max} \\
+\infty & \text{otherwise}
\end{cases}
$$

$$
t_{wc}(v) = \min_{J_j \in \mathcal{R}(v)}\{\max\{R_j^{\max}(v), A_{m_j^{\min}}^{\max}\}\}
$$

$$
t^p_{high}(v) = \min^{\infty}_{J_j \in \{\operatorname{hp}_i \cap \mathcal{R}(v)\}} \Big\{\max\big\{t_h^p(J_i, J_j), \max^0\{LFT_y^*(v) | J_y \in pred(J_i) \setminus pred(J_j)\}\big\}\Big\}
$$

$$
t^p_h(J_i, J_j) = \begin{cases}
r_j^{\max} & \text{if } m_j^{\min} \le p \\
\max\{r_j^{\max}, A_{m_j^{\min}}^{\max}\} & \text{otherwise}
\end{cases}
$$

## The solution

> We have to find the earliest time such that $J_i$ can be scheduled without replacing a valid execution of a higher-priority job that was waiting for a predecessor to finish and that we are certain that the higher-priority job could execute if $J_i$ could also execute.

Even if $J_i$ could start, higher-priority jobs may be scheduled before it. If these higher-priority jobs have precedence constraints, we have to look for the time $t_{pred}$ at which $J_i$ can start but these higher-priority jobs may not.

First, we define the certainly running predecessors of a job $J_x$, for state $v$ as:
$$
\mathcal{X}_x^{pred}(v) = \Big\{pred(J_x) \cap \mathcal{X}(v)\Big\}
$$
**Proof**: by definition of $pred(J_x)$, these are the predecessors of $J_x$, and then, by definition of $\mathcal{X}(v)$, these are certainly running jobs at state $v$. Thus the intersection are certainly running jobs that are predecessors of $J_x$ and proving our claim.

Then, at time $t$ and state $v$, higher-priority jobs with precedence constraints that can certainly start if $J_i$ does are defined as follows:
$$
\mathcal{Q}_i(v, t)= \bigg\{J_k \bigg| \underbrace{\mathcal{X}_k^{pred} \ne \emptyset}_{\substack{\text{Have a certainly} \\ \text{running predecessor}}} \land \underbrace{\Big(t \ge \max\left\{r_k^{\max}, A_{m_k^{\min}}^{\min}\right\}\Big)}_{\text{$J_k$ can start at time $t$}}\land J_k \in \operatorname{hp}_i\bigg\}
$$
**Proof**: Since these jobs have to meet three conditions we will prove them separately:

- $\Big\{pred(J_k) \cap \mathcal{X}(v)\Big\} \ne \emptyset$, by definition of $pred(J_x)$, these are the predecessors of $J_k$ and we only take the ones that are certainly running at state $v$, by definition of $\mathcal{X}(v)$. Thus this condition is met only if $J_k$ has certainly running predecessor jobs.
- $t \ge \max\left\{r_k^{\max}, A_{m_k^{\min}}^{\min}\right\}$, by rule 2 a job cannot start before begin released (so $t \ge r_k^{\max}$) and cannot start until at least $m_k^{\min}$ cores are available. Thus this condition is met only if $J_k$ can certainly start at time $t$.
- $J_k \in \operatorname{hp}_i$, by definition of $\operatorname{hp}_i$, this condition is only met if $J_k$ has a higher priority than $J_i$.

Thus we prove the claim $\blacksquare$

These are jobs that can certainly start if $J_i$ does but, since they have precedence constraints, these constraints may prevent the job from starting. Now we have to check whether $J_i$ starting means that these constraints have been fulfilled and thus the higher-priority jobs should have been executed. To do so, we check whether at time $t$ there are enough cores to execute without "needing" the cores used by the predecessors of a job in $\mathcal{Q}(v, t)$. 

The number of cores possibly available at time $t$ is defined as follows:
$$
q^{\min}(v, t) = \max_{1 \le q \le m} \{q | A_q^{\min}(v) \ge t\}
$$
Now, a higher-priority job will not certainly start executing if at least one predecessor is still running. Thus, the lower priority job $J_i$ can use the cores freed by other finished predecessors. So, 



During this formulation we are using $J_i$ for the current evaluated job, $J_k$ for the higher-priority segment with a certainly running predecessor (so $\exists J_j | J_j \in \{pred(J_k) \cap \mathcal{X}(v)\}$) and $J_j$ for the certainly running predecessors of $J_k$.

#### The change

We thus change from:
$$
EST_i^p(v) = \max\{R_i, A^{\min}_p\}
$$


To:
$$
EST_i^p(v) = \max\{R_i, A_p^{\min}, t_{hs}\}
$$
Where $t_{hs}$ is the time taken by higher priority segments and is the time at which the possibly always used cores are not all the cores of segments with currently running predecessors. 
$$
t_{hs} = \min_{\forall q | p \le q \le m}^{\infty}\left\{A_q^{\min} \left| \left(q - \sum_{J_k \in \mathcal{S}_i(v)}\min_{J_j \in \mathcal{X}^{pred}_k(v) \land EFT^*_j(v) \le A_q^{\min}} p_j\right) \ge p\right.\right\}
$$

Where:
$$
\mathcal{S}_i(v) = \left\{J_k \left| \mathcal{X}^{pred}_i(v) \ne \emptyset \land p \ge m_k^{\min} \land P_i > P_k \land \left(\sum_{J_j \in \mathcal{X}_k^{pred}(v)}p_j\right) \le p\right.\right\}
$$
Is the set of segments with a certainly running predecessor and higher priority than $J_i$ that use the same or less cores than $J_i$ or that their predecessors use the same or less cores than $J_i$. Where:
$$
\mathcal{X}^{pred}_i(v) = \{pred(J_i) \cap \mathcal{X}(v)\}
$$
Is the set of certainly running predecessors of $J_i$.
$$
\mathcal{Q}_i(v)= \bigg\{J_k \bigg| \underbrace{\Big(\Big\{pred(J_i) \cap \mathcal{X}(v)\Big\} \ne \emptyset\Big)}_{\substack{\text{Have a certainly} \\ \text{running predecessor}}} \land \underbrace{\Big(A_p^{\min} \ge \max\left\{R_k^{\min}, A_{m_k^{\min}}^{\min}\right\}\Big)}_{\text{if } J_i \text{ can start, so does } J_k}\land J_k \in \operatorname{hp}_i\bigg\}
$$


#### Explanation

So let's go step by step:
$$
J_j \in \underbrace{\mathcal{X}^{pred}_k(v)}_{\substack{\text{certainly running} \\ \text{predecessor}}} \land \underbrace{EFT^*_j(v) \le A_q^{\min}}_{\substack{\text{using cores at} \\ \text{time } A_q^{\min}}}
$$
These are the jobs that are certainly running predecessors of $J_k$ so some of the cores currently being used by them could be used by $J_i$. Then:
$$
\min_{J_j \in \mathcal{X}^{pred}_k(v) \land EFT^*_j(v) \le A_q^{\min}} p_j
$$
These are the minimum number of cores used by a certainly running predecessor of predecessor of $J_k$. Then:
$$
q - \sum_{J_k \in \mathcal{S}_i(v)}\min_{J_j \in \mathcal{X}^{pred}_k(v) \land EFT^*_j(v) \le A_q^{\min}} p_j
$$
Is the number of cores that $J_i$ can take without taking all the cores of a predecessor of $J_k$. Then:
$$
\left(q - \sum_{J_k \in \mathcal{S}_i(v)}\min_{J_j \in \mathcal{X}^{pred}_k(v) \land EFT^*_j(v) \le A_q^{\min}} p_j\right) \ge p
$$
Is true only if $J_i$ requires less cores than the ones that are available without "disturbing" a job in $\mathcal{S}(v)$ and finally:
$$
\min_{\forall q | p \le q \le m}^{\infty}\left\{A_q^{\min} \Big| \left(q - \sum_{J_k \in \mathcal{S}_i(v)}\min_{J_j \in \mathcal{X}^{pred}_k(v) \land EFT^*_j(v) \le A_q^{\min}} p_j\right) \ge p\right\}
$$
Is the minimum $A_q^{\min}$ such that job $J_i$ can be scheduled with $p$ cores without "stealing" the cores that belong to "hunter jobs".

#### Proof

We want to proof that a job $J_i$ that has low priority in a system where jobs with precedence constraints and higher priority are running can be scheduled at the earliest at time $t_s \ge t_{hs}$. We are going to prove that by contradiction:

By contradiction, let's assume that job $J_i$ is scheduled at time $t_s < t_{hs}$ with $p$ and that there are other jobs such that $S_i(v)\ne \emptyset$. Here we can have two possibilities: either (a) there are jobs such that $J_j \in \mathcal{X}^{pred}_k(v) \land EFT^*_j(v) \le t_s$ or they aren't (b). 

- If (a), by definition of availability this time can be at the earliest $A_p^{\min}$. This means that if $J_i$ where to be scheduled next it would use all the cores used currently by predecessors of a waiting higher priority job $J_k$ which would mean that the predecessors of $J_k$ had finished they execution. By rules 1 and 4 $J_k$ would be scheduled next instead of $J_i$ which contradicts the assumption that $J_i$ is the next job to be scheduled. Either $t_s \ge t_{hs}$ or there aren't jobs such that $J_j \in \mathcal{X}^{pred}_k(v) \land EFT^*_j(v) \le t_s$. 
- Otherwise if (b), by definition of availability this time can be at earliest $t_s = A_p^{\min}$. Then the equation then is simplified into $\min_{\forall q: p \le q\le m}^{\infty}\left\{A_q^{\min}|q \ge p\right\}$ which means that $t_{hs} = A_q^{\min}$. This contradicts the assumption that $t_s < t_{hs}$. 

#### Comments

With this solution we can actually work with the fact that $EFT_j \ne A_q^{\min}$ for any $q$ which is what we can have when doing merges.

