#pipeline Logic 


"""Select season
     ↓
Select race
     ↓
Load race session
     ↓
Extract lap data
     ↓
Return structured dataframe"""


import fastf1
import pandas as pd

from preprocess import preprocess_laps

# enable cache to make loading faster
fastf1.Cache.enable_cache('data')

def load_race_data(season, race, session_type):
    
    # load session
    session = fastf1.get_session(season, race, session_type)
    
    session.load()
    
    
    

    # extract lap data
    laps = session.laps

    return laps

def main():

    season = 2025
    race = "Bahrain Grand Prix"
    session_type = "R"

    laps = load_race_data(season, race, session_type)

    clean_laps = preprocess_laps(laps)
    
    print("Session loaded successfully")
    print("Total laps:", len(clean_laps))
    print(clean_laps.head())


if __name__ == "__main__":
    main()
    
    
