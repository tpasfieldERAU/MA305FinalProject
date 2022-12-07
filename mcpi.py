"""
===============================================================================
Title: Monte Carlo Method for the Approximation of Pi
Team: Team A
Written By: Thomas Pasfield
Last Update Date: 12 / 7 / 2022
-------------------------------------------------------------------------------
Description:
    Provides two methods to approximate pi. mc_area() uses the area of a circle 
    inside a square region, mc_volume() uses the overlap of a sphere and cone in
    a rectangular prism shaped region.

    Each function mentioned above return a double value, which is the last 
    approximation calculated.

    mc_area_v() returns an array of values reached during execution. 
    Same with mc_volume_v().
"""

# Imports
import random

# AREA METHODS

# Generates random values within the volume for x, and y.
# Input: None
# Output: 2 doubles
def area_points():
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    return x,y

# Approximates pi using a monte carlo method by checking if points are within
#   a circle within a square area
# Input: N (Iteration Limit)
# Output: pi (final approximation)
def mc_area(N):
    # Random point generation
    count = 0

    for i in range(N):
        x,y = area_points()
        if x*x + y*y < 1.0:
            count += 1
    
    r = count / N
    return 4 * r

# Approximates pi using a monte carlo method by checking if points are within
#   a circle within a square area. Returns the approximated value for every
#   iteration.
# Input: N (Iteration Limit)
# Output: [pi_0, pi_1, ... pi_N]
def mc_area_v(N):
    # Random point generation
    vals = []
    count = 0

    for i in range(N):
        x,y = area_points()
        if x*x + y*y < 1.0:
            count += 1
        r = count / (i+1)
        vals.append(r*4)
    return vals



# VOLUME METHODS

# Generates random values within the volume for x, y, and z.
# Input: None
# Output: 3 doubles
def vol_points():
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    z = random.uniform( 0,2)
    return x,y,z

# Approximates pi using a monte carlo method by checking if points are within
#   a sphere and cone intersection.
# Input: N (Iteration Limit)
# Output: pi (final approximation)
def mc_volume(N):
    count = 0
    for i in range(N):
        x,y,z = vol_points()
        if x*x + y*y < z*z and x*x + y*y + (z-1)**2 < 1:
            count += 1
    r = count / N
    return r*8

# Approximates pi using a monte carlo method by checking if points are within
#   a sphere and cone intersection. Returns the approximated value for every
#   iteration.
# Input: N (Iteration Limit)
# Output: [pi_0, pi_1, ... pi_N]
def mc_volume_v(N):
    vals = []
    count = 0
    for i in range(N):
        x,y,z = vol_points()
        if x*x + y*y < z*z and x**2 + y**2 + (z-1)**2 < 1:
            count += 1
        r = count / (i+1) 
        vals.append(r*8)

    return vals