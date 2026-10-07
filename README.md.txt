# Chaotic Double Pendulum:
Symbolic Derivation, Numerical Integration & Phase Space Analysis

An end-to-end computational physics pipeline to modeling, anaimating, and analyzing a non-linear chaotic double pendulum system.

This repository performs symbolic lagrangian mechanics via SymPy, integrates the non-linear differential equations using adaptive Runge-Kutta solver (solve_ivp), verifies energy conservation, quantifies deterministic chaos via initial condition sensititvity, and enforces code correctness through an adaptive pytest suite.
---

## Technical Overview and Features

* Symbolic Mechanics (src/dervive_equations.py): Formulates the Lagrangian L = T - V and solves the Euler-Lagrange equations to extract analytical expressions for angular accelerations alpha1, alpha2.
* High-Precision ODE Solver (src/simulate_pendulum.py): Converts 2nd-order non-linear ODEs into 1st-order system integrated via the explicit Runge-Kutta method of order 5(4) (RK45).
* Physics and Sensitivity Analysis (src/analyze_the_physics.py): Calculates fractional energy drift (E(t) - E0)/E0, plots sensitive dependence on initial conditions (delta_theta0 = 10^-3 rad), and constructs state phase portraits (omega2 vs. theta2).
* Dynamic Visualization (src/animate_pendulum.py): Generates smooth animation sequences and exports animated visual assets (double_pendulum.gif).
* Automated Physical Validation (tests/test_pendulum.py): pytest framework checking static equilibrium states, small-angle linearization limits, and analytical energy functions.
---

## System Visualizations & Analysis

### 1. Dynamic Simulation 
![Double Pendulum Animation](assets/double_pendulum.gif)

### 2. Numerical and Physical Verification
| Energy Drift Analysis | Chaos Sensitivity Analysis | Phase Space Trajectory |
| :---: | :---: | :---: |
| ![Energy Drift](assets/energy_drift.png) | ![Chaos Sensitivity](assets/chaos_sensitivity.png) | ![Phase Space](assets/phase_space.png) |
---

## Mathematical Formulation

The configuration of the double pendulum is defined by two generalized coordinates: angles theta1 and theta2 measured relative to the vertical axis.

### Position Coordinates
for two rigid arms of length l1, l2 and point masses m1, m2:

x1 = l1 * sin(theta1), y1 = -l1 * cos(theta1)
x2 = l1 * sin(theta1) + l2 * sin(theta2), y2 = -l1 * cos(theta1) - l2 * cos(theta2)

### The Lagrangian (L = T - V)
Kinetic Energy (T) and Potential Energy (V) are expressed as:

T = 0.5 * m1 * l1^2 * omega1^2 + 0.5 * m2 * [l1^2 * omega1^2 + l2^2 * omega2^2 + 2 * l1 * l2 * omega1 * omega2 * cos(theta1 - theta2)]
V = -(m1 + m2) * g * l1 * cos(theta1) - m2 * g * l2 * cos(theta2)

Applying the Euler-Lagrange equations yields two coupled, non-linear second-order ordinary ordinary differential equations solved numerically in first-order state-space representation y = [theta1, omega1, theta2, omega2].
---

## Project Directory Layout

double-pendulum-simulation/
|
|-- src/
|   |-- derive_equations.py
|   |-- simulate_pendulum.py
|   |-- animate_pendulum.py
|   \-- analyze_the_physics.py
|
|-- tests/
|   \-- test_pendulum.py
|
|-- assets/
|   |-- double_pendulum.gif
|   |-- energy_drift.png
|   |-- chaos_sensitivity.png
|   \-- phase_space.png
|
|-- requirements.txt
\-- README.md
---

## Installation & Execution Guide

### 1. Clone the Repository
git clone [https://github.com/your-username/double-pendulum-simulation.git](https://github.com/your-username/double-pendulum-simulation.git)
cd double-pendulum-simulation

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run Physics Analysis & Export Figures
python src/analyze_the_physics.py

###4. Execute Unit Test Suite
pytest tests/

 