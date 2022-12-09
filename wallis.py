# Little hidden bonus content
# Wallis method to approximate pi
#   Uses Product Summation
#   Not particularly precise

def wallis_pi(N):
    wpi = 1
    for i in range(1, N+1):
        if i % 2 == 0:
            wpi *= i / (i+1)
        else:
            wpi *= (i+1) / i
    return 2 * wpi

def wallis_pi_v(N):
    wpi = 1
    vals = []
    for i in range(1, N+1):
        if i % 2 == 0:
            wpi *= i / (i+1)
        else:
            wpi *= (i+1) / i
        vals.append(2*wpi)
    return vals