#run_analysis.py
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
