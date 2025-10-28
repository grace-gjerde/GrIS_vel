import numpy.testing as npt
import numpy as np
import pandas as pd
from Analysis.Tools.linfit import model

def test_find_slope():
    x = y = [0, 1]
    test_df=pd.DataFrame({"x": x, "y": y})
    coeff, intercept = model(df=test_df)
    assert(coeff == 1)

def test_find_intercept():
    x = [0, 1]
    y = [-1,0]
    test_df=pd.DataFrame({"x": x, "y": y})
    coeff, intercept = model(df=test_df)
    assert(intercept == -1)
