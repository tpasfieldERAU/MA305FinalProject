"""
===============================================================================
Title: Plots to Compare Approximation Methods of Pi
Team: Team A
Written By: Thomas Pasfield
Last Update Date: 12 / 5 / 2022
-------------------------------------------------------------------------------
Description:
    Uses Matplotlib and PyPlot to generate plots of each method, as well as
    comparisons.

Dependencies: !! Make sure to have matplotlib installed before attempting to 
                 run this code !!

                 This can be installed through `pip install matplotlib` in the 
                 terminal. Root privleges should not be needed.
"""

import mcpi as mc
# import altsum
# import numintegrate as ni

import matplotlib.pyplot as plt
from math import pi
import os

# This will have much more organization later, I'm just getting something out 
# on paper for now.

imgdir = "./paper-files/images/"

# This is an example comparing the area and volume methods, such as how much 
# they fluctuate, how long they take to consistently converge, etc.
N = 100000
mcAreaMethodVals = mc.mc_area_v(N)
mcVolumeMethodVals = mc.mc_volume_v(N)

plt.figure(0)
plt.plot(range(1,N+1), mcAreaMethodVals)
plt.plot(range(1,N+1), mcVolumeMethodVals)
plt.title("Value of $\\approx\pi$ as Iterations Increase")
plt.xlabel("Iterations")
plt.ylabel("Value")
# plt.savefig(imgdir + "mcComp.png")

plt.figure(1)
AreaError = []
VolError = []
for i in mcAreaMethodVals:
    AreaError.append((abs(pi - i) / pi) * 100)
for i in mcVolumeMethodVals:
    VolError.append((abs(pi - i) / pi) * 100)

plt.plot(range(1,N+1), AreaError)
plt.plot(range(1,N+1), VolError)
plt.xscale("log")
plt.title("Error from $\pi$ as Iterations Increases")
plt.xlabel("Iterations")
plt.ylabel("Error %")
plt.show()
