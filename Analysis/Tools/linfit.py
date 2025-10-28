import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from pathlib import Path
import zipfile

def model(station_name="NLBS", DOY=6):
    df = pd.read_csv("Data/Glacier/Glacier_transient_vel.csv")
    print(f"station selected for linear fit is {station_name}")

    doy_col = f"{station_name}_DOY"
    vel_col = f"{station_name}_VEL"

    x=df[doy_col].dropna()
    y=df[vel_col].dropna()
    mdl_frame = pd.DataFrame({"DOY": x, "Vel": y})
    mdl_select = mdl_frame[mdl_frame["DOY"].apply(int) == DOY]


    model = LinearRegression()
    model.fit(mdl_select[["DOY"]], mdl_select["Vel"])

    return(float(model.coef_), model.intercept_)



