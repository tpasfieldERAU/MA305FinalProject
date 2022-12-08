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
    y = 4*sqrt(1-x**2)
    return y
# ii
def g(x):
    if x == 1:
        return float('NaN')
    y2 = 1/sqrt(1-x**2)
    return y2


# Integration Methods:
# Midpoint rule:
def midpoint_int(f, a, b, N):
    dx = (b-a)/N
    m_sum = 0
    for i in range(N):
        m_sum += f((a + dx/2) + i*dx)
    m_sum *= dx
    return m_sum

# Simpson's 1/3rd rule:
def simpson_int(f,a,b,N):
    dx = (b-a)/N
    s_sum = f(a) + f(b)
    for i in range(1,N):
        xi_bar = a+(i*dx)
        
        if i%2 == 0:
            s_sum += 2*f(xi_bar)
        else:
            s_sum += 4*f(xi_bar)
    return (dx/3)*s_sum

# Trapezoid rule:
def trapezoid_int(f,a,b,N):
    dx = (b-a)/N
    t_sum = f(a) + f(b)
    for i in range(1,N):
        xi_bar = a+(i*dx)
        
        t_sum += 2*f(xi_bar)
    return (dx/2)*t_sum