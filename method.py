# Dan Bachler
# Janet Madrid
import numpy as np
import pandas as pd
import math

data = pd.DataFrame([
    [0.3,23, 5.6],
    [0.4, 1, 5.4],
    [1.8, 4, 5.2],
    [6, 50, 5.1],
    [-0.5, 34, 5.3],
    [0.4, 19, 5.4],
    [1.1, 11, 5.5],
])
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
    multiplier = 1/(len(arr1) - 1)

    sum = 0
    for i in range(0,len(arr1)-1):
        val1 = arr1[i] - mean_1
        val2 = arr2[i] - mean_2
        sum += (val1*val2)
    return sum * multiplier

# Cor function
def correlation(arr1, arr2):
    cov = covariance(arr1, arr2)
    var1 = variance(arr1)
    var2 = variance(arr2)

    var1 = math.sqrt(var1)
    var2 = math.sqrt(var2)

    return cov/(var1*var2)

# Range norm function
def range_norm(arr):
    # New matrix
    new_matrix = [][]
    # Iterate over the columns
    for i in range(0, len(arr[0])-1):
        column = []
        for j in range(0, len(arr)-1):
            column.append(arr[j][i])
        min_val = min(column)
        max_val = max(column)
        for j in range(0,len(column)-1):
            new_value = (column[j]-min_val) / (max_val-min_val)
            new_matrix[j][i] = new_value
    return(new_matrix)


# Standard norm function
def standard_norm(arr):
    y1 = np.array(arr)
    mean  = y1.mean(axis=0)
    sd = y1.std(axis=0)
    return((y1-mean)/sd)

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
#print(covariance(data[:,0], data[:,2]))
#print(correlation(data[:,0], data[:,2]))
#temp = variance(data[:,0]) 
#print(math.sqrt(temp))
print(stanard_norm(data))
from scipy import stats
print(stats.zscore(data))
