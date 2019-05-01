# Lesson 1

## Introduction

### What are evolutionary algorithms?

- In **Evolutionary Computation** (EC) natural evolution is used as a metaphor for constructing search/optimization algorithms
- Species can **adapt** to their environment and develop themselves as generations pass
- Strongest individuals have higher probabilities of surviving

### Why use them?

- Natural evolution can be seen as an optimization process to generate individuals that are strong
- Evolution employs populations; multiple individuals create multiple new individuals
    - Highly complex algorithms
    - Parallel process
    - Simple
    - Robust

### Definition

There are three ingredients:

1. A population of individuals
2. Variation, to create new individuals
3. Selection, to select better individuals

- Debatable constraints:
    1. Stochastic operators
    2. Population size $n \ge 2$
    3. Variation considers $\ge 2$ individuals (_interaction_)

```python
t = 0
P[t] = createAndEvaluateInitialIndividuals(n)
while terminationCriterionNotSatisfied(P[t]):
    O[t] = createAndEvaluateOffspring(P[t])
    P[t + 1] = selectSurvivingIndividuals(P[t], O[t])
    t += 1
```

- What is an EA with no selection?
- What is an EA with no variation?

- Consider general optimization problem

$$
\arg\,\max_{\pmb{x} \in \pmb{S}} \{f(\pmb{x})\}
$$

- Often, genotype is vector of $l \ge 1$ symbols
    - Vector called string
    - $l$ often called string length
- Location of symbol is locus
- Classic case: $\mathbb{A}^i = \{0, 1\}$ (and Cartesian)
- Another classic case $\mathbb{A}^i \subseteq \mathbb{R}$ 

### Simple genetic algorithm

```python
t = 0
P[t] = createAndEvaluateInitialIndividuals(n)
while terminationCriterionNotSatisfied(P[t]):
    # To be fixed, the teacher was too fast with the slides
    O[t] = createAndEvaluateOffspring(P[t])
    P[t + 1] = selectSurvivingIndividuals(P[t], O[t])
    t += 1
```

- Parent selection = proportionate selection
    - Probability selection $p_i^s$ for each individual $P_i$
    - Select $n$ individuals by sampling i.i.d.
    - $p_i^s$ is proportion of fitness contributed:
        - TODO: FORMULA
    - Expected copies of individual $i$: $np_i^s$
    - **Issues**:
        - Required: fitness maximization and non-negative fitness
        - Far-above average individuals quickly dominate population
        - Similar fitness dissolves selection pressure
- Variation
    - Construct $\frac{n}{2}$ groups of 2 parents randomly
    - With probability $p_c$ construct 2 offspring with crossover (clone parents otherwise)
        - One-point crossover
        - Two-point crossover
        - Uniform crossover
    - Permutation $p_m$ of changing a bit

```python
t = 0
P[t] = createAndEvaluateInitialIndividuals(n)
while terminationCriterionNotSatisfied(P[t]):
    S[t] = proportionateSelectionParents(P[t], n)
    O[t] = null
    # TODO: Finish this
    pi = randomPermutation(n)
    P[t + 1] = selectSurvivingIndividuals(P[t], O[t])
    t += 1
```

- When to terminate?
    - If a maximum is reached
    - If diversity is lost

## Schema analysis

When can an EA work well?



