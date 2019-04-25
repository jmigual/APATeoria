# Lesson 1 - Introduction

We will be working with quad-copters. They are dangerous :sweat_smile:

## ES Technology Today

- $\mu$proc + peripherial I/O
- $\mu$controller (all on single chip)
- DSP (same but optimized for signal proc)

## Project: Drone Controller

- Electrical model quad-rotor
- QR: no stabilization, just rotors + sensors
- Lab goal: roll, pitch, yaw stabilization
- Long-term goal: autonomous UAV

## Drone: 

### Euler Angles

We have three angles, we rotate them in the following order: $\varphi, \theta, \phi$ **Stick with the convention** 

![euler_angles](/home/jmigual/Documents/Projects/Teoria/Notes/Embedded Systems Laboratory/images/01/euler_angles.png){width=75%}



### Forces

- Forces: X, Y, Z
- Moments: L, M, N

### Actuators

Rotor 1 to rotor 4 RPM denoted by $\Omega$ driven by ES signals $ae_1 - ae_4$ 
$$
\begin{aligned}
ae &= 0 & \implies \Omega &= 0\\
ae &= 1000 & \implies \Omega &= \max
\end{aligned}
$$


### Dynamics (in hover)

- $T_i$: rotor thrust = $f(\Omega_i)$ 
- $mg$: gravity
- $h$: rotor distance ref. center of gravity
- $I_{\gamma}$: heli rotation inertia in Y-axis
- $X = \sin \Theta mg$ 
- $\frac{dq}{dt} = \frac{M}{I_{\gamma}}$
- $\frac{du}{dt} = \frac{X}{m}$ 

### Rotor actuators

In general:

- $Z = -b (\Omega_1^2 + \Omega_2^2 + \Omega_3^2 + \Omega_4^2)$
- $L = b(\Omega_4^2 - \Omega_2^2)$
- $M = b(\Omega_1^2 - \Omega_3^2)$
- $N = d(\Omega_2^2 + \Omega_4^2 - \Omega_1^2 - \Omega_3^2)$
- So compute $\Omega$ from desired lift ($Z$), roll rate ($L$), pitch rate ($M$), and yaw rate ($N$)

### Sensors

- Gyro: $p, q, r$ 
- Accelerometer: $a_x, a_y, a_z$
- $ax = \sin \Theta mg \sim \Theta mg$
- DMP: $\phi, \theta, \varphi$. Does all the computation for you and gives you the angles directly

### Control circuit

Controlling the **yaw** is hard, while controlling the _pitch_ and _roll_ is easier

> ------
>
> **EXAMPLE** control loop (yaw rate):
>
> ```python
> eps = yaw - sr		// measure deviation
> N_needed = P*eps	// compute ctl action
> ae1 = f(N_needed)	// actuate, see slide 9
> ae2 = f(N_needed)	// For every actuator
> ```
>
> ------

#### Calibration

- Real $p, q, r$ ... are sensed in terms of $sp, sq, sr$, ...
- $sp, sq,$ ... have a (voltage) bias (are not zero at rest)
- so we need to calibrate all 6 sensors at rest:
    - Let $sr_0$ be sensor output at rest
    - Real estimate of $r$ are given by ($z$ for zeroed): $zr = sr - sr_0$ 
- We want to run calibration at least _at the beginning of the flight_

#### Filtering

- Signals also need to be _filtered_ to remove noise
- Filtered signal input to embedded controller

#### Controller modes

- **Manual**
- **Calibrate**
- **Control** (yaw, pitch, roll)





