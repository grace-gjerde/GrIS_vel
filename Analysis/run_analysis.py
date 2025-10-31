#run_analysis.py


#runs Greenland glacier velocity analysis (min, max, moving mean).
#example: python3 Analysis/run_analysis.py --station FL03


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path
from Stations import Station_obj
import load_data 
import argparse
import os

root_dir = Path(__file__).resolve().parents[1]
os.chdir(root_dir) 
load_data.extract()

#add Analysis and Tools folders to sys.path
sys.path.insert(0, str(root_dir / "Analysis"))
sys.path.insert(0, str(root_dir / "Tools"))

data_folder = root_dir /"Data"/"Glacier"
data_file = data_folder /"Glacier_transient_vel.csv"

#import analysis tools
from Tools.find_max import max_vel
from Tools.find_min import find_min
from Tools.find_mean import find_mean
from plotting import plot_timeseries, plot_moving_mean

def main(file=None, station_name=None, window_days=None, outdir=None):
    """
    Run Greenland glacier velocity analysis (min, max, moving mean).
    """
    if file is None:
        file = data_file
    else:
        file = Path(file).resolve()

    if outdir is None:
        outdir = root_dir / "outputs"
    else:
        outdir = Path(outdir).resolve()

    outdir.mkdir(parents=True, exist_ok=True)
    print(f"Outputs will be saved in: {outdir}")

    
    df = load_data.vel_data()
    stations = load_data.read_stations()
    station_data = []
    station_mean_name = station_name

    if station_name != None:
        stations = [station_name]

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

    #show time series for an arbitrary number of stations
    to_plot = []
    plot_station = ""
    if station_name == None:
        all_choice = input("Do you want to see the time series for all stations? (y/n)")
        if all_choice.lower() == "y":
            to_plot = station_data
        else:
            while plot_station != "end":
                plot_station = input("Enter a station you want to see a time series for (FL03, FL04, NL01, NL02, NL03, NL04, NL06, NL07, NL08, NL09, NL10, NL11, NL12, NL13, NLBS). Enter 'end' to end adding stations:")
                for station in station_data:
                    if station.name == plot_station:
                        to_plot.append(station)
    else:
        to_plot = station_data

    plot_timeseries(to_plot)

    #run the moving mean time series per station
    #ask user for stations of interest
    if station_name is None:
        station_mean_name = input("Moving mean \n Enter station ((FL03, FL04, NL01, NL02, NL03, NL04, NL06, NL07, NL08, NL09, NL10, NL11, NL12, NL13, NLBS): ").upper()
    else:
        station_mean_name = station_name

    #ask user for moving mean window size in days
    if window_days is None:
        window_days = float(input("Enter moving mean window size (days): "))
    
    for station in station_data:
        if station.name == station_mean_name:
            station_mean = station

    plot_moving_mean(station_mean, window_days)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run glacier velocity analysis.")
    parser.add_argument("--file", "-f", type=str, default=None, help="Path to input CSV file")
    parser.add_argument("--station", type=str, default=None, help="Specify station to analyze")
    parser.add_argument("--window", type=float, default=None, help="Moving mean window size in days")
    parser.add_argument("--outdir", type=str, default=None, help="Directory to save outputs")
    args = parser.parse_args()

    main(file=args.file, station_name=args.station, outdir=args.outdir, window_days=args.window)