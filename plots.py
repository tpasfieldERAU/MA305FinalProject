#!/usr/bin/env python3
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
import altsum
import numintegrate as ni

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
diff = {}
exact = pi
for i in range(1, 100):
    result = ni.simpson_int(ni.f, 0, 1, i)
    diff[i] = abs(exact - result)   


sort = sorted(diff.items())
x,y = zip(*sort)
plt.autoscale()
plt.loglog(x,y)
plt.xlabel("n")
plt.ylabel("Error")
# plt.show()
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
plt.legend(["Area Method", "Volume Method"])

# Experimenting with different axis scaling to better convey convergence?
plt.xscale("log")

# Save figure to folder, as demonstrated in the first section above
plt.savefig(imgdir + "mcComp1" + ".png")

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

plt.title("Error from True $\pi$ as Iterations Increases")
plt.xlabel("Iterations")
plt.ylabel("Error %")
plt.legend(["Area Method", "Volume Method"])

plt.savefig(imgdir + "mcCompErr1" + ".png")

# --- Duplicate of Last Two, Used to Demonstrate Random Nature of MC Methods --

areaNums = mc.mc_area_v(N)
volNums = mc.mc_volume_v(N)

plt.figure("MC_2")
plt.plot(range(1,N+1), areaNums)
plt.plot(range(1,N+1), volNums)

# Renders a line into the plot representing the value of pi provided by math.pi
plt.plot(range(1,N+1), pi_array, linestyle="dotted", color="C0", linewidth=1)

plt.title("Calculated Value of $\pi$ as Iterations Increase")
plt.xlabel("Iterations")
plt.ylabel("Value")
plt.legend(["Area Method", "Volume Method"])

# Experimenting with different axis scaling to better convey convergence?
plt.xscale("log")

# Save figure to folder, as demonstrated in the first section above
plt.savefig(imgdir + "mcComp2" + ".png")

# --- Comparisons of Error of same run as MC_1 ---
plt.figure("MC_2_err")

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

plt.title("Error from True $\pi$ as Iterations Increases")
plt.xlabel("Iterations")
plt.ylabel("Error %")
plt.legend(["Area Method", "Volume Method"])

plt.savefig(imgdir + "mcCompErr2" + ".png")


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
avg, = plt.plot(range(1,N+1), sums, color='C1', linewidth=2)
avg.set_label("Average Value")

plt.title(f"Average of {samples} mc_area() runs")
plt.xlabel("Iterations")
plt.ylabel("Value")
plt.legend()
plt.savefig(imgdir + "areaAvg" + ".png")

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
avg, = plt.plot(range(1,N+1), sums, color='C1', linewidth=2)
avg.set_label("Average Value")

plt.title(f"Average of {samples} mc_volume() runs")
plt.xlabel("Iterations")
plt.ylabel("Value")
plt.legend()

plt.savefig(imgdir + "volAvg" + ".png")

# Shows all figures generated so far, uncomment to use.
# plt.show()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Plots comparing all methods
#   - One will have all methods overlaid to the same number of iterations
#   - Another will be all methods overlaid but ending once some error (epsilon)
#       value is reached.
#   - Comparison of error %s
#   - Possibly compare execution time for N iterations?

N = 1000
mid = []
simp = []
trap = []
arc = []
mac = []
mad = []
for i in range(1,N):
    mid.append(ni.midpoint_int(ni.f, 0, 1, i))
    simp.append(ni.simpson_int(ni.f, 0, 1, i))
    trap.append(ni.trapezoid_int(ni.f, 0, 1, i))
    arc.append(4*altsum.arctan(1, i))
    mac.append(altsum.machine(i))
    mad.append(altsum.madhava(i))
area = mc.mc_area_v(N-1)
vol = mc.mc_volume_v(N-1)

xs = range(1,N)

fig = plt.figure("ALL")
plt.plot(xs, mid, color="C0")
plt.plot(xs, simp, color="C1")
plt.plot(xs, trap, color="C2")
plt.plot(xs, arc, color="C3")
plt.plot(xs, mac, color="C4")
plt.plot(xs, mad, color="C5")
plt.plot(xs, area, color="C0")
plt.plot(xs, vol, color="C1")
plt.ylim((2,4))
fig.show()
fig.waitforbuttonpress()