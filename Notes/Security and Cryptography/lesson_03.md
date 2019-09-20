# Lecture 4: Defining security

> What does it mean to be "secure"

## Modern Cryptography and 3 key aspects

- **Definitions**: concrete mathematical definition of  what it means for a particular cryptographic mechanism to be secure
- **Schemes**: Design the schemes will meet the security definitions
- **Proofs**: Check whether the design meets the security definitions. "Probable security" or "reductionist security"

### Factoring and related problems

- How easy to factor values?

$$
\begin{aligned}
10 &= 2 \times 5 \\
60 &= 2^2 \times 3 \times 5 \\
2^{113} - 1 &= 3391 \times 23279 \times 1868569 \times 1066818132868207
\end{aligned}
$$

Factorization is an NP-hard problem

> In order to break my system you need to break factorization

- Given only $N$ which is the product of two primes $p$ and $q$
  - **Factor**: find $p$ and $q$
  - **RSA**: Given $e$ and $c$, find $m$
  - **SQRROOT**: Given $a$ such that $a=x^2 \mod N$, find $x$
  - **QUADRES**: (check section 2.2)

### Modular arithmetic

$$
\begin{aligned}
7 \equiv 1 \mod 3 \implies 7 = 3k + 1
\end{aligned}
$$

> ***
>
> **EXAMPLE**
> $$
> \begin{aligned}
> a &\equiv x^2 \mod 7 \\
> 6 &\equiv x^2 \mod 7
> \end{aligned}
> $$
> If I didn't know, I would try all the possible values then I could see that all the possible values are 1, 2 and 4 and thus there's no solution.
>
> ***

$$
\begin{aligned}
\Z_7 &= \{0, 1, 2, 3, 4, 5, 6, 7\} \\
\Z_{8^*} &= \{1, 3, 5, 7\}
\end{aligned}
$$

### Security Games: Factor

We have an adversary $A$
$$
\begin{aligned}
p, q &\leftarrow \{v/\text{2-bit primes}\} \\
N &\leftarrow p\cdot q
\end{aligned}
$$
$A$ knows $N$ and will provide two primes $p'$ and $q'$. Adversary wins if $p' \cdot q' = N$, otherwise it loses.

**Definition**: In all the games $X$ the advantage of an adversary $A$ to be a function of $t$ which she spends trying to solve the input problem.
$$
\operatorname{Adv}_v^X(A,t) = \Pr[A \text{ wins the game }X\text{ for } v = \log_2N \text{ in time less than } t]
$$


### Security Games: RSA

$$
\begin{aligned}
p,q &\leftarrow {v/\text{2-bit primes}} \\
\phi(N) &\leftarrow (p - 1)(q - 1) \\
N &\leftarrow p\cdot q \\
e, d &\leftarrow \Z \text{ s.t. } e \cdot d = 1 \pmod{\phi(N)} \\
y &\leftarrow (\Z/N\Z)^* \\
\end{aligned}
$$

Adversary gets $N, e, y$ and returns $x$. Wins if $x^e = y \pmod{N}$

### Security Games: SQRROOT

$$
\begin{aligned}
p,q&\leftarrow \{v/\text{2-bit primes}\} \\
N &\leftarrow p\cdot q \\
a &\leftarrow Q_N \\
\end{aligned}
$$

Adversary gets $N, a$ and returns $x$. Wins if $x^2 \pmod{N} = a$
$$
\begin{aligned}
\Z_5 &= \{0, 1, 2, 3, 4\} \\
\Z_{5^*} &=\{1, 2, 3, 4\} \\
\Q_5 &= \{1, 4\}
\end{aligned}
$$

### Security Games

$$
\operatorname{Adv}_v^X(A) = 2 \cdot \left|\Pr[A \text{ wins }X\text{ for }v=\log_2 N] - \frac{1}{2}\right|
$$

### Equivalent problems

- Can compute square roots if you can factor $N$? Yes

### Pseudo-random functions (PRF)

- Can $A$ decide whether $F$ is a PFR or not?
- Randomness is very important because if the adversary guesses your random number then we are done
- Game:
  - Give the random generator function $F$ to the adversary
  - $x \leftarrow D$
  - If $b = 0$ then $y \leftarrow C$
  - If $b=1$ then $y \leftarrow F(x)$
  - Give $x, y$ to adversary which returns $b'$
  - Adversary wins if $b' = b$
  - **Adversary always wins this game**

