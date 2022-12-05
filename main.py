"""
===============================================================================
Title: Examples of Computational Methods for the Approximation of Pi
Team: Team A
Written By: Thomas Pasfield, Omar Alhomaidah, Owen Mudgett
Last Update Date: 12 / 5 / 2022
-------------------------------------------------------------------------------
Description:
    This script provides and compares different methods for calculating the 
    value of pi, and provides a formatted output in to the terminal.

    Plots of these methods are generated with the accompanying plots.py file.
"""

# Remove this line before submission. Make sure to uncomment your modules
import mcpi as mc
# import altsum
# import Num_Integ as NI

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# User input
#   try: and except: are used to ensure a valid input data type. If the input
#   is invalid, it repeats the prompt until the user inputs a valid value.

N = 0  # Added so N always has a defined value
while True:
    try:
        N = int(input("N-value? "))
        if (N <= 0):
            raise ValueError
        break
    except ValueError:
        print("Please input a positive integer. ")
        continue

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

area_pi = mc.mc_area(N)
print(area_pi)

#   b. Volume Method
vol_pi = mc.mc_volume(N)
print(vol_pi)