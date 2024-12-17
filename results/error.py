import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np


def find_neighbors(arr, target):
    # Sort the list first
    # Initialize variables for the smallest greater and largest lesser
    largest_lesser = None
    smallest_greater = None
    
    for num in arr:
        if num < target:
            largest_lesser = num  # This is the largest number less than target
        elif num > target:
            if smallest_greater is None:
                smallest_greater = num  # This is the smallest number greater than target
                break  # No need to continue as we have found both numbers
    
    return largest_lesser, smallest_greater


baseline = sys.argv[1]
slope = sys.argv[2]
df_baseline = pd.read_csv(baseline, skiprows=1)
df_slope = pd.read_csv(slope, skiprows=1)

x_column = 'Cache size'  # Replace with the name of the column for x-axis
y_column = 'Miss Rate'  # Replace with the name of the column for y-axis

baseline_x = df_baseline[x_column].tolist()
baseline_y = df_baseline[y_column].tolist()
slope_x = df_slope[x_column].tolist()
slope_y = df_slope[y_column].tolist()

num_points = 0
mae = 0
errors = []
for i in range(len(baseline_x)):
    x = baseline_x[i]
    y = baseline_y[i]
    if x in slope_x:
        j = slope_x.index(x)
        mae += abs(np.power((y-slope_y[j]), 1))
    else:
        x1, x2 = find_neighbors(slope_x, x)
        if x1 == None or x2 == None:
            break
        j1 = slope_x.index(x1)
        j2 = slope_x.index(x2)
        y1 = slope_y[j1]
        y2 = slope_y[j2]
        y_lin = ((y2-y1)/(x2-x1))*(x-x1) + y1
        errors.append(abs(np.power((y-y_lin), 1)))
        mae += abs(np.power((y-y_lin), 1))
    num_points+=1

mae = (mae/num_points)

print("error ", mae)
print(errors)

