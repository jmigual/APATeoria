# Notation

## Classes

- **Hard**: system where it is absolutely imperative that responses occur within the required deadline
- **Soft**: systems where deadlines are important but which will still function correctly if deadlines are occasionally missed
- **Firm**: systems which are soft real-time but in which there is no benefit from late delivery of service

## Taxonomy

- **Task**: Code that implements one of the system functionalities
- **Job**: Instance of a task

### Activation

- **Periodic**:
  - **Single rate**: All tasks have the same period
  - **Multi-rate**: Tasks have different periods
- **Aperiodic**:
  - **Sporadic**: Bounded arrival time
  - **Event-based activation**: Unbounded arrival time

### Deadlines

- **Implicit deadline**: deadline is equal to period
- **Constrained deadline**: deadline is smaller than or equal to period
- **Arbitrary deadline**: deadline can be smaller, equal or larger than period

## Execution model

- **Preemptive execution**: The execution of a task may be stopped by the system and later restored
- **Non-preemptive execution**: A task does not leave the processor until it completes or suspends itself

## Real-Time Tasks

- **Feasible**: if it is guaranteed that it will complete before its deadline

- **Schedule**: a particular assignment of tasks to the processors and time intervals

- A task set is feasible if *there exists a feasible schedule*

- A task set $\tau$ is **schedulable** with an algorithm $A$ if only $A$ generates a feasible schedule for $\tau$

  

## Tests

- **Necessary test**: If this test fails it is not schedulable at all

## Task sets

- **Sustainable** or **predictable**: if a task takes less than the WCET to finish the task set is still schedulable