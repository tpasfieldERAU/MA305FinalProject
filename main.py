#!/usr/bin/env python3
# TODO Eq. 2 for Intergration Method having invalid returns.
"""
===============================================================================
Title: Examples of Computational Methods for the Approximation of Pi
Team: Team A
Written By: Thomas Pasfield, Omar Alhomaidah, Owen Mudgett
Last Update Date: 12 / 7 / 2022
-------------------------------------------------------------------------------
Description:
    This script provides and compares different methods for calculating the 
    value of pi, and provides a formatted output in to the terminal.

    Plots of these methods are generated with the accompanying plots.py file.
"""

# Import Sys to allow console inputs
from sys import argv

# Remove this line before submission. Make sure to uncomment your modules
import mcpi as mc
# import altsum
import numintegrate as ni

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# User input
#   try: and except: are used to ensure a valid input data type. If the input
#   is invalid, it repeats the prompt until the user inputs a valid value.

N = 0  # Added so N always has a defined value
def userInput():
    global N  # N exists outside of function, needs to be global to execute.
    while True:
        try:
            N = int(input("N-value? "))
            # Value must also be positive, so throw the same error if it's not.
            if (N <= 0):
                raise ValueError
            break
        except ValueError:
            print("Please input a positive integer. ")
            continue
        
if len(argv) < 2:
    userInput()
else:
    while True:
        try:
            N = int(argv[1])
            break
        except ValueError:
            print("Run parameter invalid, please correct.")
            userInput()
            break
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Part 1. Numerical Integration
#   a. The Trapezoid Rule
#   b. The Midpoint Rule

print("--------------------------------------------------------")
print("Numerical Integration Method with Equation `i.`")
print("  LaTeX:  \int_0^1 4\sqrt{1 - x^2}dx")
print("--------------------------------------------------------")
print("       N\tMidpoint     \tSimpson's    \tTrapezoid")
i = 0
while 2**i < N:
    n = 2**i
    mid = ni.midpoint_int(ni.f, 0.0, 1.0, n)
    simp = ni.simpson_int(ni.f, 0.0, 1.0, n)
    trap = ni.trapezoid_int(ni.f, 0.0, 1.0, n)
    
    print(f"{2**i:8}\t{mid:1.12f}\t{simp:1.12f}\t{trap:1.12f}")
    i += 1

final = [ni.midpoint_int(ni.f, 0, 1, N), ni.simpson_int(ni.f, 0, 1, N), ni.trapezoid_int(ni.f, 0, 1, N)]
print(f"{N:8}\t{final[0]:1.12f}\t{final[1]:1.12f}\t{final[2]:1.12f}")
# print("------------------------")
# print(f"pi = {final:1.16f}, calculated with {N} iterations.")

print()
print("--------------------------------------------------------")
print("Numerical Integration Method with Equation `ii.`")
print("  LaTeX:  \int_{-1}^1 \\frac{1}{\sqrt{1 - x^2}}dx")
print("--------------------------------------------------------")
print("       N\tMidpoint     \tSimpson's    \tTrapezoid")
i = 0
while 2**i < N:
    n = 2**i
    mid = ni.midpoint_int(ni.g, -1.0, 1.0, n)
    simp = ni.simpson_int(ni.g, -1.0, 1.0, n)
    trap = ni.trapezoid_int(ni.g, -1.0, 1.0, n)
    
    print(f"{2**i:8}\t{mid:1.12f}\t{simp:1.12f}\t{trap:1.12f}")
    i += 1

final = [ni.midpoint_int(ni.g, -1, 1, N), ni.simpson_int(ni.g, -1, 1, N), ni.trapezoid_int(ni.g, -1, 1, N)]
print(f"{N:8}\t{final[0]:1.12f}\t{final[1]:1.12f}\t{final[2]:1.12f}")
# print("------------------------")
# print(f"pi = {final:1.16f}, calculated with {N} iterations.")

print()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# PART 2. Sum of Alternating Series

from math import sqrt
import random

# a. arctan function part
def arctan(x,N):
    xsum=0
    for i in range(N):
        i+=1
        if i > N:
            break
        xsum+=((-1)**(i+1))*(x**(2*i-1))/(2*i-1)
    return(xsum)

def madhava(N):
    xsum=0
    for i in range(N):
        i+=1
        if i > N:
            break
        xsum += ((-1)**(i+1))/((2*i-1)*(3**(i-1)))
    return(xsum)

print('Alternating Series')
M=input('Enter a positive integer N: ')
M=int(M)
y=int(1)
xsumnation = 4 * arctan(y,M)
print('Approximation of pi is: ',xsumnation,'\n')
#This works, but undershoots the value by magnitude of 10^x
#For example, N=1,000,000 will give accurate values up to the hundred thousandths digit, but will undershoot the millionths digit slightly

# b. Machin's Formula
print("Machin's Formula")
M=input('Enter a positive integer N: ')
M=int(M)
y=float(0.2)
xsumnation = 16 * arctan(y,M)
y=float(1/239)
xsumnation -= (4 * arctan(y,M))
print('Approximation of pi is: ',xsumnation,'\n')

#Is very accurate, getting the first 6 digits at N = 10 and above

# c. Compare results, Madhava's series
print("Madhava's Series")
M=input('Enter a positive integer N: ')
M=int(M)
xsumnation = (sqrt(12))*madhava(M)
print('Approximation of pi is: ',xsumnation)

#Is very accurate, gets 6 beginning digits at N = 10 and more than Spyder can display correct at N = 100

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Part 3. Monte Carlo Integration
#   a. Area Method

area_pi_iterated = mc.mc_area_v(N)
area_pi = area_pi_iterated[-1]

print("--------------------------------------------------------")
print("Monte Carlo Method: Pi using area of a circle")
print("--------------------------------------------------------")
print("       N\tpi")
i = 0
while 2**i < N:
    print(f"{2**i:8}\t{area_pi_iterated[2**i]:1.5f}")
    i += 1
    
print(f"{N:8}\t{area_pi:1.5f}")
print("------------------------")
print(f"pi = {area_pi:1.5f}, calculated with {N} iterations.")

print()

#   b. Volume Method
vol_pi_iterated = mc.mc_volume_v(N)
vol_pi = vol_pi_iterated[-1]
print("--------------------------------------------------------")
print("Monte Carlo Method: Pi using Volume of Sphere & Cone")
print("--------------------------------------------------------")
print("       N\tpi")
i = 0
while 2**i < N:
    print(f"{2**i:8}\t{vol_pi_iterated[2**i]:1.5f}")
    i += 1
    
print(f"{N:8}\t{vol_pi:1.5f}")
print("------------------------")
print(f"pi = {vol_pi:1.5f}, calculated with {N} iterations.")

print()
