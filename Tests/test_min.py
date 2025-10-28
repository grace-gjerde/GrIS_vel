import numpy.testing as npt
import numpy as np
from Analysis.Tools.find_min import find_min

def test_find_min_integers():
    test_input = np.array([1,2,3,4])
    test_result = 1
    assert find_min(test_input)== test_result

def test_find_min_zeros():
    test_input = np.array([0,0,0,0])
    test_result = 0
    assert find_min(test_input) == test_result

def test_find_min_negatives():
    test_input = np.array([-2,-1,0,1])
    test_result = -2
    assert find_min(test_input) == test_result