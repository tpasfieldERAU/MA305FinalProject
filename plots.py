"""
===============================================================================
Title: Plots to Compare Approximation Methods of Pi
Team: Team A
Written By: Thomas Pasfield
Last Update Date: 12 / 6 / 2022
-------------------------------------------------------------------------------
Description:
    Uses Matplotlib and PyPlot to generate plots of each method, as well as
    comparisons.

Dependencies: !! Make sure to have matplotlib installed before attempting to 
                 run this code !!

                 This can be installed through `pip install matplotlib` in the 
                 terminal. Root privleges should not be needed.
"""

# Import Student-Made Modules
import mcpi as mc
# import altsum
# import numintegrate as ni

# Import Python Standard Modules
import matplotlib.pyplot as plt
from math import pi


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Universal Variable Definitions

# This is the directory that images should be saved to in order to be properly
# embedded in the paper.
imgdir = "./paper-files/images/"
# Example usage:
# plt.save(imgdir + "[File Name]" + ".png")

# Number of iterations to run each method for. Can be changed locally.
N = 10000

# Creates an array which is constantly math.pi for all x
# Use this as a constant line on your plots for comparison
# !! If you change N for your plots, make sure to redefine pi_array to match!
pi_array = [pi] * N


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Plots of Numerical Intergration Methods


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Plots of Alternating Sum Methods


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Plots for Monte Carlo Methods
#
# This is an example comparing the area and volume methods, such as how much 
# they fluctuate, how long they take to consistently converge, etc.
# !! Because Monte Carlo methods are based on random data, a plot of averages 
#    is generated, but always bear in mind that a monte carlo method isn't 
#    guaranteed to give you a result that is correct within your tolerances !!

samples = 100  # Number of runs to average

# --- Comparisons of mc_area_v() and mc_volume_v() in one run ---
areaNums = mc.mc_area_v(N)
volNums = mc.mc_volume_v(N)

plt.figure("MC_1")
plt.plot(range(1,N+1), areaNums)
plt.plot(range(1,N+1), volNums)

# Renders a line into the plot representing the value of pi provided by math.pi
plt.plot(range(1,N+1), pi_array, linestyle="dotted", color="C0", linewidth=1)

plt.title("Calculated Value of $\pi$ as Iterations Increase")
plt.xlabel("Iterations")
plt.ylabel("Value")

# Experimenting with different axis scaling to better convey convergence?
plt.xscale("log")

# Save figure to folder, as demonstrated in the first section above
# plt.savefig(imgdir + "mcComp" + ".png")

# --- Comparisons of Error of same run as MC_1 ---
plt.figure("MC_1_err")

# Lists containing error vals
AreaError = []
VolError = []

# May change this to be a single loop and indexing instead of instantiating
for i in areaNums:
    AreaError.append((abs(pi - i) / pi) * 100)
for i in volNums:
    VolError.append((abs(pi - i) / pi) * 100)

plt.plot(range(1,N+1), AreaError)
plt.plot(range(1,N+1), VolError)

# Experimental scale again
# This scale highlights changes early on, while the later, lower variation data
# is "fast-forwarded" because less info is conveyed
plt.xscale("log")

plt.title("Error from $\pi$ as Iterations Increases")
plt.xlabel("Iterations")
plt.ylabel("Error %")

# plt.savefig(imgdir + "mcCompErr" + ".png")

# --- Show average of {samples} runs of the area method to N iterations ---

areas = []
sums = [ 0 ] * N
for s in range(samples):
    areas.append(mc.mc_area_v(N))

for i in range(N):
    for s in areas:
        sums[i] += s[i]

for i in range(N):
    sums[i] = sums[i] / samples    
    
plt.figure("AreaAvg")
for plot in areas:
    plt.plot(range(1,N+1), plot, color="C0", alpha=0.2, linewidth=1)
plt.plot(range(1,N+1), sums, color='C1', linewidth=2)

# --- Show average of {samples} runs of the vol method to N iterations ---

vols = []
sums = [ 0 ] * N
for s in range(samples):
    vols.append(mc.mc_volume_v(N))

for i in range(N):
    for s in vols:
        sums[i] += s[i]

for i in range(N):
    sums[i] = sums[i] / samples    
    
plt.figure("VolAvg")
for plot in areas:
    plt.plot(range(1,N+1), plot, color="C0", alpha=0.2, linewidth=1)
plt.plot(range(1,N+1), sums, color='C1', linewidth=2)
# Shows all figures generated so far, uncomment to use.
plt.show()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Plots comparing all methods
#   - One will have all methods overlaid to the same number of iterations
#   - Another will be all methods overlaid but ending once some error (epsilon)
#       value is reached.
#   - Comparison of error %s
#   - Possibly compare execution time for N iterations?