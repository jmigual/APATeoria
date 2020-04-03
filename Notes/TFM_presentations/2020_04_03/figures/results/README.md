# Experiments description
## Experiment 0

This experiment is the first to be documented. Important aspects from it are:

- $\min(s_max - s_min) = 1$ due to a bug
- Periods follow a double log normal distribution
- Utilization is defined with a float so it's a bit unstable

#### Parameters

- Utilization: [10 - 90] in intervals of 10
- Cores (m): [2, 4, 8]
- Tasks: [5, 10, 15]
- Task sets: 100
- Moldable: YES
- Jitter: NO
- Tests:
    - Single core min
    - Single core max
    - Minimum min
    - Minimum max
    - Multicore

## Experiment 1

Fixes the issues found in experiment 0. Additionally:

- Creates some task sets with m = 1 to see if the implementation still 
  matches with the expected results for uniprocessor
  
#### Parameters

- Utilization: [10 - 90] in intervals of 10
- Cores (m): [1, 2, 4, 8]
- Tasks: [5, 10, 15]
- Task sets: 100
- Moldable: YES
- Jitter: NO
- Tests:
    - Single core min
    - Single core max
    - Minimum min
    - Minimum max
    - Multicore
    
