#run_analysis.py


#runs Greenland glacier velocity analysis (min, max, moving mean).
#example: python3 Analysis/run_analysis.py --station FL03


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path
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
from Tools.moving_mean import moving_mean

def main(file=None, station=None, window_days=None, outdir=None):
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
    results = {}

    for s in stations:
        vel_col = f"{s}_VEL"
        velocity_data = df[vel_col].values
        
        station_max = max_vel(velocity_data)
        station_min = find_min(velocity_data)
        
        results[s] =  {"max": station_max, "min": station_min}

    #print results
    for s, stats in results.items():
        print(f"{s}: {stats}")

    print(df.columns.tolist())

    #run the moving mean time series per station

    #ask user for station of interest
    if station is None:
        station = input("Enter station ((FL03, FL04, NL01, NL02, NL03, NL04, NL06, NL07, NL08, NL09, NL10, NL11, NL12, NL13, NLBS): ").upper()
    vel_col = f"{station}_VEL"
    time_col = f"{station}_DOY"

    #ask user for moving mean window size in days
    if window_days is None:
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
    print(f"{station} moving mean calculated")

    return velocity_data, time_data, moving_mean, times_for_mean, station, window_days

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run glacier velocity analysis.")
    parser.add_argument("--file", "-f", type=str, default=None, help="Path to input CSV file")
    parser.add_argument("--station", type=str, default=None, help="Specify station to analyze")
    parser.add_argument("--window", type=float, default=None, help="Moving mean window size in days")
    parser.add_argument("--outdir", type=str, default=None, help="Directory to save outputs")
    args = parser.parse_args()

    main(file=args.file, station=args.station, outdir=args.outdir, window_days=args.window)