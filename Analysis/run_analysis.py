#run_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path
import load_data 

load_data.extract()
df=load_data.vel_data()
stations=load_data.read_stations()

#add Analysis and Tools folder to Python path
analysis_path = Path(__file__).parent / "Analysis"
tools_path = analysis_path / "Tools"
sys.path.insert(0, str(analysis_path))
sys.path.insert(0, str(tools_path))

#import functions
from Tools.find_max import max_vel
from Tools.find_min import find_min
from Tools.moving_mean import moving_mean

#results
results = {}

for station in stations:
    vel_col = f"{station}_VEL"
    velocity_data = df[vel_col].values
    
    station_max = max_vel(velocity_data)
    station_min = find_min(velocity_data)
    
    results[station] =  {"max": station_max, "min": station_min}

#print results
for station, stats in results.items():
    print(f"{station}: {stats}")

print(df.columns.tolist())


#run the moving mean time series per station

#ask user for station of interest
station = input("Enter station ((FL03, FL04, NL01, NL02, NL03, NL04, NL06, NL07, NL08, NL09, NL10, NL11, NL12, NL13, NLBS): ").upper()
vel_col = f"{station}_VEL"
time_col = f"{station}_DOY"

#ask user for moving mean window size in days
window_days = float(input("Enter moving mean window size (days): "))

#extract station data and remove NaNs
velocity_data = df[vel_col].dropna().to_numpy()
time_data = df[time_col].dropna().to_numpy()


#calculate average timestep and window size in points
avg_timestep_days = np.mean(np.diff(time_data))
window_size_points = int(window_days/avg_timestep_days)


moving_mean = pd.Series(velocity_data).rolling(window=window_size_points).mean().dropna().to_numpy()

#trim time array to match moving mean length
times_for_mean = time_data[:len(moving_mean)]

plt.figure(figsize=(10,5))
plt.plot(time_data, velocity_data, color="grey", label=f"{station} GPS Data")
plt.plot(times_for_mean, moving_mean, color="red", label=f"{window_days}-day Moving Mean")
plt.xlabel("Time (DOY)")
plt.ylabel("Velocity (m/year)")
plt.title(f"Smoothed Time Series for Station {station}")
plt.legend()
plt.savefig("velocity_moving_mean.png", dpi=300)
