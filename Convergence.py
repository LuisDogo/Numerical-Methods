from math import sqrt

def convergence_f(xi, xi_1):
    num = xi_1 - xi
    den = xi_1
    frac = sqrt(pow((num/den), 2))
    return frac