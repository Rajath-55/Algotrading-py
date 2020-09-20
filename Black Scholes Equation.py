import numpy as np
from scipy.stats import norm

def BSE(S, K, stddev, r, t):
    d1 = (np.log(S/K) + (r + ((stddev**2)/2))*t)/(stddev*np.sqrt(t))
    d2 = d1 - (stddev*np.sqrt(t))
    return (S*norm.cdf(d1()) - K*np.exp(-r*t)*norm.cdf(d2()))