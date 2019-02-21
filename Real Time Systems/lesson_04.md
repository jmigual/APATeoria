# Lesson 4 - 

## Absolute vs relative deadline

- Absolute deadline: $d_i$. The exact time where the task should be finished
- Relative deadline: $D_i = d_i - a_i$

## Earliest deadline first (EDF)
Order the ready queue by increasing the absolute deadline.

- Assumptions
    - Horn's algorithm is preeemptive and is for independent tasks
    - dynamic ($d_i$ depends on the **activation time** of the task)

- Property
    - Under the assumption above, EDF minimizes maximum lateness

Sometimes there can be a tie and we have to find a way to break the tie consistently.

> How can we design an online test for EDF that tells if we can ...

## Dertouzos Transformation
It preserves schedulability because:
- For the advanced slice is obvious
- For the postponed slice, the slack cannot decrease because the deadline of the postponed task MUST 



