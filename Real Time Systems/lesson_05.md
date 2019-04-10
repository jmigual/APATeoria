# Lesson 5 - Online scheduling of periodic tasks

Buttazzo's book, chapter 4

## Introduction
### Definitions

We have a computing system with a set $\tau$ of $n$ periodic real-time tasks: $\tau = \{ \tau_1, \tau_2, \tau_3, ... \tau_n \}$.

- $T_i =$ period
- $C_i =$ worst-case execution time
- $D_i =$ relative deadline
- $\phi_i =$ offset
- $U_i = \frac{C_i}{T_i} =$ utilization

### Assumptions

- $C_i$ and $T_i$ are constant for every job $\tau_i$
- Tasks are fully preemptive
- Context switch, preemption, and scheduling overheads are zero
- Tasks are independent:
    - No precedence relations
    - No resource constraints
    - No blocking I/O operations
    - No self suspension

### Formulating the arrival time and absolute deadline

Arrival time and absolute deadline of the $k^{th}$ job of $\tau_i = (C_i, T_i, D_i, \phi_i)$, i.e. $J_{i, k}$:

$$
\begin{aligned}
    a_{i, k} &= \phi_i + (k - 1) \cdot T_i \\
    d_{i, k} &= \phi_i + (k - 1) \cdot T_i + D_i \\
\end{aligned}
$$

Note: Utilization is defined for the task, not for the job

### Feasibility of a periodic task set

> A periodic task set $\tau$ is feasible if and only if there exists a schedule in which each task $\tau_i \in \tau$ can execute for $C_i$ units of time within every interval $[a_{i, k}, d_{i, k})$ for all $k \in \mathbb{N}$.


## Scheduling algorithms for periodic tasks


### Proportional share algorithm

**Basic idea**:

- Divide the timeline into slots of equal length
- Within each slot serve each task for a time proportional to its utilization
- Slot length: $\Delta = GCD(T_i, \forall i)$
- Task share in each slot: $\delta_i = U_i \cdot \Delta$

#### Downside of proportional share algorithm

- If periods are not harmonic then the slot length is very small and the task is fragmented into many chunks $\left(\frac{T_i}{\Delta}\right)$ of small duration which can lead into **many context switchees**
- Context switch is very expensive

### Cyclic scheduling

- Method
    - The time axis is divided in interval of equal length *(time slots)*
    - Each task is statistically allocated in a slot in order to meet the desired request rate
    - The execution in each slot is activated by a timer
    - There are **major** cycles and **minor cycles**. Within one major there are several minor cycles.
        - Minor $\Delta = GCD(T_i, \forall i)$
        - Major $T = LCM(T_i, \forall i)$
- Steps:
  1. Obtain the length of major and minor cycles
  2. Assign tasks to time slots
- Advantages:
    - It has very few overhead
    - It uses flash memory instead of ram memory
- Disadvantages:
    - It requires to know all about the tasks that are going to run in the system
    - Not robust against overloads
    - It is difficult to update the code since it may change the schedule
    - It is not easy to handle aperiodic activities

### What do we do if an overrun happens?
There are two choices:

- Let the task continue: this creates a domino effect with the rest of the tasks
- Abort the task: the system can be inconsistent with this method

### Fixed-priority scheduling

Method:

1. Assign priorities to each task on its timing constraints
   1. Rate monotonic
   2. Deadline monotonic
2. Verify the feasibility of the schedule using analytical techniques
3. Execute tasks on a priority-based kernel

### Rate monotonic
Assign priorities monotonically with the activation frequency $\left(\sim \frac{1}{T}\right)$ such that a task with a smaller period gets a higher priority

### Deadline monotonic

Assign priorities monotonically with the relative deadline of the task, $\left(\sim\frac{1}{D}\right)$ such that a task with a smaller relative deadline gets a higher priority.

### Optimality

The optimality of schedules generated is:

$$
\sigma_{RM} \subseteq \sigma_{DM} \subseteq \sigma_{EDF}
$$

#### Rate monotonic

If $D_i = T_i$ then RM is optimal among all fixed-priority algorithms. 

If there exists a fixed-priority assignment which leads to a feasible schedule for $\tau$, then the RM assignment is feasible for $\tau$ $\iff$ if $\tau$ is not schedulable by RM, then it cannot be scheduled by any fixed-priority assignment.

#### Deadline monotonic

If $D_i \le T_i$ then the optimal priority assignment is given by DM

#### EDF

EDF is optimal among all algorithms

If there exists a feasible schedule for $\tau$, then EDF will generate a feasible schedule $\iff$ if $\tau$ is not schedulable by EDF then it cannot be scheduled by any algorithm.

## RM schedulability tests

### Necessary and sufficient tests

**Necessary test** (checks the feasibility): If the condition in the test is NOT satisfied, then the task set is not feasible. 

**Sufficient schedulability test** for algorithm A: If the condition in the test is satisfied, then the task set is certainly schedulable by the given scheduling algorithm.

### Utilization-based schedulability tests

Checks whether there exists a specific relation $f_A$ between the utilization values of the tasks in the task set.

**Why utilization?**:

- Each task uses the processor for a fraction of time
- Hence the processor utilization is $U = \sum_{i = 1}^n \frac{C_i}{T_i}$
- $U$ is a measure of processor load

A **necessary condition** for having a feasible schedule is $U \le 1$. This is enough for preemptive EDF.

#### Liu and Layland's test for RM

Assumptions:

- $C_i$ and $T_i$ are constant for every job $\tau_i$
- For each task $T_i = D_i$
- Tasks are fully preemptive
- Context switch, preemption, and scheduling overheads are zero
- Tasks are independent
$$
U \le n \cdot (2^{\frac{1}{n}} - 1)
$$

$$
\begin{aligned}
    n &\rightarrow \infty \\
    U &\rightarrow \ln 2 \sim 0.691
\end{aligned}
$$

However this test rejects any task set with $U > 0.83$ for $n = 2$. It is, thus, a pessimistic test

#### Hyperbolic bound

A set of $n$ periodic tasks is schedulable with RM if:

$$
\prod_{i=1}^n (U_i + 1) \le 2
$$

Hyperbolic bound is tight:

- It is impossible to invent a new utilization-based test $A$ such that $A$ accepts a task set that the hyperbolic bound rejects.
- As long as you consider task utilizations into account it is impossible to invent a test that is better than hyperbolic bound

## Summary

- Scheduling algorithms for periodic real-time tasks:
    - Processor sharing
    - Cyclic scheduling
    - Rate monotonic (RM)
    - Deadline monotonic (DM)
    - EDF
- RM schedulability tests:
    - Necessary vs sufficient tests
    - Liu and Layland's test
        - It is a sufficient utilization-based test for RM
    - Hyperbolic bound
        - It is a sufficient utilization-based test for RM
        - It is the tightest test among all utilization-based tests for RM