Kerkchoff's principle: Everything you use should be public except the key you use

## One-Way Functions and Trapdoor One-Way Functions

- One-Way Functions
  - Easy to compuute
  - it's hard to go reverse and get the original value
- Trapdoor One-Way Functions
  - Extra information helps revert the function

## Public Key Cryptography

- Key distribution problem is symmetric
- A key pair is needed
  - Private key for decryption
  - Public key for encryption
- Public keys are linked in a mathematical way
  - Obtaining private key from public key is NOT easy
  - Obtaining public key from private key is easy

### Security of Encryption

- The goal of the adversary
- The types attacks allowed
- The computational model

## Basic notions of security

- Notation and valid encryption

$$
\forall k \in \mathbb{K}, \forall m \in \mathbb{P}, d_k(e_k(m)) = m
$$

- Adversary should not learn the underlying message

### Modern notions of security

- Adversary can also partially break the system
- The adversary should not be allowed to obtain **any** information about the plaintext
  - Perfect security
  - Semantic security
  - IND security (indistinguishability of encryptions, polynomial security)
- Perfect security: Not practical
- Semantic security: Like perfect security but the adversary has polynomially bounded computing power

$$
\begin{aligned}
g:M &\rightarrow\{0, 1\} \\
\Pr[g(m) = 1] &= \Pr[g(m) =0] = \frac{1}{2} \\
\operatorname{Adv}_{\prod}^{\text{SEM}}(S) &= 2 \cdot \left|\Pr[S(c)=g(d_k(c))]-\frac{1}{2}\right|
\end{aligned}
$$

### IND Security

- Semantic security is difficult to show
- Polinomial security (IND) is easier to show
- If a system is IND secure, it is also semantically secure
- Types:
  - IND-PASS
  - IND-CPA: Chosen Plaintext Attack
  - IND-CCA: Chosen Ciphertext Attack
- A system has indistinguishable encryptions. Play a game
  - Find: Adversary generates two messages
  - Guess: Adversary receives a ciphertext. She needs to guest the correct message with a probability higher than half 

$$
\begin{aligned}
k &\leftarrow KeyGen() \\
b &\leftarrow \{0, 1\} \\
\end{aligned}
$$

- Oracle ($\mathcal{O}_{LR}$) gets two messages ($m_0, m_1 \in \mathbb{P}$), will choose one and will provide a ciphertext based on $b$. $c^* \leftarrow e_k(m_b)$
- Oracle ($\mathcal{O}_{e_k}$) gets $m \in \mathbb{P}$ and returns $c \leftarrow e_k(m)$
- Oracle ($\mathcal{O}_{d_k}$) gets $c \in \C$
  - If $c = c^*$ aborts
  - $m \leftarrow d_k(c)$

$$
\operatorname{Adv}_{\prod}^{\text{IND-PASS}}(A) = 2\cdot \left|\Pr[A\text{ wins}]-\frac{1}{2}\right|
$$

- For a system to be IND-CPA secure, it should be probabilistic

  - **Definition**: An encryption algorithm is secure if it is semantically secure against a CPA attack
  - **Definition**: An encryption algorithm is secure if it is IND-CCA secure
  - **Theorem**: A system which is IND-PASS secure must be semantically secure against passive adversaries

  $$
  \Pi\text{ is IND-CCA} \implies \Pi\text{ is IND-CPA}\implies\Pi\text{ is IND-PASS}
  $$

  $$
  \Pi\text{ is IND-XXX}\implies\Pi\text{ is OW-XXX}
  $$

  

### Other notions of Security

- **Many Time Security**: How many times can we use the LR oracle?
- **Real-or-Random**: Oracle encrypts either the real message or a random message of same size
- **Lunchtime Attacks**: (CCA1) Adversary has decryption oracle during the find stage for some time
- **Nonce-Based Encryption**: Deterministic algorithms are not IND-CPA secure. Therefore, nonce (number used once) should be used
- **Data Encapsulation Mechanism**: Symmetric system but key is used once
- **Non-malleability**: Given a ciphertext of an unknown plaintext, the adversary can compute a new ciphertext for a *related* plaintext
- **Plaintext aware**: One needs to know the plaintext to encrypt

