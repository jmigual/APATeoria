---
geometry: margin=2.5cm
header-includes:
	- \usepackage[linesnumbered]{algorithm2e}
---



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

### Earliest Start Time


$$
EST^p_i = \max\{R_i^{\min}(v), t_{gang}(v)\}
$$

$$
t^p_{gang}(v) = \begin{cases}
A_p^{\min}(v) & \text{if } p = m_i^{\max} \\
A_p^{exact}(v) & \text{otherwise}
\end{cases}
$$

### Latest Start Time

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

A job $J_i$, can start before a higher-priority job $J_k$ if $J_k$ has precedence constraints. However, sometimes if $J_i$ can start, so does $J_k$ as this would mean that the running precedence constraints jobs have just finished. We have to find the time $t_i^{pred}(v)$ at which $J_i$ can start without certainly using cores from all the predecessors of a higher priority job $J_k$.

First, we define the certainly running predecessors of a job $J_x$:
$$
\mathcal{X}_x^{pred}(v) = \Big\{pred(J_x) \cap \mathcal{X}(v)\Big\}
$$
**Proof**: by definition of $pred(J_x)$, these are the predecessors of $J_x$, and then, by definition of $\mathcal{X}(v)$, these are certainly running jobs at state $v$. Thus the intersection are certainly running jobs that are predecessors of $J_x$ and proving our claim.  $\blacksquare$

Usually, a higher-priority job $J_k$ would be always scheduled before $J_i$. However, since $J_k$ has precedence constraints, $J_i$ can start executing before $J_k$ if that execution scenario does not mean that $J_i$ is making use of cores freed by all the predecessors of $J_k$. So, we have to check all possible jobs $J_k$ to see if $J_i$ being dispatched at time $t$ could be a real execution scenario or not. So, the properties of jobs $J_k$ that have to be checked are:

- If $J_i$ can start running, so does $J_k$. This means that $J_k$ has been released, at least $m_k^{\min}$ cores are available and all the predecessors of $J_k$ have been scheduled already.
- $J_k$ has certainly running predecessors.
- $J_k$ has a higher priority than $J_i$.

**Lemma**: The set of jobs to be checked because $J_i$ can use cores from their certainly running predecessors is defined by:
$$
\mathcal{Q}_i(v, t)= \bigg\{J_k \bigg| \underbrace{\Big(t \ge \max\left\{r_k^{\max}, A_{m_k^{\min}}^{\min}\right\}\Big) \land \Big(pred(J_k) \subseteq \mathcal{S}(v)\Big)}_{\text{$J_k$ can start at time $t$}}\land\underbrace{\mathcal{X}_k^{pred}(v) \ne \emptyset}_{\substack{\text{Have a certainly} \\ \text{running predecessor}}} \land  J_k \in \operatorname{hp}_i\bigg\}
$$



**Proof**: Since these jobs have to meet three conditions we will prove them separately:

- $t \ge \max\left\{r_k^{\max}, A_{m_k^{\min}}^{\min}\right\}$, by rule 2 a job cannot start before begin released (so $t \ge r_k^{\max}$) and cannot start until at least $m_k^{\min}$ cores are available. Thus this condition is met only if $J_k$ can possibly start at time $t$.
- $pred(J_k) \subseteq \mathcal{S}(v)$, as defined in the task model, a job cannot start executing until all its predecessors have been scheduled and finished.
- $\mathcal{X}_k^{pred}(v) \ne \emptyset$, by definition of $\mathcal{X}_k^{pred(v)}$, it contains the certainly running predecessors of $J_k$. Thus this condition is met only if $J_k$ has certainly running predecessors.
- $J_k \in \operatorname{hp}_i$, by definition of $\operatorname{hp}_i$, this condition is only met if $J_k$ has a higher priority than $J_i$.

Thus we prove the claim $\blacksquare$

These are jobs that can certainly start if $J_i$ does but, since they have precedence constraints, these constraints may prevent the job from starting. Now we have to check whether $J_i$ starting means that these constraints have been fulfilled and thus the higher-priority jobs should have been executed. To do so, we check whether at time $t$ there are enough cores to execute without "needing" the cores used by the predecessors of a job in $\mathcal{Q}(v, t)$. 

The number of cores possibly available at time $t$ is defined as follows:
$$
q^{\min}(v, t) = \max_{1 \le q \le m} \{q | A_q^{\min}(v) \ge t\}
$$
**Lemma**: $J_i$ will not possibly start executing if, by doing it so, it would certainly use cores from all the certainly running predecessors of a job $J_k \in \mathcal{Q}_i(v, t)$.

**Proof**: By contradiction, let's assume that $J_i$ is scheduled at time $t$ and uses cores from all the certainly running predecessors of $J_k$. As $J_i$ uses cores from all the certainly running predecessors of $J_k$ this means that all the precedence constraints of $J_k$ have been fulfilled. Then, by rule 4, $J_k$ would be scheduled first, instead of $J_i$ at time $t$. This contradicts the assumption that $J_i$ is scheduled at time $t$, and thus proves our claim. $\blacksquare$

Now, in order to check if $J_i$ would use cores from all the certainly running predecessors of a job $J_k$ we know that $J_i$ can use the possibly available cores, $q^{\min}(v, t)$, minus the number of cores that would ensure that $J_i$ is certainly running on cores freed by the predecessors of $J_k$. 

