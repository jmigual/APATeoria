# Lesson 1 - Real-Time Systems

## Introduction

### What is a real-time system?

> **Real-time system**: A system whose correctness depends not only on the correctness of the logical results, but also on the time at which the results are produced

**Characteristics**:
- Event-driven, reactive
- High cost of failure

### Classes of real-time systems

- Hard real-time: systems where it is absolutely imperative that responses occur within the required deadline.
  - Safety critical
  - Business critical
- Soft real-time: systems where deadlines are important but which will still function correctly if deadlines are occasionally missed.
  - Online gaming
  - Augmented Reality
- Firm real-time: systems which are soft real-time but in which ther eis no benefit from late delivery of service
  - Virtual reality
  - Video streaming
  - Voice over IP

## Taxonomy of real-time systems

**Task**:
- Code that implements one of the system's functionalities
- It can have inputs and outputs
- It can be activated by events
- They usually:
  - Share data
  - Communicate with each other
  - Perform I/O operations

**Job**:
- Instance of a task that has arrived to the system

### Workload characterization
The activation pattern of tasks can be:
- Periodic:
  - Single rate: all tasks have the same period
  - Multi rate: tasks have different periods
- Aperiodic
  - Bounded arrival time
  - Unbounded arrival time: event-based activation

**Periodic**:
- Each task executes repeatedly with a particular period
- It allows static analysis techniques to be used
- It is widely used in real systems
- Types:
  - Single rate
  - Multi rate

**Aperiodic**:
- They are activated by _events_
- The workload is dynamic, it cannot be predicted
- Analyzing these tasks is challenging:
  - Since it is hard to predict the future workload, it is hard to analyze the system to find the worst-case response time of the tasks
  - With unbounded arrival time times, it is impossible to guarantee the timeliness of a resource-constrained system

**Sporadic tasks**:
- The next activation time is lower-bounded by the _minimum inter-arrival time_ but they are not upper bounded

**Relation between deadline and period**

- **Implicit deadline**: the deadline is equal to period
- **Constrained deadline**: the deadline is smaller or equal to period
- **Arbitrary deadline**: the deadline can be smaller, equal or larger than the period (this one is harder to analyze)

### Execution model

- **Preemptive execution**: The execution of a task may be stopped by the system
- **Non-preemptive execution**: A task does not leave the processor until it completes or suspend itself

