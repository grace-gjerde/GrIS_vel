# test_max.py

import numpy as np
from Analysis.Tools.find_max import max_vel
from Analysis.load_data import vel_data, read_stations
df=vel_data()
stations=read_stations()

def test_max_integers():
    test_input = np.array([1, 2, 3, 4])
    assert max_vel(test_input) == 4

def test_max_zeros():
    test_input = np.array([0, 0, 0, 0])
    assert max_vel(test_input) == 0

def test_max_negatives():
    test_input = np.array([-2, -1, 0, 1])
    assert max_vel(test_input) == 1

def test_station_max_values():
    for station in stations:
        vel_col = f"{station}_VEL"
        velocity_data = df[vel_col].values
        station_max = max_vel(velocity_data)
        assert station_max is not None
