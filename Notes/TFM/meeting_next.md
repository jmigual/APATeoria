# Meeting Next

## Intuition about higher priority formulation

$$
\begin{aligned}
t_{high}(J_i) &= \min_{J_j \in \{hp_i\} \cap \{\mathcal{J} \setminus \mathcal{J}^v\}}\{t_{cores}(J_i, J_j)\} \\
t_{cores}(J_i, J_j) &= \begin{cases}
r_j^{\max} & \text{ if } s_j^{\min} \le s_i^{\max} \\
\max\{r_j^{\max}, A_{s_j^{\min}}^{\max}\} & \text{ otherwise}
\end{cases}
\end{aligned}
$$

Proof

- First part:
  - Assumptions: $s_j^{\min} \le s_i^{\min}$, $r_j^{\max} \le r_i$ and $J_j \in hp_i \cap \{\mathcal{J} \setminus \mathcal{J}^v\}$. 
  - By contradiction, assume that $J_i$ starts executing before $J_j$
  - Let $t$ be the time at which $J_i$ starts executing. At least $s_i^{\min}$ cores are available at $t$ to execute $J_i$. At least $s_j^{\min} \le s_i^{\min}$ cores are available to execute $J_j$. 
  - Since $r_j^{\max} \le r_i$, by the (Job-level fixed-priority) JLFP scheduling policy, $J_j$ is chosen first by the scheduler to be dispatched at time $t$
  - This contradicts the assumption the $J_i$ starts executing before $J_j$. Either $r_j^{\max} > r_i$ or $s_j^{\min} > s_i^{\min}$
- Second part (v1):
  - Assumptions: $s_j^{\min} > s_i^{\min}$, $r_j^{\max} \le r_i$, $A_{s_j^{\min}}^{\max} \le r_i$ and $J_j \in hp_i \cap \{\mathcal{J} \setminus \mathcal{J}^v\}$
  - By contradiction, assume that $J_i$ starts executing before $J_j$
  - Let $t$ be the time at which $J_i$ starts executing. At least $s_j^{\min}$ cores are available, since $A_{s_j^{\min}}^{\max} \le r_i$, to execute $J_j$.
  - Since $r_j^{\max} \le r_i$, by the JLFP scheduling policy, $J_j$ is chosen first by the scheduler to be dispatched at time $t$
  - This contradicts the assumption that $J_i$ starts executing before $J_j$. Either $r_j^{\max} > r_i$, $A_{s_j^{\min}}^{\max} > r_i$ or $s_j^{\min} \le s_i^{\min}$
- Second part (v2):
  - Assumptions: $s_j^{\min} > s_i^{\min}$ and $A_{s_i^{\min}}^{\max} < r_i^{\max} < A_{s_j^{\min}}^{\max}$ and $J_j \in hp_i \cap \{\mathcal{J} \setminus \mathcal{J}^v\}$
  - By contradiction, assume that $J_j$ starts executing before $J_i$
  - Let $t$ be the time at which $J_j$ starts executing. At least $s_i^{\min} < s_j^{\min}$ cores are available to execute $J_j$ and $t \ge \max\{r_j, A_{s_j^{\min}}^{\max}\}$
  - Since $t \ge A_{s_j^{\min}}^{\max} > r_i^{\max} > A_{s_i^{\min}}^{\max}$, by the JLFP scheduling policy $J_i$ should have been chosen first by the scheduler to be dispatched at time $\max\{r_i^{\max}, A_{s_i^{\min}}^{\max} \}$ instead of time $t$
  - This contradicts the assumption that $J_j$ starts executing before $J_i$.

