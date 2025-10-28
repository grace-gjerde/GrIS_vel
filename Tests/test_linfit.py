import numpy.testing as npt
import numpy as np
import pandas as pd
from Analysis.Tools.linfit import model
from Analysis.load_data import extract
import math

extract()

def test_find_slope():
    x = y = [0.1, 0,2]
    test_df=pd.DataFrame({"NLBS_DOY": x, "NLBS_VEL": y})
    coeff, intercept = model(df=test_df, DOY=0)
    assert math.isclose(coeff, 1.0)

def test_find_intercept():
    x = [-0.1, 0]
    y = [0, 0.1]
    test_df=pd.DataFrame({"NLBS_DOY": x, "NLBS_VEL": y})
    coeff, intercept = model(df=test_df, DOY=0)
    assert math.isclose(intercept, 0.1)
