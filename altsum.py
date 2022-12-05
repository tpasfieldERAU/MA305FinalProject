"""
===============================================================================
Title:
Team:
Team Members:
Date Due:
-------------------------------------------------------------------------------
Description:
"""

from math import sqrt
import random

#------------------------------------------------------------------------------
# PART 1. Numerical Integration
#   Value of pi can be computed using definite integrals, implement with the
#   trapezoid rule, Simpson's rule, and the Midpoint Rule.
# a. Trapezoid/Simpson's Rule

# b. Midpoint Rule


#------------------------------------------------------------------------------
# PART 2. Sum of Alternating Series
#   See worksheet for details
# a. arctan function part
def arctan(x,N):
    xsum=0
    for i in range(N):
        i+=1
        if i > N:
            break
        xsum+=((-1)**(i+1))*(x**(2*i-1))/(2*i-1)
    return(xsum)

def madhava(N):
    xsum=0
    for i in range(N):
        i+=1
        if i > N:
            break
        xsum += ((-1)**(i+1))/((2*i-1)*(3**(i-1)))
    return(xsum)

print('Alternating Series')
M=input('Enter a positive integer N: ')
M=int(M)
y=int(1)
xsumnation = 4 * arctan(y,M)
print('Approximation of pi is: ',xsumnation,'\n')
#This works, but undershoots the value by magnitude of 10^x
#For example, N=1,000,000 will give accurate values up to the hundred thousandths digit, but will undershoot the millionths digit slightly

# b. Machin's Formula
print("Machin's Formula")
M=input('Enter a positive integer N: ')
M=int(M)
y=float(0.2)
xsumnation = 16 * arctan(y,M)
y=float(1/239)
xsumnation -= (4 * arctan(y,M))
print('Approximation of pi is: ',xsumnation,'\n')

#Is very accurate, getting the first 6 digits at N = 10 and above

# c. Compare results, Madhava's series
print("Madhava's Series")
M=input('Enter a positive integer N: ')
M=int(M)
xsumnation = (sqrt(12))*madhava(M)
print('Approximation of pi is: ',xsumnation)

#Is very accurate, gets 6 beginning digits at N = 10 and more than Spyder can display correct at N = 100

#------------------------------------------------------------------------------
# PART 3. Monte Carlo Integration
#   Approximation through random point sampling. See worksheet for detailed
#   description.

