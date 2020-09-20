import numpy as np
import scipy.stats as si
from sympy.stats import Normal, cdf

#function returning the call price option

def BSE(S, K, stdev, r, t):
    d1 = (np.log(S / K) + (r + (stdev ** 2 / 2)) * t) / (stdev * np.sqrt(t))
    d2 = (np.log(S / K) + (r - (stdev ** 2 / 2)) * t) / (stdev * np.sqrt(t))
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * t) * si.norm.cdf(d2, 0.0, 1.0))
    return call

print(BSE(50, 100, 0.25, 0.05, 1))