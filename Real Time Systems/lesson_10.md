# Lesson 10 - Multiprocessor scheduling

## Switching to multi-core systems

Trends:
- Consolidation
- Parallelism

## Industry challenges

1. Parallelizing legacy code implies a tremendous cost and effort
2. Something

## WCET in multicore

It can be up to 6 times larger due to shared resources

Why does it happen?

## Types of memory

Usually we have:
- Primary storage (DRAM)
- Secondary storage (Disk)
- Cache (SRAM)

Because there are multiple accesses to the same memory the other tasks can interfere with the memory load.

## Cache in multicore systems

If there's, for example, a L3 cache shared every core can interfere with the cache.

**Possible solution**: Partition the last-level cache between the tasks. This can be done by software or by hardware.

**Problems**: Every task has less cache as you have effectively divided the cache in two. The cache is faster but it's more common to have conflicts.

- Use _non-preemptive scheduling_ on the cores
- Partition the shared cache L3 by the number of cores (rather than the number of tasks)

## Memory banks

Divide the memory in different banks, but still there are many I/O conflicts 

## Parallel real-time tasks

We always assume homogeneous processors

## Important factors
- **Critical path length** $C_i^p$

## Multiprocessor models

- Identical: Processors are the same type and have the same speed. Each task has the same WCET on each processor
- Uniform: Processors are the same type but may have different tasks
- Heterogeneous

## Real-time scheduling for multicore platforms

## Partitioned scheduling

- Each processor manages its own ready queue
- It is like every processor is unicore




