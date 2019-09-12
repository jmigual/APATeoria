# Lecture 2: Classical systems

## Cryptography

- Dictionary definition: "the art of writing and solving codes"
- Katz and Lindell: "the study of mathematical techniques for securing digital information, systems and distributed computations against adversarial attacks"

### Settling 1: Secure communication

We have two parties that want to communicate securely (Alice and Bob) and we have a third party (Eve) that's trying to get some of the information, can be active or passive

### Settling 2: Secure data storage

Alice has some piece of data that she wants to store it in a secure storage in an encrypted way. Eve wants to access the storage so we have to protect the storage against an attacker.

## The syntax of encryption

- Message space: $M$
- All possible key space: $K$
- Ciphertext space: $C$
- Three algorithms:
  - Key generation: **Gen** a probabilistic algorithm that outputs a key $k$ chosen according to some distribution
  - Encryption: **Enc** takes a key $k$ and a message $m$ and outputs a ciphertext $c$
  - Decryption: **Dec** takes as input a key and a ciphertext $c$ and outputs $m$
- Notation:

$$
\begin{aligned}
c &= Enc_k(m) \\
m &= Dec_k(c)
\end{aligned}
$$

- Correctness requirement:

$$
\forall k; \text{output by Gen},\ m \in M
$$

$$
Dec_k(Enc_k(m)) = m
$$

### Kerckhoffs Principle

> The cipher method must **not** be required to be secret, and it must be able to fall into the hands of the enemy without inconvenience

The only secret part should be the key

## Classical Ciphers

### Caesar Cipher

- One of the oldest recorded ciphers
- Alphabet is shifted 3 letters, so the secret key is known

$$
\begin{aligned}
Enc_{k=3}(M) &= M + 3 \mod{26} \\
Dec_{k=3}(C) &= C - 3 \mod{26}
\end{aligned}
$$

It can be broken because we know that the key is 3

### Shift Cipher

- Keyed variant of Caesar cipher: key can take value between 0-26
- Assign numbers to the letters of the alphabet

$$
\begin{aligned}
Enc_{k}(M) &= M + k \mod{26} \\
Dec_{k}(C) &= C - k \mod{26}
\end{aligned}
$$

### Brute-force attack

Also exhaustion search attack. Try every possible key, the shift cipher can be broken with that because there's only 26 possible keys.

How do you decide the right key size to avoid brute-force attacks? There are international standards

### Shift-cipher cryptanalysis

- English letter frequencies
- English Bigram frequencies

#### Statistical distance

$$
\Delta[X, Y] = \frac{1}{2} \sum_{u \in V} \left|\Pr_{X \leftarrow D_1}[X = u] - 
\Pr_{Y \leftarrow D_2}[Y = u]\right|
$$

- $X$ and $Y$: random variables with distributions $D_1$ and $D_2$ respectively
- $V$: set of values that $X$ and $Y$ can occur with non-zero probability

### Substitution Cipher

- The key space consists of all bijections or permutations
- Also known as mono-alphabetic substitution cipher
- Key space is: $26! \approx 4.03 \times 10^{26} \approx 2^{88}$ so it is secure against brute-force attacks
- But ... using letter frequencies, the puzzle can be solved easily

### Vigenère Cipher

- Giovan Battista Bellasco in 1533
- Poly-alphabetic substitution cipher: encrypting each letter with a different alphabet
- Still ... cryptanalysis easy
- **Kasiski Test** find the occurrences of the repeated sequences and use $\gcd$ to determine the key length

### Permutation Cipher

- A set of letters is permuted

### Summary

- All historical, classical systems have been broken
- They rely on substitution and permutation
- Designing secure ciphers is hard

# Lecture 3: Information Theoretic Security

## Security

- **Computationally secure** it takes $N$ operations using the _best known algorithm_ to break a cryptographic system and $N$ is too large to be feasible
- **Probably secure**: breaking the system is reduced to solving some well-studied hard problem
- The key size is important
- Advances in computer hardware and algorithms are important
- In the future, it will be broken due to hardware or better algorithms
- **Unconditional security** (perfect security or information theoretic security): Even an adversary with unlimited computational power cannot break the cryptographic system

## Probability and ciphers

- Let $P$ denote the set of plaintexts
- Let $K$ denote the set of keys
- Let $C$ denote the set of ciphertexts
- $\Pr(P=m)$ the probability of plaintext being $m$

$$
\Pr(C = c) = \sum_{k :c \in \mathbb{C}(k)} \Pr(K = k) \cdot \Pr(P = Dec_k(c))
$$

- What is the probability that $c$ is the ciphertext given that $m$ is the plaintext:

