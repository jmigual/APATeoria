# Lecture 7: Hash functions and MACs

CIA:

- Confidentiality
- Integrity
- Availability

## Hash Functions

- Integrity protection
  - Strong checksum
  - For file system integrity or software downloads
- One-way 'encryption'
  - Password protection
- Asymmetric digital signatrue
- MAC - message authentication code
  - Efficient symmetric 'digital signature'
- Key derivation
- Pseudo-random number generator

### Preimage Resistance

- Takes an arbitrary length input and the output is fixed

- Hash functions:

  - receive an arbitrary length bit strings
  - output a fixed length string called: hash value, digest,  hashcode

- **Cryptographic** hash functions

  - One-way: easy to compute $y$ given $x$ but infeasible to find $x$ given $y: H: \{0,1\}^*\rightarrow\{0,1\}^n$

  $$
  H(x) = y
  $$

- Or more formally, it should be preimage resistant: given an output of $t$ bits, it should take $O(2^t)$ time to find a preimage ($x$ is preimage of $y$)

### Second Preimage Resistance

- A (cryptographic) hash function should also be second preimage resistant: Given $m$, it should be hard to find an $m'$ which is $H(m)=H(m')$.

![Security game for second preimage resistance](images/07/second_preimage_game.png){width=60%}

- We need to make it infeaseable to find the second preimage

### Collision Resistance

- Assume Domain is much larger than Codomain
- Given $H$, it should be infeasible to compute $m$ and $m'$ such that $H(m)=H(m')$

![Security game for collision resistance of a function](images/07/collision_game.png){width=60%}

- The adversary will compute multiple hashes and compare all against each other. So collision resistance is difficult to achieve