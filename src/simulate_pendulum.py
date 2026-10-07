# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:38:19 2026

@author: Ebiringa
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


#Import derived acceleration expressions directly from the previous file
from derive_equations import get_derived_equations

alpha1_ex, alpha2_ex, (theta1, theta2, dtheta1, dtheta2, g, m1, m2, l1, l2) = get_derived_equations()

#Create dummy angula velocity symbols
w1_sym, w2_sym = sp.symbols('w1 w2')
alpha1_sub = alpha1_ex.subs({dtheta1: w1_sym, dtheta2: w2_sym})
alpha2_sub = alpha2_ex.subs({dtheta1: w1_sym, dtheta2: w2_sym})

#Compile sympy equations into fast fast numerical functions
calc_alpha1 = sp.lambdify((theta1, theta2, w1_sym, w2_sym, g, m1, m2, l1, l2), alpha1_sub, 'numpy')
calc_alpha2 = sp.lambdify((theta1, theta2, w1_sym, w2_sym, g, m1, m2, l1, l2), alpha2_sub, 'numpy')

#Define system parameters: g, m1, m2, l1, l2
parameters = (9.81, 1.0, 1.0, 1.0, 1.0)

#First order system for solve_ivp
def derivatives(t, y, g, m1, m2, l1, l2):
    th1, w1, th2, w2 = y
    a1 = calc_alpha1(th1, th2, w1, w2, g, m1, m2, l1, l2)
    a2 = calc_alpha2(th1, th2, w1, w2, g, m1, m2, l1, l2)
    return [w1, a1, w2, a2]
#Initial conditions: [theta1, omega1, theta2, omega2]
y0 = [np.pi/2, 0.0, np.pi/4, 0.0]

#Time span (30 seconds)
t_span = (0, 30)
t_eval = np.linspace(0, 30, 3000)

#Solve ODE system using RK45
sol = solve_ivp(derivatives, t_span, y0, t_eval=t_eval, args=parameters, method='RK45', rtol=1e-8, atol=1e-8)

#Plot Phase Space (Bob 1)
plt.figure(figsize=(8, 5))
plt.plot(sol.y[0], sol.y[1], color='crimson', lw=0.7)
plt.title("Double Pendulum Phase Space (Bob 1)")
plt.xlabel(r"$\theta_1$ (rad)")
plt.ylabel(r"$\omega_1$ (rad)")
plt.grid(True)
plt.tight_layout()
plt.show()












