#!/usr/bin/env python3
"""
===============================================================================
Title: Numerical Intergration Calculation Methods for Pi
Team: Team A
Written By: Omar Alhomaidah
Last Update Date: 12 / 8 / 2022
-------------------------------------------------------------------------------
Description:
"""

# Imports
from math import sqrt

# Define the functions to represent the equations of the definite integrals
# i
def f(x):
    y = 4.0*sqrt(1.0 - x**2)
    return y
# ii
def g(x):
    # Catches the asymptotes, doesn't let them affect calculation
    # Edited by Thomas so it works for Simpson's and Trapezoid Rules
    # (Blame Thomas if this is incorrect, this is written by Thomas)
    if x**2 == 1.0:
        return 0
    y = 1.0/sqrt(1.0 - x**2)
    return y


# Integration Methods:
# Midpoint rule:
def midpoint_int(eq, a, b, N):
    dx = (b-a)/N
    m_sum = 0
    for i in range(N):
        m_sum += eq((a + dx/2) + i*dx)
    m_sum *= dx
    return m_sum

# Simpson's 1/3rd rule:
def simpson_int(eq,a,b,N):
    dx = (b-a)/N
    s_sum = eq(a) + eq(b)
    for i in range(1,N):
        xi_bar = a+(i*dx)
        
        if i%2 == 0:
            s_sum += 2*eq(xi_bar)
        else:
            s_sum += 4*eq(xi_bar)
    return (dx/3)*s_sum


# Trapezoid rule:
def trapezoid_int(eq,a,b,N):
    dx = (b-a)/N
    t_sum = eq(a) + eq(b)
    for i in range(1,N):
        xi_bar = a+(i*dx)
        
        t_sum += 2*eq(xi_bar)
    return (dx/2)*t_sum