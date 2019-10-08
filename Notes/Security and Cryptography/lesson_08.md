# Lecture 8: Number Theory and Elliptic Curves

## Modular Arithmetic

- A positive integer $N$, called modulus
- $a = b \mod N$ if $N$ divides $a -b$
- $a$ and $b$ are congruent modulo $N$

- The set of values produced by postfix operation mod $N$:
  - $\mathbb{Z}/N\mathbb{Z} = \{ 0, 1, \dotsc, N-1\}$
  - Or $\mathbb{Z}_N$
- $\#$ denotes the number of elements in a set
  - $\#(\mathbb{Z}/N\mathbb{Z})=N$

### Properties

1. Addition is closed: $\forall a,b\in \mathbb{Z}/N\mathbb{Z}: a + b \in \mathbb{Z}/N\mathbb{Z}$
2. Addition is associative: $\forall a,b\in \mathbb{Z}/N\mathbb{Z}: (a+b)+c = a+(b+c)$
3. $0$ is an additive identity: $\forall a \in \mathbb{Z}/N\mathbb{Z}: a + 0 = 0 + a = a$
4. The additive inverse always exists: $\forall a \in \mathbb{Z}/N\mathbb{Z}: a + (N - a) = (N - a) + a = 0$
5. Addition is commutative: $\forall a,b\in \mathbb{Z}/N\mathbb{Z}: a + b = b + a$
6. Multiplication is closed: $\forall a, b \in \mathbb{Z}/N\mathbb{Z}: a \cdot b \in \mathbb{Z}/N\mathbb{Z}$
7. Multiplication is associative: $\forall a,b\in \mathbb{Z}/N\mathbb{Z}: (a \cdot b) \cdot c = a \cdot (b\cdot c)$
8. $1$ is a multiplicative identity: $\forall a \in \mathbb{Z}/N\mathbb{Z}: a \cdot 1 = 1 \cdot a = a$
9. Multiplication and addition satisfy the distributive law: $\forall a,b\in \mathbb{Z}/N\mathbb{Z}: (a+b)\cdot c = a\cdot c + b\cdot c$
10. Multiplication is commutative: $\forall a,b\in\mathbb{Z}/N\mathbb{Z}: a\cdot b = b \cdot a$

### Group

- A A group
  - Is closed
  - Has an identity
  - Is associative
  - Every element has an inverse
- A group which is commutative is called **abelian**
- Properties 1,2,3,4 Group
- Properties 1,2,3,4,5 Abelian Group
- **Examples**:
  - The integers, the reals or the complex numbers under addition. Here the identity is $0$ and the inverse of $x$ is $-x$, since $x+(-x) = 0$

### Group types

- **Multiplicative Group**: group operation is multiplication
  - $(G,x): f = g \cdot h$ and $g^5 = g \cdot g \cdot g \cdot g \cdot g$
- **Additive Group**: group operation is addition
  - $f = g + h$ and $5 \cdot g = g + g + g + g + g$
- **Cyclic Abelian Group**: if there is a special element (generator) from which every other element can be obtained.
  - $G = <g>$: Cyclic group $G$ with a generator $g$
    - Integer under addition $1$ is a generator
      - $7 = 1 + 1 + 1 + 1 + 1 + 1 + 1$
    - Additive group: $h = x \cdot g$
    - Multiplicative group: $h = g^x$

### Rings

- A ring has two operations $(+,\times)$ with properties 1 to 9
- Denoted as $(R,+,\times)$
- If multiplication is commutative (property 10), then the ring is commutative
- Infinite rings: integers, real and complex numbers
- Finite rings: modulo $N$, $\mathbb{Z}/N\mathbb{Z}$
  - An abelian group if you consider only addition
  - A ring if you also consider multiplications

### Divisors

- An integer $a$ divides integer $b$ if and only if $b = k \cdot a$ for some integer $k$
- **Prime**: Integer $p$ is prime if and only if $1$ and $p$ are its only divisors

$$
\frac{3}{2} \mod 7 \equiv 3 \cdot 2^{-1} \mod 7 \equiv 5
$$

$$
2 \cdot x = 1 \implies x = 4
$$

$$
3 \cdot 4 \equiv 5 \mod 7
$$

### Greatest Common Divisor

- **GCD**: $c = \operatorname{gcd}(a,b)$ if and only if $c$ is the largest number that divides both $a$ and $b$
- **Theorem**: Every positive integer can be written as a product of primers in an unique way

### Euler's Totient Function

- What is the solution for $a \cdot x = b \mod N$?
- Compute the greatest common divisor (gcd) of $a$ and $N$
  1. If $\operatorname{gcd}(a,N)=1$ there is exactly one solution
  2. If $\operatorname{gcd}(a,N)=g \ne 1$ and $\operatorname{gcd}(a,N)$ divides $b$, there are $g$ solutions
  3. Otherwise there is no solution

- The number of integers in $\mathbb{Z}/N\mathbb{Z}$ that are co-prime to $N$ is given by Euler's Totient Function:

$$
\phi(N) = \prod_{i=1}^np_i^{e_i - 1}(p_i-1)
$$

where
$$
N = \prod_{i=1}^n p_i^{e_i}
$$
For $\mathbb{Z}_8 = \{0, 1, 2, 3, 4, 5, 6, 7\}$, $\phi(8) = 4 \implies$ there are 4 co-primes in this set

### Multiplicative Inverse Modulo $N$

- Solution for $a\cdot x = b \mod N$
- We need to find $c$ such that $a \cdot c = c\dot a = 1 \mod N$
- Such a $c$ is called the multiplicative inverse modulo $N$ of $a$: $a^{-1}$
- $a^{-1}$ exists only when $\operatorname{gcd}(a,N)=1$

### Fields

- If $N$ is a prime $p$, then all none-zero elements have a multiplicative inverse in $\mathbb{Z}/p\mathbb{Z}$
- Thus, $a \cdot x = b \mod p$ has unique solution
- A ring like $\mathbb{Z}/p\mathbb{Z}$ with all none-zero elements having a multiplicative inverse is called a field

**Definition**: A field is a set with two operations $(G,\times,+)$ such that:

- $(G,+)$ is an abelian group
- $(G\setminus 0,x)$ is an abelian group
- $(G,\times,+)$ satisfies the distribution law

- $(\mathbb{Z}/N\mathbb{Z})^*$ is the set of all elements that are invertible (the set of elements that are co-prime of $N$)

$$
(\mathbb{Z}/N\mathbb{Z})^* = \{x \in \mathbb{Z}/N\mathbb{Z}: \operatorname{gcd}(x,N)=1\}
$$

- The size of $(\mathbb{Z}/N\mathbb{Z})^*$ is $\phi(N)$
- If $N$ is a prime $p$

$$
(\mathbb{Z}/p\mathbb{Z})^* = \{1, \dotsc, p -1\}
$$

### Theorems

- **Lagrange's Theorem**: If $(G,\times)$ is a group of order (size) $n = \# G$ then for all $a$ in $G$ we have $a^n = 1$
- So, if $x$ is in $(\mathbb{Z}/N\mathbb{Z})^*$, then:

$$
x ^{\phi(N)} = 1 \pmod{N}
$$

- **Fermat's Little Theorem**: Suppose $p$ is a prime and $a$ is in $\mathbb{Z}$, then

$$
a^p = a \pmod{p}
$$

## Basic Algorithms

### Greatest Common Divisor

- If we could factor numbers, it would be easy to find gcd
- However, computing factors is not easy

### The Euclidean Algorithm

- Computation of $\operatorname{gcd}(a,b)$
- $a = qb + r$ where $r$ is less than $b$

Set $r_0 = a$ and $r_1 =b$ and compute $r_2,r_3,\dotsc$ by $r_{i+2} = r_i \mod r_{i+1}$ until $r_{m+1}=0$

### Extended Euclidean Algorithm

- For $\operatorname{gcd}(a,b)=r$, this algorithm computes $ax + by=r$
- Hence, for $\operatorname{gcd}(a,N)=d$ where $d=1$ we can compute $ax+yN=1$
- Here $\boldsymbol{x}$ is the multiplicative inverse of $a$ in modulo $N$

- $\operatorname{gcd}(a,b)=ax+by=r$
- If $\operatorname{gcd}(a,b)=1\implies ax+by=1$

> ***
>
> **EXAMPLE**:
>
> - $\operatorname{gcd}(7,11) = 1$
> - $11=7 \cdot 1 + 4$
> - $7 = 4 \cdot 1 + 3$
> - $4 = 3 \cdot 1 + 1$
> - $1 = 4 - 3$: Now go back
> - $1 = 4 - (7 - 4) = 2\cdot 4 - 7$
> - $1 = 2 \cdot (11-7) - 7$
> - $1 = 2 \cdot 11 - 3 \cdot 7$
>
> ***

```{.python caption="Extended Euclidean Algorithm"}
def inverse(a, b):
    (s, s1) = (0, 1)
    (t, t1) = (1, 0)
    (r, r1) = (b, a)
    while r != 0:
        q = r1 // r
        (r1, r) = (r, r1 - q*r)
        (s1, s) = (s, s1 - q*s)
        (t1, t) = (t, t1 - q*t)
    d = r1
    x = t
    y = s
    return d, x, y
```

### CRT: Chinese Remainder Theorem

- Ancient Chinese army needs to be fed
- But how many soldiers are there?

Let $m_1,\dotsc,m_r$ be pairwise relatively prime and let $x = a_i \mod m_i$ for all $i$ and $M = \prod_i^r m_i$. The Chinese Remainder Theorem guarantees a unique solution given by
$$
x = \sum_{i=1}^r a_iM_iy_i \mod M
$$
where
$$
M_i = M/m_i
$$
and
$$
y_i = M_i^{-1} \mod m_i
$$
