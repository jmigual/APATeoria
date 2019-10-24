# Lecture 12: Secret Sharing

### Asymmetric Encryption

- Case 1: Alice wants to communicate with her Bank. Bob is an employee at the bank
  - Should you rely on individuals
  - Do you want the secret key to be known to anyone?
- Case 2: Nuclear Missile Launch Code, there are 3 generals
  - Who should have it?
  - One general can be compromised, killed, hijacked, or unreachable

## Threshold Cryptography

- Split the secret key into shares
- A certain number of them can reconstruct the secret key

### Threshold Cryptography: Ideas

- Only one public key known to everyone
  - Everyone can encrypt messages, or verify the signature on messages
- Only one secret key, shared among a specific group of parties
  - No one knows the secret key
  - Only prescribed groups can decrypt ciphertexts, or sign messages
  - **Preferably**: Key is not revealed after decryption/signing
- **Applications**:
  - Group signatures
  - Efficient encryption to dynamic groups
    - Keys need not to be revoked when small changes applied to the group
  - Secure Multiparty Computation (Secure Signal Processing)
  - i.e. computation on encrypted/shared inputs

## Secret Sharing

### Definition

- Dealer ($D$) having secret input ($s$)
- Receiving parties $P_1, \dotsc, P_n$
- Protocols
  - Distribution: Protocol in which the dealer provides each party $P_i$ a share $s_i$
  - Reconstruction: Protocol in which a qualified set of parties pool their shares to obtain a secret $s$
- Dealer is the weakest link in secret sharing
- Security
  - Any qualified set of parties can reconstruct the secret
  - Any non-qualified set of parties cannot deduce **any** information about the secret

### Access Structure

- Access Structure ($\boldsymbol{\Gamma}$): The collection of all groups of parties that can reconstruct
  - Qualified set: a set $Q \in \Gamma$
  - $Q = \{P_{i1},\dotsc, P_{it}\}$
- Monotone Access Structure: If $Q$ is a qualified set then any group containing $Q$ is a qualified set
  - Theorem: For all monotone Access Structures, there exists a corresponding secret sharing scheme
- $(\boldsymbol{t},\boldsymbol{n})$-threshold Secret Sharing Scheme: A secret sharing scheme, where any group $Q \in \Gamma$ if and only if $|Q| \ge t$

> ***
>
> **EXAMPLE**: Bad example
>
> - Splitting the bits of $\boldsymbol{sk}$:
>   - Let $sk$ be an L-bit number
>   - Distribution (2-party):
>     - $P_1$ gets $s_1$ being the $\left\lfloor \frac{L}{2}\right\rfloor$ least significant bits of $sk$
>     - $P_2$ gets $s_2$ being the $\left\lceil \frac{L}{2}\right\rceil$ most significant bits of $sk$
>   - Reconstruction
>     - $P_1$ and $P_2$ compute $sk = s_1||s_2$
> - Both parties learn half of the bits of $\boldsymbol{sk}$
> - How to share bits?
>
> ***

> ***
>
> **EXAMPLE** Sharing a bit
>
> - Suppose that $b \in \{0, 1\}$
>   - Distribution
>     - Pick $u \in \{0,1\}$ uniformly at random, i.e., $P(u=1) = P(u=0) = 1/2$
>     - Party $P_1$ gets $s_1 = u$
>     - Party $P_2$ gets $s_2 = b \oplus u$
>   - Reconstruction
>     - $b = s_1 \oplus s_2$
>   - $P(b = 0|s_1) = P(b=1|s_1) = 1/2$
>   - $P(b=0|s_2) = P(b=1|s_2) =1 /2$
>   - In words: Given one share, each value of the secret bit is equally likely
>   - OR: No information gained by getting one share
>
> ***

### Secret Sharing $(n,n)$-threshold Secret Sharing over $\mathbb{Z}_m$

- Generalising to $\mathbb{Z}_m$:
  - A random variable $X \in \mathbb{Z}_m$ is called uniformly random if $P(X=y)=1/m$ for all $y\in \mathbb{Z}_m$
  - Theorem: Let $Y \in \mathbb{Z}_m$ be a random variable, then $Z = X+Y$ is uniformly random in $\mathbb{Z}_m$
- Suppose that $s \in \mathbb{Z}_m$
  - Distribution
    - Pick $u \dotsc u_{n-1} \in \mathbb{Z}_m$ uniformly at random
    - For $i = 1,\dotsc, n-1$: Party $P_i$ gets $s_i = u_i$
    - Party $P_n$ gets $s_n = s - \sum_{i=1}^{n-1} u_i \pmod{m}$
  - Reconstruction
    - $s = \sum_{i=1}^{n}s_i$

