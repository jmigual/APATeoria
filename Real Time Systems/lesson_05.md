# Lesson 5 - Scheduling of Real-Time Systems

## Definitions

- $T_i =$ period
- $C_i =$ worst-case execution time
- $D_i =$ relative deadline
- $\phi_i =$ offset
- $U_i = \frac{C_i}{\tau_i} =$ utilization

## Proportional share algorithm

**Basic idea**:

- Divide the timeline into slots of equal length
- Within each slot serve each task for a time proportional to its utilization
- Slot length: $\Delta = GCD(T_i, \forall i)$
- Task share in each slot: $\delta_i = U_i \cdot \Delta$

### Downside of proportional share algorithm

- Context switch is very expensive
- It can have many context switches

## Cyclic scheduling

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

### What do we do if an overrun happens?
There are two choices:

- Let the task continue: this creates a domino effect with the rest of the tasks
- Abort the task: the system can be inconsistent with this method

## Fixed-priority scheduling

1. Assign priorities to each task on its timing constraints
   1. Rate monotonic
   2. Deadline monotonic
2. Verify the feasibility of the schedule using analytical techniques
3. Execute tasks on 

### Rate monotonic
Assign priorities monotonically with the activation frequency ($rate = ~\frac{1}{T}$) such that a task with a smaller period gets a higher priority

#### Liu and Layland's test for RM

$$
U \le n \cdot (2^{\frac{1}{n}} - 1)
$$

$$
\begin{aligned}
    n \rightarrow \infty \\
    U \rightarrow \ln 2
\end{aligned}
$$

#### Hyperbolic bound

$$
\prod_{i=1}^n (U_i + 1) \le 2
$$

### Deadline monotonic
Assing priorities monotonically with the relative deadline of the task ($~\frac{1}{D}$) such that a task with a smaller relative deadline gets a higher priority

It is optimal. If $D_i \le T_i$ then the optimal priority assignment is given by **Deadline Monotonic (DM)**.





