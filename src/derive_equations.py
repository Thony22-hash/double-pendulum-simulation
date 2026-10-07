# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sympy as sp

#Define symbolic variables
t = sp.symbols('t')
g, m1, m2, l1, l2 = sp.symbols('g m1 m2 l1 l2')

#Define Generalized coordinates as functions of time
theta1 = sp.Function('theta1')(t)
theta2 = sp.Function('theta2')(t)

#Define time derivatives (angular velocities and accelerations)
dtheta1 = theta1.diff(t)
dtheta2 = theta2.diff(t)
ddtheta1 = dtheta1.diff(t)
ddtheta2 = dtheta2.diff(t)

#Define cartesian position coordinates
x1 = l1*sp.sin(theta1)
y1 = -l1*sp.cos(theta1)

x2 = x1 + l2*sp.sin(theta2)
y2 = y1 - l2*sp.cos(theta2)

#Define cartesian velocity coordinates (time derivatives of position)
vx1, vy1 = x1.diff(t), y1.diff(t)
vx2, vy2 = x2.diff(t), y2.diff(t)

#Define Kinetic (T) and Potential (V) Energy
T1 = sp.Rational(1, 2)*m1*(vx1**2 + vy1**2)
T2 = sp.Rational(1, 2)*m2*(vx2**2 + vy2**2)
T = sp.simplify(T1 + T2)

V1 = m1*g*y1
V2 = m2*g*y2
V = sp.simplify(V1 + V2)

#Define Lagrangian
L = T - V

#Set up the Euler-Lagrange Equations: d/dt(dL/dtheta_dot) - dL/dtheta = 0
EL1 = sp.diff(sp.diff(L, dtheta1),t) - sp.diff(L, theta1)
EL2 = sp.diff(sp.diff(L, dtheta2), t) - sp.diff(L, theta2)

#Solve for highest derivatives (ddtheta1 and ddtheta2)
solutions = sp.solve([EL1, EL2], (ddtheta1, ddtheta2))

#Extrat angular acceleration expressions
alpha1_ex = sp.simplify(solutions[ddtheta1])
alpha2_ex = sp.simplify(solutions[ddtheta2])

print("--- Angular Acceleration 1 (ddtheta1) ---")
print(alpha1_ex)

print("\n--- Angular Acceleration 2 (ddtheta2) ---")
print(alpha2_ex)

#Print raw LaTeX formatted string for the README.md
print("\n--- LaTeX for README.md ---")
print(f"\\ddot{{\\theta}}_1 = {sp.latex(alpha1_ex)}")
print(f"\\ddot{{\\theta}}_2 = {sp.latex(alpha2_ex)}")

def get_derived_equations():
    return alpha1_ex, alpha2_ex, (theta1, theta2, dtheta1, dtheta2, g, m1, m2, l1, l2)

