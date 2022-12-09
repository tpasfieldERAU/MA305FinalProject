#!/usr/bin/env python3
# TODO Add list outputs for use in a plot
# TODO Add time-to-highest-accuracy
# TODO Wtf is up with Madhava's method being so slow lmao, python sucks sometimes
#       (I tried to rewrite it to optimize it, it's just an unavoidably slow function.)

import mcpi as mc
import altsum
import numintegrate as ni
import time

print("McArea")
print("iter      \tpi      \tEx. Time")
for i in range(8):
    iter = 10**i
    startTime = time.perf_counter()
    out = mc.mc_area(iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")

print()
print("McVol")
print("iter      \tpi      \tEx. Time")
for i in range(8):
    iter = 10**i
    startTime = time.perf_counter()
    out = mc.mc_volume(iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")

print()
print("arctan")
print("iter      \tpi      \tEx. Time")
for i in range(8):
    iter = 10**i
    startTime = time.perf_counter()
    out = altsum.arctan(1, iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")
    
print()
print("machin")
print("iter      \tpi      \tEx. Time")
for i in range(8):
    iter = 10**i
    startTime = time.perf_counter()
    out = altsum.machine(iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")

print()
print("Madhava")
print("iter      \tpi      \tEx. Time")
for i in range(8):
    iter = 10**i
    startTime = time.perf_counter()
    out = altsum.madhava(iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")

print()
print("mid")
print("iter      \tpi      \tEx. Time")
for i in range(8):
    iter = 10**i
    startTime = time.perf_counter()
    out = ni.midpoint_int(ni.f, 0, 1, iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")
    
print()
print("simp") 
print("iter      \tpi      \tEx. Time")
for i in range(8):
    iter = 10**i
    startTime = time.perf_counter()
    out = ni.simpson_int(ni.f, 0, 1, iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")

print()
print("trap")
print("iter      \tpi      \tEx. Time")
for i in range(8):
    iter = 10**i
    startTime = time.perf_counter()
    out = ni.trapezoid_int(ni.f, 0, 1, iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")