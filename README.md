**GrIS_vel: Glacier Velocity Analysis Tool**  
\
GrIS_vel is a Python-based toolkit for analyzing glacier velocity data. It includes functionality to calculate moving averages, perform station-specific analysis, and generate plots.
\

## Package overview
Python package to identify and characterize transient acceleration events at North Lake in Southwest Greenland. This package is structured as follows:
\
- **`Data/`** Data from stations around North Lake. This is also where results of data analysis are stored.
- **`Analysis/`** Python scripts that take the data in Data/ as an input, and provide an analysis of transient acceleration events.
- **`Tests/`** Suite of tests to check that the Analysis script is working correctly.
- **`Results/`** Upon successful execution of the analysis pipeline, this directory will be generated, and analysis figures will be saved here.

\
**Installation**

Clone the repository:
```bash
git clone https://github.com/<username>/GrIS_vel.git
cd GrIS_vel
```

Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate 
```

install dependencies
```bash
pip install -r requirements.txt
```