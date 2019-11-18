# Lesson 1

## TCP

### Errors

Errors can occur and we need ways to deal with those errors

### Error Control

Three ways:

- Retransmission (ARQ/TCP)
- Forward Error Correction (real-time services): Add some extra information for error correction purposes
- Discard (UDP)

### Time-out and Retransmission

When a packet fails you will not send an ACK

### Sliding Window

Send a batch of packets and acknowledge them in batch too. 

### Transmission Control Protocol (TCP)

- Connection-oriented over connectionless
- Reliable transport
  - Principles of sliding window
  - Positive acknowledgement with retransmission
- Details:
  - Full duplex, ports, connections and endpoints

### TCP is self-clocking

By using the sender has to wait for the acknowledgements then if there's a bottleneck the sender will not continue sending because it will not receive the ACKs due to the bottleneck

### TCP Congestion Window: no loss

On the arrival of an ack:

```{.python caption="Congestion window algorithm"}
if W < sstresh:
    W += 1
else:
    W += 1/W
```

### Multi-Path TCP (MTCP)

Creates one connection for every interface

## Multi Protocol Label Switching (MPLS)

### Concepts

- Forwarding information (label) separate from content of IP header
- Single forwarding paradigm (label swapping) with hierarchy (label stacking) using multiple routing types (L3, L2)
- Flexibility to form forwarding equivalence classes (FEC) related to QoS or VPN
- Traffic engineering (TE): to override IP routing. TE is a powerful mechanism for current ISPs to:
  - Direct traffic away from congested paths
  - Balance traffic across multiple paths
  - Offer QoS in case of failures

### Labels

- Label:
  - Short
  - Fixed-length
  - Local significance
  - Exact match for forwarding
- Forwarding Equivalence Class (FEC):
  - Packets that share the same next hop share the same next label (locally)
- Needs label distribution mechanism

### Labels stacking

- Label stacking allows an indefinite number of labels to be used
- 3 Label operations:
  - Push
  - Pop
  - Swap
- Separates control and forwarding

### (G)MPLS

- Label Distribution Protocol (LDP) or RSVP?
  - LDP can support explicit routing (or QoS constraint routing)
  - RSVP uses the routing tables of current non-QoS-aware routing 
    protocols
- MPLS use cases:
  - Traffic engineering
  - Scalable IP virtual private networks
  - GMPLS: extension to non-packet switching networks (TDM, optical DWDM)

