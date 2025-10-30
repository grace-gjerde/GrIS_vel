#Test_linfit.py

#Import modules
import numpy.testing as npt
import numpy as np
import pandas as pd
from Analysis.Tools.linfit import model
from Analysis.load_data import extract
import math

#Unzip data file
extract()

#Check the gradient function is correct for a set of test data
def test_find_slope():
    x = y = [0.1, 0,2]
    test_df=pd.DataFrame({"NLBS_DOY": x, "NLBS_VEL": y})
    coeff, intercept = model(df=test_df, DOY=0)
    assert math.isclose(coeff, 1.0)

#Check the y-intercept function is correct for a set of test data
def test_find_intercept():
    x = [-0.1, 0]
    y = [0, 0.1]
    test_df=pd.DataFrame({"NLBS_DOY": x, "NLBS_VEL": y})
    coeff, intercept = model(df=test_df, DOY=0)
    assert math.isclose(intercept, 0.1)
