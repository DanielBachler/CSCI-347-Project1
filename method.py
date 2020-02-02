# Dan Bachler
# Janet Madrid
import numpy as np
import pandas as pd

data = pd.read_csv("poker-hand-training-true.data", sep = ",", header = None)
data = data.to_numpy()
#print(data)
# Multi-dim mean function
def multi_dim_mean(arr):
    # Get average of all columns
    size = arr.shape
    total = 0
    for i in range(0, size[1]):
        column_total = 0
        for j in range(0, size[0]):
            column_total += data[j][i]
        total += column_total / size[0]
    return total / size[1]
    
# Covar function
def covariance(arr1, arr2):
    pass

# Cor function
def correlation(arr1, arr2):
    pass

# Range norm function
def range_norm(arr):
    pass

# Standard norm function
def stanard_norm(arr):
    pass

# Covar matrix function
def covar_matrix(arr):
    pass

print(multi_dim_mean(data))