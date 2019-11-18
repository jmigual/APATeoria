# Lecture 2 - Software defined networking

OSPF 

### Traditional routing: Disadvantages

- Difficult to make changes
- Static
- Dependent on hardware (vendors)
- Constant communication between routers

## SDN

Decouple control plane from data plane

- Centralize the network control and let the switches do what they do best

### SDN Elements

- Controllers
  - Centralized decision making
  - Programmable
- Switches
  - Dumb (cheap)
  - Forwarding rules configured by controller

### Advantages

- Programmable
  - Flexible
  - Fine-grained traffic management
- Centralized view of network, so easier to:
  - Compute paths/trees
  - Add security
  - Provide fault tolerance

### Disadvantages

- Centralized
  - Single point of failure (Multiple controllers possible)
  - Security issue
- Scalability
  - Memory (switches)
  - Processing power (controller)
- Initial delay when installing flows reactively

### Currently used by

- Google
- ISPs
- Data centers
- You (exercises)