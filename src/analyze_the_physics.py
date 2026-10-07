# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:43:12 2026

@author: Ebiringa
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#Define physical constants
g = 9.81
m1, m2 = 1.0, 1.0
l1, l2 = 1.0, 1.0

def double_pendulum_equations(t,y):
    """
    Evaluate the first-order ODE system for the double pendulum
    State vector y = [theta1, omega1, theta2, omega2]
    """
    t1, w1, t2, w2 = y
    delta = t1 - t2
    
    #Common denominators for angula accelerations
    den1 = l1*(2*m1 + m2 - m2*np.cos(2*t1 - 2*t2))
    den2 = l2*(2*m1 + m2 - m2*np.cos(2*t1 - 2*t2))
    
    #Angular acceleration 1 (alpha1 = d(omega1)/dt)
    num1 = -g*(2*m1 + m2)*np.sin(t1) - m2*g*np.sin(t1 - 2*t2) - 2*np.sin(delta)*m2*(w2*w2*l2 + w1*w1*l1*np.cos(delta))
    alpha1 = num1/den1
    
    #Angular acceleration 2 (alpha2 = d(omega2)/dt)
    num2 = 2*np.sin(delta)*(w1*w1*l1*(m1 + m2) + g*(m1 + m2)*np.cos(t1) + w2*w2*l2*m2*np.cos(delta))
    alpha2 = num2/den2
    
    return [w1, alpha1, w2, alpha2]

def compute_total_energy(t1, w1, t2, w2):
    """
    Calculates total energy E = T + V for each time step
    """
    
    #Kinetic Energy (T)
    T = 0.5*m1*(l1*w1)**2 + 0.5*m2*((l1*w1)**2 + (l2*w2)**2 + 2*l1*l2*w1*w2*np.cos(t1-t2))
    
    #Potential Energy(V) wrt pivot at y = 0
    V = -(m1 + m2)*g*l1*np.cos(t1) - m2*g*l2*np.cos(t2)
    
    return T + V

#Simulation setup
t_span = (0, 30)
t_eval = np.linspace(t_span[0], t_span[1], 3000)

#Trajectory 1 (Base initial condition; both arms horizontally at 90 degrees)
y0_1 = [np.pi/2, 0.0, np.pi/2, 0.0]
sol1 = solve_ivp(double_pendulum_equations, t_span, y0_1, t_eval=t_eval, rtol=1e-9, atol=1e-9)

#Trajectory 2 (Slightly perturbed initial condition: delta_theta = 0.001rad)
y0_2 = [np.pi/2 + 0.001, 0.0, np.pi/2, 0.0]
sol2 = solve_ivp(double_pendulum_equations, t_span, y0_2, t_eval=t_eval, rtol=1e-9, atol=1e-9)

#Extract time-series vectors explicitly
t1_1, w1_1, t2_1, w2_1 = sol1.y[0], sol1.y[1], sol1.y[2], sol1.y[3]
t1_2, w1_2, t2_2, w2_2 = sol2.y[0], sol2.y[1], sol2.y[2], sol2.y[3]

#Compute Energy
E1 = compute_total_energy(t1_1, w1_1, t2_1, w2_1)
E_drift = (E1 - E1[0])/E1[0]       #This is the fractional energy error

#Compute trajectory divergence
delta_theta = np.sqrt((t1_1 - t1_2)**2 + (t2_1 - t2_2)**2)

#Plotting Analysis:

#Figure 1: Energy Drift
plt.figure()
plt.plot(sol1.t, E_drift, 'r-')
plt.title("Energy Drift analysis: (E(t) - E0)/E0")
plt.xlabel("Time(s)")
plt.ylabel("Fractional Error")
plt.grid(True)
    
#Figure 2: Chaos Sensitivity
plt.figure()    
plt.semilogy(sol1.t, delta_theta, 'm-')
plt.title("Sensitivity to initial conditions")
plt.xlabel("Time(s)")
plt.ylabel("Angular Separation delta_theta (rad)")
plt.grid(True)

#Figure 3: Phase Space Trajectory
plt.figure()
plt.plot(t2_1, w2_1, 'b-', linewidth=0.5)
plt.title("Phase Space Portrait (Omega2 vs theta2")
plt.xlabel("theta2 (rad)")
plt.ylabel("Omega2 (rad/s)")
plt.grid(True)

#Save Figure 1: Energy Drift
plt.figure(1)
plt.savefig("energy_drift.png", dpi=300, bbox_inches='tight')

#Save Figure 2: Chaos Sensitivity
plt.figure(2)
plt.savefig("chaos_sensitivity.png", dpi=300, bbox_inches='tight')

#Save Figure 3: Phase Space
plt.figure(3)
plt.savefig("phase_space.png", dpi=300, bbox_inches='tight')

plt.show()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    