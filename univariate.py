import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation

def compute_residual(coefs, data):
    squared_residual = 0
    for i in range(0,len(data)):
        hypothesis = coefs[0] + coefs[1] * data[i,0]
        squared_residual += (hypothesis - data[i,1]) ** 2
    residual = squared_residual / (2*len(data))
    return residual
