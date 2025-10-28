import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from pathlib import Path
from Analysis.load_data import vel_data
from decimal import Decimal


def model(df=vel_data(), station_name="NLBS", DOY=6):
    
    print(f"station selected for linear fit is {station_name}")

    doy_col = f"{station_name}_DOY"
    vel_col = f"{station_name}_VEL"

    x=df[doy_col].dropna()
    y=df[vel_col].dropna()
    mdl_frame = pd.DataFrame({"DOY": x, "Vel": y})
    mdl_select = mdl_frame[mdl_frame["DOY"].apply(int) == DOY]

    model = LinearRegression()
    model.fit(mdl_select[["DOY"]], mdl_select["Vel"])

    coeff = float(model.coef_)
    inter = float(model.intercept_)

    return(coeff, inter)



