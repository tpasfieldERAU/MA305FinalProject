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
        msum += f(xi_bar)
        return mid_sum*dx
            
        
