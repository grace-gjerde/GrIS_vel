#test_moving_mean.py

#Import modules
from Analysis.Tools.moving_mean import moving_mean

# 1 data point per 1 day window
def test_moving_mean():
    test_input_velocity_data = [1, 2, 3, 4]
    test_input_time_data = [1, 2, 3, 4]
    test_input_window_days = 1
    result = moving_mean(test_input_velocity_data, test_input_time_data, test_input_window_days)
    assert result == [1.0, 2.0, 3.0, 4.0]

#constant velocity data
def test_moving_mean_constant_values():
    test_input_velocity_data = [1, 1, 1, 1]
    test_input_time_data = [1, 2, 3, 4]
    test_input_window_days = 1
    result = moving_mean(test_input_velocity_data, test_input_time_data, test_input_window_days)
    assert result == [1.0, 1.0, 1.0, 1.0]
