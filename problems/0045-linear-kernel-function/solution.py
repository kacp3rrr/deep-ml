import numpy as np

def kernel_function(x1, x2):
    res = 0
    # assuming guarantee of equal array sizes
    for i in range(len(x1)):
        res += x1[i] * x2[i]
    return res