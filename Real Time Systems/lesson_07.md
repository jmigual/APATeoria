# Lesson 07 - DB analysis + non-preemptive scheduling

## EDF schedulability analysis for $D <T$

> If any interval of length $L$

$$
\forall L > 0, \qquad g(0, L) \le L
$$

### Understanding the processor demand ($g$ function)

The demand in $[t_1, t_2]$ is the computation time of those tasks arrived at or after $t_1$ with deadline less than or equal to $t_2$

$$
g(t_1, t_2) = \sum_{\forall J_{k,j}, t_1 \le a_{k, j} < d_{k,j} \le t_2} C_k
$$

$$
g_i(0, L) = \max \left\{ 0, \left\lfloor\frac{L - D_i}{T_i} \right\rfloor \cdot C_i\right\}
$$

$$
g(0, L) = \sum_{\forall J_{k}} g_k(0, L)
$$

- $L$ is continuous
- $g$ is a step function
- How can we make it faster? We can look only at the hyper-period

$$
G(0, L) = L \cdot U + \sum_{i=1}^n (T_i - D_i) \cdot U_i \qquad U \le 1
$$


## EDF vs FP

Both EFD and FP ca be implemented using a binary min heap

- The root always points to the smallest value
- Each node has a value that is less than or equal to the values of its children


## Disadvantages of preemptions
1. Context switches cost
2. Cache-related preemption delay (CRPD): It is the delay introduced by high-priority tasks that evict cache lines containing data used in the future
3. Simplifies the access to shared resources
4. It reduces stack size: Task can share the same stack, since no more than one tasks can be in execution
5. Preemption cost can be very large: WCETs may increase up to 35% in the presence of preemptions (less efficiency)

Some tasks cannot be scheduled in preemptive mode and can be scheduled in non-preemptive mode

## Disadvantages of NP scheduling
1. Some deadlines can be missed
2. The utilization bound under non-preemptive scheduling drops to zero
3. Anomalies: you had a schedulable system. You increase the processor speed and suddenly it is not schedulable anymore

## Response-time analysis of NP-FP

- **Maximum blocking** $B_i = \max\left\{C_j | \forall \tau_j, P_i < P_j \right\}$
- **Maximum interference**
- 

$$
WO_i^{(n)} = B_i + \sum_{k=1}^{i-1} \left(\left\lfloor\frac{WO_i^{(n-1)}}{T_k}\right\rfloor\right) \cdot C_k
$$
$$
R_i = C_i + WO_i
$$

## History of schedulability analysis of NP-FP
In 1994 Tindel introduced the test we saw earlier. They did not know that their test is correct only if some conditions met.

In the late 90's this test was used in CAN controllers in the cars for any type of task set.

In 2007 TU/e noticed a bug in the test. However, thankfully no accident happened because of this bug. Why?

Engineers actually implemented the test in a wrong way which actually was the proper way that did not have a bug 🙃. 



