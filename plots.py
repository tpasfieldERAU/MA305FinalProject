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
# import Num_Integ as NI

import matplotlib.pyplot as plt

# This will have much more organization later, I'm just getting something out 
# on paper for now.


# This is an example comparing the area and volume methods, such as how much 
# they fluctuate, how long they take to consistently converge, etc.
N = 10000
mcAreaMethodVals = mc.mc_area_v(N)
mcVolumeMethodVals = mc.mc_volume_v(N)

plt.plot(range(1,N+1), mcAreaMethodVals)
plt.plot(range(1,N+1), mcVolumeMethodVals)
plt.show()

