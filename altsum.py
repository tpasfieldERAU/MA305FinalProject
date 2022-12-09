"""
===============================================================================
Title: Sum of Alternating Series Methods to Calculate Pi
Team: Team A
Written By: Owen Mudgett
Last Update Date: 12 / 9 / 2022
-------------------------------------------------------------------------------
Description:
    Approximates pi using an alternating series definition of arctan. Three
    methods are used, including just arctan, Machin's Formula, and Madhava's
    Series.
    
    arctan(x, N):
        This method takes x as the input, and N as the iteration limit for
        calculating the arctan of that input.
        
    machine(N):
        Input N is iteration limit to be fed into arctans.
        Computes pi using two arctans in a formula.
        See https://en.wikipedia.org/wiki/Machin-like_formula for general info
            about how this method works
            
    madhava(N):
        Series method for calculating pi without an trig operations.
        Accepts N as input for iteration limit.
        https://en.wikipedia.org/wiki/Madhava_series
            Add `#Another_formula_for_the_circumference_of_a_circle` to 
            navigatev directly to the proper section of the article.
"""

# Imports
from math import sqrt

# a. arctan function part
def arctan(x,N):
    xsum=0
    for i in range(N):
        i+=1
        if i > N:
            break
        xsum += ((-1)**(i+1)) * (x**(2*i-1)) / (2*i-1)
    # Removed the 4 multiplier because it needs to be general purpose
    return xsum  

# b. Machin's Formula
def machine(N):
    machins_pi = 16*arctan(1/5, N) - 4*arctan(1/239, N)
    return machins_pi 

# c. Madhava Series
def madhava(N):
    xsum=0
    for i in range(N):
        i+=1
        if i > N:
            break
        xsum += ((-1)**(i+1))/((2*i-1)*(3**(i-1)))
    return sqrt(12) * xsum


# --- General Info ---
# Alternating Series
# 4 * arctan(N)
# This works, but undershoots the value by magnitude of 10^x
# For example, N=1,000,000 will give accurate values up to the hundred 
#   thousandths digit, but will undershoot the millionths digit slightly

# Machin's Formula:
# Is very accurate, getting the first 6 digits at N = 10 and above

# Madhava's Series:
# Is very accurate, gets 6 beginning digits at N = 10 and more than Spyder can display correct at N = 100