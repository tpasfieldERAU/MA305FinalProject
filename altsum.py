"""
===============================================================================
Title:
Team:
Written By:
Last Update Date: 12 / 5 / 2022
-------------------------------------------------------------------------------
Description:
    Placeholder Text
"""

# Split this into functions that are callable as a module please
# Anything outside of the functions will be run when other code attempts to use
# the module, so anything handled by main.py can be removed, such as input.
# 
# Also you may want to use the math.atan and math.tan methods, they could 
# simplify some things for you
#
# I see that you started this though, which is awesome. Thanks!
#   - Thomas

# Imports
from math import sqrt

# Probably move this into the description in some form
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
