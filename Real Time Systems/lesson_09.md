# Lesson 9 - Handling shared resources


## Semaphores

- $s = 1 \implies$ free resource
- $s = 0 \implies$ busy (locked) resource

```python
def wait(s):
    if s == 0:
        # Task must be blocked
        pass
    else:
        s = 0

def signal(s):
    if blocked_tasks:
        # Awaken the first in the queue
        pass
    else:
        s = 1
```

## Using semaphores to protect shared resources

Even though you solve the data inconsistency with semaphores, this can cause deadline misses.

### Guidelines:

- Try to shorten the critical section
  - Global variables can be copied into local variables
- Avoid critical sections across loops or conditions
- Avoid nested critical sections
  - You will keep one lock and wait for another one, wasting tasks on the system
- Avoid cross-cutting critical sections

Do these guidelines solve the "blocking" problem?

## Impact on schedulability

## Non-Preemptive Protocol (NPP)

Whenever a task accesses a resource, it enters a **non-preemptive mode** until it releases the resource.

### Advantages
Simplicity and efficiency

### Disadvantages

- Tasks can be blocked even if they don't use any critical sections
- It restricts too many parameters. Even if there's an access to a different shared resource it also blocks

## Highest-locker priority (HLP) protocol
When a task accesses a resource (e.g. `wait(s)`), its priority upgrade to the priority of the priority of the highest-priority task that **may use** the resource $S$

$$
p_i(S) = \min(P_j | \forall \tau_j, \tau_j \text{ uses } S)
$$

### Advantages
Simplicity and efficiency

### Disadvantages

- A task could be blocked even if it "may" not access the resource
- It is not transparent to programmers (due to ceilings)

## Priority-inheritance protocol (PIP)

Whenever a task accesses a resource $S$ that is locked by another task, the priority of the locking task **upgrades** to the priority of the highest-priority task that is currently blocked on resource $S$.

There are two types of blocking:

- Direct blocking
- Push-through blocking

### Bounding blocking times
Theorem:
> $\tau_i$ can be blocked at most for the duration of $\alpha_i = \min(n_i, m_i)$ critical sections

### Advantages

- Removes the pessimism of NPP and HLP
- It is transparent to the programmer

### Problems

- More complex to implement
- Prime to chained blocking
- It does not avoid deadlocks







