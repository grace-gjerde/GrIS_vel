## Data 

This package contains two datasets:

- **GPS_stations_coords.csv:**  Contains the following three fields of information for each station:
    - `Station_name`
    - `Latitude`
    - `Longitude`
    
- **Glacier.zip:** Velocity observations across the glacier, automatically unzipped through the `Analysis` pipeline. For each station `{Station_name}`, this file contains two fields:
    - `{Station_name}_DOY`: Time at which observation was taken.
    - `{Station_name}_vel`: Horizontal velocity of ice movement at station's sensor at time of recording `Station_name_DOY`.






