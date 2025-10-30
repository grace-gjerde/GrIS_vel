# test_max.py

#Load modules
from Analysis.Tools.find_max import max_vel
from Analysis.load_data import vel_data, read_stations, extract

#Call extract to unzip the data file
extract()
#Extract the velocity data from the unzipped csv
df=vel_data()
#Extract the stations data 
stations=read_stations()

#Test max function for an array of positive integers
def test_max_integers():
    test_input = [1, 2, 3, 4]
    assert max_vel(test_input) == 4

#Test max function for an array of zeros
def test_max_zeros():
    test_input = [0, 0, 0, 0]
    assert max_vel(test_input) == 0

#Test max function for an array including negatives
def test_max_negatives():
    test_input = [-2, -1, 0, 1]
    assert max_vel(test_input) == 1

#Test the real data 
def test_station_max_values():
    extract()
    for station in stations:
        vel_col = f"{station}_VEL"
        velocity_data = df[vel_col].values
        station_max = max_vel(velocity_data)
        assert station_max is not None
