# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:05:19 2026

@author: Ebiringa
"""

import numpy as np
import pytest

#Import the derivative and energy functions from the analysis script
from analyze_the_physics import double_pendulum_equations, compute_total_energy

#Physical constants matching the simulation
g = 9.81
m1, m2 = 1.0, 1.0
l1, l2 = 1.0, 1.0

def test_equilibrium_state():
    """
   Test 1: Verification of Static Equilibrium:
   A pendulum at rest pointing straight down (all states zero) must experience zero angular acceleration
    """
    y_rest = [0.0, 0.0, 0.0, 0.0]
    derivs = double_pendulum_equations(0, y_rest)
    
    #Derivs return [w1, alpha1, w2, alpha2]
    
    np.testing.assert_allclose(derivs, [0.0, 0.0, 0.0, 0.0], atol=1e-12, 
        err_msg="Equilibrium state failed: non-zero derivatives found at rest")
    
def test_small_angle_linearization():
    """
    Test 2: Small-Angle approximation limit:
    For theta1 displaced by small_angle with theta2=0, w1=0, w2=0:
    The full equations evaluate to alpha1 = -2*(g/l1)*theta1
    """
    small_angle = 1e-4          #0.0001 radians
    y_small = [small_angle, 0.0, 0.0, 0.0]      #Only theta1 slightly displaced
    
    #Numerical output from full nonlinear equations
    _, alpha1_num, _, alpha2_num = double_pendulum_equations(0, y_small)
    
    #Analytical small-angle limit prediction for theta1 displacement
    #For m1=m2=1, l1=l1=1 : den1 = 1*(2+1-1) = 2
    #num1 = -g*4*theta1 = -4*g*theta1 -> alpha1 = num1/den1 = -2.0*g*theta1
    alpha1_expected = -2.0*g*small_angle
    
    np.testing.assert_allclose(alpha1_num, alpha1_expected, rtol=1e-3,
    err_msg="Small-angle linearization test failed for alpha1")
    
def test_energy_conservation_initialization():
    """
    Test 3: Energy Function Verification
    Verify that compute_total_energy yields the exact potential energy at maximum deflection
    when initial angular velocities are zero
    """
    t1, w1, t2, w2 = np.pi/2, 0.0, 0.0, 0.0   #theta1 = 90deg, rest = 0
    E_total = compute_total_energy(t1, w1, t2, w2)
    
    #T = 0
    #V = -(m1 + m2)*g*l1*cos(pi/2) - m2*g*l2*cos(0) = 0 - m2*g*l2 = -g
    V_expected = -m2*g*l2
    
    np.testing.assert_allclose(E_total, V_expected, atol=1e-10, 
    err_msg="Energy calculation mismatch at initial displacement")
    
    
if __name__ == "__main__":
    #Execute tests directly when run as a script
    test_equilibrium_state()

    test_small_angle_linearization()
    test_energy_conservation_initialization()
    print("All unit tests passed successfully")

    
























