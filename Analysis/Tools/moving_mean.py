#Tools/moving_mean.py
#moving mean function (in days) - FINAL
import numpy as np

def moving_mean(velocity_data, time_data, window_days):
 
    #calculate average timestep in days
    time_diffs = np.diff(time_data)
    avg_timestep_days = np.mean(time_diffs)
        
    #convert window size from days to number of data points
    window_size_points = int(window_days / avg_timestep_days)
        
    #calculate moving mean
    means = []
    for i in range(len(velocity_data) - window_size_points + 1):
        window = velocity_data[i:i+window_size_points]
        window_mean = sum(window) / window_size_points
        means.append(window_mean)
    return means