**Lemma**: The minimum number of cores that ensures that $J_i$ is not using cores from all the certainly running predecessors of $J_k$ is defined by:
$$
p_k^{pred} = \min_{J_j \in \mathcal{X}_k^{pred}(v)} p_j
$$
**Corollary 1**: The job with the minimum number of cores is defined by:
$$
J_k^{pred,\min} = \operatorname*{arg\,min}_{J_j \in \mathcal{X}_k^{pred}(v)} p_j
$$
**Corollary 2**: If there's only one higher-priority job $J_k$, then in order for $J_i$ to be scheduled at time $t$ it needs to fulfil the following condition:
$$
q^{\min}(v, t) - p_k^{pred} \ge p
$$


**Proof**: By contradiction, let's assume that $p_k^{pred}$ is not the minimum among all the certainly running predecessors $\mathcal{X}_k^{pred}(v)$. This means that $J_i$ cannot be scheduled with more than $q^{\min}(v, t) - p^{pred}_k$ cores without using cores from all the certainly running predecessors of $J_k$. As we assumed that $p_k^{pred}$ is not the minimum among all the certainly running predecessors, this means that there's a job $J_x$ such that $p_x < p_k^{pred} \land J_x \in \mathcal{X}_k^{pred}$. Now, we can see how we can schedule $J_i$ with $q^{\min}(v, t) - p_x$ cores and still not use the cores from all the predecessors, as the cores from $J_x$ where not used. This contradicts the assumption that $p_k^{pred}$ is not the minimum among all the certainly running predecessors $\mathcal{X}_k^{pred}(v)$ of $J_k \in \mathcal{Q}_i(v, t)$.

**Lemma**: For multiple higher-priority jobs $J_k \in \mathcal{Q}_i(v, t)$. The jobs whose number of cores cannot be used by $J_i$ are defined by:
$$
\mathcal{Q}_i^{pred}(v, t) = \left\{ J_k^{pred,\min} \Bigg| J_k \in \mathcal{Q}_i(v, t) \right\}
$$
Note that it is a set, so there are no repeated jobs

**Corollary**: $J_i$ may be scheduled at time $t$ at the earliest if it matches the following condition:
$$
q^{\min}(v, t) - \sum_{J_j \in \mathcal{Q}_i^{pred}(v, t)} p_j \ge p
$$
**Proof**: By definition of $J_k^{pred,\min}$, this is the job whose number of cores cannot be used by $J_i$, as there are multiple higher-priority jobs in $J_k \in\mathcal{Q}
_i(v, t)$,  each of them has their own $J_k^{pred,\min}$. Thus, $J_i$ cannot use the cores from any of the $J_k^{pred,\min}$.

## Final formulation 

$$
R_i^{\min} = \max\big\{r_i^{\min}, \max^{0}\{EFT_x^*(v) | J_x \in pred(J_i)\}\big\}
$$

$$
R_i^{\max} = \max\big\{r_i^{\max}, \max^0 \{LFT_x^*(v) | J_x \in pred(J_i)\}\big\}
$$

$$
\mathcal{R}(v) = \{ J_i, | J_i \in \mathcal{J} \setminus \mathcal{S}(v) \land pred(J_i) \subseteq \mathcal{S}(v) \}
$$



### Earliest Start Time


$$
EST^p_i = \max\{R_i^{\min}(v), t_{gang}(v), t_i^{pred}\}
$$

$$
t^p_{gang}(v) = \begin{cases}
A_p^{\min}(v) & \text{if } p = m_i^{\max} \\
A_p^{exact}(v) & \text{otherwise}
\end{cases}
$$

#### Computing $t_i^{pred}$

$$
\mathcal{X}_x^{pred}(v) = \big\{pred(J_x) \cap \mathcal{X}(v)\big\}
$$


$$
\mathcal{Q}_i(v, t)= \bigg\{J_k \bigg| \Big(t \ge \max\left\{r_k^{\max}, A_{m_k^{\min}}^{\min}\right\}\Big) \land \Big(pred(J_k) \subseteq \mathcal{S}(v)\Big)\land\mathcal{X}_k^{pred}(v) \ne \emptyset \land  J_k \in \operatorname{hp}_i\bigg\}
$$

$$
J_k^{pred,\min} = \operatorname*{arg\,min}_{J_j \in \mathcal{X}_k^{pred}(v)} p_j
$$

$$
\mathcal{Q}_i^{pred}(v, t) = \left\{ J_k^{pred,\min} \Bigg| J_k \in \mathcal{Q}_i(v, t) \right\}
$$

$$
q^{\min}(v, t) = \max_{1 \le q \le m} \{q | A_q^{\min}(v) \ge t\}
$$

$$
q^{\min}(v, t) - \sum_{J_j \in \mathcal{Q}_i^{pred}(v, t)} p_j \ge p
$$



```{=latex}
\begin{algorithm}[H]
\SetKwInOut{Input}{input}\SetKwInOut{Output}{output}

\Input{State $v$, $p$ and $J_i$}
\Output{$t_i^{pred}$}
\BlankLine

$r := p$\;
$t_i^{pred} := R_i^{\min}$\;
\While{$r \le m$}{
	$t_i^{pred} := \max\{t_i^{pred}, A_r^{\min}\}$\;
	\If{$q^{\min}(v, t_i^{pred}) - \sum_{J_j \in \mathcal{Q}_i^{pred}(v, t_i^{pred})} p_j \ge p$}{
		\Return $t_i^{pred}$\;
	}
	$r := r + 1$\;
}

\Return $+\infty$\;

\caption{Algorithm to find lower bound of $t_i^{pred}$}
\end{algorithm}
```



### Latest Start Time

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

