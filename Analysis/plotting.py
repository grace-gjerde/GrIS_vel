#Plotting Velocity Time Series of all GPS Stations
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import load_data
from Tools.moving_mean import moving_mean

df=load_data.vel_data()
stations=load_data.read_stations()

def plot_timeseries(to_plot):
    plt.figure(figsize=(10,6))

    for station in to_plot:
    #plt.plot(x, y, marker='.', markersize=3, label=station)
        plt.scatter(station.times, station.velocities, s=0.5, label=station.name)

    plt.title("2011 Velocity Time Series", fontsize=14)
    plt.xlabel("Day of Year (DOY)", fontsize=12)
    plt.ylabel("Velocity (m/year)", fontsize=12)
    plt.xlim(150, 300)
    plt.ylim(0, 400)
    plt.legend(title="Stations", fontsize=9)
    plt.tight_layout()
    plt.savefig("velocity_times_eries.png")
    plt.figure(figsize=(10,6))
    print("velocity_timeseries.png saved")

def plot_moving_mean(station_mean, window_days):
     #extract station data and remove NaNs
    time_data = station_mean.times
    time_data = time_data[~np.isnan(time_data)]
    velocity_data = station_mean.velocities
    velocity_data = velocity_data[~np.isnan(velocity_data)]
    vel_mean = moving_mean(velocity_data, time_data, window_days)

    #trim time array to match moving mean length
    times_for_mean = time_data[:len(vel_mean)]
    plt.figure(figsize=(10,5))
    plt.plot(time_data, velocity_data, color="grey", label=f"{station_mean.name} GPS Data")
    plt.plot(times_for_mean, vel_mean, color="red", label=f"{window_days}-day Moving Mean")
    plt.xlabel("Time (DOY)")
    plt.ylabel("Velocity (m/year)")
    plt.title(f"Smoothed Time Series for Station {station_mean.name}")
    plt.legend()
    plt.savefig("velocity_moving_mean.png", dpi=300)
    print("velocity_moving_mean.png saved")


'''
for station in stations:
    doy_col = f"{station}_DOY"
    vel_col = f"{station}_VEL"

    x=df[doy_col]
    y=df[vel_col]

    #plt.plot(x, y, marker='.', markersize=3, label=station)
    plt.scatter(x, y, s=0.5, label=station)

plt.title("2011 Velocity Time Series", fontsize=14)
plt.xlabel("Day of Year (DOY)", fontsize=12)
plt.ylabel("Velocity (m/year)", fontsize=12)
plt.xlim(150, 300)
plt.ylim(0, 400)
plt.legend(title="Stations", fontsize=9)
plt.tight_layout()

plt.savefig("velocity_timeseries.png", dpi=300)
plt.show()

print("velocity_timeseries.png saved")

from run_analysis import time_data, velocity_data, times_for_mean, window_days, station, moving_mean

plt.figure(figsize=(10,5))
plt.plot(time_data, velocity_data, color="grey", label=f"{station} GPS Data")
plt.plot(times_for_mean, moving_mean, color="red", label=f"{window_days}-day Moving Mean")
plt.xlabel("Time (DOY)")
plt.ylabel("Velocity (m/year)")
plt.title(f"Smoothed Time Series for Station {station}")
plt.legend()
plt.savefig("velocity_moving_mean.png", dpi=300)
'''