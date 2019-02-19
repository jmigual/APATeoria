# Lesson 03 - Online Scheduling of Aperiodic Tasks

## FIFO: the judgement day
- Disadvantages:
    - Creates non-pree

- Advantages:

## Feasibility vs. schedulability

A scheduling algorithm may not be able to schedule all the feasible tasks but only a subset of them. However, two algorithms could schedule the same tasks, so the intersection is possible.

## General scheduling problem

The scheduling problem is an NP-Complete problem. So Complexity in the scheduling algorithms is important.

**Complexity** is a very important factor but there are other factors:
- Runtime
- Hardware platform capabilities
- Memory consumption
- Memory limits
- ...

## Work-conserving vs non-work-conserving

- Work conserving: Does not leave the processor **idgle** as long as there is a ready task in the system
- Non-work conserving: May leave the processor **idle** even if there is a task in the system

## Scheduling algorithms

### Shortest-job-first (SJF)

It selects the ready task with the shortest computation time. 

- Kind of **static** (if $C_i$ is a constant parameter, it is given beforehand to the algorithm)
- It can be used online or offline
- Can be preemptive or non-preemptive
- It minimizes the average response time

#### Is SJF suited for Real-Time?

It is not optimal in the sense of feasibility


## Fixed-priority scheduling
- Each task has a priority $P_i$, typically $P_i \in [0, 255]$. ($P_i < P_j$ means that task $\tau_i$ has higher priority than task $\tau_j$)
- The task with the highest priority is selected for execution
- Tasks with the same priority are served FIFO

## Round robin
- The ready queue is served with FIFO, but
- Each task $\tau_i$ cannot execute for more than **Q** time units
- When **Q** expires, $\tau_i$ is preempted

However, there are a lot of context switches

## Multi-level scheduling

Have a high, medium and low priority queue






