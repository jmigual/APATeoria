# Lesson 8 - Simulation-based schedulability tests

## Necessary test for non-preemptive scheduling

We can have a task that is too long and whatever you do the deadline miss cannot be avoided.

$$
\begin{aligned}
    & U \le 1 \\
    & \forall i, 1 < \le n
\end{aligned}
$$

## Why non-preemptive scheduling is hard?

**How the periodicity helps?**

Knowing tasks are periodic, we exactly know when the future jobs of the tasks will arrive. Hence we can check if our current decision

## A general non-work-conserving solution

1. Select the highest-priority ready job: Can be chosen by any scheduling policy
2. Check if executing that job will cause a deadline miss for a set of jobs that will arrive in the future
   1. **Yes**: Don't schedule the current task, leave the processor **idle** instead
   2. **No**: Then schedule the current high-priority ready task

## Critical window EDF (CW-EDF)

- Considers the next job of each task
- Sorts their deadlines
- Obtains the latest start time of each job starting from the one with the latest deadline
- Checks if the current high priority job can finish before th latest start time $S$

## A closer look at the "scheduling"

There can be some task sets that are schedulable but that are rejected by the tests

## The *dumbest* yet *smartest* schedulability test (for periodic tasks)
The previous tests work with *worst execution time* while this one works with actual time. It is a **simulation-based** schedulability test. It is not a sound test.

- Schedule the tasks until the hyper-period with the given scheduling policy
- If there is a deadline miss it is not schedulable
- Otherwise it is schedulable

It is not an exact test but any scheduling policy can be used.

Because it allows designing schedulability analyses for a wide class of scheduling policies and task sets

#### Why is it dumb?

- If you have many tasks, it can take a lot of time to execute
- Hyper-period could be too big but usually this is still doable 
- There are uncertainties in the task set, like the execution time

For example we do not know what is the exact execution time or release time of the tasks at runtime.

## What is a schedule-abstraction graph

- A path in the graph represents an ordered set of dispatched jobs
- A vertex abstracts a system update
- An edge abstracts a dispatched job
- A state represents the finish-time interval of any path reaching that state


