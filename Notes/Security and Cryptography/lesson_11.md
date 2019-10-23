# Lecture 11: Certificates, Key Transport and Key Agreement

### Secure Communication

- Now we know
  - Symmetric systems
  - Asymmetric systems
  - Integrity (Hash functions, MACs...)
  - To design hybrid systems based on KEM/DEM
- But
  - How to use the same key for symmetric encryptions
  - How to obtain the public keys of others?
- We have solutions for that... building cryptographic protocols!

## Key Management

> In a well designed cryptographic system, only the key needs to be secret; there should be no secrecy in the algorithm
>
> Auguste Kerchkhoff, 1883

Using the right cryptographic algorithms, the problem of protecting data is transferred to the problem of protecting keys.

Key management is the backbone of cryptography

### What is Key Management

- Key Generation
- Key Distribution
- Key Storage
- Key Change
- Key Usage
- Key Destruction

### Key Generation

- Requirements
  - Secret
  - Unpredictable
  - Strong key
- Methods
  - Manual (Tossing)
  - (Pseudo) Random Number Generator (FSR)
- Secure hardware, secure room, secure procedures are needed

### Key Freshness

- It is often desirable to frequently change the key in a cryptographic system
  - If a key is exposed (e.g. through hackers), there is limited damage if the key is changed often
  - Some cryptographic attacks become more difficult if only a limited amount of ciphertext was generated under one key
  - If an attacker wants to recover long pieces of ciphertext, he has to recover several keys which makes attacks harder

TODO: Stopped here 1:08:23

