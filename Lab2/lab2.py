import numpy, random, math 
from scipy.optimze import minimize
import matplotlib.pyplot as plt

def objective(vector):
    #takes vector alpha and returns a scalar value
    # see equation 4
    print()
N = 0
B = 0
XC = 0
start = numpy.zeros(N)
ret = minimize(objective, start, bounds = B, constraints = XC)
alpha = ret['x']