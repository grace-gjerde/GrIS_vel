import numpy.testing as npt
import numpy as np
from Analysis.Tools.find_mean import find_mean

def test_find_mean_integers():
    test_input = np.array([1,2,3,4])
    test_result = 2.5
    assert find_mean(test_input)== test_result

def test_find_mean_nans():
    test_input = np.array([np.nan,-1,0,4])
    test_result = 1
    assert find_mean(test_input) == test_result
