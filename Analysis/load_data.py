#load_data.py

#Import modules
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import zipfile

#Function to extract data from the zip file to a csv.
def extract():
    zip_path = Path("Data/Glacier.zip")  # your .zip file
    extract_dir = Path("Data/")          # folder to extract to

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print("Extraction complete.")

#Function to extract information about the stations from the csv
def read_stations():
    df = pd.read_csv("Data/Glacier/Glacier_transient_vel.csv")
    #Identify stations and their velocity data
    stations = []
    for col in df.columns:
        if "_DOY" in col:
            station = col.split("_DOY")[0]
            vel_col = f"{station}_VEL"
            if vel_col in df.columns:
                stations.append(station)

    return stations

#Function to create a data frame from the velocity data
def vel_data():
    df = pd.read_csv("Data/Glacier/Glacier_transient_vel.csv")
    return df