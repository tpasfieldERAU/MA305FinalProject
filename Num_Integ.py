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
    fx = 4*sqrt(1-x**2)
    return fx
# ii
def f2(x):
    f2x = 1/sqrt(1-x**2)
    return f2x
# Midpoint rule:
    def mid(a,b,N,f):
        s1=0
        dx = (b-a)/N
        for i in range(N):
            x_i = a+((2*i-1)/2)*dx
            s1+= f(x_i)
            return s1*dx
            
        