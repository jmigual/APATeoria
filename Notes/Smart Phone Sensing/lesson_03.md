# Lesson 3

## First assignment

- Confusion matrices: As a result we have to show a $2 \times 2$ matrix for accelerometer data and a $4 \times 4$ matrix for localization results
- Picture of App: only a picture is enough
- 1 Page:
    - Don't explain things already known
    - If you use another machine learning method should be explained
- All the code must be on the phone

### Radio map

- Each cell has now a probability mass function (pmf)
- The higher the difference among pmf's the better
- Notice that the big room has two cells

1. .
2. .
3. Store data in phone
4. .
5. Apply Bayes. Probability I am in cell $i$ given that I got an RSS measurement $r$ from access point $j$

$$
P(cell_i|rss_j^r) = \frac{P(cell_i) P(rss_j^r|cell_j)}{P(rss_j^r)}
$$

6. When do I stop iterations?
    - No clear answer
    - At every step you can update _prior_ with
        - data from other access points
        - new scans
    - Stops when you
        - Pass a threshold
        - Reach a "steady state": oscillation around a max $p$

To decide when to stop there are two different approaches:

- **Serial**: You keep multiplying the information by the prior knowledge until you find a good enough value

- **Parallel**: 
    $$
    \begin{aligned}
    \overrightarrow{P}_0 \cdot \overrightarrow{W}_i^r = P_1 \\
    \overrightarrow{P}_1 \cdot \overrightarrow{W}_i^r = P_2 \\
    \cdots \\
    \end{aligned}
    $$
    Then:
    
    
    $$
    P = P_1 + P_2 + \cdots
    $$
    

7. Motion model

## Log Normal Model

