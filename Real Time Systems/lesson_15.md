# Lesson 15 - WCET analysis

## Estimating the worst-case execution time (WCET)

### Execution time analysis

Timing analysis must be carried out for:

- Program code and libraries
- Real-time operating systems code
- Virtual machine code
- Hardware

#### Execution time distribution

- Testing provides realistic, feasible execution times, but it is not safe
- Static methods (WCET analysis) give _guaranteed upper bound_ on the execution time, but **over estimate** the actual worst-case execution time

#### Main sources of over-approximation

- **Hardware**:
    - Precise modeling of hardware state is impossible in practice
    - Abstractions (simplifications) are necessary, however, these abstractions must be pessimistic, in order to get a safe upper bound
- **Software**:
    - Some execution of the code are infeasible, because of the program semantics
    - Considering infeasible executions may lead to a false WCET

### Main approaches for timing analysis

**Static** timing analysis: Look at the code, software stack, and the hardware platform and "analyze" the worst-case execution time. Static timing analysis is always "safe", if it is performed correctly, the prediction is always worse than the real worst case.

**Dynamic** timing analysis: Execute the code and measure the time it takes. Dynamic timing analysis is always "unsafe", the prediction is always lower than the real worst case.

### Dynamic timing analysis

- What you don't execute you cannot measure
- What you don't cover you cannot execute

#### Basic coverage idea

- **Function coverage**: Has each function in the program been called?
- **Statement coverage**: Has each statement in the program been called?
- **Branch coverage**: Has each branch of each control structure been executed?
    - For example, given an `if` statement, have both the `then`  and `else` branches been executed?
- **Condition coverage**: Has each boolean sub-expression evaluated to both `true` and `false`?
- **Parameter value coverage**: Have all the common values for the parameters been considered?
    - `null`, empty, whitespace, valid string, invalid string...
- **Other**:
  - Path coverage
  - Entry/exit coverage
  - Loop coverage
  - State coverage
  - Data-flow coverage

> Doing these many measurements (tests) manually is hard, time consuming and error prone

### Static timing analysis

**Characteristics**:

Assumes that the time for all parts of a program can be calculated

- Deterministic hardware
- Deterministic system calls
- Deterministic programming constructs

> For arbitrary (and complex) programs and platforms the static timing analysis may become extremely pessimistic $\implies$ it works better with deterministic programs and platforms

### WCET analysis (static)

**Timing analysis problem**: Given a binary code and a precise model of the hardware find an upper bound of the execution time.

The "right" structure to start with: **Control Flow Graphs (CFG)**:

- Identify Basic Blocks (BB)
- Represent the control flow with transitions connecting the BB

#### Classical WCET tool organization

- Micro-architecture analysis
    1. Control Flow Graph construction
        - Basic blocks of sequential instructions
        - Connected by edges
    2. Assign a local WCET to each BB/edge  
        - Instruction specification
        - Harware state
        - Flow history

This is not enough because it does not include how task are executed together on the platform. For example, preemptions influence the state of cache:

- Derive a pessimistic upper bound on the instruction execution times
- Better analysis for hardware interference

#### WCET calculation

- Given: the longest time required for each instruction to be performed independently from other instructions
- Find: an upper bound on the WCET

**Case analysis**:

- Sequence of simple constructs: Assume that $WCET(i)$ denotes the time required to perform the instruction $i$. 
    - Sum of the estimations for the simple constructs in the sequence:
$$
WCET \le \sum_{i=1}^n WCET(i)
$$
- Alternative construct (if-then-else)
    - Time for the evaluation of the condition
    - Plus the maximum of the two alternatives
$$
WCET \le WCET(\text{condition}) + 
\max(WCET(\text{construct}_1), WCET(\text{construct}_2))
$$
- Iteration-bounded loop
    - Time for condition evaluation, multiplied by the maximal number of iterations
    - Loop body multiplied by the max number of iterations
- Time-bounded loop
    - Maximum time specified for the loop

### Deterministic programs

- **Loops**
    - It must be guaranteed that every loop terminates
        - Predetermined by the number of iterations
        - Predetermined by the amount of time
- **Recursion**
    - It must be guaranteed that the recursion stops
        - Predetermined call depth
        - Implies bounded stack space
    - Difficult to extract from code
        - Forbid recursion

## Engineering guidelines and standards

### Coding standards

> Code for safety-critical systems must be certified by a certification authority that certifies that a software product complies with the requirements

**Safety-critical** means that a failure or a design error could cause a risk to human life. In order to be certified, safety-critical software must comply with given coding standards. For example:

- DO-178 is uses for avionic/aerospace applications
- EN 50128 is used for railway systems
- MISRA is used for automotive systems

### Safety integrity levels (SIL)

> The safety level associated with a safety-critical code is measured by a Safety Integrity Level (SIL) in terms of _probability of failure per hour_ (PFH). Most safety-critical systems require a SIL4 certification for the control software.

SIL | PFH
-|-
SIL0 | $> 10^{-5}$
SIL1 | $10^{-5} - 10^{-6}$
SIL2 | $10^{-7} - 10^{-8}$
SIL3 | $10^{-9} - 10^{-10}$
SIL4 | $10^{-11} - 10^{-12}$

### Code complexity

> _The complexity of an object is a measure of the mental effort required to understand and create that object_. [Myers, 1976]

> _Code complexity is a major cause of unreliability in software_ [McCabe, 1976]

### Coding standards

- To produce software that has to be certified SIL4, programmers must follow some specific guidelines
- They can be distinguished in:
    - **Coding rules**: they limit the use of the language constructs that can be dangerous
    - **Coding styles**: they are meant to improve code readability and maintainability

#### Coding rules

The Motor Industry Software Reliability Association (MISRA) provided some guidelines for the use of C language in safety-critical systems.

## Coding styles

Programming style is fundamental for many reasons:

- It simplifies program reading and comprehension
- It facilitates program maintenance
- It reduces the possibility of making mistakes
- It allows quickly identifying syntactic and semantic errors
- It avoids irritating project reviewers

**Adopt these rules from the beginning**

Style rules concern the following aspects:

- Horizontal spacing: rules to follow to separate objects contained in the same line of code
- Vertical spacing: it refers to the use of newline to separate groups of statements
- Indentation: it refers to the space put at the beginning of a line.
- Comments: must be used to explain the meaning of variables and functionality of parts of the program
- Code organization:
    - Organize according to the following order:
        1. Header files
        2. Global constants
        3. Function prototypes
        4. Global data structures
        5. Functions definitions
        6. Tasks definitions
        7. Main function 
    - Any function should NOT be longer than one page
      - If so, it means that you should define a new auxiliary function
      - A program should be self explanatory by the sequence of functions it contains


