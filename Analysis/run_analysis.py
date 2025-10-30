#run_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path
from Stations import Station_obj
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
from Tools.find_mean import find_mean
from Tools.moving_mean import moving_mean
from plotting import plot_timeseries

#results
results = {}
station_data = []

for station in stations:
    time_col = f"{station}_DOY"
    vel_col = f"{station}_VEL"

    time_data = df[time_col].values
    velocity_data = df[vel_col].values
    
    station_max = max_vel(velocity_data)
    station_min = find_min(velocity_data)
    station_mean = find_mean(velocity_data)

    station_data.append(Station_obj(station, time_data, velocity_data, station_min, station_max, station_mean))

for station in station_data:
    print(station)

print(df.columns.tolist())


#show time series for an arbitrary number of stations
to_plot = []
plot_station = ""
all_choice = input("Do you want to see the time series for all stations? (y/n)")
if all_choice.lower() == "y":
    to_plot = station_data
else:
    while plot_station != "end":
        plot_station = input("Enter a station you want to see a time series for (FL03, FL04, NL01, NL02, NL03, NL04, NL06, NL07, NL08, NL09, NL10, NL11, NL12, NL13, NLBS). Print 'end' to end adding stations:")
        for station in station_data:
            if station.name == plot_station:
                to_plot.append(station)

plot_timeseries(to_plot)

#run the moving mean time series per station

#ask user for stations of interest
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
