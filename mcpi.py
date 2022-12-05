# TEMPORARY FILE FOR VERSION CONTROL
# mc_volume is not correct, needs to be finished properly.

# LOOK INTO NUMPY TO SPEED THINGS UP

"""
===============================================================================
Title:
Team:
Team Members:
Date Due:
-------------------------------------------------------------------------------
Description:
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import random

#------------------------------------------------------------------------------
# PART 1. Numerical Integration
#   Value of pi can be computed using definite integrals, implement with the
#   trapezoid rule, Simpson's rule, and the Midpoint Rule.
# a. Trapezoid/Simpson's Rule

# b. Midpoint Rule


#------------------------------------------------------------------------------
# PART 2. Sum of Alternating Series
#   See worksheet for details
# a. arctan function part

# b. Machin's Formula

# c. Compare results, Madhava's series


#------------------------------------------------------------------------------
# PART 3. Monte Carlo Integration
#   Approximation through random point sampling. See worksheet for detailed
#   description.

# Get input for `N` variable, repeat if not an int
while True:
    try:
        N = int(input("N-value? "))
        break
    except ValueError:
        print("Please input a positive integer.")
        continue

while True:
    try:
        lim = int(input("Terms to average? "))
        break
    except ValueError:
        print("Please input a positive integer.")
        continue

def mc_area(N):
    # Random point generation
    points = []

    for i in range(N):
        points.append([random.uniform(-1,1), random.uniform(-1,1)])

    count_in = 0
    count_out = 0

    for point in points:
        a = point[0]
        b = point[1]
        if a*a + b*b >= 1.0:
            count_out += 1
        else:
            count_in += 1

    r = count_in / N
    return 4*r

def vol_points():
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    z = random.uniform( 0,2)
    return x,y,z

def mc_volume(N):
    points = []
    plot_vals = []
    count = 0
    for i in range(N):
        x,y,z = vol_points()
        points.append([x,y,z])
        if x*x + y*y < z*z and x**2 + y**2 + (z-1)**2 < 1:
            count += 1
        r = count / (i+1) 
        plot_vals.append(r*8)

    return plot_vals

# lim = 25
lines = []
for i in range(lim):
    vals = mc_volume(N)
    lines.append(vals)
    plt.plot(vals, linewidth=1.0, linestyle='--', color='b')
avg = [0]*N
for line in lines:
    for j in range(N):
        avg[j] += line[j]

for k in range(N):
    avg[k] = avg[k] / lim
plt.plot(avg, linewidth=2.0, linestyle='-', color='r')
print(avg[-1])
plt.title("Approximation of $\pi$ by Volume")
plt.xlabel("Iterations")
plt.ylabel("$\pi$ Value")
plt.text(N-(N/10), 3.5, f"$\pi$ = {avg[-1]:1.5f}")
plt.show()
