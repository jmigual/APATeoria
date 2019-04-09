# Lesson 6 - Schedulability analysis

## Utilization-based tests and RM scheduling

Under which circumstances hyperbolic bound is better than L&L test?

When there is one big tasks and some very small tasks. However, this never happens usually in a normal system.

## Secrets behind

They found the hardest-to-schedule task set with the minimal utilization:

- It is schedulable by RM
- It fully utilizes the processor. If the execution time of any of the tasks is increased by $\epsilon_i$
- All tasks are released at the same time (no release offset)
- Periods follow $T_1 < T_2 < ... < T_n < 2T_1$

To make sure that your schedule is on time. Just draw the schedule and find the Worst Case Real Time.

## Computational complexity of RTA

- Calculating the WCRT of a task using RTA is a **weakly NP-Hard** problem
- It has a pseudo-polynomial time computational complexity.

## Using RTA to build fast sufficient tests
Idea: Instead of searching for the exact WCRT just check if the workload that must be completed before the deadline is smaller thant the deadline of the task.

How? 





