#test_mean.py

#Import modules
import numpy.testing as npt
import numpy as np
from Analysis.Tools.find_mean import find_mean

#Test the mean function works for an array of positive numbers
def test_find_mean_integers():
    test_input = np.array([1,2,3,4])
    test_result = 2.5
    assert find_mean(test_input) == test_result

#Test the mean function works for an array of positive and negative and NaN numbers. 
def test_find_mean_nans():
    test_input = np.array([np.nan,-1,0,4])
    test_result = 1
    assert find_mean(test_input) == test_result