### Secret Sharing $(t,n)$-threshold SSS

$$
P(x) = a_0 + a_1x + a_2x^2 + \dotsb + a_{t-1}x^{t-1}
$$

Theorem Lagrange: Given $t$ distinct points $P$: $(x_1,y_1),\dotsc,(x_t,y_t)$, then $P(x) = \sum_{i=1}^t y_if_i(x)$, where
$$
f_i(x) = \prod_{j\ne i}^t \frac{x_j - x}{x_j - x_i}
$$

$$
f_i(x_k) = 0 \text{ if } i\ne k
$$

$$
f_i(x_i) = 1
$$

Hence: $(x_i, P(x_i)) = (x_i, y_i)$

> ***
>
> **EXAMPLE**: Reconstruct a line
>
> - Given $(1,2)$ and $(2,3)$ over $\mathbb{Z}_5$
>
> $$
> L(x) = 2 \cdot \frac{x - 5}{1-2} + 3 \cdot \frac{x-1}{2-1} = 1 + x \mod 5
> $$
>
> - With only 1 point, there are infinite number of lines possible
>
> ***

### In General

- Theorem
  - Let $P(x)$ be a polynomial of degree $t-1$ over $\mathbb{Z}_p$
  - Let $S$ be a set of $t-1$ points of $P(x)$, such that $(0, P(0)) \notin S$
  - Then $S$ does not reveal any information about $P(0)$
- Proof:
  - For any $y \in \mathbb{Z}_p$
  - Lagrange Interpolation on $(0, y) \cup S$
  - Returns a degree $t-1$ polynomial through the points in $S$ intersecting the y-axis in $y$

### Shamir Secret Sharing

- Suppose $s \in \mathbb{Z}_p$, where $p$ is prime

- **Distribution**:

  - The Dealer picks $a_1, \dotsc, a_{t-1}$ uniformly random from $\mathbb{Z}_p$ and defines $P(x) = s + a_1x + \dotsb + a_{t-1}x^{t-1} \mod p$
  - Party $P_i$ gets share $s_i = P(i)$

- **Reconstruction**

  - Let $Q$ be any subgroup of size $t$. For example $\{P_1, \dotsc, P_t\}$
  - Then $s = \sum_{i=1}^t \lambda_is_i\mod p$, where $\lambda_i = \prod_{i\ne j}\frac{j}{j-i}\mod p$
  - **Correctness**
    - Lagrange interpolation over $(1, s_1),\dotsc,(t,s_t)$, with $\lambda_i=f_i(0)$
    - Hence $\sum_{i=1}^t\lambda_i s_i = P(0) = s$

  

### Shared RSA Signature Generation

- Imagine that a company has a secret key $d$ to sign documents
  - It should be split into 3 parts: Asia, Europe, America
  - When they are all online, a document can be signed
- Distribution:
  - Create $d$, and split into 3 shared; $d = d_1 + d_2 + d_3$
  - Delete $d$ and give each shared to the servers in Asia, Europe and America
- Reconstruction
  - Use the multiplicative homomorphism of the scheme
- **Problems**?

- What about 2 servers being online?
- Definitely $(2,3)$-threshold SSS
  - However, $\phi(n)$ should be secret
  - Denominator might not be co-prime to $\phi(n)$

- By Shoup
- $(t,n)$-threshold RSA Signature Scheme
- Generate a polynomial of degree $t-1$
- $e$ is a prime and $e > $n
  1. Compute points on the polynomial
  2. Each server signs partially a document
  3. User received the shared and constructs the signature from $t$ shares

$$
f(x) = d + f_1x + f_2x^2 + \dotsb + f_{t-1}x^{t-1}
$$

$$
\Delta = n!
$$

$$
s_i = m^{2\Delta d_i} \mod N
$$

$$
\begin{aligned}
\sigma &= \prod_t s_i^{2\Delta r_y} \mod N \\
& = (m^{2\Delta d_i})^{2\Delta \sum_t r_y} \\
&= (m^{4\Delta^2})^{\sum r_y d_i} = m^{4\Delta^2d}
\end{aligned}
$$

$$
e, 4\Delta^2 \rightarrow u \cdot e + v\cdot 4\Delta ^2 = 1 \text{ euclidean algorithm}
$$


$$
s \leftarrow m^u\sigma^v \mod N
$$
