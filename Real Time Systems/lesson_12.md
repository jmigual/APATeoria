# Lesson 12 - Fixed-priority and dynamic-priority servers

Book chapter 5, 6

## Aperiodic tasks
> While many real-time tasks are periodic, a system may still have some "aperiodic tasks as well"

This usually happens when having interactions with the environment and/or the user. We cannot avoid accepting the fact that **aperiodic tasks exist in our system**

How do we schedule periodic + aperiodic tasks?

## Aperiodic task scheduling

> ***
> **EXAMPLE**: Two periodic tasks scheduled by RM and a single aperiodic job $J_a$ (arrives at $a_a = 2$ and its WCET is $C_a = 2$). How do we schedule this task without missing a deadline?
>
> 1. Run the task in the background, when there aren't other tasks running
> 2. Start scheduling immediately (not very safe)
> 3. Inside a reservation server (safer)
> ***

### Solution 1: scheduling as a background service

Let's suppose that we have a FP scheduler.

In this case we would have a _long response time_. 

**Advantages**:

- None of the periodic tasks will be affected by the aperiodic task

**Disadvantages**:

- If the schedule is busy, the task needs to wait a long time

### Solution 2: schedule them immediately

The response time will be low but other task may need to be pre-emptied.

**Advantages**:

- Very short response time for the aperiodic task
- More responsive system

**Disadvantages**:

- Long response time and possible deadline misses for the other periodic tasks

## Handling aperiodic tasks

We want to keep the system schedulable and also as short response time as possible for an aperiodic task.

## Soft and hard aperiodic tasks

- **Hard** aperiodic tasks:
  - Task with **hard** deadlines must be guaranteed under worst-case conditions
  - Offline guarantee is only possible if we can bound inter-arrival times

- **Soft** aperiodic tasks:
  - Deadlines should be executed as soon as possible but without jeopardizing hard tasks
  - We are interested in:
    - Minimizing the response time
    - Having an online scheduling test

## Types of servers

- Fixed-priority servers
- Dynamic-priority servers (to be used with EDF scheduler)

## Aperiodic servers

> We assume only one server in the system

A new aperiodic tasks comes and the server has some budget.

- The server is scheduled as **any periodic task**

## What was bad about periodic servers?

- Not all of the reserved space is used
- It doesn't let the task start as soon as possible and thus increases response time

## Improving periodic servers

> It wastes the budget if there is nothing in the queue to execute

**How can we fix this?**

- The server shouldn't take the space when there's nothing in the queue
- _Discharge the budget of the server if there is nothing in the queue_

This is called a **Polling Server (PS)**

## Polling Server (PS)
**Example 1**
Slide 16

The server is discharged in the first period because there's no task scheduled at that time. Then at time 4 the server does not discharge since there's a scheduled task. This task can be executed at time 5.

In the example the response time is 9.

**Example 2**

In this case the server also discharges on the first period since the task is not scheduled yet. 

How can we formulate the worst-case response time of a single aperiodic job that is released?

## WCRT of an aperiodic task under PS
Slide 18

We know that the server has a $C_s = 2$ every 4 times. The period can help us in knowing the WCRT of the task

- Initial delay: $\Delta_a$. Delay between the task is released and the server has some budge again
- **Number** of full service periods: $F_a$
- Final chunk: $\delta_a$. Part of the last service period that will be used by the task

$$
\begin{aligned}
    \Delta_a &= \left\lceil \frac{a_a}{T_s}\right\rceil \cdot T_s - a_s \rightarrow \text{ a bit pessimistic}\\
    F_a &= \left\lceil \frac{C_a}{C_s} \right\rceil - 1 \\
    \delta_a &\le \underbrace{(R_s - C_s)}_{\text{latest start time}} + \underbrace{}_{\text{remained execution time}}
\end{aligned}
$$

$$
\Delta_a + F_a \cdot T_s + \delta_a
$$

## Small presentation
Presentation by another woman about different projects that they are working on

What if data is not static and comes and goes over the time?

### From edge to cloud
How to run AI on mobile devices?

You can run AI on a mobile phone but training a neural network requires thousands of parameters. Usually the training is done in the cloud.

### Private IoT sensing
Is smartness at the cost of privacy?

When you upload this information, do you anonymize that? What can you do with that?

- Anonymize: this is not a really good solution
- Not upload the data 😅
- Lie in the data. Upload data that has been modified

### Smart drone
How to teach drone to find an object. Reinforce learning

## Polling server vs background service

If the polling server has the lowest priority, can we say it is like if the aperiodic tasks are executed as a background service?

No since if there was a free slot but the polling server had already discharged the slot then the free space would not be used. So, in this case, **it can be worse than a background service**.

## How to improve PS?

> If aperiodic tasks come later than the release time of the server, they have to wai for the next release of the server

How can we fix this?

Keep the budget even if there is no aperiodic task in the queue. This is called **Deferrable Server (DS)**.

_Slide 26_. What happens if DS has a higher priority than $\tau_2$?

There's a deadline miss that could have been avoided otherwise

## Issue with DS

- Note that DS does not behave like a periodic task


### WCRT of periodic tasks in the presence of a DS

DS cannot impact the schedule of any high-priority task but it can for lower-priority tasks. This means that the analysis for this server is different than the one used for PS.

## Constant Bandwidth Server

- It is designed to work with EDF scheduling policy
- It keeps the "bandwidth = utilisation" constant

CBS parameters

- Maximum budget: $Q_s$
- Server period: $T_s$
- Server bandwidth: $U_s = \frac{Q_s}{T_s}$
- Current budget: $q_s$
- Current deadline: $d_s$

## CBS idea

> Replenish the budget as soon as it is finished. However, each time you do so, increase the current deadline by the value of $T_s$

This decreases priority since for EDF the deadline is the priority.

It smoothly reduces priority of the current job of the server among other jobs in the system while keeping the utilization of the server constant

## Basic CBS rules

Arrival of job $J_k$ at time $a_k \implies$ assign a new $d_s$

```python
if not periodic_jobs.empty():
    periodic_jobs.add(job)
elif q_s >= (d_s - a_k)**_s:
    q_s = Q_s
    d_s = d_s + T_s
```




















