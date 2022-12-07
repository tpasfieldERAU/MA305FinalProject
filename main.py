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
# import numintegrate as ni

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

# Please add an implemention of your module here, using N as the input parameter

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Part 2. Sum of Alternating Series
#   a. arctan() Method
#   b. Machin's Formula
#   c. Madhava's Series

# Please add an implemention of your module here, using N as the input parameter

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