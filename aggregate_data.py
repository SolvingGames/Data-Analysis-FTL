# imports
# data wrangling
import pandas as pd
# string manipulation (regex)
import re
# path information
import pathlib
# file information
import os
import datetime
# excel file creation
import openpyxl
# supressing runtime warning
# RuntimeWarning: Mean of empty slice warnings.warn("Mean of empty slice", RuntimeWarning)
import warnings
warnings.simplefilter("ignore", category=RuntimeWarning)
# determine runtime
import timeit

def aggregate_data(FILE):

    PATH = str(pathlib.Path().absolute()) + "\Data\\"
    df = pd.read_csv(PATH+FILE)

    df = df.reindex(columns=[
        "BEACON",
        "SECTOR NUMBER",
        "TOTAL SHIPS DEFEATED",
        "TOTAL SCRAP COLLECTED",
        "TOTAL CREW HIRED",
        "SCORE",
        "STORE",
        "SCRAP",
        "HULL",
        "FUEL",
        "DRONE PARTS",
        "MISSILES",
        "CREW SIZE",
        "WEAPON SLOT 1",
        "WEAPON SLOT 2",
        "WEAPON SLOT 3",
        "WEAPON SLOT 4",
        "DRONE SLOT 1",
        "DRONE SLOT 2",
        "DRONE SLOT 3",
        "AUGMENTS",
        "POWER CAPACITY",
        "SHIELDS CAPACITY",
        "ENGINES CAPACITY",
        "OXYGEN SYSTEM CAPACITY",
        "WEAPONS SYSTEM CAPACITY",
        "DRONE CONTROL SYSTEM CAPACITY",
        "MEDBAY SYSTEM CAPACITY",
        "TELEPORTER SYSTEM CAPACITY",
        "CLOAKING SYSTEM CAPACITY",
        "ARTILLERY SYSTEM CAPACITY",
        "CLONEBAY SYSTEM CAPACITY",
        "MINDCONTROL SYSTEM CAPACITY",
        "HACKING SYSTEM CAPACITY",
        "PILOT SYTEM CAPACITY",
        "SENSORS SYSTEM CAPACITY",
        "DOORS SYSTEM CAPACITY",
        "BATTERY SYSTEM CAPACITY",
        "CARGO",  
    ])

    # data extraction 1

    # ship used
    ship = re.search(r'\((.*?)-', FILE).group(1)
    ship = ship.strip()

    # date time
    date = os.path.getmtime(PATH+FILE)
    date = datetime.datetime.fromtimestamp(date)

    # result
    if FILE.startswith("w"):
        result = "victory"
    else:
        result = "loss"

    # weapons
    weapon1 = df["WEAPON SLOT 1"].iloc[-1]
    weapon2 = df["WEAPON SLOT 2"].iloc[-1]
    weapon3 = df["WEAPON SLOT 3"].iloc[-1]
    weapon4 = df["WEAPON SLOT 4"].iloc[-1]
    weapons = [weapon1, weapon2, weapon3, weapon4]

    # augments
    augments = df["AUGMENTS"].iloc[-1]

    try:
        augments = augments.split(",")
    except:
        augments = [augments]
        
    ## possible results
    ## no exception: list with 2 or 3 augments
    ## exception thrown: list with none or 1 augment

    if str(augments) == "[nan]" or str(augments) == "nan" or not augments:
        ## list is empty
        print("Ship had no augments installed when finishing the run.")
        augment1 = ""
        augment2 = ""
        augment3 = ""
        augment1_beacon = float("NaN")
        augment2_beacon = float("NaN")
        augment3_beacon = float("NaN")
        
    else:
        augments_beacon = []
        augments_sorted = []
        idx = 0
        

        while idx < df["BEACON"].iloc[-1]-1:
            try:
                val = df.loc[idx,"AUGMENTS"]
            except:
                pass
            idx += 1
            if str(val) == "nan":
                break
                #print("debug-message: current value is nan for augments, beacon {}".format(df.loc[idx,"BEACON"]))
            ## if val only contains one augment
            elif val in augments:
                augments.remove(val)
                augments_beacon.append(idx)
                augments_sorted.append(val)
                idx=0
            else:
                ## val has to be a list of 2-3 augments
                try:
                    val = val.split(",")
                except:
                    pass
                for v in val:
                    if v in augments:
                        augments.remove(v)
                        augments_beacon.append(idx)
                        augments_sorted.append(v)
                        #print(print("FOUND, idx: {}, val: {}, v: {}".format(idx, val, v)))
                        idx=0
                        break
        ## end of loop

        try:
            augment1 = augments_sorted.pop(0)
            augment1_beacon = augments_beacon.pop(0)
        except: 
            augment1 = ""
            augment1_beacon = float("NaN")

        try:
            augment2 = augments_sorted.pop(0)
            augment2_beacon = augments_beacon.pop(0)
        except: 
            augment2 = ""
            augment2_beacon = float("NaN")

        try:
            augment3 = augments_sorted.pop(0)
            augment3_beacon = augments_beacon.pop(0)
        except: 
            augment3 = ""
            augment3_beacon = float("NaN")

    # drones
    drone1 = df["DRONE SLOT 1"].iloc[-1]
    drone2 = df["DRONE SLOT 2"].iloc[-1]
    drone3 = df["DRONE SLOT 3"].iloc[-1]
    drones= [drone1, drone2, drone3]

    # data extraction 2

    ## helper function
    def seperate(series, idx):
        try:
            return series.iloc[idx]
        except: return float("NaN")
        
    # Observation: total, med, mean, std, min, max, sector[1-8], med, mean, std, min, max

    # score
    score_total = df["SCORE"].max()
    score_med = df["SCORE"].median()
    score_mean = df["SCORE"].mean()
    score_std = df["SCORE"].std()
    score_min = df["SCORE"].min()
    score_max = df["SCORE"].max()

    score_per_sector = df["SCORE"].groupby(df["SECTOR NUMBER"]).max()

    # correcting score per sector to show gain instead of total
    temp = 0
    for idx, val in score_per_sector.iteritems():
        score_per_sector[idx] = val - temp
        temp = val

    score_s1 = seperate(score_per_sector, 0)
    score_s2 = seperate(score_per_sector, 0)
    score_s3 = seperate(score_per_sector, 0)
    score_s4 = seperate(score_per_sector, 0)
    score_s5 = seperate(score_per_sector, 0)
    score_s6 = seperate(score_per_sector, 0)
    score_s7 = seperate(score_per_sector, 0)
    score_s8 = seperate(score_per_sector, 0)
    score_s_med = score_per_sector.median()
    score_s_mean = score_per_sector.mean()
    score_s_std = score_per_sector.std()
    score_s_min = score_per_sector.min()
    score_s_max = score_per_sector.max()

    # scrap earned
    temp = 0
    for idx, val in df["SCRAP"].iteritems():
        df.loc[idx,"SCRAP EARNED"] = val - temp
        temp = df.loc[idx,"SCRAP"]

    scrap_earned_total = int(df.loc[df["SCRAP EARNED"] > 0, "SCRAP EARNED"].sum())
    scrap_earned_med = int(df.loc[df["SCRAP EARNED"] > 0, "SCRAP EARNED"].median())
    scrap_earned_mean = int(df.loc[df["SCRAP EARNED"] > 0, "SCRAP EARNED"].mean())
    scrap_earned_std = int(df.loc[df["SCRAP EARNED"] > 0, "SCRAP EARNED"].std())
    scrap_earned_min = int(df.loc[df["SCRAP EARNED"] > 0, "SCRAP EARNED"].min())
    scrap_earned_max = int(df.loc[df["SCRAP EARNED"] > 0, "SCRAP EARNED"].max())

    ## scrap earned per sector
    scrap_earned_per_sector = df.loc[df["SCRAP EARNED"] > 0, "SCRAP EARNED"].groupby(df["SECTOR NUMBER"]).sum()

    scrap_earned_s1 = seperate(scrap_earned_per_sector, 0)
    scrap_earned_s2 = seperate(scrap_earned_per_sector, 1)
    scrap_earned_s3 = seperate(scrap_earned_per_sector, 2)
    scrap_earned_s4 = seperate(scrap_earned_per_sector, 3)
    scrap_earned_s5 = seperate(scrap_earned_per_sector, 4)
    scrap_earned_s6 = seperate(scrap_earned_per_sector, 5)
    scrap_earned_s7 = seperate(scrap_earned_per_sector, 6)
    scrap_earned_s8 = seperate(scrap_earned_per_sector, 7)
    scrap_earned_s_med = scrap_earned_per_sector.median()
    scrap_earned_s_mean = scrap_earned_per_sector.mean()
    scrap_earned_s_std = scrap_earned_per_sector.std()
    scrap_earned_s_min = scrap_earned_per_sector.min()
    scrap_earned_s_max = scrap_earned_per_sector.max()

    # scrap held
    scrap_held_total = df["SCRAP"].sum()
    scrap_held_med = df["SCRAP"].median()
    scrap_held_mean = df["SCRAP"].mean()
    scrap_held_std = df["SCRAP"].std()
    scrap_held_min = df["SCRAP"].min()
    scrap_held_max = df["SCRAP"].max()

    ## ATTENTION: average held scrap is taken into account for sector aggregation
    scrap_held_per_sector = df["SCRAP"].groupby(df["SECTOR NUMBER"]).mean()

    scrap_held_s1 = seperate(scrap_held_per_sector, 0)
    scrap_held_s2 = seperate(scrap_held_per_sector, 1)
    scrap_held_s3 = seperate(scrap_held_per_sector, 2)
    scrap_held_s4 = seperate(scrap_held_per_sector, 3)
    scrap_held_s5 = seperate(scrap_held_per_sector, 4)
    scrap_held_s6 = seperate(scrap_held_per_sector, 5)
    scrap_held_s7 = seperate(scrap_held_per_sector, 6)
    scrap_held_s8 = seperate(scrap_held_per_sector, 7)
    scrap_held_s_med = scrap_held_per_sector.median()
    scrap_held_s_mean = scrap_held_per_sector.mean()
    scrap_held_s_std = scrap_held_per_sector.std()
    scrap_held_s_min = scrap_held_per_sector.min()
    scrap_held_s_max = scrap_held_per_sector.max()

    # beacons
    beacons_total = df["BEACON"].max()
    beacons_med = float("NaN")
    beacons_mean = float("NaN")
    beacons_std = float("NaN")
    beacons_min = float("NaN")
    beacons_max = float("NaN")

    sector_beacons = df["BEACON"].groupby(df["SECTOR NUMBER"]).max()

    beacons_s1 = seperate(sector_beacons, 0)
    beacons_s2 = seperate(sector_beacons, 1)
    beacons_s3 = seperate(sector_beacons, 2)
    beacons_s4 = seperate(sector_beacons, 3)
    beacons_s5 = seperate(sector_beacons, 4)
    beacons_s6 = seperate(sector_beacons, 5)
    beacons_s7 = seperate(sector_beacons, 6)
    beacons_s8 = seperate(sector_beacons, 7)
    beacons_s_med = sector_beacons.median()
    beacons_s_mean = sector_beacons.mean()
    beacons_s_std = sector_beacons.std()
    beacons_s_min = sector_beacons.min()
    beacons_s_max = sector_beacons.max()

    # ships defeated
    ships_defeated_total = df["TOTAL SHIPS DEFEATED"].max()
    ships_defeated_med = float("NaN")
    ships_defeated_mean = float("NaN")
    ships_defeated_std = float("NaN")
    ships_defeated_min = float("NaN")
    ships_defeated_max = float("NaN")

    ships_defeated_per_sector = df["TOTAL SHIPS DEFEATED"].groupby(df["SECTOR NUMBER"]).max()

    # correcting ships defeated per sector to show defeated ships instead of total
    temp = 0
    for idx, val in ships_defeated_per_sector.iteritems():
        ships_defeated_per_sector[idx] = val - temp
        temp = val
        
    ships_defeated_s1 = seperate(ships_defeated_per_sector, 0)
    ships_defeated_s2 = seperate(ships_defeated_per_sector, 1)
    ships_defeated_s3 = seperate(ships_defeated_per_sector, 2)
    ships_defeated_s4 = seperate(ships_defeated_per_sector, 3)
    ships_defeated_s5 = seperate(ships_defeated_per_sector, 4)
    ships_defeated_s6 = seperate(ships_defeated_per_sector, 5)
    ships_defeated_s7 = seperate(ships_defeated_per_sector, 6)
    ships_defeated_s8 = seperate(ships_defeated_per_sector, 7)
    ships_defeated_s_med = ships_defeated_per_sector.median()
    ships_defeated_s_mean = ships_defeated_per_sector.mean()
    ships_defeated_s_std = ships_defeated_per_sector.std()
    ships_defeated_s_min = ships_defeated_per_sector.min()
    ships_defeated_s_max = ships_defeated_per_sector.max()

    # hull
    ## hull_total is a bad descriptor but is a good indicator for a combination of
    ## 2 attributes that need to be maximized anyways --> beacons_total * hull
    hull_total = df["HULL"].sum()
    hull_med = df["HULL"].median()
    hull_mean = df["HULL"].mean()
    hull_std = df["HULL"].std()
    hull_min = df["HULL"].min()
    hull_max = df["HULL"].max()

    ## average hull is taken into account for sector aggregation
    hull_per_sector = df["HULL"].groupby(df["SECTOR NUMBER"]).mean()

    hull_s1 = seperate(hull_per_sector, 0)
    hull_s2 = seperate(hull_per_sector, 1)
    hull_s3 = seperate(hull_per_sector, 2)
    hull_s4 = seperate(hull_per_sector, 3)
    hull_s5 = seperate(hull_per_sector, 4)
    hull_s6 = seperate(hull_per_sector, 5)
    hull_s7 = seperate(hull_per_sector, 6)
    hull_s8 = seperate(hull_per_sector, 7)
    hull_s_med = hull_per_sector.median()
    hull_s_mean = hull_per_sector.mean()
    hull_s_std = hull_per_sector.std()
    hull_s_min = hull_per_sector.min()
    hull_s_max = hull_per_sector.max()

    # hull damage
    temp = 30
    for idx, val in df["HULL"].iteritems():
        if temp == df.loc[idx,"HULL"]:
            df.loc[idx, "HULL DAMAGE"] = 0
        else:
            df.loc[idx, "HULL DAMAGE"] = temp - df.loc[idx,"HULL"]
            temp = df.loc[idx,"HULL"]

    hull_damage_total = df.loc[df["HULL DAMAGE"] > 0, "HULL DAMAGE"].sum()
    hull_damage_med = df.loc[df["HULL DAMAGE"] > 0, "HULL DAMAGE"].median()
    hull_damage_mean = df.loc[df["HULL DAMAGE"] > 0, "HULL DAMAGE"].mean()
    hull_damage_std = df.loc[df["HULL DAMAGE"] > 0, "HULL DAMAGE"].std()
    hull_damage_min = df.loc[df["HULL DAMAGE"] > 0, "HULL DAMAGE"].min()
    hull_damage_max = df.loc[df["HULL DAMAGE"] > 0, "HULL DAMAGE"].max()

    hull_damage_per_sector = df.loc[df["HULL DAMAGE"] > 0, "HULL DAMAGE"].groupby(df["SECTOR NUMBER"]).sum()

    hull_damage_s1 = seperate(hull_damage_per_sector, 0)
    hull_damage_s2 = seperate(hull_damage_per_sector, 1)
    hull_damage_s3 = seperate(hull_damage_per_sector, 2)
    hull_damage_s4 = seperate(hull_damage_per_sector, 3)
    hull_damage_s5 = seperate(hull_damage_per_sector, 4)
    hull_damage_s6 = seperate(hull_damage_per_sector, 5)
    hull_damage_s7 = seperate(hull_damage_per_sector, 6)
    hull_damage_s8 = seperate(hull_damage_per_sector, 7)
    hull_damage_s_med = hull_damage_per_sector.median()
    hull_damage_s_mean = hull_damage_per_sector.mean()
    hull_damage_s_std = hull_damage_per_sector.std()
    hull_damage_s_min = hull_damage_per_sector.min()
    hull_damage_s_max = hull_damage_per_sector.max()

    # cargo amount
    for idx, val in df["CARGO"].iteritems():
        val = str(val)
        if val == "nan":
            df.loc[idx,"CARGO AMOUNT"] = 0
        elif val.count(",") == 1:
            df.loc[idx,"CARGO AMOUNT"] = 2
        elif val.count(",") == 2:
            df.loc[idx,"CARGO AMOUNT"] = 3
        elif val.count(",") == 3:
            df.loc[idx,"CARGO AMOUNT"] = 4
        else:
            df.loc[idx,"CARGO AMOUNT"] = 1

    cargo_total = float("NaN")
    cargo_med = df["CARGO AMOUNT"].median()
    cargo_mean = df["CARGO AMOUNT"].mean()
    cargo_std = df["CARGO AMOUNT"].std()
    cargo_min = df["CARGO AMOUNT"].min()
    cargo_max = df["CARGO AMOUNT"].max()

    ## average cargo amount is taken into account for sector aggregation
    cargo_per_sector = df["CARGO AMOUNT"].groupby(df["SECTOR NUMBER"]).mean()

    cargo_s1 = seperate(cargo_per_sector, 0)
    cargo_s2 = seperate(cargo_per_sector, 1)
    cargo_s3 = seperate(cargo_per_sector, 2)
    cargo_s4 = seperate(cargo_per_sector, 3)
    cargo_s5 = seperate(cargo_per_sector, 4)
    cargo_s6 = seperate(cargo_per_sector, 5)
    cargo_s7 = seperate(cargo_per_sector, 6)
    cargo_s8 = seperate(cargo_per_sector, 7)
    cargo_s_med = cargo_per_sector.median()
    cargo_s_mean = cargo_per_sector.mean()
    cargo_s_std = cargo_per_sector.std()
    cargo_s_min = cargo_per_sector.min()
    cargo_s_max = cargo_per_sector.max()

    # stores visited
    for idx, val in df["STORE"].iteritems():
        val = str(val)
        if val != "nan":
            df.loc[idx,"STORES VISITED"] = 1
        else:
            df.loc[idx,"STORES VISITED"] = float("NaN")
            
    stores_visited_total = df["STORES VISITED"].sum()
    stores_visited_med = float("NaN")
    stores_visited_mean = float("NaN")
    stores_visited_std = float("NaN")
    stores_visited_min = float("NaN")
    stores_visited_max = float("NaN")

    stores_per_sector = df["STORES VISITED"].groupby(df["SECTOR NUMBER"]).sum()

    stores_visited_s1 = seperate(stores_per_sector, 0)
    stores_visited_s2 = seperate(stores_per_sector, 1)
    stores_visited_s3 = seperate(stores_per_sector, 2)
    stores_visited_s4 = seperate(stores_per_sector, 3)
    stores_visited_s5 = seperate(stores_per_sector, 4)
    stores_visited_s6 = seperate(stores_per_sector, 5)
    stores_visited_s7 = seperate(stores_per_sector, 6)
    stores_visited_s8 = seperate(stores_per_sector, 7)
    stores_visited_s_med = stores_per_sector.median()
    stores_visited_s_mean = stores_per_sector.mean()
    stores_visited_s_std = stores_per_sector.std()
    stores_visited_s_min = stores_per_sector.min()
    stores_visited_s_max = stores_per_sector.max()

    # fuel
    temp = 0
    for idx, val in df["FUEL"].iteritems():
        df.loc[idx,"FUEL EARNED"] = val - temp
        temp = df.loc[idx,"FUEL"]
        
    fuel_total = int(df.loc[df["FUEL EARNED"] > 0, "FUEL EARNED"].sum())
    fuel_med = df["FUEL"].median()
    fuel_mean = df["FUEL"].mean()
    fuel_std = df["FUEL"].std()
    fuel_min = df["FUEL"].min()
    fuel_max = df["FUEL"].max()

    ## average fuel amount is taken into account for sector aggregation
    fuel_per_sector = df["FUEL"].groupby(df["SECTOR NUMBER"]).mean()

    fuel_s1 = seperate(fuel_per_sector, 0)
    fuel_s2 = seperate(fuel_per_sector, 1)
    fuel_s3 = seperate(fuel_per_sector, 2)
    fuel_s4 = seperate(fuel_per_sector, 3)
    fuel_s5 = seperate(fuel_per_sector, 4)
    fuel_s6 = seperate(fuel_per_sector, 5)
    fuel_s7 = seperate(fuel_per_sector, 6)
    fuel_s8 = seperate(fuel_per_sector, 7)
    fuel_s_med = fuel_per_sector.median()
    fuel_s_mean = fuel_per_sector.mean()
    fuel_s_std = fuel_per_sector.std()
    fuel_s_min = fuel_per_sector.min()
    fuel_s_max = fuel_per_sector.max()

    # missiles
    temp = 0
    for idx, val in df["MISSILES"].iteritems():
        df.loc[idx,"MISSILES EARNED"] = val - temp
        temp = df.loc[idx,"MISSILES"]

    missiles_total = int(df.loc[df["MISSILES EARNED"] > 0, "MISSILES EARNED"].sum())
    missiles_med = df["MISSILES"].median()
    missiles_mean = df["MISSILES"].mean()
    missiles_std = df["MISSILES"].std()
    missiles_min = df["MISSILES"].min()
    missiles_max = df["MISSILES"].max()

    ## average missile amount is taken into account for sector aggregation
    missiles_per_sector = df["MISSILES"].groupby(df["SECTOR NUMBER"]).mean()

    missiles_s1 = seperate(missiles_per_sector, 0)
    missiles_s2 = seperate(missiles_per_sector, 1)
    missiles_s3 = seperate(missiles_per_sector, 2)
    missiles_s4 = seperate(missiles_per_sector, 3)
    missiles_s5 = seperate(missiles_per_sector, 4)
    missiles_s6 = seperate(missiles_per_sector, 5)
    missiles_s7 = seperate(missiles_per_sector, 6)
    missiles_s8 = seperate(missiles_per_sector, 7)
    missiles_s_med = missiles_per_sector.median()
    missiles_s_mean = missiles_per_sector.mean()
    missiles_s_std = missiles_per_sector.std()
    missiles_s_min = missiles_per_sector.min()
    missiles_s_max = missiles_per_sector.max()

    # drone parts
    temp = 0
    for idx, val in df["DRONE PARTS"].iteritems():
        df.loc[idx,"DRONE PARTS EARNED"] = val - temp
        temp = df.loc[idx,"DRONE PARTS"]

    drone_parts_total = int(df.loc[df["DRONE PARTS EARNED"] > 0, "DRONE PARTS EARNED"].sum())
    drone_parts_med = df["DRONE PARTS"].median()
    drone_parts_mean = df["DRONE PARTS"].mean()
    drone_parts_std = df["DRONE PARTS"].std()
    drone_parts_min = df["DRONE PARTS"].min()
    drone_parts_max = df["DRONE PARTS"].max()

    ## average drone part amount is taken into account for sector aggregation
    drone_parts_per_sector = df["DRONE PARTS"].groupby(df["SECTOR NUMBER"]).mean()

    drone_parts_s1 = seperate(drone_parts_per_sector, 0)
    drone_parts_s2 = seperate(drone_parts_per_sector, 1)
    drone_parts_s3 = seperate(drone_parts_per_sector, 2)
    drone_parts_s4 = seperate(drone_parts_per_sector, 3)
    drone_parts_s5 = seperate(drone_parts_per_sector, 4)
    drone_parts_s6 = seperate(drone_parts_per_sector, 5)
    drone_parts_s7 = seperate(drone_parts_per_sector, 6)
    drone_parts_s8 = seperate(drone_parts_per_sector, 7)
    drone_parts_s_med = drone_parts_per_sector.median()
    drone_parts_s_mean = drone_parts_per_sector.mean()
    drone_parts_s_std = drone_parts_per_sector.std()
    drone_parts_s_min = drone_parts_per_sector.min()
    drone_parts_s_max = drone_parts_per_sector.max()

    # crew hired
    crew_hired_total = df["TOTAL CREW HIRED"].max()
    crew_hired_med = float("NaN")
    crew_hired_mean = float("NaN")
    crew_hired_std = float("NaN")
    crew_hired_min = float("NaN")
    crew_hired_max = float("NaN")

    crew_hired_per_sector = df["TOTAL CREW HIRED"].groupby(df["SECTOR NUMBER"]).max()

    crew_hired_s1 = seperate(crew_hired_per_sector, 0)
    crew_hired_s2 = seperate(crew_hired_per_sector, 1)
    crew_hired_s3 = seperate(crew_hired_per_sector, 2)
    crew_hired_s4 = seperate(crew_hired_per_sector, 3)
    crew_hired_s5 = seperate(crew_hired_per_sector, 4)
    crew_hired_s6 = seperate(crew_hired_per_sector, 5)
    crew_hired_s7 = seperate(crew_hired_per_sector, 6)
    crew_hired_s8 = seperate(crew_hired_per_sector, 7)
    crew_hired_s_med = crew_hired_per_sector.median()
    crew_hired_s_mean = crew_hired_per_sector.mean()
    crew_hired_s_std = crew_hired_per_sector.std()
    crew_hired_s_min = crew_hired_per_sector.min()
    crew_hired_s_max = crew_hired_per_sector.max()

    #crew lost
    for idx, val in df["CREW SIZE"].iteritems():
        ## fixing data collection bug
        if val > 8:
            df.loc[idx, "CREW SIZE"] = 8

    crew_lost = 0
    temp = df["CREW SIZE"].iloc[0]
    for idx, val in df["CREW SIZE"].iteritems():
        if val < temp:
            crew_lost += val - temp
            df.loc[idx,"CREW LOST"] = abs(crew_lost)
        else:
            df.loc[idx,"CREW LOST"] = 0
        temp = val

    crew_lost_total = df["CREW LOST"].sum()
    crew_lost_med = df["CREW LOST"].median()
    crew_lost_mean = df["CREW LOST"].mean()
    crew_lost_std = df["CREW LOST"].std()
    crew_lost_min = df["CREW LOST"].min()
    crew_lost_max = df["CREW LOST"].max()

    crew_lost_per_sector = df.loc[df["CREW LOST"] > 0, "CREW LOST"].groupby(df["SECTOR NUMBER"]).sum()

    crew_lost_s1 = seperate(crew_lost_per_sector, 0)
    crew_lost_s2 = seperate(crew_lost_per_sector, 1)
    crew_lost_s3 = seperate(crew_lost_per_sector, 2)
    crew_lost_s4 = seperate(crew_lost_per_sector, 3)
    crew_lost_s5 = seperate(crew_lost_per_sector, 4)
    crew_lost_s6 = seperate(crew_lost_per_sector, 5)
    crew_lost_s7 = seperate(crew_lost_per_sector, 6)
    crew_lost_s8 = seperate(crew_lost_per_sector, 7)
    crew_lost_s_med = crew_lost_per_sector.median()
    crew_lost_s_mean = crew_lost_per_sector.mean()
    crew_lost_s_std = crew_lost_per_sector.std()
    crew_lost_s_min = crew_lost_per_sector.min()
    crew_lost_s_max = crew_lost_per_sector.max()

    # crew size
    crew_size_total = float("NaN")
    crew_size_med = df["CREW SIZE"].median()
    crew_size_mean = df["CREW SIZE"].mean()
    crew_size_std = df["CREW SIZE"].std()
    crew_size_min = df["CREW SIZE"].min()
    crew_size_max = df["CREW SIZE"].max()

    crew_size_per_sector = df["CREW SIZE"].groupby(df["SECTOR NUMBER"]).max()

    crew_size_s1 = seperate(crew_size_per_sector, 0)
    crew_size_s2 = seperate(crew_size_per_sector, 1)
    crew_size_s3 = seperate(crew_size_per_sector, 2)
    crew_size_s4 = seperate(crew_size_per_sector, 3)
    crew_size_s5 = seperate(crew_size_per_sector, 4)
    crew_size_s6 = seperate(crew_size_per_sector, 5)
    crew_size_s7 = seperate(crew_size_per_sector, 6)
    crew_size_s8 = seperate(crew_size_per_sector, 7)
    crew_size_s_med = crew_size_per_sector.median()
    crew_size_s_mean = crew_size_per_sector.mean()
    crew_size_s_std = crew_size_per_sector.std()
    crew_size_s_min = crew_size_per_sector.min()
    crew_size_s_max = crew_size_per_sector.max()

    # power capacity
    power_capacity_total = float("NaN")
    power_capacity_med = df["POWER CAPACITY"].median()
    power_capacity_mean = df["POWER CAPACITY"].mean()
    power_capacity_std = df["POWER CAPACITY"].std()
    power_capacity_min = df["POWER CAPACITY"].min()
    power_capacity_max = df["POWER CAPACITY"].max()

    power_capacity_per_sector = df["POWER CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    power_capacity_s1 = seperate(power_capacity_per_sector, 0)
    power_capacity_s2 = seperate(power_capacity_per_sector, 1)
    power_capacity_s3 = seperate(power_capacity_per_sector, 2)
    power_capacity_s4 = seperate(power_capacity_per_sector, 3)
    power_capacity_s5 = seperate(power_capacity_per_sector, 4)
    power_capacity_s6 = seperate(power_capacity_per_sector, 5)
    power_capacity_s7 = seperate(power_capacity_per_sector, 6)
    power_capacity_s8 = seperate(power_capacity_per_sector, 7)
    power_capacity_s_med = power_capacity_per_sector.median()
    power_capacity_s_mean = power_capacity_per_sector.mean()
    power_capacity_s_std = power_capacity_per_sector.std()
    power_capacity_s_min = power_capacity_per_sector.min()
    power_capacity_s_max = power_capacity_per_sector.max()

    # weapons system capacity
    weapons_capacity_total = float("NaN")
    weapons_capacity_med = df["WEAPONS SYSTEM CAPACITY"].median()
    weapons_capacity_mean = df["WEAPONS SYSTEM CAPACITY"].mean()
    weapons_capacity_std = df["WEAPONS SYSTEM CAPACITY"].std()
    weapons_capacity_min = df["WEAPONS SYSTEM CAPACITY"].min()
    weapons_capacity_max = df["WEAPONS SYSTEM CAPACITY"].max()

    weapons_capacity_per_sector = df["WEAPONS SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    weapons_capacity_s1 = seperate(weapons_capacity_per_sector, 0)
    weapons_capacity_s2 = seperate(weapons_capacity_per_sector, 1)
    weapons_capacity_s3 = seperate(weapons_capacity_per_sector, 2)
    weapons_capacity_s4 = seperate(weapons_capacity_per_sector, 3)
    weapons_capacity_s5 = seperate(weapons_capacity_per_sector, 4)
    weapons_capacity_s6 = seperate(weapons_capacity_per_sector, 5)
    weapons_capacity_s7 = seperate(weapons_capacity_per_sector, 6)
    weapons_capacity_s8 = seperate(weapons_capacity_per_sector, 7)
    weapons_capacity_s_med = weapons_capacity_per_sector.median()
    weapons_capacity_s_mean = weapons_capacity_per_sector.mean()
    weapons_capacity_s_std = weapons_capacity_per_sector.std()
    weapons_capacity_s_min = weapons_capacity_per_sector.min()
    weapons_capacity_s_max = weapons_capacity_per_sector.max()

    # engines capacity
    engines_capacity_total = float("NaN")
    engines_capacity_med = df["ENGINES CAPACITY"].median()
    engines_capacity_mean = df["ENGINES CAPACITY"].mean()
    engines_capacity_std = df["ENGINES CAPACITY"].std()
    engines_capacity_min = df["ENGINES CAPACITY"].min()
    engines_capacity_max = df["ENGINES CAPACITY"].max()

    engines_capacity_per_sector = df["ENGINES CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    engines_capacity_s1 = seperate(engines_capacity_per_sector, 0)
    engines_capacity_s2 = seperate(engines_capacity_per_sector, 1)
    engines_capacity_s3 = seperate(engines_capacity_per_sector, 2)
    engines_capacity_s4 = seperate(engines_capacity_per_sector, 3)
    engines_capacity_s5 = seperate(engines_capacity_per_sector, 4)
    engines_capacity_s6 = seperate(engines_capacity_per_sector, 5)
    engines_capacity_s7 = seperate(engines_capacity_per_sector, 6)
    engines_capacity_s8 = seperate(engines_capacity_per_sector, 7)
    engines_capacity_s_med = engines_capacity_per_sector.median()
    engines_capacity_s_mean = engines_capacity_per_sector.mean()
    engines_capacity_s_std = engines_capacity_per_sector.std()
    engines_capacity_s_min = engines_capacity_per_sector.min()
    engines_capacity_s_max = engines_capacity_per_sector.max()

    # shields capacity
    shields_capacity_total = float("NaN")
    shields_capacity_med = df["SHIELDS CAPACITY"].median()
    shields_capacity_mean = df["SHIELDS CAPACITY"].mean()
    shields_capacity_std = df["SHIELDS CAPACITY"].std()
    shields_capacity_min = df["SHIELDS CAPACITY"].min()
    shields_capacity_max = df["SHIELDS CAPACITY"].max()

    shields_capacity_per_sector = df["SHIELDS CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    shields_capacity_s1 = seperate(shields_capacity_per_sector, 0)
    shields_capacity_s2 = seperate(shields_capacity_per_sector, 1)
    shields_capacity_s3 = seperate(shields_capacity_per_sector, 2)
    shields_capacity_s4 = seperate(shields_capacity_per_sector, 3)
    shields_capacity_s5 = seperate(shields_capacity_per_sector, 4)
    shields_capacity_s6 = seperate(shields_capacity_per_sector, 5)
    shields_capacity_s7 = seperate(shields_capacity_per_sector, 6)
    shields_capacity_s8 = seperate(shields_capacity_per_sector, 7)
    shields_capacity_s_med = shields_capacity_per_sector.median()
    shields_capacity_s_mean = shields_capacity_per_sector.mean()
    shields_capacity_s_std = shields_capacity_per_sector.std()
    shields_capacity_s_min = shields_capacity_per_sector.min()
    shields_capacity_s_max = shields_capacity_per_sector.max()

    # oxygen system capacity
    oxygen_capacity_total = float("NaN")
    oxygen_capacity_med = df["OXYGEN SYSTEM CAPACITY"].median()
    oxygen_capacity_mean = df["OXYGEN SYSTEM CAPACITY"].mean()
    oxygen_capacity_std = df["OXYGEN SYSTEM CAPACITY"].std()
    oxygen_capacity_min = df["OXYGEN SYSTEM CAPACITY"].min()
    oxygen_capacity_max = df["OXYGEN SYSTEM CAPACITY"].max()

    oxygen_capacity_per_sector = df["OXYGEN SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    oxygen_capacity_s1 = seperate(oxygen_capacity_per_sector, 0)
    oxygen_capacity_s2 = seperate(oxygen_capacity_per_sector, 1)
    oxygen_capacity_s3 = seperate(oxygen_capacity_per_sector, 2)
    oxygen_capacity_s4 = seperate(oxygen_capacity_per_sector, 3)
    oxygen_capacity_s5 = seperate(oxygen_capacity_per_sector, 4)
    oxygen_capacity_s6 = seperate(oxygen_capacity_per_sector, 5)
    oxygen_capacity_s7 = seperate(oxygen_capacity_per_sector, 6)
    oxygen_capacity_s8 = seperate(oxygen_capacity_per_sector, 7)
    oxygen_capacity_s_med = oxygen_capacity_per_sector.median()
    oxygen_capacity_s_mean = oxygen_capacity_per_sector.mean()
    oxygen_capacity_s_std = oxygen_capacity_per_sector.std()
    oxygen_capacity_s_min = oxygen_capacity_per_sector.min()
    oxygen_capacity_s_max = oxygen_capacity_per_sector.max()

    # medbay system capacity
    medbay_capacity_total = float("NaN")
    medbay_capacity_med = df["MEDBAY SYSTEM CAPACITY"].median()
    medbay_capacity_mean = df["MEDBAY SYSTEM CAPACITY"].mean()
    medbay_capacity_std = df["MEDBAY SYSTEM CAPACITY"].std()
    medbay_capacity_min = df["MEDBAY SYSTEM CAPACITY"].min()
    medbay_capacity_max = df["MEDBAY SYSTEM CAPACITY"].max()

    medbay_capacity_per_sector = df["MEDBAY SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    medbay_capacity_s1 = seperate(medbay_capacity_per_sector, 0)
    medbay_capacity_s2 = seperate(medbay_capacity_per_sector, 1)
    medbay_capacity_s3 = seperate(medbay_capacity_per_sector, 2)
    medbay_capacity_s4 = seperate(medbay_capacity_per_sector, 3)
    medbay_capacity_s5 = seperate(medbay_capacity_per_sector, 4)
    medbay_capacity_s6 = seperate(medbay_capacity_per_sector, 5)
    medbay_capacity_s7 = seperate(medbay_capacity_per_sector, 6)
    medbay_capacity_s8 = seperate(medbay_capacity_per_sector, 7)
    medbay_capacity_s_med = medbay_capacity_per_sector.median()
    medbay_capacity_s_mean = medbay_capacity_per_sector.mean()
    medbay_capacity_s_std = medbay_capacity_per_sector.std()
    medbay_capacity_s_min = medbay_capacity_per_sector.min()
    medbay_capacity_s_max = medbay_capacity_per_sector.max()

    # clonebay system capacity
    clonebay_capacity_total = float("NaN")
    clonebay_capacity_med = df["CLONEBAY SYSTEM CAPACITY"].median()
    clonebay_capacity_mean = df["CLONEBAY SYSTEM CAPACITY"].mean()
    clonebay_capacity_std = df["CLONEBAY SYSTEM CAPACITY"].std()
    clonebay_capacity_min = df["CLONEBAY SYSTEM CAPACITY"].min()
    clonebay_capacity_max = df["CLONEBAY SYSTEM CAPACITY"].max()

    clonebay_capacity_per_sector = df["CLONEBAY SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    clonebay_capacity_s1 = seperate(clonebay_capacity_per_sector, 0)
    clonebay_capacity_s2 = seperate(clonebay_capacity_per_sector, 1)
    clonebay_capacity_s3 = seperate(clonebay_capacity_per_sector, 2)
    clonebay_capacity_s4 = seperate(clonebay_capacity_per_sector, 3)
    clonebay_capacity_s5 = seperate(clonebay_capacity_per_sector, 4)
    clonebay_capacity_s6 = seperate(clonebay_capacity_per_sector, 5)
    clonebay_capacity_s7 = seperate(clonebay_capacity_per_sector, 6)
    clonebay_capacity_s8 = seperate(clonebay_capacity_per_sector, 7)
    clonebay_capacity_s_med = clonebay_capacity_per_sector.median()
    clonebay_capacity_s_mean = clonebay_capacity_per_sector.mean()
    clonebay_capacity_s_std = clonebay_capacity_per_sector.std()
    clonebay_capacity_s_min = clonebay_capacity_per_sector.min()
    clonebay_capacity_s_max = clonebay_capacity_per_sector.max()

    # pilot system capacity
    pilot_capacity_total = float("NaN")
    pilot_capacity_med = df["PILOT SYTEM CAPACITY"].median()
    pilot_capacity_mean = df["PILOT SYTEM CAPACITY"].mean()
    pilot_capacity_std = df["PILOT SYTEM CAPACITY"].std()
    pilot_capacity_min = df["PILOT SYTEM CAPACITY"].min()
    pilot_capacity_max = df["PILOT SYTEM CAPACITY"].max()

    pilot_capacity_per_sector = df["PILOT SYTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    pilot_capacity_s1 = seperate(pilot_capacity_per_sector, 0)
    pilot_capacity_s2 = seperate(pilot_capacity_per_sector, 1)
    pilot_capacity_s3 = seperate(pilot_capacity_per_sector, 2)
    pilot_capacity_s4 = seperate(pilot_capacity_per_sector, 3)
    pilot_capacity_s5 = seperate(pilot_capacity_per_sector, 4)
    pilot_capacity_s6 = seperate(pilot_capacity_per_sector, 5)
    pilot_capacity_s7 = seperate(pilot_capacity_per_sector, 6)
    pilot_capacity_s8 = seperate(pilot_capacity_per_sector, 7)
    pilot_capacity_s_med = pilot_capacity_per_sector.median()
    pilot_capacity_s_mean = pilot_capacity_per_sector.mean()
    pilot_capacity_s_std = pilot_capacity_per_sector.std()
    pilot_capacity_s_min = pilot_capacity_per_sector.min()
    pilot_capacity_s_max = pilot_capacity_per_sector.max()

    # sensors system capacity
    sensors_capacity_total = float("NaN")
    sensors_capacity_med = df["SENSORS SYSTEM CAPACITY"].median()
    sensors_capacity_mean = df["SENSORS SYSTEM CAPACITY"].mean()
    sensors_capacity_std = df["SENSORS SYSTEM CAPACITY"].std()
    sensors_capacity_min = df["SENSORS SYSTEM CAPACITY"].min()
    sensors_capacity_max = df["SENSORS SYSTEM CAPACITY"].max()

    sensors_capacity_per_sector = df["SENSORS SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    sensors_capacity_s1 = seperate(sensors_capacity_per_sector, 0)
    sensors_capacity_s2 = seperate(sensors_capacity_per_sector, 1)
    sensors_capacity_s3 = seperate(sensors_capacity_per_sector, 2)
    sensors_capacity_s4 = seperate(sensors_capacity_per_sector, 3)
    sensors_capacity_s5 = seperate(sensors_capacity_per_sector, 4)
    sensors_capacity_s6 = seperate(sensors_capacity_per_sector, 5)
    sensors_capacity_s7 = seperate(sensors_capacity_per_sector, 6)
    sensors_capacity_s8 = seperate(sensors_capacity_per_sector, 7)
    sensors_capacity_s_med = sensors_capacity_per_sector.median()
    sensors_capacity_s_mean = sensors_capacity_per_sector.mean()
    sensors_capacity_s_std = sensors_capacity_per_sector.std()
    sensors_capacity_s_min = sensors_capacity_per_sector.min()
    sensors_capacity_s_max = sensors_capacity_per_sector.max()

    # doors system capacity
    doors_capacity_total = float("NaN")
    doors_capacity_med = df["DOORS SYSTEM CAPACITY"].median()
    doors_capacity_mean = df["DOORS SYSTEM CAPACITY"].mean()
    doors_capacity_std = df["DOORS SYSTEM CAPACITY"].std()
    doors_capacity_min = df["DOORS SYSTEM CAPACITY"].min()
    doors_capacity_max = df["DOORS SYSTEM CAPACITY"].max()

    doors_capacity_per_sector = df["DOORS SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    doors_capacity_s1 = seperate(doors_capacity_per_sector, 0)
    doors_capacity_s2 = seperate(doors_capacity_per_sector, 1)
    doors_capacity_s3 = seperate(doors_capacity_per_sector, 2)
    doors_capacity_s4 = seperate(doors_capacity_per_sector, 3)
    doors_capacity_s5 = seperate(doors_capacity_per_sector, 4)
    doors_capacity_s6 = seperate(doors_capacity_per_sector, 5)
    doors_capacity_s7 = seperate(doors_capacity_per_sector, 6)
    doors_capacity_s8 = seperate(doors_capacity_per_sector, 7)
    doors_capacity_s_med = doors_capacity_per_sector.median()
    doors_capacity_s_mean = doors_capacity_per_sector.mean()
    doors_capacity_s_std = doors_capacity_per_sector.std()
    doors_capacity_s_min = doors_capacity_per_sector.min()
    doors_capacity_s_max = doors_capacity_per_sector.max()

    # drone system capacity
    drone_capacity_total = float("NaN")
    drone_capacity_med = df["DRONE CONTROL SYSTEM CAPACITY"].median()
    drone_capacity_mean = df["DRONE CONTROL SYSTEM CAPACITY"].mean()
    drone_capacity_std = df["DRONE CONTROL SYSTEM CAPACITY"].std()
    drone_capacity_min = df["DRONE CONTROL SYSTEM CAPACITY"].min()
    drone_capacity_max = df["DRONE CONTROL SYSTEM CAPACITY"].max()

    drone_capacity_per_sector = df["DRONE CONTROL SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    drone_capacity_s1 = seperate(drone_capacity_per_sector, 0)
    drone_capacity_s2 = seperate(drone_capacity_per_sector, 1)
    drone_capacity_s3 = seperate(drone_capacity_per_sector, 2)
    drone_capacity_s4 = seperate(drone_capacity_per_sector, 3)
    drone_capacity_s5 = seperate(drone_capacity_per_sector, 4)
    drone_capacity_s6 = seperate(drone_capacity_per_sector, 5)
    drone_capacity_s7 = seperate(drone_capacity_per_sector, 6)
    drone_capacity_s8 = seperate(drone_capacity_per_sector, 7)
    drone_capacity_s_med = drone_capacity_per_sector.median()
    drone_capacity_s_mean = drone_capacity_per_sector.mean()
    drone_capacity_s_std = drone_capacity_per_sector.std()
    drone_capacity_s_min = drone_capacity_per_sector.min()
    drone_capacity_s_max = drone_capacity_per_sector.max()

    # teleporter system capacity
    teleporter_capacity_total = float("NaN")
    teleporter_capacity_med = df["TELEPORTER SYSTEM CAPACITY"].median()
    teleporter_capacity_mean = df["TELEPORTER SYSTEM CAPACITY"].mean()
    teleporter_capacity_std = df["TELEPORTER SYSTEM CAPACITY"].std()
    teleporter_capacity_min = df["TELEPORTER SYSTEM CAPACITY"].min()
    teleporter_capacity_max = df["TELEPORTER SYSTEM CAPACITY"].max()

    teleporter_capacity_per_sector = df["TELEPORTER SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    teleporter_capacity_s1 = seperate(teleporter_capacity_per_sector, 0)
    teleporter_capacity_s2 = seperate(teleporter_capacity_per_sector, 1)
    teleporter_capacity_s3 = seperate(teleporter_capacity_per_sector, 2)
    teleporter_capacity_s4 = seperate(teleporter_capacity_per_sector, 3)
    teleporter_capacity_s5 = seperate(teleporter_capacity_per_sector, 4)
    teleporter_capacity_s6 = seperate(teleporter_capacity_per_sector, 5)
    teleporter_capacity_s7 = seperate(teleporter_capacity_per_sector, 6)
    teleporter_capacity_s8 = seperate(teleporter_capacity_per_sector, 7)
    teleporter_capacity_s_med = teleporter_capacity_per_sector.median()
    teleporter_capacity_s_mean = teleporter_capacity_per_sector.mean()
    teleporter_capacity_s_std = teleporter_capacity_per_sector.std()
    teleporter_capacity_s_min = teleporter_capacity_per_sector.min()
    teleporter_capacity_s_max = teleporter_capacity_per_sector.max()

    # cloaking system capacity
    cloaking_capacity_total = float("NaN")
    cloaking_capacity_med = df["CLOAKING SYSTEM CAPACITY"].median()
    cloaking_capacity_mean = df["CLOAKING SYSTEM CAPACITY"].mean()
    cloaking_capacity_std = df["CLOAKING SYSTEM CAPACITY"].std()
    cloaking_capacity_min = df["CLOAKING SYSTEM CAPACITY"].min()
    cloaking_capacity_max = df["CLOAKING SYSTEM CAPACITY"].max()

    cloaking_capacity_per_sector = df["CLOAKING SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    cloaking_capacity_s1 = seperate(cloaking_capacity_per_sector, 0)
    cloaking_capacity_s2 = seperate(cloaking_capacity_per_sector, 1)
    cloaking_capacity_s3 = seperate(cloaking_capacity_per_sector, 2)
    cloaking_capacity_s4 = seperate(cloaking_capacity_per_sector, 3)
    cloaking_capacity_s5 = seperate(cloaking_capacity_per_sector, 4)
    cloaking_capacity_s6 = seperate(cloaking_capacity_per_sector, 5)
    cloaking_capacity_s7 = seperate(cloaking_capacity_per_sector, 6)
    cloaking_capacity_s8 = seperate(cloaking_capacity_per_sector, 7)
    cloaking_capacity_s_med = cloaking_capacity_per_sector.median()
    cloaking_capacity_s_mean = cloaking_capacity_per_sector.mean()
    cloaking_capacity_s_std = cloaking_capacity_per_sector.std()
    cloaking_capacity_s_min = cloaking_capacity_per_sector.min()
    cloaking_capacity_s_max = cloaking_capacity_per_sector.max()

    # mindcontrol system capacity
    mindcontrol_capacity_total = float("NaN")
    mindcontrol_capacity_med = df["MINDCONTROL SYSTEM CAPACITY"].median()
    mindcontrol_capacity_mean = df["MINDCONTROL SYSTEM CAPACITY"].mean()
    mindcontrol_capacity_std = df["MINDCONTROL SYSTEM CAPACITY"].std()
    mindcontrol_capacity_min = df["MINDCONTROL SYSTEM CAPACITY"].min()
    mindcontrol_capacity_max = df["MINDCONTROL SYSTEM CAPACITY"].max()

    mindcontrol_capacity_per_sector = df["MINDCONTROL SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    mindcontrol_capacity_s1 = seperate(mindcontrol_capacity_per_sector, 0)
    mindcontrol_capacity_s2 = seperate(mindcontrol_capacity_per_sector, 1)
    mindcontrol_capacity_s3 = seperate(mindcontrol_capacity_per_sector, 2)
    mindcontrol_capacity_s4 = seperate(mindcontrol_capacity_per_sector, 3)
    mindcontrol_capacity_s5 = seperate(mindcontrol_capacity_per_sector, 4)
    mindcontrol_capacity_s6 = seperate(mindcontrol_capacity_per_sector, 5)
    mindcontrol_capacity_s7 = seperate(mindcontrol_capacity_per_sector, 6)
    mindcontrol_capacity_s8 = seperate(mindcontrol_capacity_per_sector, 7)
    mindcontrol_capacity_s_med = mindcontrol_capacity_per_sector.median()
    mindcontrol_capacity_s_mean = mindcontrol_capacity_per_sector.mean()
    mindcontrol_capacity_s_std = mindcontrol_capacity_per_sector.std()
    mindcontrol_capacity_s_min = mindcontrol_capacity_per_sector.min()
    mindcontrol_capacity_s_max = mindcontrol_capacity_per_sector.max()

    # hacking system capacity
    hacking_capacity_total = float("NaN")
    hacking_capacity_med = df["HACKING SYSTEM CAPACITY"].median()
    hacking_capacity_mean = df["HACKING SYSTEM CAPACITY"].mean()
    hacking_capacity_std = df["HACKING SYSTEM CAPACITY"].std()
    hacking_capacity_min = df["HACKING SYSTEM CAPACITY"].min()
    hacking_capacity_max = df["HACKING SYSTEM CAPACITY"].max()

    hacking_capacity_per_sector = df["HACKING SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    hacking_capacity_s1 = seperate(hacking_capacity_per_sector, 0)
    hacking_capacity_s2 = seperate(hacking_capacity_per_sector, 1)
    hacking_capacity_s3 = seperate(hacking_capacity_per_sector, 2)
    hacking_capacity_s4 = seperate(hacking_capacity_per_sector, 3)
    hacking_capacity_s5 = seperate(hacking_capacity_per_sector, 4)
    hacking_capacity_s6 = seperate(hacking_capacity_per_sector, 5)
    hacking_capacity_s7 = seperate(hacking_capacity_per_sector, 6)
    hacking_capacity_s8 = seperate(hacking_capacity_per_sector, 7)
    hacking_capacity_s_med = hacking_capacity_per_sector.median()
    hacking_capacity_s_mean = hacking_capacity_per_sector.mean()
    hacking_capacity_s_std = hacking_capacity_per_sector.std()
    hacking_capacity_s_min = hacking_capacity_per_sector.min()
    hacking_capacity_s_max = hacking_capacity_per_sector.max()

    # battery system capacity
    battery_capacity_total = float("NaN")
    battery_capacity_med = df["BATTERY SYSTEM CAPACITY"].median()
    battery_capacity_mean = df["BATTERY SYSTEM CAPACITY"].mean()
    battery_capacity_std = df["BATTERY SYSTEM CAPACITY"].std()
    battery_capacity_min = df["BATTERY SYSTEM CAPACITY"].min()
    battery_capacity_max = df["BATTERY SYSTEM CAPACITY"].max()

    battery_capacity_per_sector = df["BATTERY SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    battery_capacity_s1 = seperate(battery_capacity_per_sector, 0)
    battery_capacity_s2 = seperate(battery_capacity_per_sector, 1)
    battery_capacity_s3 = seperate(battery_capacity_per_sector, 2)
    battery_capacity_s4 = seperate(battery_capacity_per_sector, 3)
    battery_capacity_s5 = seperate(battery_capacity_per_sector, 4)
    battery_capacity_s6 = seperate(battery_capacity_per_sector, 5)
    battery_capacity_s7 = seperate(battery_capacity_per_sector, 6)
    battery_capacity_s8 = seperate(battery_capacity_per_sector, 7)
    battery_capacity_s_med = battery_capacity_per_sector.median()
    battery_capacity_s_mean = battery_capacity_per_sector.mean()
    battery_capacity_s_std = battery_capacity_per_sector.std()
    battery_capacity_s_min = battery_capacity_per_sector.min()
    battery_capacity_s_max = battery_capacity_per_sector.max()

    # artillery system capacity
    artillery_capacity_total = float("NaN")
    artillery_capacity_med = df["ARTILLERY SYSTEM CAPACITY"].median()
    artillery_capacity_mean = df["ARTILLERY SYSTEM CAPACITY"].mean()
    artillery_capacity_std = df["ARTILLERY SYSTEM CAPACITY"].std()
    artillery_capacity_min = df["ARTILLERY SYSTEM CAPACITY"].min()
    artillery_capacity_max = df["ARTILLERY SYSTEM CAPACITY"].max()

    artillery_capacity_per_sector = df["ARTILLERY SYSTEM CAPACITY"].groupby(df["SECTOR NUMBER"]).max()

    artillery_capacity_s1 = seperate(artillery_capacity_per_sector, 0)
    artillery_capacity_s2 = seperate(artillery_capacity_per_sector, 1)
    artillery_capacity_s3 = seperate(artillery_capacity_per_sector, 2)
    artillery_capacity_s4 = seperate(artillery_capacity_per_sector, 3)
    artillery_capacity_s5 = seperate(artillery_capacity_per_sector, 4)
    artillery_capacity_s6 = seperate(artillery_capacity_per_sector, 5)
    artillery_capacity_s7 = seperate(artillery_capacity_per_sector, 6)
    artillery_capacity_s8 = seperate(artillery_capacity_per_sector, 7)
    artillery_capacity_s_med = artillery_capacity_per_sector.median()
    artillery_capacity_s_mean = artillery_capacity_per_sector.mean()
    artillery_capacity_s_std = artillery_capacity_per_sector.std()
    artillery_capacity_s_min = artillery_capacity_per_sector.min()
    artillery_capacity_s_max = artillery_capacity_per_sector.max()

    # data extraction 3
    # weapons and drones pickup beacons

    # placeholder
    weapon1_beacon = float("NaN")
    weapon2_beacon = float("NaN")
    weapon3_beacon = float("NaN")
    weapon4_beacon = float("NaN")
    drone1_beacon = float("NaN")
    drone2_beacon = float("NaN")
    drone3_beacon = float("NaN")

    # weapon pickup beacons
    for idx, val in df["BEACON"].iteritems():
        if (
            weapon1 == df.loc[idx,"WEAPON SLOT 1"] or
            weapon1 == df.loc[idx,"WEAPON SLOT 2"] or
            weapon1 == df.loc[idx,"WEAPON SLOT 3"] or
            weapon1 == df.loc[idx,"WEAPON SLOT 4"]
        ):
            weapon1_beacon = val
            break

    for idx, val in df["BEACON"].iteritems():
        if (
            weapon2 == df.loc[idx,"WEAPON SLOT 1"] or
            weapon2 == df.loc[idx,"WEAPON SLOT 2"] or
            weapon2 == df.loc[idx,"WEAPON SLOT 3"] or
            weapon2 == df.loc[idx,"WEAPON SLOT 4"]
        ):
            weapon2_beacon = val
            break

    for idx, val in df["BEACON"].iteritems():
        if (
            weapon3 == df.loc[idx,"WEAPON SLOT 1"] or
            weapon3 == df.loc[idx,"WEAPON SLOT 2"] or
            weapon3 == df.loc[idx,"WEAPON SLOT 3"] or
            weapon3 == df.loc[idx,"WEAPON SLOT 4"]
        ):
            weapon3_beacon = val
            break

    for idx, val in df["BEACON"].iteritems():
        if (
            weapon4 == df.loc[idx,"WEAPON SLOT 1"] or
            weapon4 == df.loc[idx,"WEAPON SLOT 2"] or
            weapon4 == df.loc[idx,"WEAPON SLOT 3"] or
            weapon4 == df.loc[idx,"WEAPON SLOT 4"]
        ):
            weapon4_beacon = val
            break

    # drone pickup beacons
    for idx, val in df["BEACON"].iteritems():
        if (
            drone1 == df.loc[idx,"DRONE SLOT 1"] or
            drone1 == df.loc[idx,"DRONE SLOT 2"] or
            drone1 == df.loc[idx,"DRONE SLOT 3"]
        ):
            drone1_beacon = val
            break

    for idx, val in df["BEACON"].iteritems():
        if (
            drone2 == df.loc[idx,"DRONE SLOT 1"] or
            drone2 == df.loc[idx,"DRONE SLOT 2"] or
            drone2 == df.loc[idx,"DRONE SLOT 3"]
        ):
            drone2_beacon = val
            break
            
    for idx, val in df["BEACON"].iteritems():
        if (
            drone3 == df.loc[idx,"DRONE SLOT 1"] or
            drone3 == df.loc[idx,"DRONE SLOT 2"] or
            drone3 == df.loc[idx,"DRONE SLOT 3"]
        ):
            drone3_beacon = val
            break

    weapon1_percentage = weapon1_beacon/beacons_total*100
    weapon2_percentage = weapon2_beacon/beacons_total*100
    weapon3_percentage = weapon3_beacon/beacons_total*100
    weapon4_percentage = weapon4_beacon/beacons_total*100
    drone1_percentage = drone1_beacon/beacons_total*100
    drone2_percentage = drone2_beacon/beacons_total*100
    drone3_percentage = drone3_beacon/beacons_total*100

    # dict creation

    dict = {
        "ship":[ship],
        "date":[date],
        "result":[result],
        "weapon1":[weapon1],
        "weapon1_beacon":[weapon1_beacon],
        "weapon2":[weapon2],
        "weapon2_beacon":[weapon2_beacon],
        "weapon3":[weapon3],
        "weapon3_beacon":[weapon3_beacon],
        "weapon4":[weapon4],
        "weapon4_beacon":[weapon4_beacon],
        "augment1":[augment1],
        "augment2":[augment2],
        "augment3":[augment3],
        "augment1_beacon":[augment1_beacon],
        "augment2_beacon":[augment2_beacon],
        "augment3_beacon":[augment3_beacon],
        "drone1":[drone1],
        "drone2":[drone2],
        "drone3":[drone3],
        "drone1_beacon":[drone1_beacon],
        "drone2_beacon":[drone2_beacon],
        "drone3_beacon":[drone3_beacon],
        "score_total":[score_total],
        "score_med":[score_med],
        "score_mean":[score_mean],
        "score_std":[score_std],
        "score_min":[score_min],
        "score_max":[score_max],
        "score_s1":[score_s1],
        "score_s2":[score_s2],
        "score_s3":[score_s3],
        "score_s4":[score_s4],
        "score_s5":[score_s5],
        "score_s6":[score_s6],
        "score_s7":[score_s7],
        "score_s8":[score_s8],
        "score_s_med":[score_s_med],
        "score_s_mean":[score_s_mean],
        "score_s_std":[score_s_std],
        "score_s_min":[score_s_min],
        "score_s_max":[score_s_max],
        "scrap_earned_total":[scrap_earned_total],
        "scrap_earned_med":[scrap_earned_med],
        "scrap_earned_mean":[scrap_earned_mean],
        "scrap_earned_std":[scrap_earned_std],
        "scrap_earned_min":[scrap_earned_min],
        "scrap_earned_max":[scrap_earned_max],
        "scrap_earned_s1":[scrap_earned_s1],
        "scrap_earned_s2":[scrap_earned_s2],
        "scrap_earned_s3":[scrap_earned_s3],
        "scrap_earned_s4":[scrap_earned_s4],
        "scrap_earned_s5":[scrap_earned_s5],
        "scrap_earned_s6":[scrap_earned_s6],
        "scrap_earned_s7":[scrap_earned_s7],
        "scrap_earned_s8":[scrap_earned_s8],
        "scrap_earned_s_med":[scrap_earned_s_med],
        "scrap_earned_s_mean":[scrap_earned_s_mean],
        "scrap_earned_s_std":[scrap_earned_s_std],
        "scrap_earned_s_min":[scrap_earned_s_min],
        "scrap_earned_s_max":[scrap_earned_s_max],
        "scrap_held_total":[scrap_held_total],
        "scrap_held_med":[scrap_held_med],
        "scrap_held_mean":[scrap_held_mean],
        "scrap_held_std":[scrap_held_std],
        "scrap_held_min":[scrap_held_min],
        "scrap_held_max":[scrap_held_max],
        "scrap_held_s1":[scrap_held_s1],
        "scrap_held_s2":[scrap_held_s2],
        "scrap_held_s3":[scrap_held_s3],
        "scrap_held_s4":[scrap_held_s4],
        "scrap_held_s5":[scrap_held_s5],
        "scrap_held_s6":[scrap_held_s6],
        "scrap_held_s7":[scrap_held_s7],
        "scrap_held_s8":[scrap_held_s8],
        "scrap_held_s_med":[scrap_held_s_med],
        "scrap_held_s_mean":[scrap_held_s_mean],
        "scrap_held_s_std":[scrap_held_s_std],
        "scrap_held_s_min":[scrap_held_s_min],
        "scrap_held_s_max":[scrap_held_s_max],
        "beacons_total":[beacons_total],
        "beacons_med":[beacons_med],
        "beacons_mean":[beacons_mean],
        "beacons_std":[beacons_std],
        "beacons_min":[beacons_min],
        "beacons_max":[beacons_max],
        "beacons_s1":[beacons_s1],
        "beacons_s2":[beacons_s2],
        "beacons_s3":[beacons_s3],
        "beacons_s4":[beacons_s4],
        "beacons_s5":[beacons_s5],
        "beacons_s6":[beacons_s6],
        "beacons_s7":[beacons_s7],
        "beacons_s8":[beacons_s8],
        "beacons_s_med":[beacons_s_med],
        "beacons_s_mean":[beacons_s_mean],
        "beacons_s_std":[beacons_s_std],
        "beacons_s_min":[beacons_s_min],
        "beacons_s_max":[beacons_s_max],
        "ships_defeated_total":[ships_defeated_total],
        "ships_defeated_med":[ships_defeated_med],
        "ships_defeated_mean":[ships_defeated_mean],
        "ships_defeated_std":[ships_defeated_std],
        "ships_defeated_min":[ships_defeated_min],
        "ships_defeated_max":[ships_defeated_max],
        "ships_defeated_s1":[ships_defeated_s1],
        "ships_defeated_s2":[ships_defeated_s2],
        "ships_defeated_s3":[ships_defeated_s3],
        "ships_defeated_s4":[ships_defeated_s4],
        "ships_defeated_s5":[ships_defeated_s5],
        "ships_defeated_s6":[ships_defeated_s6],
        "ships_defeated_s7":[ships_defeated_s7],
        "ships_defeated_s8":[ships_defeated_s8],
        "ships_defeated_s_med":[ships_defeated_s_med],
        "ships_defeated_s_mean":[ships_defeated_s_mean],
        "ships_defeated_s_std":[ships_defeated_s_std],
        "ships_defeated_s_min":[ships_defeated_s_min],
        "ships_defeated_s_max":[ships_defeated_s_max],
        "hull_total":[hull_total],
        "hull_med":[hull_med],
        "hull_mean":[hull_mean],
        "hull_std":[hull_std],
        "hull_min":[hull_min],
        "hull_max":[hull_max],
        "hull_s1":[hull_s1],
        "hull_s2":[hull_s2],
        "hull_s3":[hull_s3],
        "hull_s4":[hull_s4],
        "hull_s5":[hull_s5],
        "hull_s6":[hull_s6],
        "hull_s7":[hull_s7],
        "hull_s8":[hull_s8],
        "hull_s_med":[hull_s_med],
        "hull_s_mean":[hull_s_mean],
        "hull_s_std":[hull_s_std],
        "hull_s_min":[hull_s_min],
        "hull_s_max":[hull_s_max],
        "hull_damage_total":[hull_damage_total],
        "hull_damage_med":[hull_damage_med],
        "hull_damage_mean":[hull_damage_mean],
        "hull_damage_std":[hull_damage_std],
        "hull_damage_min":[hull_damage_min],
        "hull_damage_max":[hull_damage_max],
        "hull_damage_s1":[hull_damage_s1],
        "hull_damage_s2":[hull_damage_s2],
        "hull_damage_s3":[hull_damage_s3],
        "hull_damage_s4":[hull_damage_s4],
        "hull_damage_s5":[hull_damage_s5],
        "hull_damage_s6":[hull_damage_s6],
        "hull_damage_s7":[hull_damage_s7],
        "hull_damage_s8":[hull_damage_s8],
        "hull_damage_s_med":[hull_damage_s_med],
        "hull_damage_s_mean":[hull_damage_s_mean],
        "hull_damage_s_std":[hull_damage_s_std],
        "hull_damage_s_min":[hull_damage_s_min],
        "hull_damage_s_max":[hull_damage_s_max],
        "cargo_total":[cargo_total],
        "cargo_med":[cargo_med],
        "cargo_mean":[cargo_mean],
        "cargo_std":[cargo_std],
        "cargo_min":[cargo_min],
        "cargo_max":[cargo_max],
        "cargo_s1":[cargo_s1],
        "cargo_s2":[cargo_s2],
        "cargo_s3":[cargo_s3],
        "cargo_s4":[cargo_s4],
        "cargo_s5":[cargo_s5],
        "cargo_s6":[cargo_s6],
        "cargo_s7":[cargo_s7],
        "cargo_s8":[cargo_s8],
        "cargo_s_med":[cargo_s_med],
        "cargo_s_mean":[cargo_s_mean],
        "cargo_s_std":[cargo_s_std],
        "cargo_s_min":[cargo_s_min],
        "cargo_s_max":[cargo_s_max],
        "stores_visited_total":[stores_visited_total],
        "stores_visited_med":[stores_visited_med],
        "stores_visited_mean":[stores_visited_mean],
        "stores_visited_std":[stores_visited_std],
        "stores_visited_min":[stores_visited_min],
        "stores_visited_max":[stores_visited_max],
        "stores_visited_s1":[stores_visited_s1],
        "stores_visited_s2":[stores_visited_s2],
        "stores_visited_s3":[stores_visited_s3],
        "stores_visited_s4":[stores_visited_s4],
        "stores_visited_s5":[stores_visited_s5],
        "stores_visited_s6":[stores_visited_s6],
        "stores_visited_s7":[stores_visited_s7],
        "stores_visited_s8":[stores_visited_s8],
        "stores_visited_s_med":[stores_visited_s_med],
        "stores_visited_s_mean":[stores_visited_s_mean],
        "stores_visited_s_std":[stores_visited_s_std],
        "stores_visited_s_min":[stores_visited_s_min],
        "stores_visited_s_max":[stores_visited_s_max],
        "fuel_total":[fuel_total],
        "fuel_med":[fuel_med],
        "fuel_mean":[fuel_mean],
        "fuel_std":[fuel_std],
        "fuel_min":[fuel_min],
        "fuel_max":[fuel_max],
        "fuel_s1":[fuel_s1],
        "fuel_s2":[fuel_s2],
        "fuel_s3":[fuel_s3],
        "fuel_s4":[fuel_s4],
        "fuel_s5":[fuel_s5],
        "fuel_s6":[fuel_s6],
        "fuel_s7":[fuel_s7],
        "fuel_s8":[fuel_s8],
        "fuel_s_med":[fuel_s_med],
        "fuel_s_mean":[fuel_s_mean],
        "fuel_s_std":[fuel_s_std],
        "fuel_s_min":[fuel_s_min],
        "fuel_s_max":[fuel_s_max],
        "missiles_total":[missiles_total],
        "missiles_med":[missiles_med],
        "missiles_mean":[missiles_mean],
        "missiles_std":[missiles_std],
        "missiles_min":[missiles_min],
        "missiles_max":[missiles_max],
        "missiles_s1":[missiles_s1],
        "missiles_s2":[missiles_s2],
        "missiles_s3":[missiles_s3],
        "missiles_s4":[missiles_s4],
        "missiles_s5":[missiles_s5],
        "missiles_s6":[missiles_s6],
        "missiles_s7":[missiles_s7],
        "missiles_s8":[missiles_s8],
        "missiles_s_med":[missiles_s_med],
        "missiles_s_mean":[missiles_s_mean],
        "missiles_s_std":[missiles_s_std],
        "missiles_s_min":[missiles_s_min],
        "missiles_s_max":[missiles_s_max],
        "drone_parts_total":[drone_parts_total],
        "drone_parts_med":[drone_parts_med],
        "drone_parts_mean":[drone_parts_mean],
        "drone_parts_std":[drone_parts_std],
        "drone_parts_min":[drone_parts_min],
        "drone_parts_max":[drone_parts_max],
        "drone_parts_s1":[drone_parts_s1],
        "drone_parts_s2":[drone_parts_s2],
        "drone_parts_s3":[drone_parts_s3],
        "drone_parts_s4":[drone_parts_s4],
        "drone_parts_s5":[drone_parts_s5],
        "drone_parts_s6":[drone_parts_s6],
        "drone_parts_s7":[drone_parts_s7],
        "drone_parts_s8":[drone_parts_s8],
        "drone_parts_s_med":[drone_parts_s_med],
        "drone_parts_s_mean":[drone_parts_s_mean],
        "drone_parts_s_std":[drone_parts_s_std],
        "drone_parts_s_min":[drone_parts_s_min],
        "drone_parts_s_max":[drone_parts_s_max],
        "crew_hired_total":[crew_hired_total],
        "crew_hired_med":[crew_hired_med],
        "crew_hired_mean":[crew_hired_mean],
        "crew_hired_std":[crew_hired_std],
        "crew_hired_min":[crew_hired_min],
        "crew_hired_max":[crew_hired_max],
        "crew_hired_s1":[crew_hired_s1],
        "crew_hired_s2":[crew_hired_s2],
        "crew_hired_s3":[crew_hired_s3],
        "crew_hired_s4":[crew_hired_s4],
        "crew_hired_s5":[crew_hired_s5],
        "crew_hired_s6":[crew_hired_s6],
        "crew_hired_s7":[crew_hired_s7],
        "crew_hired_s8":[crew_hired_s8],
        "crew_hired_s_med":[crew_hired_s_med],
        "crew_hired_s_mean":[crew_hired_s_mean],
        "crew_hired_s_std":[crew_hired_s_std],
        "crew_hired_s_min":[crew_hired_s_min],
        "crew_hired_s_max":[crew_hired_s_max],
        "crew_lost_total":[crew_lost_total],
        "crew_lost_med":[crew_lost_med],
        "crew_lost_mean":[crew_lost_mean],
        "crew_lost_std":[crew_lost_std],
        "crew_lost_min":[crew_lost_min],
        "crew_lost_max":[crew_lost_max],
        "crew_lost_s1":[crew_lost_s1],
        "crew_lost_s2":[crew_lost_s2],
        "crew_lost_s3":[crew_lost_s3],
        "crew_lost_s4":[crew_lost_s4],
        "crew_lost_s5":[crew_lost_s5],
        "crew_lost_s6":[crew_lost_s6],
        "crew_lost_s7":[crew_lost_s7],
        "crew_lost_s8":[crew_lost_s8],
        "crew_lost_s_med":[crew_lost_s_med],
        "crew_lost_s_mean":[crew_lost_s_mean],
        "crew_lost_s_std":[crew_lost_s_std],
        "crew_lost_s_min":[crew_lost_s_min],
        "crew_lost_s_max":[crew_lost_s_max],
        "crew_size_total":[crew_size_total],
        "crew_size_med":[crew_size_med],
        "crew_size_mean":[crew_size_mean],
        "crew_size_std":[crew_size_std],
        "crew_size_min":[crew_size_min],
        "crew_size_max":[crew_size_max],
        "crew_size_s1":[crew_size_s1],
        "crew_size_s2":[crew_size_s2],
        "crew_size_s3":[crew_size_s3],
        "crew_size_s4":[crew_size_s4],
        "crew_size_s5":[crew_size_s5],
        "crew_size_s6":[crew_size_s6],
        "crew_size_s7":[crew_size_s7],
        "crew_size_s8":[crew_size_s8],
        "crew_size_s_med":[crew_size_s_med],
        "crew_size_s_mean":[crew_size_s_mean],
        "crew_size_s_std":[crew_size_s_std],
        "crew_size_s_min":[crew_size_s_min],
        "crew_size_s_max":[crew_size_s_max],
        "power_capacity_total":[power_capacity_total],
        "power_capacity_med":[power_capacity_med],
        "power_capacity_mean":[power_capacity_mean],
        "power_capacity_std":[power_capacity_std],
        "power_capacity_min":[power_capacity_min],
        "power_capacity_max":[power_capacity_max],
        "power_capacity_s1":[power_capacity_s1],
        "power_capacity_s2":[power_capacity_s2],
        "power_capacity_s3":[power_capacity_s3],
        "power_capacity_s4":[power_capacity_s4],
        "power_capacity_s5":[power_capacity_s5],
        "power_capacity_s6":[power_capacity_s6],
        "power_capacity_s7":[power_capacity_s7],
        "power_capacity_s8":[power_capacity_s8],
        "power_capacity_s_med":[power_capacity_s_med],
        "power_capacity_s_mean":[power_capacity_s_mean],
        "power_capacity_s_std":[power_capacity_s_std],
        "power_capacity_s_min":[power_capacity_s_min],
        "power_capacity_s_max":[power_capacity_s_max],
        "weapons_capacity_total":[weapons_capacity_total],
        "weapons_capacity_med":[weapons_capacity_med],
        "weapons_capacity_mean":[weapons_capacity_mean],
        "weapons_capacity_std":[weapons_capacity_std],
        "weapons_capacity_min":[weapons_capacity_min],
        "weapons_capacity_max":[weapons_capacity_max],
        "weapons_capacity_s1":[weapons_capacity_s1],
        "weapons_capacity_s2":[weapons_capacity_s2],
        "weapons_capacity_s3":[weapons_capacity_s3],
        "weapons_capacity_s4":[weapons_capacity_s4],
        "weapons_capacity_s5":[weapons_capacity_s5],
        "weapons_capacity_s6":[weapons_capacity_s6],
        "weapons_capacity_s7":[weapons_capacity_s7],
        "weapons_capacity_s8":[weapons_capacity_s8],
        "weapons_capacity_s_med":[weapons_capacity_s_med],
        "weapons_capacity_s_mean":[weapons_capacity_s_mean],
        "weapons_capacity_s_std":[weapons_capacity_s_std],
        "weapons_capacity_s_min":[weapons_capacity_s_min],
        "weapons_capacity_s_max":[weapons_capacity_s_max],
        "engines_capacity_total":[engines_capacity_total],
        "engines_capacity_med":[engines_capacity_med],
        "engines_capacity_mean":[engines_capacity_mean],
        "engines_capacity_std":[engines_capacity_std],
        "engines_capacity_min":[engines_capacity_min],
        "engines_capacity_max":[engines_capacity_max],
        "engines_capacity_s1":[engines_capacity_s1],
        "engines_capacity_s2":[engines_capacity_s2],
        "engines_capacity_s3":[engines_capacity_s3],
        "engines_capacity_s4":[engines_capacity_s4],
        "engines_capacity_s5":[engines_capacity_s5],
        "engines_capacity_s6":[engines_capacity_s6],
        "engines_capacity_s7":[engines_capacity_s7],
        "engines_capacity_s8":[engines_capacity_s8],
        "engines_capacity_s_med":[engines_capacity_s_med],
        "engines_capacity_s_mean":[engines_capacity_s_mean],
        "engines_capacity_s_std":[engines_capacity_s_std],
        "engines_capacity_s_min":[engines_capacity_s_min],
        "engines_capacity_s_max":[engines_capacity_s_max],
        "shields_capacity_total":[shields_capacity_total],
        "shields_capacity_med":[shields_capacity_med],
        "shields_capacity_mean":[shields_capacity_mean],
        "shields_capacity_std":[shields_capacity_std],
        "shields_capacity_min":[shields_capacity_min],
        "shields_capacity_max":[shields_capacity_max],
        "shields_capacity_s1":[shields_capacity_s1],
        "shields_capacity_s2":[shields_capacity_s2],
        "shields_capacity_s3":[shields_capacity_s3],
        "shields_capacity_s4":[shields_capacity_s4],
        "shields_capacity_s5":[shields_capacity_s5],
        "shields_capacity_s6":[shields_capacity_s6],
        "shields_capacity_s7":[shields_capacity_s7],
        "shields_capacity_s8":[shields_capacity_s8],
        "shields_capacity_s_med":[shields_capacity_s_med],
        "shields_capacity_s_mean":[shields_capacity_s_mean],
        "shields_capacity_s_std":[shields_capacity_s_std],
        "shields_capacity_s_min":[shields_capacity_s_min],
        "shields_capacity_s_max":[shields_capacity_s_max],
        "oxygen_capacity_total":[oxygen_capacity_total],
        "oxygen_capacity_med":[oxygen_capacity_med],
        "oxygen_capacity_mean":[oxygen_capacity_mean],
        "oxygen_capacity_std":[oxygen_capacity_std],
        "oxygen_capacity_min":[oxygen_capacity_min],
        "oxygen_capacity_max":[oxygen_capacity_max],
        "oxygen_capacity_s1":[oxygen_capacity_s1],
        "oxygen_capacity_s2":[oxygen_capacity_s2],
        "oxygen_capacity_s3":[oxygen_capacity_s3],
        "oxygen_capacity_s4":[oxygen_capacity_s4],
        "oxygen_capacity_s5":[oxygen_capacity_s5],
        "oxygen_capacity_s6":[oxygen_capacity_s6],
        "oxygen_capacity_s7":[oxygen_capacity_s7],
        "oxygen_capacity_s8":[oxygen_capacity_s8],
        "oxygen_capacity_s_med":[oxygen_capacity_s_med],
        "oxygen_capacity_s_mean":[oxygen_capacity_s_mean],
        "oxygen_capacity_s_std":[oxygen_capacity_s_std],
        "oxygen_capacity_s_min":[oxygen_capacity_s_min],
        "oxygen_capacity_s_max":[oxygen_capacity_s_max],
        "medbay_capacity_total":[medbay_capacity_total],
        "medbay_capacity_med":[medbay_capacity_med],
        "medbay_capacity_mean":[medbay_capacity_mean],
        "medbay_capacity_std":[medbay_capacity_std],
        "medbay_capacity_min":[medbay_capacity_min],
        "medbay_capacity_max":[medbay_capacity_max],
        "medbay_capacity_s1":[medbay_capacity_s1],
        "medbay_capacity_s2":[medbay_capacity_s2],
        "medbay_capacity_s3":[medbay_capacity_s3],
        "medbay_capacity_s4":[medbay_capacity_s4],
        "medbay_capacity_s5":[medbay_capacity_s5],
        "medbay_capacity_s6":[medbay_capacity_s6],
        "medbay_capacity_s7":[medbay_capacity_s7],
        "medbay_capacity_s8":[medbay_capacity_s8],
        "medbay_capacity_s_med":[medbay_capacity_s_med],
        "medbay_capacity_s_mean":[medbay_capacity_s_mean],
        "medbay_capacity_s_std":[medbay_capacity_s_std],
        "medbay_capacity_s_min":[medbay_capacity_s_min],
        "medbay_capacity_s_max":[medbay_capacity_s_max],
        "clonebay_capacity_total":[clonebay_capacity_total],
        "clonebay_capacity_med":[clonebay_capacity_med],
        "clonebay_capacity_mean":[clonebay_capacity_mean],
        "clonebay_capacity_std":[clonebay_capacity_std],
        "clonebay_capacity_min":[clonebay_capacity_min],
        "clonebay_capacity_max":[clonebay_capacity_max],
        "clonebay_capacity_s1":[clonebay_capacity_s1],
        "clonebay_capacity_s2":[clonebay_capacity_s2],
        "clonebay_capacity_s3":[clonebay_capacity_s3],
        "clonebay_capacity_s4":[clonebay_capacity_s4],
        "clonebay_capacity_s5":[clonebay_capacity_s5],
        "clonebay_capacity_s6":[clonebay_capacity_s6],
        "clonebay_capacity_s7":[clonebay_capacity_s7],
        "clonebay_capacity_s8":[clonebay_capacity_s8],
        "clonebay_capacity_s_med":[clonebay_capacity_s_med],
        "clonebay_capacity_s_mean":[clonebay_capacity_s_mean],
        "clonebay_capacity_s_std":[clonebay_capacity_s_std],
        "clonebay_capacity_s_min":[clonebay_capacity_s_min],
        "clonebay_capacity_s_max":[clonebay_capacity_s_max],
        "pilot_capacity_total":[pilot_capacity_total],
        "pilot_capacity_med":[pilot_capacity_med],
        "pilot_capacity_mean":[pilot_capacity_mean],
        "pilot_capacity_std":[pilot_capacity_std],
        "pilot_capacity_min":[pilot_capacity_min],
        "pilot_capacity_max":[pilot_capacity_max],
        "pilot_capacity_s1":[pilot_capacity_s1],
        "pilot_capacity_s2":[pilot_capacity_s2],
        "pilot_capacity_s3":[pilot_capacity_s3],
        "pilot_capacity_s4":[pilot_capacity_s4],
        "pilot_capacity_s5":[pilot_capacity_s5],
        "pilot_capacity_s6":[pilot_capacity_s6],
        "pilot_capacity_s7":[pilot_capacity_s7],
        "pilot_capacity_s8":[pilot_capacity_s8],
        "pilot_capacity_s_med":[pilot_capacity_s_med],
        "pilot_capacity_s_mean":[pilot_capacity_s_mean],
        "pilot_capacity_s_std":[pilot_capacity_s_std],
        "pilot_capacity_s_min":[pilot_capacity_s_min],
        "pilot_capacity_s_max":[pilot_capacity_s_max],
        "sensors_capacity_total":[sensors_capacity_total],
        "sensors_capacity_med":[sensors_capacity_med],
        "sensors_capacity_mean":[sensors_capacity_mean],
        "sensors_capacity_std":[sensors_capacity_std],
        "sensors_capacity_min":[sensors_capacity_min],
        "sensors_capacity_max":[sensors_capacity_max],
        "sensors_capacity_s1":[sensors_capacity_s1],
        "sensors_capacity_s2":[sensors_capacity_s2],
        "sensors_capacity_s3":[sensors_capacity_s3],
        "sensors_capacity_s4":[sensors_capacity_s4],
        "sensors_capacity_s5":[sensors_capacity_s5],
        "sensors_capacity_s6":[sensors_capacity_s6],
        "sensors_capacity_s7":[sensors_capacity_s7],
        "sensors_capacity_s8":[sensors_capacity_s8],
        "sensors_capacity_s_med":[sensors_capacity_s_med],
        "sensors_capacity_s_mean":[sensors_capacity_s_mean],
        "sensors_capacity_s_std":[sensors_capacity_s_std],
        "sensors_capacity_s_min":[sensors_capacity_s_min],
        "sensors_capacity_s_max":[sensors_capacity_s_max],
        "doors_capacity_total":[doors_capacity_total],
        "doors_capacity_med":[doors_capacity_med],
        "doors_capacity_mean":[doors_capacity_mean],
        "doors_capacity_std":[doors_capacity_std],
        "doors_capacity_min":[doors_capacity_min],
        "doors_capacity_max":[doors_capacity_max],
        "doors_capacity_s1":[doors_capacity_s1],
        "doors_capacity_s2":[doors_capacity_s2],
        "doors_capacity_s3":[doors_capacity_s3],
        "doors_capacity_s4":[doors_capacity_s4],
        "doors_capacity_s5":[doors_capacity_s5],
        "doors_capacity_s6":[doors_capacity_s6],
        "doors_capacity_s7":[doors_capacity_s7],
        "doors_capacity_s8":[doors_capacity_s8],
        "doors_capacity_s_med":[doors_capacity_s_med],
        "doors_capacity_s_mean":[doors_capacity_s_mean],
        "doors_capacity_s_std":[doors_capacity_s_std],
        "doors_capacity_s_min":[doors_capacity_s_min],
        "doors_capacity_s_max":[doors_capacity_s_max],
        "drone_capacity_total":[drone_capacity_total],
        "drone_capacity_med":[drone_capacity_med],
        "drone_capacity_mean":[drone_capacity_mean],
        "drone_capacity_std":[drone_capacity_std],
        "drone_capacity_min":[drone_capacity_min],
        "drone_capacity_max":[drone_capacity_max],
        "drone_capacity_s1":[drone_capacity_s1],
        "drone_capacity_s2":[drone_capacity_s2],
        "drone_capacity_s3":[drone_capacity_s3],
        "drone_capacity_s4":[drone_capacity_s4],
        "drone_capacity_s5":[drone_capacity_s5],
        "drone_capacity_s6":[drone_capacity_s6],
        "drone_capacity_s7":[drone_capacity_s7],
        "drone_capacity_s8":[drone_capacity_s8],
        "drone_capacity_s_med":[drone_capacity_s_med],
        "drone_capacity_s_mean":[drone_capacity_s_mean],
        "drone_capacity_s_std":[drone_capacity_s_std],
        "drone_capacity_s_min":[drone_capacity_s_min],
        "drone_capacity_s_max":[drone_capacity_s_max],
        "teleporter_capacity_total":[teleporter_capacity_total],
        "teleporter_capacity_med":[teleporter_capacity_med],
        "teleporter_capacity_mean":[teleporter_capacity_mean],
        "teleporter_capacity_std":[teleporter_capacity_std],
        "teleporter_capacity_min":[teleporter_capacity_min],
        "teleporter_capacity_max":[teleporter_capacity_max],
        "teleporter_capacity_s1":[teleporter_capacity_s1],
        "teleporter_capacity_s2":[teleporter_capacity_s2],
        "teleporter_capacity_s3":[teleporter_capacity_s3],
        "teleporter_capacity_s4":[teleporter_capacity_s4],
        "teleporter_capacity_s5":[teleporter_capacity_s5],
        "teleporter_capacity_s6":[teleporter_capacity_s6],
        "teleporter_capacity_s7":[teleporter_capacity_s7],
        "teleporter_capacity_s8":[teleporter_capacity_s8],
        "teleporter_capacity_s_med":[teleporter_capacity_s_med],
        "teleporter_capacity_s_mean":[teleporter_capacity_s_mean],
        "teleporter_capacity_s_std":[teleporter_capacity_s_std],
        "teleporter_capacity_s_min":[teleporter_capacity_s_min],
        "teleporter_capacity_s_max":[teleporter_capacity_s_max],
        "cloaking_capacity_total":[cloaking_capacity_total],
        "cloaking_capacity_med":[cloaking_capacity_med],
        "cloaking_capacity_mean":[cloaking_capacity_mean],
        "cloaking_capacity_std":[cloaking_capacity_std],
        "cloaking_capacity_min":[cloaking_capacity_min],
        "cloaking_capacity_max":[cloaking_capacity_max],
        "cloaking_capacity_s1":[cloaking_capacity_s1],
        "cloaking_capacity_s2":[cloaking_capacity_s2],
        "cloaking_capacity_s3":[cloaking_capacity_s3],
        "cloaking_capacity_s4":[cloaking_capacity_s4],
        "cloaking_capacity_s5":[cloaking_capacity_s5],
        "cloaking_capacity_s6":[cloaking_capacity_s6],
        "cloaking_capacity_s7":[cloaking_capacity_s7],
        "cloaking_capacity_s8":[cloaking_capacity_s8],
        "cloaking_capacity_s_med":[cloaking_capacity_s_med],
        "cloaking_capacity_s_mean":[cloaking_capacity_s_mean],
        "cloaking_capacity_s_std":[cloaking_capacity_s_std],
        "cloaking_capacity_s_min":[cloaking_capacity_s_min],
        "cloaking_capacity_s_max":[cloaking_capacity_s_max],
        "mindcontrol_capacity_total":[mindcontrol_capacity_total],
        "mindcontrol_capacity_med":[mindcontrol_capacity_med],
        "mindcontrol_capacity_mean":[mindcontrol_capacity_mean],
        "mindcontrol_capacity_std":[mindcontrol_capacity_std],
        "mindcontrol_capacity_min":[mindcontrol_capacity_min],
        "mindcontrol_capacity_max":[mindcontrol_capacity_max],
        "mindcontrol_capacity_s1":[mindcontrol_capacity_s1],
        "mindcontrol_capacity_s2":[mindcontrol_capacity_s2],
        "mindcontrol_capacity_s3":[mindcontrol_capacity_s3],
        "mindcontrol_capacity_s4":[mindcontrol_capacity_s4],
        "mindcontrol_capacity_s5":[mindcontrol_capacity_s5],
        "mindcontrol_capacity_s6":[mindcontrol_capacity_s6],
        "mindcontrol_capacity_s7":[mindcontrol_capacity_s7],
        "mindcontrol_capacity_s8":[mindcontrol_capacity_s8],
        "mindcontrol_capacity_s_med":[mindcontrol_capacity_s_med],
        "mindcontrol_capacity_s_mean":[mindcontrol_capacity_s_mean],
        "mindcontrol_capacity_s_std":[mindcontrol_capacity_s_std],
        "mindcontrol_capacity_s_min":[mindcontrol_capacity_s_min],
        "mindcontrol_capacity_s_max":[mindcontrol_capacity_s_max],
        "hacking_capacity_total":[hacking_capacity_total],
        "hacking_capacity_med":[hacking_capacity_med],
        "hacking_capacity_mean":[hacking_capacity_mean],
        "hacking_capacity_std":[hacking_capacity_std],
        "hacking_capacity_min":[hacking_capacity_min],
        "hacking_capacity_max":[hacking_capacity_max],
        "hacking_capacity_s1":[hacking_capacity_s1],
        "hacking_capacity_s2":[hacking_capacity_s2],
        "hacking_capacity_s3":[hacking_capacity_s3],
        "hacking_capacity_s4":[hacking_capacity_s4],
        "hacking_capacity_s5":[hacking_capacity_s5],
        "hacking_capacity_s6":[hacking_capacity_s6],
        "hacking_capacity_s7":[hacking_capacity_s7],
        "hacking_capacity_s8":[hacking_capacity_s8],
        "hacking_capacity_s_med":[hacking_capacity_s_med],
        "hacking_capacity_s_mean":[hacking_capacity_s_mean],
        "hacking_capacity_s_std":[hacking_capacity_s_std],
        "hacking_capacity_s_min":[hacking_capacity_s_min],
        "hacking_capacity_s_max":[hacking_capacity_s_max],
        "battery_capacity_total":[battery_capacity_total],
        "battery_capacity_med":[battery_capacity_med],
        "battery_capacity_mean":[battery_capacity_mean],
        "battery_capacity_std":[battery_capacity_std],
        "battery_capacity_min":[battery_capacity_min],
        "battery_capacity_max":[battery_capacity_max],
        "battery_capacity_s1":[battery_capacity_s1],
        "battery_capacity_s2":[battery_capacity_s2],
        "battery_capacity_s3":[battery_capacity_s3],
        "battery_capacity_s4":[battery_capacity_s4],
        "battery_capacity_s5":[battery_capacity_s5],
        "battery_capacity_s6":[battery_capacity_s6],
        "battery_capacity_s7":[battery_capacity_s7],
        "battery_capacity_s8":[battery_capacity_s8],
        "battery_capacity_s_med":[battery_capacity_s_med],
        "battery_capacity_s_mean":[battery_capacity_s_mean],
        "battery_capacity_s_std":[battery_capacity_s_std],
        "battery_capacity_s_min":[battery_capacity_s_min],
        "battery_capacity_s_max":[battery_capacity_s_max],
        "artillery_capacity_total":[artillery_capacity_total],
        "artillery_capacity_med":[artillery_capacity_med],
        "artillery_capacity_mean":[artillery_capacity_mean],
        "artillery_capacity_std":[artillery_capacity_std],
        "artillery_capacity_min":[artillery_capacity_min],
        "artillery_capacity_max":[artillery_capacity_max],
        "artillery_capacity_s1":[artillery_capacity_s1],
        "artillery_capacity_s2":[artillery_capacity_s2],
        "artillery_capacity_s3":[artillery_capacity_s3],
        "artillery_capacity_s4":[artillery_capacity_s4],
        "artillery_capacity_s5":[artillery_capacity_s5],
        "artillery_capacity_s6":[artillery_capacity_s6],
        "artillery_capacity_s7":[artillery_capacity_s7],
        "artillery_capacity_s8":[artillery_capacity_s8],
        "artillery_capacity_s_med":[artillery_capacity_s_med],
        "artillery_capacity_s_mean":[artillery_capacity_s_mean],
        "artillery_capacity_s_std":[artillery_capacity_s_std],
        "artillery_capacity_s_min":[artillery_capacity_s_min],
        "artillery_capacity_s_max":[artillery_capacity_s_max],
        "weapon1_percentage":[weapon1_percentage],
        "weapon2_percentage":[weapon2_percentage],
        "weapon3_percentage":[weapon3_percentage],
        "weapon4_percentage":[weapon4_percentage],
        "drone1_percentage":[drone1_percentage],
        "drone2_percentage":[drone2_percentage],
        "drone3_percentage":[drone3_percentage]
    }

    # append data in excel

    # create new row
    row = pd.DataFrame.from_dict(dict)

    # read in aggregations and add new row
    data = pd.read_excel('analysis.xlsx')
    data = data.append(row)
    data = data.drop_duplicates()

    # saving aggregation with excel writer
    # needed to not overwrite existing sheets and build report

    FILE = str(pathlib.Path().absolute()) + r"\analysis.xlsx"

    with pd.ExcelWriter(FILE, engine = "openpyxl",  mode='a', float_format="%.1f") as writer:
        workBook = writer.book
        try:
            workBook.remove(workBook['aggregation'])
        except:
            print("worksheet doesn't exist")
        finally:
            data.to_excel(writer, sheet_name='aggregation', index = False)
        writer.save()
        writer.close()



if __name__ == "__main__":
    
    start = timeit.default_timer()

    PATH = str(pathlib.Path().absolute()) + "\Data\\"
    
    for FILE in os.listdir(PATH):
        
        print("working - {}".format(FILE))
        aggregate_data(FILE)
        print("done - {}".format(FILE))
        
    stop = timeit.default_timer()
    print("Runtime: {:.2f} s".format(stop - start))