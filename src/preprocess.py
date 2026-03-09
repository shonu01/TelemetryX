# need of this file is to preprocess the data and make it ready for the model to train on it

"""Clean data
↓
Select important columns
↓
Convert lap times
↓
Prepare analytics dataset"""


import pandas as pd

def preprocess_laps(laps):
    """
    Clean and prepare lap data for analytics
    """

    # remove laps with missing lap time
    laps = laps.dropna(subset=["LapTime"])

    # select important columns
    laps = laps[[
        "Driver",
        "LapNumber",
        "LapTime",
        "Compound",
        "Stint"
    ]]

    # convert LapTime to seconds
    laps["LapTimeSeconds"] = laps["LapTime"].dt.total_seconds()

    # drop original LapTime column
    laps = laps.drop(columns=["LapTime"])

    return laps