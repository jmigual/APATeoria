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

