
# Lesson 2 - Online scheduling

- Modeling real-time systems
  - Modeling computation
  - Modeling task execution time
  - Modeling task execution

- Real-time tasks: formal definitions

- Online scheduling

## Modeling real-time activities
A **model** is a representation of something. Captures the *relevant attributes*.

Should be:
- Expressive: accurate to the real system
- Tractable: not including too many details

We need to make the model complex enough so it's not useless but not too many complex so it has to many details and it's difficult to analyse.

> All models are WRONG! But some of them are useful!

### Why do we need models?
To be able to analyze a system. Then you can give other properties of the system (reliability...)

### Modeling computation
1. System to be controlled
2. System model
3. Definition of task/app parameters
4. Application model

Then you add the operating system model and the platform model and do a timing analysis. Then create a solution and analyse if the proposed solution is feasible.

### Modeling task execution time
**Task**: a sequence of instructions that, in the absence of other Activities, is continuously executed by the processor until compression

- Finish time: $f_i$
- Start time: $s_i$. When the first instruction of the task is actually executed
- Activation time: $a_i$. When the task wants to start executing instructions
- Response time: $R_i = f_i - a_i$
- Computation time: $C_i = f_i - s_i$

#### How good is to model task's execution time by a constant value $C_i$?

The execution time can change depending on different factors:
- Software
    - Input value
    - Program path (branches)
    - Number of iterations per loop
- Hardware
    - Cache misses
    - Out-of-order execution in the processor
    - Processor buses (memory bus, ...)

#### How to get a safe $C_i$?

It is not a constant, it depends on architecture and software but we still need a $C_i$ to make the analysis simple.

Measurement is important. So, data is generated and the number of occurrences of a certain execution time is shown. E.g.: 40 times out of 100 the measured execution time is 26.

Then three definitions are done:
- Minimum execution time: $C_i^{\min}$
- Maximum execution time: $C_i^{\max}$
- Average execution time: $C_i^{\text{avg}}$

We may not be able to achieve the true **worst-case execution time** so we add a **safe** upper bound on the worst-case execution time. This is done by assuming the worst in every case, like always cache misses.

### Modeling task execution

#### Online scheduler

In a concurrent system we have one processor and many tasks but only one task can be executed at a time.

Ready tasks are kept in the ready queue and managed by a scheduling policy. The processor is assigned a task by the scheduling policy.

#### Preemption
Allow for a task with higher priority to execute before another one with lower priority. The **preempted task** goes to the ready queue.

#### Suspension
Happens when a task decides to suspend itself or tries to access a shared resource that is currently being used by another task. *The task has nothing to do so it suspends itself*.

The suspended task goes to the pending queue.

#### Real time tasks

A real time task $\tau_i$ is said to be feasible if it is guaranteed that it will complete before its deadline, that is if $f_i \le d_i$, or equivalently $R_i \le D_i$.

- Absolute deadline: $d_i$
- Relative deadline: $D_i$

#### Slack and lateness
- Slack: $\text{slack}_i = d_i - f_i$. How far are you from the deadline when you finish
- Lateness: $L_i = f_i - d_i$. How far you finish **after** your deadline. It should be negative or 0 to be fine. 

## Online scheduling
### Definitions: Schedule
**Schedule** is a particular assignment of tasks to the processor and time intervals. 

Formally, given a task set $\tau = \{\tau_1, \tau_2, ..., \tau_n \}$, a schedule is a function $\sigma: \mathbb{R}^+ \rightarrow \mathbb{R}$

A schedule $\sigma$ is said to be feasible if it satisfies all given requirements. How do we guarantee that we meet all given requirements?

A task set $\tau$ is said to be feasible, if there exists  an algorithm that generates a feasible schedule for $\tau$.

A task set $\tau$ is said to be schedulable with ana algorithm $A$, if $A$ generates a feasible schedule for $\tau$.






















