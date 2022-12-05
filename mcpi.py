# Current version doesn't have proper functionality for area
# Needs to all accept parameters

"""
===============================================================================
Title: Monte Carlo Method for the Approximation of Pi
Team: Team A
Written By: Thomas Pasfield
Last Update Date: 12 / 5 / 2022
-------------------------------------------------------------------------------
Description:
    Provides two methods to approximate pi. mcarea() uses the area of a circle 
    inside a square region, mcvolume() uses the overlap of a sphere and cone in
    a rectangular prism shaped region.

    Each function mentioned above return a double value, which is the last approximation calculated.

    mcarea_v() returns an array of values reached during execution. Same with mcvolume_v().
"""

# Imports
from math import sqrt
import random

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

def mcvolume_v(N):
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