$$
\Pr(C = c | P = m) = \sum_{k:m=Dec_k(c)} \Pr(K = k)
$$

- What is the probability that the plaintext is $m$ given that the ciphertext is $c$?

$$
\Pr(P = m | C = c) = \frac{\Pr(P = m) \cdot \Pr(C = c | P = m)}{\Pr(C = c)}
$$

## Perfect secrecy

- In the previous example, the ciphertext reveals a lot of information about the plaintext
- We want a system in which ciphertext does not reveal anything about the plaintext
- **Definition** perfect secrecy: a crypto-system has perfect secrecy if:

$$
\Pr(P=m|C=c) = \Pr(P=m)
$$

for all plaintexts $m$ and ciphertexts $c$

**Lemma**: Assume the crypto system is perfectly secure, then
$$
\#K \ge \#C \ge \#P
$$
Where $\#$ denotes the number of items in the corresponding set

**Note**: Proof is an assignment for the students

## Shannon's Theorem

Let $(P,C,K,e_k(), d_k())$ denote a cryptosystem with $\#P=\#C=\#K$. Then the crypto system provides perfect secrecy if and only if

- Every key is used with equal probability $\frac{1}{\#K}$
- For each $m\in P$ and $c \in C$, there is a unique key $k$ such that $e_k(m) = c$

## Modified Shift Cipher

- A shift cipher with a random key of the same length with the plaintext ($m$)

$$
\#K = \#P = \#C = 26^n
$$

- And $\Pr(K = k) = \frac{1}{26^n}$
- Vernam cipher, 1917, one-time pad is perfectly secure $c = m \oplus k$

## Entropy (Uncertainty)

- Perfect secrecy is not practical - due to key distribution problem
- We need a crypto system
  - One key can be used many times
  - A small key can encrypt a long message
- Such a system is not perfectly secure but it should be computationally secure
- We need to measure the amount of information first - Shannon's entropy

### Uncertainty and information

- For a specific question $X$: "Will you go out with me?"
  - Answer **Yes** or **No**
  - If I always answer No, the amount of information, $H(X)$ is 0
  - If I say Yes or No with equal probability $H(X) =1$
- $H()$ is the entropy
- _Independent_ of the length $X$

### Shannon's Entropy

**Definition**: Entropy. Let $X$ be a random variable which takes a finite set of values $x_i$, with $1 \le i \le n$ and has probability of distribution $\p_i = \Pr(X=x_i)$, where we use the conversion that if $\p_i = 0$ then $\p_i \log_2 \p_i = 0$. The entropy of $X$ is defined to be:
$$
H(X) = - \sum_{i = 1}^n p_i \cdot \log_2 p_i
$$

### Properties of Entropy

- $H(X) \ge 0$
- $H(X) = 0$ if $p_i = 1$ and $p_j = 0$ for $i \ne j$
- If $p_i = \frac{1}{n}$ for all $i$ then $H(X) = \log_2 n$

> ***
>
> **EXAMPLE**: Coin tossing
>
> - $\Pr(\text{head}) = p$
> - $\Pr(\text{tail}) = 1 - p \quad, \quad 0 \le p \le 1$
> - What is the formula for entropy?
>
> $$
> H(p) = -p \log_2 p - (1 - p) \log_2(1 - p)
> $$
>
> - What is $H(p)$ when $p$ is $\frac{1}{2}$?
>
> $$
> H\left(\frac{1}{2}\right) = -\frac{1}{2}\log_2 \frac{1}{2} - \left(1 - \frac{1}{2}\right)\log_2\left(1 - \frac{1}{2}\right) = 1
> $$
>
> - What is $H(p)$ when $p$ is $\frac{1}{4}$?
>
> $$
> H\left(\frac{1}{4}\right) = -\frac{1}{4}\log_2\frac{1}{4} - \left(1 - \frac{1}{4}\right)\log_2\left(1 - \frac{1}{4}\right) = 0.8113
> $$
>
> When things are equiprobable the information you get is more valuable while when they are not, the information you get is less important.
>
> | Two tossings | Probability    | Representation |
> | ------------ | -------------- | -------------- |
> | `hh`         | $\frac{1}{16}$ | `111`          |
> | `ht`         | $\frac{3}{16}$ | `110`          |
> | `th`         | $\frac{3}{16}$ | `10`           |
> | `tt`         | $\frac{9}{16}$ | `0`            |
>
> - What is the expected length of 2 tossings?
>
> $$
> \frac{1}{16}3 + \frac{3}{16}3 + \frac{3}{16}2 + \frac{9}{16}1 = \frac{27}{16} = 1.6875
> $$
>
> 
>
> ***