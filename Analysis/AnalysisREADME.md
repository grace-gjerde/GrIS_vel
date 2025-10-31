**File Contents**
\
This directory contains routines to load and plot the ice sheet data, as well as routine to run all of the analyses. 
The directory also contains a sub-directory called Tools, which contains the functions used in the analyses. 
These functions find the minimum, maximum, and mean velocity, whilst a further function performs a linear fit on the data. \
\
**How to Run**\
run_analysis can be run from the terminal with a CLI\
\
**Example:**
\
```python3 run_analysis.py --station FL03 --window 20```

\
The main script for analysis is run_analysis.py located in the Analysis/ folder. It allows you to analyze glacier velocity data and calculate moving averages for specific stations. **Note:** `run_analysis.py` is intended to be run as a script and is wrapped in `if __name__ == "__main__":`.

Example: 
```bash 
python3 Analysis/run_analysis.py --file <input_csv> --station <station_id> --window <window_days> --outdir <output_directory>
```
\
Arguments:
-h, --help	Show help message and exit
--file FILE, -f FILE	Path to input CSV file (should contain columns: date, velocity, station)
--station STATION	Station ID to analyze (integer)
--window WINDOW	Moving mean window size in days (integer)
--outdir OUTDIR	Directory to save outputs (plots and CSVs)

Examples:

Calculate moving mean for station 3 over a 7-day window:
```bash 
python3 Analysis/run_analysis.py -f data/glacier_velocity.csv -s 3 -w 7 -o results/
```

Analyze all stations using default window and save outputs:
```bash 
python3 Analysis/run_analysis.py -f data/glacier_velocity.csv --outdir results/
```

\
You can also use individual functions by importing them:

Example:
```python 
from Analysis.Tools.moving_mean import moving_mean
```


