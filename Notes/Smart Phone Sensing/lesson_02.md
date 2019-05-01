# Lesson 2

### Guidelines for App

The K-NN method can be done for:

- Accelerometer $\rightarrow$ To check an activity
- WiFi $\rightarrow$ To get localization

1. Determine where you are among four zones
2. Determine whether you are still or walking

## Sensing

Where am I?

- Step 0: **Cluelesss**. I could be anywhere
- Step 1: **Sense**. I can see a tall building
- Step 2: **Move**. Ooops!
- Step 3: **Sense**
- Step 4: **Move**
- Step 5: **Sense**

This is an iterative process.

> ***
>
> Example**: WiFi probabilities
>
> - Room A:
>     - WiFi A: 70%
>     - WiFi B: 30%
> - Roob B:
>     - WiFi A: 40%
>     - WiFi B: 60%
>
> $$
> P(A|B) = \frac{P(A \text{ and } B)}{P(B)} = \frac{P(B|A)P(A)}{P(B)}
> $$
>
> $$
> \begin{aligned}
> P(A|\text{WiFi}_{A}) &= \frac{P(\text{WiFi}_A|A) \cdot P(A)}{P(\text{WiFi}_A)} \\
> &= P(\text{WiFi}_A|A) + P(\text{WiFi}_A|B) \cdot P(B) \\
> &= 0.7 \cdot 0.5 + 0.4 \cdot 0.5 = \pmb{0.55}
> \end{aligned}
> $$
>
> We applied the _chain rule_ in conditional probability
>
> ***

Even though we may not have realized it, we already know the gist of Particle (and Bayesian) filters. $X$ represents location and $Z$ measurements:



**Bayesian and particle filters are _very_ popular and useful**

- Job interviews
- Self driving cars

- Particle filters are a general tool

## Bayesian Filter

There's the following steps:

- Prior
- Sense
- Posterior: Multiply the prior by the sense
- Move

$$
p(X_k | Z_{1:k}) = \frac{P(Z_{1:k}|X_k)}{}
$$

> ***
>
> **EXAMPLE**: Car moving
>
> Initial values:
>
> | Stage                  | Blue                | Red                 | Red                 | Blue                | Blue                |
> | ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
> | Prior ($P(X)$)         | 0.2                 | 0.2                 | 0.2                 | 0.2                 | 0.2                 |
> | Sense (red) ($P(Z|X)$) | 0.2                 | 0.6                 | 0.6                 | 0.2                 | 0.2                 |
> | $P(Z|X)\cdot P(X)$     | 0.04                | 0.12                | 0.12                | 0.04                | 0.04                |
> | Normalize              | $\frac{0.04}{0.36}$ | $\frac{0.12}{0.36}$ | $\frac{0.12}{0.36}$ | $\frac{0.04}{0.36}$ | $\frac{0.04}{0.36}$ |
> | Posterior              | $\frac{1}{9}$       | $\frac{1}{3}$       | $\frac{1}{3}$       | $\frac{1}{9}$       | $\frac{1}{9}$       |
>
> _Important_: The sum of the probabilities must be 1
>
> ***

$$
P(X_i^t|Z_i^{t-1})
$$

> ***
>
> **EXAMPLE**: Movement model
> $$
> \begin{aligned}
> &P(X_i&|X_i) &= 0.1 \\
> &P(X_{i + 1}&|X_i) &= 0.8 \\
> &P(X_{i + 2}&|X_i) &= 0.1
> \end{aligned}
> $$
>
> | Stage         | Blue | Red            | Red                             | Blue                            | Blue            |
> | ------------- | ---- | -------------- | ------------------------------- | ------------------------------- | --------------- |
> | Prior         | 0    | 0.5            | 0.5                             | 0                               | 0               |
> | Probabilities | 0    | 0.1            | 0.8                             | 0.1                             | 0               |
> | Multiply      | 0    | $0.1\cdot 0.5$ | $0.8 \cdot 0.5 + 0.1 \cdot 0.5$ | $0.1 \cdot 0.5 + 0.8 \cdot 0.5$ | $0.1 \cdot 0.5$ |
> | Result        | 0    | 0.05           | 0.45                            | 0.45                            | .05             |
> 
>***





