import mcpi as mc
import altsum
import numintegrate as ni

import matplotlib.pyplot as plt
from math import pi
N = 1000

plt.figure("mcarea")
vals = mc.mc_area_v(N)
for i in range(len(vals)):
    vals[i] = abs(pi - vals[i])
plt.plot(range(1,N+1), vals)
print("mcarea done")


plt.figure("mcvol")
vals = mc.mc_volume_v(N)
for i in range(len(vals)):
    vals[i] = abs(pi - vals[i])
plt.plot(range(1,N+1), vals)
print("mcvol done")

plt.figure("arc")
vals = [0] * N
N1 = 1000
for i in range(1,N1+1):
    vals[i-1] = abs(pi - (4*altsum.arctan(1,i)))
plt.plot(range(1,N+1), vals)
print("arc done")

plt.figure("mac")
vals = [0] * N
for i in range(1,N1+1):
    vals[i-1] = abs(pi - (altsum.machine(i)))
plt.plot(range(1,N+1), vals)
print("mac done")

plt.figure("mad")
vals = [0] * N
for i in range(1,N1+1):
    vals[i-1] = abs(pi - (4*altsum.arctan(1,i)))
plt.plot(range(1,N+1), vals)
print("mad done")

plt.figure("mid")
vals = [0] * N
for i in range(1,N+1):
    vals[i-1] = abs(pi - ni.midpoint_int(ni.f, 0, 1, i))
plt.plot(range(1,N+1), vals)
print("mid done")

plt.figure("trap")
vals = [0] * N
for i in range(1,N+1):
    vals[i-1] = abs(pi - ni.trapezoid_int(ni.f, 0, 1, i))
plt.plot(range(1,N+1), vals)
print("trap done")

plt.figure("simp")
vals = [0] * N
for i in range(1,N+1):
    vals[i-1] = abs(pi - ni.simpson_int(ni.f, 0, 1, i))
plt.plot(range(1,N+1), vals)
print("mid done")
plt.show()