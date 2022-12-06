#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:01:44 2022

@author: alhomaio
"""
#Part 1: Numerical Integration
#import numpy as np
from math import sqrt
# i
def f(x):
    y = 4*sqrt(1-x**2)
    return y
# ii
def g(x):
    y2 = 1/sqrt(1-x**2)
    return y2
# Midpoint rule:
def mid(f,a,b,N):
    mid_sum = 0
    dx = (b-a)/N
    for i in range(N):
        xi_bar = a+(i-0.5)*dx
        mid_sum += f(xi_bar)
        return dx*mid_sum
# Simpson's 1/3rd rule:
def simpson(f,a,b,N):
    dx = (b-a)/N
    s_sum = f(a) + f(b)
    for i in range(1,N):
        xi_bar = a+(i*dx)
        
        if i%2 == 0:
            s_sum += 2*f(xi_bar)
            else:
                s_sum += 4*f(xi_bar)
        return (dx/3)*s_sum
        
