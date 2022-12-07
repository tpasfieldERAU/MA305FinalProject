#!/usr/bin/env python3
import mcpi as mc
import time

print("iter      \tpi      \tEx. Time")
for i in range(9):
    iter = 10**i
    startTime = time.perf_counter()
    out = mc.mc_area(iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")

print("iter      \tpi      \tEx. Time")
for i in range(9):
    iter = 10**i
    startTime = time.perf_counter()
    out = mc.mc_volume(iter)
    endTime = time.perf_counter()
    print(f"{iter:10}\t{out:1.6f}\t{endTime-startTime}")