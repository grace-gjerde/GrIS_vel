#maximum station velocity function

import numpy as np

def max_vel(velocity_data):
    return np.nanmax(velocity_data)  # ignores NaNs