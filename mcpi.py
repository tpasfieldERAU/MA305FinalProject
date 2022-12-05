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
    Provides two methods to approximate pi. mc_area() uses the area of a circle 
    inside a square region, mc_volume() uses the overlap of a sphere and cone in
    a rectangular prism shaped region.

    Each function mentioned above return a double value, which is the last 
    approximation calculated.

    mc_area_v() returns an array of values reached during execution. 
    Same with mc_volume_v().
"""

# Imports
from math import sqrt
import random

# AREA METHODS
def area_points():
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    return x,y

def mc_area(N):
    # Random point generation
    points = []
    count = 0

    for i in range(N):
        x,y = area_points()
        points.append([x,y])
        if x*x + y*y < 1.0:
            count += 1
    
    r = count / N
    return 4 * r

def mc_area_v(N):
    # Random point generation
    points = []
    vals = []
    count = 0

    for i in range(N):
        x,y = area_points()
        points.append([x,y])
        if x*x + y*y < 1.0:
            count += 1
        r = count / (i+1)
        vals.append(r*4)
    return vals

# VOLUME METHODS
def vol_points():
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    z = random.uniform( 0,2)
    return x,y,z

def mc_volume(N):
    points = []
    count = 0
    for i in range(N):
        x,y,z = vol_points()
        points.append([x,y,z])
        if x*x + y*y < z*z and x*x + y*y + (z-1)**2 < 1:
            count += 1
    r = count / N
    return r*8

def mc_volume_v(N):
    points = []
    vals = []
    count = 0
    for i in range(N):
        x,y,z = vol_points()
        points.append([x,y,z])
        if x*x + y*y < z*z and x**2 + y**2 + (z-1)**2 < 1:
            count += 1
        r = count / (i+1) 
        vals.append(r*8)

    return vals