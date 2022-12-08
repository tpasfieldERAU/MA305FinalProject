#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:01:44 2022

@author: alhomaio
"""
#Part 1: Numerical Integration
import numpy as np
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
def mid(f, a, b, N):
    dx = (b-a)/N
    m_sum = 0
    for i in range(N):
        m_sum += f((a + dx/2) + i*dx)
    m_sum *= dx
    return m_sum
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
# Trapezoid rule:
def trap(f,a,b,N):
    dx = (b-a)/N
    t_sum = f(a) + f(b)
    for i in range(1,N):
        xi_bar = a+(i*dx)
        
        t_sum += 2*f(xi_bar)
    return (dx/2)*t_sum
        
#########################################################################
    #Error calculation
if __name__=='__main__':
   def abs_err(approximate,exact):
        error1 = abs(approximate-exact)
        return error1
   def ex_err(approximate,exact):
        error2 = abs((approximate-exact)/exact)*100
        return error2


for i in range(10):    
   # Limits of integration
   a=0
   b=1 

   # Exact value of the integral
   exact= np.pi # exact integral of f(x) 
   N = 10**i
   # Evaluate the approximate value of the integral using different methods
   approx1=mid(f,a,b,N)
   approx2 = trap(f,a, b, N)
   approx3 = simpson(f,a, b, N)

   # Compute the absolute errors
   abs_error1=abs_err(approx1,exact)
   rel_error1=ex_err(approx1,exact)
   abs_error2=abs_err(approx2,exact)
   rel_error2=ex_err(approx2,exact)
   abs_error3=abs_err(approx3,exact)
   rel_error3=ex_err(approx3,exact)
   print(N)
   print()
   print("Results using n={} sub-intervals:".format(N))
   print("=============================================")
   print("                 Approximation       Error")
   print("   Midpoint: \t {0:12.10f}\t {1:12.10f}".format(approx1, abs_error1))
   print("   Simpson: \t {0:12.10f}\t {1:12.10f}".format(approx2, abs_error2))
   print("   Trapezoid: \t {0:12.10f}\t {1:12.10f}".format(approx3, abs_error3))
   print("=============================================")
   print()
################################
   # print("Integration result by Midpoint method is: %0.6f" % (approx1) )
   # print("Absolute Error is: %0.6f" % (abs_error1))
   # print("Relative Error is: %0.6f" % (rel_error1))
   # print()
   # print("Integration result by impson's 1/3rd method is: %0.6f" % (approx2) )
   # print("Absolute Error is: %0.6f" % (abs_error2))
   # print("Relative Error is: %0.6f" % (rel_error2))
   # print()
   # print("Integration result by Trapezoidal method is: %0.6f" % (approx3) )
   # print("Absolute Error is: %0.6f" % (abs_error3))
   # print("Relative Error is: %0.6f" % (rel_error3))
