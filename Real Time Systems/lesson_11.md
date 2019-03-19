# Lesson 11 - Reservation based scheduling

## What do we do with varying workloads?

### Calculate and use the worst-case execution time

**Advantages**:
- Is is safe
- Necessary for hard real-time systems

**Disadvantages**:
- Too conservative
- Pessimistic analysis far from reality
- It leads to overprovisioning the system

### Model it using more expensive task models

**Advantages**:
- It is safe but not pesimistic: you can use it to obtain the WCRT of the task
- Necessary for hard real-time systems

**Disadvantages**:
- It is too complex to derive such a model from a general application
- Some system do not have such a regular pattern
- It is hard to analyze such a complex workload

### Just use a smaller value

There will be cases where the actual execution time is larger than you expected it to be. This is called **overrun**. 

**Advantages**:
- It is different since it allows having an analysis that is closer to the average case performance of the system
- Allows using the existing analysis techniques

**Disadvantages**:
- It is unsafe, we may have deadline misses
- If the value we assign is too small there are many overruns
- You cannot use it for hard real-time systems

## Consequences of overruns

A task overrun may or may not cause a deadline miss. The deadline miss is not always for the task that has the overrun but it can be for another task

### What can go wrong if they are not controlled?

**EDF** may have a domino effect: one or more overruns may result in a series of deadline misses

In **FP**, low-priority tasks may starve due to an overrun in high-priority tasks

## Handling overruns: not-so-good solutions

- Cut the task as soon as the task overruns: this totally violates data consistency
- Do not do anything. "Pray" that nothing will happen
- Exception handling mechanisms: It can be a good or bad solution depending in how it is handled

## Handling overruns: good solutions

- Performance degradation (or graceful degradation)
  - Execute a shorter version of the program. Example
    - Fast and low quality
    - Middle ground
    - Slow but high quality
- Resource reservation
  - Allows analyzing WCRT despite possible transient overruns
  - Isolates task's overrun from each other

## Performance degradation
- Degrading functionality (reducing task execution time)
- Skipping specific jobs
- Increasing periods

The load can be decreased not only by rejecting tasks but also by reducing their performance requirements

### Functional degradation
In some applications computation can be performed at different level of accuracy or quality of service

> The higher the QoS, the longer the computation

- Imprecise computation
- Multiple version

#### Imprecise computation
Each task $\tau_i$ is divided in two parts:
- A mandatory part with the worst case execution time $M_i$
- An optional part with the worst case execution time $O_i$
  
Error: $\varepsilon_i = O_i - \sigma_i$

In this case a schedule is:
- Feasible if all mandatory parts complete within $D_i$
- Precise, if also the optional parts are completed

#### Multiple versions
If a task does not comply with the imprecise computational model, another option is to implement multiple versions

**Example**: Engine control task
Some tasks are activated at specific angles. If the car accelerates then the engine task is run more often and the car cannot brake anymore.

What can be done is when the speed increases just use smaller functionality for the engine that takes less time to execute.


### Job skipping

Periodic load can also be reduced by skipping some jobs, once in a while. Many systems tolerate skips, if they do not occur too often:
- Multimedia systems
- Inertial systems

**Example** (slide 24): The system is overloaded, but tasks can be EDF-schedulable if $\tau_1$ skips one instance every 3.

$$
U_p = \frac{1}{2} + \frac{4}{6} = 1.17 = 1
$$

#### Weakly-hard systems
A task with $(m, k)$ weakly-hard timing constraint is feasible if and only if in every window of $k$ **consecutive** jobs of that task, at least $m$ jobs meet their deadlines.

In general if a task set is $(m, k)$ feasible, as long as we increase $k$ or decrease $m$ is always feasible.




