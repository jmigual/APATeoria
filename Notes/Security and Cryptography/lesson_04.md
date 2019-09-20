# Lecture 5 - Modern Stream Ciphers

Stream ciphers are important because they use less power. A very simple example is
$$
C = M \oplus K
$$
Delivering a large key is the problem

## Stream Ciphers

- Encrypt bits rather than blocks
- The are fast due to bit operations
  - easy to implement in **hardware** and **software**

### Stream Ciphers from PRFs

- Consider the following stream cipher

$$
c = m \oplus F_k(0)
$$

- This cipher is IND-PASS secure if PRF is secure (See the textbook)
- Then, how are we going to build a secure PRF?

### Linear Feedback Shift Registers

- For generating a binary stream, we can use feedback shift registers

![Feedback shift register](images/04/shift_register.png){width=75}

The registers are single bit registers

### Feedback functions

- **Non-linear**: We would like to have them but they are difficult to design
- **Linear**: We can design more easily and it is easy to determine the period

### Mathematical expression

- Cell is tapped or not: $[c_1, c_2,...,c_L]$
- Initial state of the registers: $[s_{L-1}, ...., s_1,s_0]$
- Output: $[s_0, s_1, ...,s_L,s_{L+1},...]$
- Then for $j\ge L$

$$
s_j = c_1 \cdot s_{j-1} \oplus c_2\cdot s_{j-2} \oplus \cdots \oplus c_L \cdot s_{j-L}
$$

- We need to see a repetition after a certain period, $N$, such that

$$
s_{N+i} = s_i
$$

- $N$ can be maximum $2^L -1$

### Characteristic Polynomial

- Connection polynomial

$$
C(X) = 1 + c_1 \cdot X + c_2 \cdot x^2 + \cdots + c_L \cdot x^L \in \mathbb{F}_2[X]
$$

- Characteristic polynomial

$$
G(X)=X^L \cdot C(1/X)
$$

### Primitive Polynomial

$$
C(X) = 1 + c_1\cdot X + c_2 \cdot x^2 + \cdots + c_L \cdot X^L \in \mathbb{F}_2[X]
$$

- $c_L = 0$, then it is singular
- $c_L=1$, non-singular, there is a period
  - $C(X)$ is irreducible: period smallest $N$ such that $C(X)$ divides $1+X^N$. ($N$ will divide $2^L-1$)

### What does it mean?

> If $N$ is the period, then a characteristic polynomial $f(X)$ is a factor of $1 - x^N$

> ***
>
> **EXAMPLE**:
> $$
> \begin{aligned}
> &m=3,\ p=2^3-1=7\\
> &1 - x^7=(1-x)(1+x+x^3)(1+x^2+x^3)
> \end{aligned}
> $$
>
> - Which one we should **not** use?
>   - $(1 - x)$ because if you don't choose the highest order this polynomial will not be singular
>
> ***

### Period

The initial values are important. Imagine that we have the following polynomial
$$
C(X) = X^3 + X + 1
$$
![Transitions of the polynomial](images/04/polynomial.png){width=60%}

- This polynomial is not good because:
  - It is singular
  - Depending on the initial state then $N$ becomes 1