import fastf1
import pandas as pd
import numpy as np

all_laps = []

for rnd in range(1, 23):
    try:
        print(f"Processing Round {rnd}...")

        session = fastf1.get_session(2021, rnd, "R") # R is to retrieve only race data and not practice or qualifying data
        # this creates a session object that retrieves the 2021 race data
        session.load() # this is where we download the data

        weather = session.weather_data # we collect weather data 

        for _, lap in session.laps.iterrows(): # this is to loop through each lap of each round/race
            if pd.isna(lap["LapTime"]): # in case of null lap time values we ignore those data
                continue

            try:
                telemetry = lap.get_car_data().add_distance() # to get telemetry data of each/current lap

                # telemetry data anlysis 
                avg_speed = telemetry["Speed"].mean()
                max_speed = telemetry["Speed"].max()
                avg_throttle = telemetry["Throttle"].mean()
                brake_percent = telemetry["Brake"].mean() * 100
                avg_rpm = telemetry["RPM"].mean()
                avg_gear = telemetry["nGear"].mean()
                drs_percent = telemetry["DRS"].gt(0).mean() * 100

            except Exception: # in case of telemetry data retrieval failures
                avg_speed = np.nan
                max_speed = np.nan
                avg_throttle = np.nan
                brake_percent = np.nan
                avg_rpm = np.nan
                avg_gear = np.nan
                drs_percent = np.nan

            # to structure how a row should be for each round
            row = {
                "Race": session.event["EventName"],
                "Round": rnd,
                "Driver": lap["Driver"],
                "Team": lap["Team"],
                "LapNumber": lap["LapNumber"],
                "Position": lap["Position"],
                "Stint": lap["Stint"],
                "Compound": lap["Compound"],
                "TyreLife": lap["TyreLife"],
                "FreshTyre": lap["FreshTyre"],
                "TrackStatus": lap["TrackStatus"],
                "Sector1Time": lap["Sector1Time"].total_seconds() if pd.notna(lap["Sector1Time"]) else np.nan,
                "Sector2Time": lap["Sector2Time"].total_seconds() if pd.notna(lap["Sector2Time"]) else np.nan,
                "Sector3Time": lap["Sector3Time"].total_seconds() if pd.notna(lap["Sector3Time"]) else np.nan,
                "LapTime": lap["LapTime"].total_seconds(),
                "AvgSpeed": avg_speed,
                "MaxSpeed": max_speed,
                "AvgThrottle": avg_throttle,
                "BrakePercent": brake_percent,
                "AvgRPM": avg_rpm,
                "AvgGear": avg_gear,
                "DRSUsagePercent": drs_percent,
                "AirTemp": weather["AirTemp"].mean(),
                "TrackTemp": weather["TrackTemp"].mean(),
                "Humidity": weather["Humidity"].mean(),
                "Pressure": weather["Pressure"].mean(),
                "WindDirection": weather["WindDirection"].mean(),
                "WindSpeed": weather["WindSpeed"].mean()
            }

            all_laps.append(row)

        print(f"Finished {session.event['EventName']}")

    except Exception as e:
        print(f"Failed Round {rnd}")
        print(e)

df = pd.DataFrame(all_laps)
df.to_csv("laps_2021.csv", index=False)
