# Dan Bachler
# Janet Madrid
import numpy as np
import pandas as pd
import math

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
    # Get sample means
    mean_1 = np.mean(arr1)
    mean_2 = np.mean(arr2)

    # Get multipler
    multiplier = len(arr1) - 1

    sum = 0
    for i in range(0,len(arr1)-1):
        val1 = arr1[i] - mean_1
        val2 = arr2[i] - mean_2
        sum += (val1*val2)
    return sum * (1/multiplier)

# Cor function
def correlation(arr1, arr2):
    cov = covariance(arr1, arr2)
    var1 = math.sqrt(variance(arr1))
    var2 = math.sqrt(variance(arr2))

    return cov/(var1*var2)

# Range norm function
def range_norm(arr):
    pass

# Standard norm function
def stanard_norm(arr):
    pass

# Covar matrix function
def covar_matrix(arr):
    pass

def variance(arr):
    multiplier = 1/(len(arr)-1)

    mean = np.mean(arr)

    sum = 0
    for i in range(0,len(arr)-1):
        sum += (arr[i]-mean)**2
    return sum * multiplier

#print(multi_dim_mean(data))
#print(covariance(data[0], data[1]))
print(correlation(data[0], data[1]))