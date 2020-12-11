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

# reading file

df = pd.read_excel(io="analysis.xlsx",sheet_name="aggregation")

# extract data for overview report

ship = df["ship"].iloc[-1]
date = df["date"].iloc[-1]

result = df["result"].iloc[-1]
total_games = len(df)
wins = int(df.loc[df["result"] == "victory", "result"].count())
losses = int(df.loc[df["result"] == "loss", "result"].count())
win_percentage = wins/len(df)

x = df[["weapon1","weapon2","weapon3","weapon4"]].stack()
x = x.value_counts()
common_weapons = list(pd.Series(x[:3].index.values, index=x[:3]))
common_weapon1 = common_weapons[0]
common_weapon2 = common_weapons[1]
common_weapon3 = common_weapons[2]

x = df[["drone1","drone2","drone3"]].stack()
x = x.value_counts()
common_drones = list(pd.Series(x[:3].index.values, index=x[:3]))
common_drone1 = common_drones[0]
common_drone2 = common_drones[1]

x = df[["augment1","augment2","augment3"]].stack()
x = x.value_counts()
common_augments = list(pd.Series(x[:3].index.values, index=x[:3]))
common_augment1 = common_augments[0]
common_augment2 = common_augments[1]
common_augment3 = common_augments[2]

x = df["ship"].value_counts()
common_ship = list(pd.Series(x[:1].index.values, index=x[:1]))
common_ship = common_ship[0]

# prepare data for overview report

data = [
    ship, date, result, total_games, win_percentage,
    common_weapon1, common_weapon2, common_weapon3,
    common_drone1, common_drone2, common_augment1,
    common_augment2, common_augment3, common_ship
]
category = [
    "latest round", "latest round", "latest round",
    "player stats", "player stats", "player stats", 
    "player stats", "player stats", "player stats", 
    "player stats", "player stats", "player stats", 
    "player stats", "player stats" 
]
attribute = [
     "ship:", "date:", "result:", "amount of games:",
    "win rate:", "most used weapon:", "second most used weapon:",
    "third most used weapon:", "most used drone:",
    "most used drone:", "most used augment:",
    "second most used augment:", "third most used augment:",
    "most used ship:"
]

overview = pd.DataFrame(
    data,
    index=[category, attribute],
    columns=['stats']
)

# save overview report

FILE = str(pathlib.Path().absolute()) + r"\analysis.xlsx"

with pd.ExcelWriter(FILE, engine = "openpyxl",  mode='a', float_format="%.1f") as writer:
    workBook = writer.book
    try:
        workBook.remove(workBook['overview'])
    except:
        print("worksheet doesn't exist")
    finally:
        overview.to_excel(writer, sheet_name='overview', index = True, header = False)
    writer.save()
    writer.close()

# helper function

def mean(column):
    try:
        return df[column].mean()
    except:
        return float("NaN")

def locmean(result, column):
    try:
        return int(df.loc[df["result"] == result, column].mean())
    except:
        return float("NaN")

# extract data for overview report

# score
score_total = df["score_total"].iloc[-1]
score_med = df["score_med"].iloc[-1]
score_mean = df["score_mean"].iloc[-1]
score_std = df["score_std"].iloc[-1]
score_min = df["score_min"].iloc[-1]
score_max = df["score_max"].iloc[-1]
score_s1 = df["score_s1"].iloc[-1]
score_s2 = df["score_s2"].iloc[-1]
score_s3 = df["score_s3"].iloc[-1]
score_s4 = df["score_s4"].iloc[-1]
score_s5 = df["score_s5"].iloc[-1]
score_s6 = df["score_s6"].iloc[-1]
score_s7 = df["score_s7"].iloc[-1]
score_s8 = df["score_s8"].iloc[-1]
score_s_med = df["score_s_med"].iloc[-1]
score_s_mean = df["score_s_mean"].iloc[-1]
score_s_std = df["score_s_std"].iloc[-1]
score_s_min = df["score_s_min"].iloc[-1]
score_s_max = df["score_s_max"].iloc[-1]
score_observation = [
    score_total, score_med, score_mean, score_std, score_min, score_max, score_s1,
    score_s2, score_s3,score_s4, score_s5, score_s6, score_s7, score_s8,
    score_s_med, score_s_mean, score_s_std, score_s_min, score_s_max,
]

mean_score_total = mean("score_total")
mean_score_med = mean("score_med")
mean_score_mean = mean("score_mean")
mean_score_std = mean("score_std")
mean_score_min = mean("score_min")
mean_score_max = mean("score_max")
mean_score_s1 = mean("score_s1")
mean_score_s2 = mean("score_s2")
mean_score_s3 = mean("score_s3")
mean_score_s4 = mean("score_s4")
mean_score_s5 = mean("score_s5")
mean_score_s6 = mean("score_s6")
mean_score_s7 = mean("score_s7")
mean_score_s8 = mean("score_s8")
mean_score_s_med = mean("score_s_med")
mean_score_s_mean = mean("score_s_mean")
mean_score_s_std = mean("score_s_std")
mean_score_s_min = mean("score_s_min")
mean_score_s_max = mean("score_s_max")
mean_score_observation = [
    mean_score_total, mean_score_med, mean_score_mean, mean_score_std, mean_score_min, 
    mean_score_max, mean_score_s1, mean_score_s2, mean_score_s3, mean_score_s4,
    mean_score_s5, mean_score_s6, mean_score_s7, mean_score_s8, mean_score_s_med,
    mean_score_s_mean, mean_score_s_std, mean_score_s_min, mean_score_s_max,
]

mean_win_score_total = locmean("victory", "score_total")
mean_win_score_med =  locmean("victory", "score_med")
mean_win_score_mean =  locmean("victory", "score_mean")
mean_win_score_std =  locmean("victory", "score_std")
mean_win_score_min =  locmean("victory", "score_min")
mean_win_score_max =  locmean("victory", "score_max")
mean_win_score_s1 =  locmean("victory", "score_s1")
mean_win_score_s2 =  locmean("victory", "score_s2")
mean_win_score_s3 =  locmean("victory", "score_s3")
mean_win_score_s4 =  locmean("victory", "score_s4")
mean_win_score_s5 =  locmean("victory", "score_s5")
mean_win_score_s6 =  locmean("victory", "score_s6")
mean_win_score_s7 =  locmean("victory", "score_s7")
mean_win_score_s8 =  locmean("victory", "score_s8")
mean_win_score_s_med =  locmean("victory", "score_s_med")
mean_win_score_s_mean =  locmean("victory", "score_s_mean")
mean_win_score_s_std =  locmean("victory", "score_s_std")
mean_win_score_s_min =  locmean("victory", "score_s_min")
mean_win_score_s_max =  locmean("victory", "score_s_max")
mean_win_score_observation = [
    mean_win_score_total, mean_win_score_med, mean_win_score_mean, mean_win_score_std, mean_win_score_min, 
    mean_win_score_max, mean_win_score_s1, mean_win_score_s2, mean_win_score_s3, mean_win_score_s4,
    mean_win_score_s5, mean_win_score_s6, mean_win_score_s7, mean_win_score_s8, mean_win_score_s_med,
    mean_win_score_s_mean, mean_win_score_s_std, mean_win_score_s_min, mean_win_score_s_max,
]

mean_loss_score_total = locmean("loss", "score_total")
mean_loss_score_med =  locmean("loss", "score_med")
mean_loss_score_mean =  locmean("loss", "score_mean")
mean_loss_score_std =  locmean("loss", "score_std")
mean_loss_score_min =  locmean("loss", "score_min")
mean_loss_score_max =  locmean("loss", "score_max")
mean_loss_score_s1 =  locmean("loss", "score_s1")
mean_loss_score_s2 =  locmean("loss", "score_s2")
mean_loss_score_s3 =  locmean("loss", "score_s3")
mean_loss_score_s4 =  locmean("loss", "score_s4")
mean_loss_score_s5 =  locmean("loss", "score_s5")
mean_loss_score_s6 =  locmean("loss", "score_s6")
mean_loss_score_s7 =  locmean("loss", "score_s7")
mean_loss_score_s8 =  locmean("loss", "score_s8")
mean_loss_score_s_med =  locmean("loss", "score_s_med")
mean_loss_score_s_mean =  locmean("loss", "score_s_mean")
mean_loss_score_s_std =  locmean("loss", "score_s_std")
mean_loss_score_s_min =  locmean("loss", "score_s_min")
mean_loss_score_s_max =  locmean("loss", "score_s_max")
mean_loss_score_observation = [
    mean_loss_score_total, mean_loss_score_med, mean_loss_score_mean, mean_loss_score_std, mean_loss_score_min, 
    mean_loss_score_max, mean_loss_score_s1, mean_loss_score_s2, mean_loss_score_s3, mean_loss_score_s4,
    mean_loss_score_s5, mean_loss_score_s6, mean_loss_score_s7, mean_loss_score_s8, mean_loss_score_s_med,
    mean_loss_score_s_mean, mean_loss_score_s_std, mean_loss_score_s_min, mean_loss_score_s_max,
]

# scrap_earned
scrap_earned_total = df["scrap_earned_total"].iloc[-1]
scrap_earned_med = df["scrap_earned_med"].iloc[-1]
scrap_earned_mean = df["scrap_earned_mean"].iloc[-1]
scrap_earned_std = df["scrap_earned_std"].iloc[-1]
scrap_earned_min = df["scrap_earned_min"].iloc[-1]
scrap_earned_max = df["scrap_earned_max"].iloc[-1]
scrap_earned_s1 = df["scrap_earned_s1"].iloc[-1]
scrap_earned_s2 = df["scrap_earned_s2"].iloc[-1]
scrap_earned_s3 = df["scrap_earned_s3"].iloc[-1]
scrap_earned_s4 = df["scrap_earned_s4"].iloc[-1]
scrap_earned_s5 = df["scrap_earned_s5"].iloc[-1]
scrap_earned_s6 = df["scrap_earned_s6"].iloc[-1]
scrap_earned_s7 = df["scrap_earned_s7"].iloc[-1]
scrap_earned_s8 = df["scrap_earned_s8"].iloc[-1]
scrap_earned_s_med = df["scrap_earned_s_med"].iloc[-1]
scrap_earned_s_mean = df["scrap_earned_s_mean"].iloc[-1]
scrap_earned_s_std = df["scrap_earned_s_std"].iloc[-1]
scrap_earned_s_min = df["scrap_earned_s_min"].iloc[-1]
scrap_earned_s_max = df["scrap_earned_s_max"].iloc[-1]
scrap_earned_observation = [
    scrap_earned_total, scrap_earned_med, scrap_earned_mean, scrap_earned_std, scrap_earned_min, scrap_earned_max, scrap_earned_s1,
    scrap_earned_s2, scrap_earned_s3,scrap_earned_s4, scrap_earned_s5, scrap_earned_s6, scrap_earned_s7, scrap_earned_s8,
    scrap_earned_s_med, scrap_earned_s_mean, scrap_earned_s_std, scrap_earned_s_min, scrap_earned_s_max,
]

mean_scrap_earned_total = mean("scrap_earned_total")
mean_scrap_earned_med = mean("scrap_earned_med")
mean_scrap_earned_mean = mean("scrap_earned_mean")
mean_scrap_earned_std = mean("scrap_earned_std")
mean_scrap_earned_min = mean("scrap_earned_min")
mean_scrap_earned_max = mean("scrap_earned_max")
mean_scrap_earned_s1 = mean("scrap_earned_s1")
mean_scrap_earned_s2 = mean("scrap_earned_s2")
mean_scrap_earned_s3 = mean("scrap_earned_s3")
mean_scrap_earned_s4 = mean("scrap_earned_s4")
mean_scrap_earned_s5 = mean("scrap_earned_s5")
mean_scrap_earned_s6 = mean("scrap_earned_s6")
mean_scrap_earned_s7 = mean("scrap_earned_s7")
mean_scrap_earned_s8 = mean("scrap_earned_s8")
mean_scrap_earned_s_med = mean("scrap_earned_s_med")
mean_scrap_earned_s_mean = mean("scrap_earned_s_mean")
mean_scrap_earned_s_std = mean("scrap_earned_s_std")
mean_scrap_earned_s_min = mean("scrap_earned_s_min")
mean_scrap_earned_s_max = mean("scrap_earned_s_max")
mean_scrap_earned_observation = [
    mean_scrap_earned_total, mean_scrap_earned_med, mean_scrap_earned_mean, mean_scrap_earned_std, mean_scrap_earned_min, 
    mean_scrap_earned_max, mean_scrap_earned_s1, mean_scrap_earned_s2, mean_scrap_earned_s3, mean_scrap_earned_s4,
    mean_scrap_earned_s5, mean_scrap_earned_s6, mean_scrap_earned_s7, mean_scrap_earned_s8, mean_scrap_earned_s_med,
    mean_scrap_earned_s_mean, mean_scrap_earned_s_std, mean_scrap_earned_s_min, mean_scrap_earned_s_max,
]

mean_win_scrap_earned_total = locmean("victory", "scrap_earned_total")
mean_win_scrap_earned_med =  locmean("victory", "scrap_earned_med")
mean_win_scrap_earned_mean =  locmean("victory", "scrap_earned_mean")
mean_win_scrap_earned_std =  locmean("victory", "scrap_earned_std")
mean_win_scrap_earned_min =  locmean("victory", "scrap_earned_min")
mean_win_scrap_earned_max =  locmean("victory", "scrap_earned_max")
mean_win_scrap_earned_s1 =  locmean("victory", "scrap_earned_s1")
mean_win_scrap_earned_s2 =  locmean("victory", "scrap_earned_s2")
mean_win_scrap_earned_s3 =  locmean("victory", "scrap_earned_s3")
mean_win_scrap_earned_s4 =  locmean("victory", "scrap_earned_s4")
mean_win_scrap_earned_s5 =  locmean("victory", "scrap_earned_s5")
mean_win_scrap_earned_s6 =  locmean("victory", "scrap_earned_s6")
mean_win_scrap_earned_s7 =  locmean("victory", "scrap_earned_s7")
mean_win_scrap_earned_s8 =  locmean("victory", "scrap_earned_s8")
mean_win_scrap_earned_s_med =  locmean("victory", "scrap_earned_s_med")
mean_win_scrap_earned_s_mean =  locmean("victory", "scrap_earned_s_mean")
mean_win_scrap_earned_s_std =  locmean("victory", "scrap_earned_s_std")
mean_win_scrap_earned_s_min =  locmean("victory", "scrap_earned_s_min")
mean_win_scrap_earned_s_max =  locmean("victory", "scrap_earned_s_max")
mean_win_scrap_earned_observation = [
    mean_win_scrap_earned_total, mean_win_scrap_earned_med, mean_win_scrap_earned_mean, mean_win_scrap_earned_std, mean_win_scrap_earned_min, 
    mean_win_scrap_earned_max, mean_win_scrap_earned_s1, mean_win_scrap_earned_s2, mean_win_scrap_earned_s3, mean_win_scrap_earned_s4,
    mean_win_scrap_earned_s5, mean_win_scrap_earned_s6, mean_win_scrap_earned_s7, mean_win_scrap_earned_s8, mean_win_scrap_earned_s_med,
    mean_win_scrap_earned_s_mean, mean_win_scrap_earned_s_std, mean_win_scrap_earned_s_min, mean_win_scrap_earned_s_max,
]

mean_loss_scrap_earned_total = locmean("loss", "scrap_earned_total")
mean_loss_scrap_earned_med =  locmean("loss", "scrap_earned_med")
mean_loss_scrap_earned_mean =  locmean("loss", "scrap_earned_mean")
mean_loss_scrap_earned_std =  locmean("loss", "scrap_earned_std")
mean_loss_scrap_earned_min =  locmean("loss", "scrap_earned_min")
mean_loss_scrap_earned_max =  locmean("loss", "scrap_earned_max")
mean_loss_scrap_earned_s1 =  locmean("loss", "scrap_earned_s1")
mean_loss_scrap_earned_s2 =  locmean("loss", "scrap_earned_s2")
mean_loss_scrap_earned_s3 =  locmean("loss", "scrap_earned_s3")
mean_loss_scrap_earned_s4 =  locmean("loss", "scrap_earned_s4")
mean_loss_scrap_earned_s5 =  locmean("loss", "scrap_earned_s5")
mean_loss_scrap_earned_s6 =  locmean("loss", "scrap_earned_s6")
mean_loss_scrap_earned_s7 =  locmean("loss", "scrap_earned_s7")
mean_loss_scrap_earned_s8 =  locmean("loss", "scrap_earned_s8")
mean_loss_scrap_earned_s_med =  locmean("loss", "scrap_earned_s_med")
mean_loss_scrap_earned_s_mean =  locmean("loss", "scrap_earned_s_mean")
mean_loss_scrap_earned_s_std =  locmean("loss", "scrap_earned_s_std")
mean_loss_scrap_earned_s_min =  locmean("loss", "scrap_earned_s_min")
mean_loss_scrap_earned_s_max =  locmean("loss", "scrap_earned_s_max")
mean_loss_scrap_earned_observation = [
    mean_loss_scrap_earned_total, mean_loss_scrap_earned_med, mean_loss_scrap_earned_mean, mean_loss_scrap_earned_std, mean_loss_scrap_earned_min, 
    mean_loss_scrap_earned_max, mean_loss_scrap_earned_s1, mean_loss_scrap_earned_s2, mean_loss_scrap_earned_s3, mean_loss_scrap_earned_s4,
    mean_loss_scrap_earned_s5, mean_loss_scrap_earned_s6, mean_loss_scrap_earned_s7, mean_loss_scrap_earned_s8, mean_loss_scrap_earned_s_med,
    mean_loss_scrap_earned_s_mean, mean_loss_scrap_earned_s_std, mean_loss_scrap_earned_s_min, mean_loss_scrap_earned_s_max,
]

# scrap_held
scrap_held_total = df["scrap_held_total"].iloc[-1]
scrap_held_med = df["scrap_held_med"].iloc[-1]
scrap_held_mean = df["scrap_held_mean"].iloc[-1]
scrap_held_std = df["scrap_held_std"].iloc[-1]
scrap_held_min = df["scrap_held_min"].iloc[-1]
scrap_held_max = df["scrap_held_max"].iloc[-1]
scrap_held_s1 = df["scrap_held_s1"].iloc[-1]
scrap_held_s2 = df["scrap_held_s2"].iloc[-1]
scrap_held_s3 = df["scrap_held_s3"].iloc[-1]
scrap_held_s4 = df["scrap_held_s4"].iloc[-1]
scrap_held_s5 = df["scrap_held_s5"].iloc[-1]
scrap_held_s6 = df["scrap_held_s6"].iloc[-1]
scrap_held_s7 = df["scrap_held_s7"].iloc[-1]
scrap_held_s8 = df["scrap_held_s8"].iloc[-1]
scrap_held_s_med = df["scrap_held_s_med"].iloc[-1]
scrap_held_s_mean = df["scrap_held_s_mean"].iloc[-1]
scrap_held_s_std = df["scrap_held_s_std"].iloc[-1]
scrap_held_s_min = df["scrap_held_s_min"].iloc[-1]
scrap_held_s_max = df["scrap_held_s_max"].iloc[-1]
scrap_held_observation = [
    scrap_held_total, scrap_held_med, scrap_held_mean, scrap_held_std, scrap_held_min, scrap_held_max, scrap_held_s1,
    scrap_held_s2, scrap_held_s3,scrap_held_s4, scrap_held_s5, scrap_held_s6, scrap_held_s7, scrap_held_s8,
    scrap_held_s_med, scrap_held_s_mean, scrap_held_s_std, scrap_held_s_min, scrap_held_s_max,
]

mean_scrap_held_total = mean("scrap_held_total")
mean_scrap_held_med = mean("scrap_held_med")
mean_scrap_held_mean = mean("scrap_held_mean")
mean_scrap_held_std = mean("scrap_held_std")
mean_scrap_held_min = mean("scrap_held_min")
mean_scrap_held_max = mean("scrap_held_max")
mean_scrap_held_s1 = mean("scrap_held_s1")
mean_scrap_held_s2 = mean("scrap_held_s2")
mean_scrap_held_s3 = mean("scrap_held_s3")
mean_scrap_held_s4 = mean("scrap_held_s4")
mean_scrap_held_s5 = mean("scrap_held_s5")
mean_scrap_held_s6 = mean("scrap_held_s6")
mean_scrap_held_s7 = mean("scrap_held_s7")
mean_scrap_held_s8 = mean("scrap_held_s8")
mean_scrap_held_s_med = mean("scrap_held_s_med")
mean_scrap_held_s_mean = mean("scrap_held_s_mean")
mean_scrap_held_s_std = mean("scrap_held_s_std")
mean_scrap_held_s_min = mean("scrap_held_s_min")
mean_scrap_held_s_max = mean("scrap_held_s_max")
mean_scrap_held_observation = [
    mean_scrap_held_total, mean_scrap_held_med, mean_scrap_held_mean, mean_scrap_held_std, mean_scrap_held_min, 
    mean_scrap_held_max, mean_scrap_held_s1, mean_scrap_held_s2, mean_scrap_held_s3, mean_scrap_held_s4,
    mean_scrap_held_s5, mean_scrap_held_s6, mean_scrap_held_s7, mean_scrap_held_s8, mean_scrap_held_s_med,
    mean_scrap_held_s_mean, mean_scrap_held_s_std, mean_scrap_held_s_min, mean_scrap_held_s_max,
]

mean_win_scrap_held_total = locmean("victory", "scrap_held_total")
mean_win_scrap_held_med =  locmean("victory", "scrap_held_med")
mean_win_scrap_held_mean =  locmean("victory", "scrap_held_mean")
mean_win_scrap_held_std =  locmean("victory", "scrap_held_std")
mean_win_scrap_held_min =  locmean("victory", "scrap_held_min")
mean_win_scrap_held_max =  locmean("victory", "scrap_held_max")
mean_win_scrap_held_s1 =  locmean("victory", "scrap_held_s1")
mean_win_scrap_held_s2 =  locmean("victory", "scrap_held_s2")
mean_win_scrap_held_s3 =  locmean("victory", "scrap_held_s3")
mean_win_scrap_held_s4 =  locmean("victory", "scrap_held_s4")
mean_win_scrap_held_s5 =  locmean("victory", "scrap_held_s5")
mean_win_scrap_held_s6 =  locmean("victory", "scrap_held_s6")
mean_win_scrap_held_s7 =  locmean("victory", "scrap_held_s7")
mean_win_scrap_held_s8 =  locmean("victory", "scrap_held_s8")
mean_win_scrap_held_s_med =  locmean("victory", "scrap_held_s_med")
mean_win_scrap_held_s_mean =  locmean("victory", "scrap_held_s_mean")
mean_win_scrap_held_s_std =  locmean("victory", "scrap_held_s_std")
mean_win_scrap_held_s_min =  locmean("victory", "scrap_held_s_min")
mean_win_scrap_held_s_max =  locmean("victory", "scrap_held_s_max")
mean_win_scrap_held_observation = [
    mean_win_scrap_held_total, mean_win_scrap_held_med, mean_win_scrap_held_mean, mean_win_scrap_held_std, mean_win_scrap_held_min, 
    mean_win_scrap_held_max, mean_win_scrap_held_s1, mean_win_scrap_held_s2, mean_win_scrap_held_s3, mean_win_scrap_held_s4,
    mean_win_scrap_held_s5, mean_win_scrap_held_s6, mean_win_scrap_held_s7, mean_win_scrap_held_s8, mean_win_scrap_held_s_med,
    mean_win_scrap_held_s_mean, mean_win_scrap_held_s_std, mean_win_scrap_held_s_min, mean_win_scrap_held_s_max,
]

mean_loss_scrap_held_total = locmean("loss", "scrap_held_total")
mean_loss_scrap_held_med =  locmean("loss", "scrap_held_med")
mean_loss_scrap_held_mean =  locmean("loss", "scrap_held_mean")
mean_loss_scrap_held_std =  locmean("loss", "scrap_held_std")
mean_loss_scrap_held_min =  locmean("loss", "scrap_held_min")
mean_loss_scrap_held_max =  locmean("loss", "scrap_held_max")
mean_loss_scrap_held_s1 =  locmean("loss", "scrap_held_s1")
mean_loss_scrap_held_s2 =  locmean("loss", "scrap_held_s2")
mean_loss_scrap_held_s3 =  locmean("loss", "scrap_held_s3")
mean_loss_scrap_held_s4 =  locmean("loss", "scrap_held_s4")
mean_loss_scrap_held_s5 =  locmean("loss", "scrap_held_s5")
mean_loss_scrap_held_s6 =  locmean("loss", "scrap_held_s6")
mean_loss_scrap_held_s7 =  locmean("loss", "scrap_held_s7")
mean_loss_scrap_held_s8 =  locmean("loss", "scrap_held_s8")
mean_loss_scrap_held_s_med =  locmean("loss", "scrap_held_s_med")
mean_loss_scrap_held_s_mean =  locmean("loss", "scrap_held_s_mean")
mean_loss_scrap_held_s_std =  locmean("loss", "scrap_held_s_std")
mean_loss_scrap_held_s_min =  locmean("loss", "scrap_held_s_min")
mean_loss_scrap_held_s_max =  locmean("loss", "scrap_held_s_max")
mean_loss_scrap_held_observation = [
    mean_loss_scrap_held_total, mean_loss_scrap_held_med, mean_loss_scrap_held_mean, mean_loss_scrap_held_std, mean_loss_scrap_held_min, 
    mean_loss_scrap_held_max, mean_loss_scrap_held_s1, mean_loss_scrap_held_s2, mean_loss_scrap_held_s3, mean_loss_scrap_held_s4,
    mean_loss_scrap_held_s5, mean_loss_scrap_held_s6, mean_loss_scrap_held_s7, mean_loss_scrap_held_s8, mean_loss_scrap_held_s_med,
    mean_loss_scrap_held_s_mean, mean_loss_scrap_held_s_std, mean_loss_scrap_held_s_min, mean_loss_scrap_held_s_max,
]


# beacons
beacons_total = df["beacons_total"].iloc[-1]
beacons_med = df["beacons_med"].iloc[-1]
beacons_mean = df["beacons_mean"].iloc[-1]
beacons_std = df["beacons_std"].iloc[-1]
beacons_min = df["beacons_min"].iloc[-1]
beacons_max = df["beacons_max"].iloc[-1]
beacons_s1 = df["beacons_s1"].iloc[-1]
beacons_s2 = df["beacons_s2"].iloc[-1]
beacons_s3 = df["beacons_s3"].iloc[-1]
beacons_s4 = df["beacons_s4"].iloc[-1]
beacons_s5 = df["beacons_s5"].iloc[-1]
beacons_s6 = df["beacons_s6"].iloc[-1]
beacons_s7 = df["beacons_s7"].iloc[-1]
beacons_s8 = df["beacons_s8"].iloc[-1]
beacons_s_med = df["beacons_s_med"].iloc[-1]
beacons_s_mean = df["beacons_s_mean"].iloc[-1]
beacons_s_std = df["beacons_s_std"].iloc[-1]
beacons_s_min = df["beacons_s_min"].iloc[-1]
beacons_s_max = df["beacons_s_max"].iloc[-1]
beacons_observation = [
    beacons_total, beacons_med, beacons_mean, beacons_std, beacons_min, beacons_max, beacons_s1,
    beacons_s2, beacons_s3,beacons_s4, beacons_s5, beacons_s6, beacons_s7, beacons_s8,
    beacons_s_med, beacons_s_mean, beacons_s_std, beacons_s_min, beacons_s_max,
]

mean_beacons_total = mean("beacons_total")
mean_beacons_med = mean("beacons_med")
mean_beacons_mean = mean("beacons_mean")
mean_beacons_std = mean("beacons_std")
mean_beacons_min = mean("beacons_min")
mean_beacons_max = mean("beacons_max")
mean_beacons_s1 = mean("beacons_s1")
mean_beacons_s2 = mean("beacons_s2")
mean_beacons_s3 = mean("beacons_s3")
mean_beacons_s4 = mean("beacons_s4")
mean_beacons_s5 = mean("beacons_s5")
mean_beacons_s6 = mean("beacons_s6")
mean_beacons_s7 = mean("beacons_s7")
mean_beacons_s8 = mean("beacons_s8")
mean_beacons_s_med = mean("beacons_s_med")
mean_beacons_s_mean = mean("beacons_s_mean")
mean_beacons_s_std = mean("beacons_s_std")
mean_beacons_s_min = mean("beacons_s_min")
mean_beacons_s_max = mean("beacons_s_max")
mean_beacons_observation = [
    mean_beacons_total, mean_beacons_med, mean_beacons_mean, mean_beacons_std, mean_beacons_min, 
    mean_beacons_max, mean_beacons_s1, mean_beacons_s2, mean_beacons_s3, mean_beacons_s4,
    mean_beacons_s5, mean_beacons_s6, mean_beacons_s7, mean_beacons_s8, mean_beacons_s_med,
    mean_beacons_s_mean, mean_beacons_s_std, mean_beacons_s_min, mean_beacons_s_max,
]

mean_win_beacons_total = locmean("victory", "beacons_total")
mean_win_beacons_med =  locmean("victory", "beacons_med")
mean_win_beacons_mean =  locmean("victory", "beacons_mean")
mean_win_beacons_std =  locmean("victory", "beacons_std")
mean_win_beacons_min =  locmean("victory", "beacons_min")
mean_win_beacons_max =  locmean("victory", "beacons_max")
mean_win_beacons_s1 =  locmean("victory", "beacons_s1")
mean_win_beacons_s2 =  locmean("victory", "beacons_s2")
mean_win_beacons_s3 =  locmean("victory", "beacons_s3")
mean_win_beacons_s4 =  locmean("victory", "beacons_s4")
mean_win_beacons_s5 =  locmean("victory", "beacons_s5")
mean_win_beacons_s6 =  locmean("victory", "beacons_s6")
mean_win_beacons_s7 =  locmean("victory", "beacons_s7")
mean_win_beacons_s8 =  locmean("victory", "beacons_s8")
mean_win_beacons_s_med =  locmean("victory", "beacons_s_med")
mean_win_beacons_s_mean =  locmean("victory", "beacons_s_mean")
mean_win_beacons_s_std =  locmean("victory", "beacons_s_std")
mean_win_beacons_s_min =  locmean("victory", "beacons_s_min")
mean_win_beacons_s_max =  locmean("victory", "beacons_s_max")
mean_win_beacons_observation = [
    mean_win_beacons_total, mean_win_beacons_med, mean_win_beacons_mean, mean_win_beacons_std, mean_win_beacons_min, 
    mean_win_beacons_max, mean_win_beacons_s1, mean_win_beacons_s2, mean_win_beacons_s3, mean_win_beacons_s4,
    mean_win_beacons_s5, mean_win_beacons_s6, mean_win_beacons_s7, mean_win_beacons_s8, mean_win_beacons_s_med,
    mean_win_beacons_s_mean, mean_win_beacons_s_std, mean_win_beacons_s_min, mean_win_beacons_s_max,
]

mean_loss_beacons_total = locmean("loss", "beacons_total")
mean_loss_beacons_med =  locmean("loss", "beacons_med")
mean_loss_beacons_mean =  locmean("loss", "beacons_mean")
mean_loss_beacons_std =  locmean("loss", "beacons_std")
mean_loss_beacons_min =  locmean("loss", "beacons_min")
mean_loss_beacons_max =  locmean("loss", "beacons_max")
mean_loss_beacons_s1 =  locmean("loss", "beacons_s1")
mean_loss_beacons_s2 =  locmean("loss", "beacons_s2")
mean_loss_beacons_s3 =  locmean("loss", "beacons_s3")
mean_loss_beacons_s4 =  locmean("loss", "beacons_s4")
mean_loss_beacons_s5 =  locmean("loss", "beacons_s5")
mean_loss_beacons_s6 =  locmean("loss", "beacons_s6")
mean_loss_beacons_s7 =  locmean("loss", "beacons_s7")
mean_loss_beacons_s8 =  locmean("loss", "beacons_s8")
mean_loss_beacons_s_med =  locmean("loss", "beacons_s_med")
mean_loss_beacons_s_mean =  locmean("loss", "beacons_s_mean")
mean_loss_beacons_s_std =  locmean("loss", "beacons_s_std")
mean_loss_beacons_s_min =  locmean("loss", "beacons_s_min")
mean_loss_beacons_s_max =  locmean("loss", "beacons_s_max")
mean_loss_beacons_observation = [
    mean_loss_beacons_total, mean_loss_beacons_med, mean_loss_beacons_mean, mean_loss_beacons_std, mean_loss_beacons_min, 
    mean_loss_beacons_max, mean_loss_beacons_s1, mean_loss_beacons_s2, mean_loss_beacons_s3, mean_loss_beacons_s4,
    mean_loss_beacons_s5, mean_loss_beacons_s6, mean_loss_beacons_s7, mean_loss_beacons_s8, mean_loss_beacons_s_med,
    mean_loss_beacons_s_mean, mean_loss_beacons_s_std, mean_loss_beacons_s_min, mean_loss_beacons_s_max,
]

# ships_defeated
ships_defeated_total = df["ships_defeated_total"].iloc[-1]
ships_defeated_med = df["ships_defeated_med"].iloc[-1]
ships_defeated_mean = df["ships_defeated_mean"].iloc[-1]
ships_defeated_std = df["ships_defeated_std"].iloc[-1]
ships_defeated_min = df["ships_defeated_min"].iloc[-1]
ships_defeated_max = df["ships_defeated_max"].iloc[-1]
ships_defeated_s1 = df["ships_defeated_s1"].iloc[-1]
ships_defeated_s2 = df["ships_defeated_s2"].iloc[-1]
ships_defeated_s3 = df["ships_defeated_s3"].iloc[-1]
ships_defeated_s4 = df["ships_defeated_s4"].iloc[-1]
ships_defeated_s5 = df["ships_defeated_s5"].iloc[-1]
ships_defeated_s6 = df["ships_defeated_s6"].iloc[-1]
ships_defeated_s7 = df["ships_defeated_s7"].iloc[-1]
ships_defeated_s8 = df["ships_defeated_s8"].iloc[-1]
ships_defeated_s_med = df["ships_defeated_s_med"].iloc[-1]
ships_defeated_s_mean = df["ships_defeated_s_mean"].iloc[-1]
ships_defeated_s_std = df["ships_defeated_s_std"].iloc[-1]
ships_defeated_s_min = df["ships_defeated_s_min"].iloc[-1]
ships_defeated_s_max = df["ships_defeated_s_max"].iloc[-1]
ships_defeated_observation = [
    ships_defeated_total, ships_defeated_med, ships_defeated_mean, ships_defeated_std, ships_defeated_min, ships_defeated_max, ships_defeated_s1,
    ships_defeated_s2, ships_defeated_s3,ships_defeated_s4, ships_defeated_s5, ships_defeated_s6, ships_defeated_s7, ships_defeated_s8,
    ships_defeated_s_med, ships_defeated_s_mean, ships_defeated_s_std, ships_defeated_s_min, ships_defeated_s_max,
]

mean_ships_defeated_total = mean("ships_defeated_total")
mean_ships_defeated_med = mean("ships_defeated_med")
mean_ships_defeated_mean = mean("ships_defeated_mean")
mean_ships_defeated_std = mean("ships_defeated_std")
mean_ships_defeated_min = mean("ships_defeated_min")
mean_ships_defeated_max = mean("ships_defeated_max")
mean_ships_defeated_s1 = mean("ships_defeated_s1")
mean_ships_defeated_s2 = mean("ships_defeated_s2")
mean_ships_defeated_s3 = mean("ships_defeated_s3")
mean_ships_defeated_s4 = mean("ships_defeated_s4")
mean_ships_defeated_s5 = mean("ships_defeated_s5")
mean_ships_defeated_s6 = mean("ships_defeated_s6")
mean_ships_defeated_s7 = mean("ships_defeated_s7")
mean_ships_defeated_s8 = mean("ships_defeated_s8")
mean_ships_defeated_s_med = mean("ships_defeated_s_med")
mean_ships_defeated_s_mean = mean("ships_defeated_s_mean")
mean_ships_defeated_s_std = mean("ships_defeated_s_std")
mean_ships_defeated_s_min = mean("ships_defeated_s_min")
mean_ships_defeated_s_max = mean("ships_defeated_s_max")
mean_ships_defeated_observation = [
    mean_ships_defeated_total, mean_ships_defeated_med, mean_ships_defeated_mean, mean_ships_defeated_std, mean_ships_defeated_min, 
    mean_ships_defeated_max, mean_ships_defeated_s1, mean_ships_defeated_s2, mean_ships_defeated_s3, mean_ships_defeated_s4,
    mean_ships_defeated_s5, mean_ships_defeated_s6, mean_ships_defeated_s7, mean_ships_defeated_s8, mean_ships_defeated_s_med,
    mean_ships_defeated_s_mean, mean_ships_defeated_s_std, mean_ships_defeated_s_min, mean_ships_defeated_s_max,
]

mean_win_ships_defeated_total = locmean("victory", "ships_defeated_total")
mean_win_ships_defeated_med =  locmean("victory", "ships_defeated_med")
mean_win_ships_defeated_mean =  locmean("victory", "ships_defeated_mean")
mean_win_ships_defeated_std =  locmean("victory", "ships_defeated_std")
mean_win_ships_defeated_min =  locmean("victory", "ships_defeated_min")
mean_win_ships_defeated_max =  locmean("victory", "ships_defeated_max")
mean_win_ships_defeated_s1 =  locmean("victory", "ships_defeated_s1")
mean_win_ships_defeated_s2 =  locmean("victory", "ships_defeated_s2")
mean_win_ships_defeated_s3 =  locmean("victory", "ships_defeated_s3")
mean_win_ships_defeated_s4 =  locmean("victory", "ships_defeated_s4")
mean_win_ships_defeated_s5 =  locmean("victory", "ships_defeated_s5")
mean_win_ships_defeated_s6 =  locmean("victory", "ships_defeated_s6")
mean_win_ships_defeated_s7 =  locmean("victory", "ships_defeated_s7")
mean_win_ships_defeated_s8 =  locmean("victory", "ships_defeated_s8")
mean_win_ships_defeated_s_med =  locmean("victory", "ships_defeated_s_med")
mean_win_ships_defeated_s_mean =  locmean("victory", "ships_defeated_s_mean")
mean_win_ships_defeated_s_std =  locmean("victory", "ships_defeated_s_std")
mean_win_ships_defeated_s_min =  locmean("victory", "ships_defeated_s_min")
mean_win_ships_defeated_s_max =  locmean("victory", "ships_defeated_s_max")
mean_win_ships_defeated_observation = [
    mean_win_ships_defeated_total, mean_win_ships_defeated_med, mean_win_ships_defeated_mean, mean_win_ships_defeated_std, mean_win_ships_defeated_min, 
    mean_win_ships_defeated_max, mean_win_ships_defeated_s1, mean_win_ships_defeated_s2, mean_win_ships_defeated_s3, mean_win_ships_defeated_s4,
    mean_win_ships_defeated_s5, mean_win_ships_defeated_s6, mean_win_ships_defeated_s7, mean_win_ships_defeated_s8, mean_win_ships_defeated_s_med,
    mean_win_ships_defeated_s_mean, mean_win_ships_defeated_s_std, mean_win_ships_defeated_s_min, mean_win_ships_defeated_s_max,
]

mean_loss_ships_defeated_total = locmean("loss", "ships_defeated_total")
mean_loss_ships_defeated_med =  locmean("loss", "ships_defeated_med")
mean_loss_ships_defeated_mean =  locmean("loss", "ships_defeated_mean")
mean_loss_ships_defeated_std =  locmean("loss", "ships_defeated_std")
mean_loss_ships_defeated_min =  locmean("loss", "ships_defeated_min")
mean_loss_ships_defeated_max =  locmean("loss", "ships_defeated_max")
mean_loss_ships_defeated_s1 =  locmean("loss", "ships_defeated_s1")
mean_loss_ships_defeated_s2 =  locmean("loss", "ships_defeated_s2")
mean_loss_ships_defeated_s3 =  locmean("loss", "ships_defeated_s3")
mean_loss_ships_defeated_s4 =  locmean("loss", "ships_defeated_s4")
mean_loss_ships_defeated_s5 =  locmean("loss", "ships_defeated_s5")
mean_loss_ships_defeated_s6 =  locmean("loss", "ships_defeated_s6")
mean_loss_ships_defeated_s7 =  locmean("loss", "ships_defeated_s7")
mean_loss_ships_defeated_s8 =  locmean("loss", "ships_defeated_s8")
mean_loss_ships_defeated_s_med =  locmean("loss", "ships_defeated_s_med")
mean_loss_ships_defeated_s_mean =  locmean("loss", "ships_defeated_s_mean")
mean_loss_ships_defeated_s_std =  locmean("loss", "ships_defeated_s_std")
mean_loss_ships_defeated_s_min =  locmean("loss", "ships_defeated_s_min")
mean_loss_ships_defeated_s_max =  locmean("loss", "ships_defeated_s_max")
mean_loss_ships_defeated_observation = [
    mean_loss_ships_defeated_total, mean_loss_ships_defeated_med, mean_loss_ships_defeated_mean, mean_loss_ships_defeated_std, mean_loss_ships_defeated_min, 
    mean_loss_ships_defeated_max, mean_loss_ships_defeated_s1, mean_loss_ships_defeated_s2, mean_loss_ships_defeated_s3, mean_loss_ships_defeated_s4,
    mean_loss_ships_defeated_s5, mean_loss_ships_defeated_s6, mean_loss_ships_defeated_s7, mean_loss_ships_defeated_s8, mean_loss_ships_defeated_s_med,
    mean_loss_ships_defeated_s_mean, mean_loss_ships_defeated_s_std, mean_loss_ships_defeated_s_min, mean_loss_ships_defeated_s_max,
]

# hull
hull_total = df["hull_total"].iloc[-1]
hull_med = df["hull_med"].iloc[-1]
hull_mean = df["hull_mean"].iloc[-1]
hull_std = df["hull_std"].iloc[-1]
hull_min = df["hull_min"].iloc[-1]
hull_max = df["hull_max"].iloc[-1]
hull_s1 = df["hull_s1"].iloc[-1]
hull_s2 = df["hull_s2"].iloc[-1]
hull_s3 = df["hull_s3"].iloc[-1]
hull_s4 = df["hull_s4"].iloc[-1]
hull_s5 = df["hull_s5"].iloc[-1]
hull_s6 = df["hull_s6"].iloc[-1]
hull_s7 = df["hull_s7"].iloc[-1]
hull_s8 = df["hull_s8"].iloc[-1]
hull_s_med = df["hull_s_med"].iloc[-1]
hull_s_mean = df["hull_s_mean"].iloc[-1]
hull_s_std = df["hull_s_std"].iloc[-1]
hull_s_min = df["hull_s_min"].iloc[-1]
hull_s_max = df["hull_s_max"].iloc[-1]
hull_observation = [
    hull_total, hull_med, hull_mean, hull_std, hull_min, hull_max, hull_s1,
    hull_s2, hull_s3,hull_s4, hull_s5, hull_s6, hull_s7, hull_s8,
    hull_s_med, hull_s_mean, hull_s_std, hull_s_min, hull_s_max,
]

mean_hull_total = mean("hull_total")
mean_hull_med = mean("hull_med")
mean_hull_mean = mean("hull_mean")
mean_hull_std = mean("hull_std")
mean_hull_min = mean("hull_min")
mean_hull_max = mean("hull_max")
mean_hull_s1 = mean("hull_s1")
mean_hull_s2 = mean("hull_s2")
mean_hull_s3 = mean("hull_s3")
mean_hull_s4 = mean("hull_s4")
mean_hull_s5 = mean("hull_s5")
mean_hull_s6 = mean("hull_s6")
mean_hull_s7 = mean("hull_s7")
mean_hull_s8 = mean("hull_s8")
mean_hull_s_med = mean("hull_s_med")
mean_hull_s_mean = mean("hull_s_mean")
mean_hull_s_std = mean("hull_s_std")
mean_hull_s_min = mean("hull_s_min")
mean_hull_s_max = mean("hull_s_max")
mean_hull_observation = [
    mean_hull_total, mean_hull_med, mean_hull_mean, mean_hull_std, mean_hull_min, 
    mean_hull_max, mean_hull_s1, mean_hull_s2, mean_hull_s3, mean_hull_s4,
    mean_hull_s5, mean_hull_s6, mean_hull_s7, mean_hull_s8, mean_hull_s_med,
    mean_hull_s_mean, mean_hull_s_std, mean_hull_s_min, mean_hull_s_max,
]

mean_win_hull_total = locmean("victory", "hull_total")
mean_win_hull_med =  locmean("victory", "hull_med")
mean_win_hull_mean =  locmean("victory", "hull_mean")
mean_win_hull_std =  locmean("victory", "hull_std")
mean_win_hull_min =  locmean("victory", "hull_min")
mean_win_hull_max =  locmean("victory", "hull_max")
mean_win_hull_s1 =  locmean("victory", "hull_s1")
mean_win_hull_s2 =  locmean("victory", "hull_s2")
mean_win_hull_s3 =  locmean("victory", "hull_s3")
mean_win_hull_s4 =  locmean("victory", "hull_s4")
mean_win_hull_s5 =  locmean("victory", "hull_s5")
mean_win_hull_s6 =  locmean("victory", "hull_s6")
mean_win_hull_s7 =  locmean("victory", "hull_s7")
mean_win_hull_s8 =  locmean("victory", "hull_s8")
mean_win_hull_s_med =  locmean("victory", "hull_s_med")
mean_win_hull_s_mean =  locmean("victory", "hull_s_mean")
mean_win_hull_s_std =  locmean("victory", "hull_s_std")
mean_win_hull_s_min =  locmean("victory", "hull_s_min")
mean_win_hull_s_max =  locmean("victory", "hull_s_max")
mean_win_hull_observation = [
    mean_win_hull_total, mean_win_hull_med, mean_win_hull_mean, mean_win_hull_std, mean_win_hull_min, 
    mean_win_hull_max, mean_win_hull_s1, mean_win_hull_s2, mean_win_hull_s3, mean_win_hull_s4,
    mean_win_hull_s5, mean_win_hull_s6, mean_win_hull_s7, mean_win_hull_s8, mean_win_hull_s_med,
    mean_win_hull_s_mean, mean_win_hull_s_std, mean_win_hull_s_min, mean_win_hull_s_max,
]

mean_loss_hull_total = locmean("loss", "hull_total")
mean_loss_hull_med =  locmean("loss", "hull_med")
mean_loss_hull_mean =  locmean("loss", "hull_mean")
mean_loss_hull_std =  locmean("loss", "hull_std")
mean_loss_hull_min =  locmean("loss", "hull_min")
mean_loss_hull_max =  locmean("loss", "hull_max")
mean_loss_hull_s1 =  locmean("loss", "hull_s1")
mean_loss_hull_s2 =  locmean("loss", "hull_s2")
mean_loss_hull_s3 =  locmean("loss", "hull_s3")
mean_loss_hull_s4 =  locmean("loss", "hull_s4")
mean_loss_hull_s5 =  locmean("loss", "hull_s5")
mean_loss_hull_s6 =  locmean("loss", "hull_s6")
mean_loss_hull_s7 =  locmean("loss", "hull_s7")
mean_loss_hull_s8 =  locmean("loss", "hull_s8")
mean_loss_hull_s_med =  locmean("loss", "hull_s_med")
mean_loss_hull_s_mean =  locmean("loss", "hull_s_mean")
mean_loss_hull_s_std =  locmean("loss", "hull_s_std")
mean_loss_hull_s_min =  locmean("loss", "hull_s_min")
mean_loss_hull_s_max =  locmean("loss", "hull_s_max")
mean_loss_hull_observation = [
    mean_loss_hull_total, mean_loss_hull_med, mean_loss_hull_mean, mean_loss_hull_std, mean_loss_hull_min, 
    mean_loss_hull_max, mean_loss_hull_s1, mean_loss_hull_s2, mean_loss_hull_s3, mean_loss_hull_s4,
    mean_loss_hull_s5, mean_loss_hull_s6, mean_loss_hull_s7, mean_loss_hull_s8, mean_loss_hull_s_med,
    mean_loss_hull_s_mean, mean_loss_hull_s_std, mean_loss_hull_s_min, mean_loss_hull_s_max,
]

# hull_damage
hull_damage_total = df["hull_damage_total"].iloc[-1]
hull_damage_med = df["hull_damage_med"].iloc[-1]
hull_damage_mean = df["hull_damage_mean"].iloc[-1]
hull_damage_std = df["hull_damage_std"].iloc[-1]
hull_damage_min = df["hull_damage_min"].iloc[-1]
hull_damage_max = df["hull_damage_max"].iloc[-1]
hull_damage_s1 = df["hull_damage_s1"].iloc[-1]
hull_damage_s2 = df["hull_damage_s2"].iloc[-1]
hull_damage_s3 = df["hull_damage_s3"].iloc[-1]
hull_damage_s4 = df["hull_damage_s4"].iloc[-1]
hull_damage_s5 = df["hull_damage_s5"].iloc[-1]
hull_damage_s6 = df["hull_damage_s6"].iloc[-1]
hull_damage_s7 = df["hull_damage_s7"].iloc[-1]
hull_damage_s8 = df["hull_damage_s8"].iloc[-1]
hull_damage_s_med = df["hull_damage_s_med"].iloc[-1]
hull_damage_s_mean = df["hull_damage_s_mean"].iloc[-1]
hull_damage_s_std = df["hull_damage_s_std"].iloc[-1]
hull_damage_s_min = df["hull_damage_s_min"].iloc[-1]
hull_damage_s_max = df["hull_damage_s_max"].iloc[-1]
hull_damage_observation = [
    hull_damage_total, hull_damage_med, hull_damage_mean, hull_damage_std, hull_damage_min, hull_damage_max, hull_damage_s1,
    hull_damage_s2, hull_damage_s3,hull_damage_s4, hull_damage_s5, hull_damage_s6, hull_damage_s7, hull_damage_s8,
    hull_damage_s_med, hull_damage_s_mean, hull_damage_s_std, hull_damage_s_min, hull_damage_s_max,
]

mean_hull_damage_total = mean("hull_damage_total")
mean_hull_damage_med = mean("hull_damage_med")
mean_hull_damage_mean = mean("hull_damage_mean")
mean_hull_damage_std = mean("hull_damage_std")
mean_hull_damage_min = mean("hull_damage_min")
mean_hull_damage_max = mean("hull_damage_max")
mean_hull_damage_s1 = mean("hull_damage_s1")
mean_hull_damage_s2 = mean("hull_damage_s2")
mean_hull_damage_s3 = mean("hull_damage_s3")
mean_hull_damage_s4 = mean("hull_damage_s4")
mean_hull_damage_s5 = mean("hull_damage_s5")
mean_hull_damage_s6 = mean("hull_damage_s6")
mean_hull_damage_s7 = mean("hull_damage_s7")
mean_hull_damage_s8 = mean("hull_damage_s8")
mean_hull_damage_s_med = mean("hull_damage_s_med")
mean_hull_damage_s_mean = mean("hull_damage_s_mean")
mean_hull_damage_s_std = mean("hull_damage_s_std")
mean_hull_damage_s_min = mean("hull_damage_s_min")
mean_hull_damage_s_max = mean("hull_damage_s_max")
mean_hull_damage_observation = [
    mean_hull_damage_total, mean_hull_damage_med, mean_hull_damage_mean, mean_hull_damage_std, mean_hull_damage_min, 
    mean_hull_damage_max, mean_hull_damage_s1, mean_hull_damage_s2, mean_hull_damage_s3, mean_hull_damage_s4,
    mean_hull_damage_s5, mean_hull_damage_s6, mean_hull_damage_s7, mean_hull_damage_s8, mean_hull_damage_s_med,
    mean_hull_damage_s_mean, mean_hull_damage_s_std, mean_hull_damage_s_min, mean_hull_damage_s_max,
]

mean_win_hull_damage_total = locmean("victory", "hull_damage_total")
mean_win_hull_damage_med =  locmean("victory", "hull_damage_med")
mean_win_hull_damage_mean =  locmean("victory", "hull_damage_mean")
mean_win_hull_damage_std =  locmean("victory", "hull_damage_std")
mean_win_hull_damage_min =  locmean("victory", "hull_damage_min")
mean_win_hull_damage_max =  locmean("victory", "hull_damage_max")
mean_win_hull_damage_s1 =  locmean("victory", "hull_damage_s1")
mean_win_hull_damage_s2 =  locmean("victory", "hull_damage_s2")
mean_win_hull_damage_s3 =  locmean("victory", "hull_damage_s3")
mean_win_hull_damage_s4 =  locmean("victory", "hull_damage_s4")
mean_win_hull_damage_s5 =  locmean("victory", "hull_damage_s5")
mean_win_hull_damage_s6 =  locmean("victory", "hull_damage_s6")
mean_win_hull_damage_s7 =  locmean("victory", "hull_damage_s7")
mean_win_hull_damage_s8 =  locmean("victory", "hull_damage_s8")
mean_win_hull_damage_s_med =  locmean("victory", "hull_damage_s_med")
mean_win_hull_damage_s_mean =  locmean("victory", "hull_damage_s_mean")
mean_win_hull_damage_s_std =  locmean("victory", "hull_damage_s_std")
mean_win_hull_damage_s_min =  locmean("victory", "hull_damage_s_min")
mean_win_hull_damage_s_max =  locmean("victory", "hull_damage_s_max")
mean_win_hull_damage_observation = [
    mean_win_hull_damage_total, mean_win_hull_damage_med, mean_win_hull_damage_mean, mean_win_hull_damage_std, mean_win_hull_damage_min, 
    mean_win_hull_damage_max, mean_win_hull_damage_s1, mean_win_hull_damage_s2, mean_win_hull_damage_s3, mean_win_hull_damage_s4,
    mean_win_hull_damage_s5, mean_win_hull_damage_s6, mean_win_hull_damage_s7, mean_win_hull_damage_s8, mean_win_hull_damage_s_med,
    mean_win_hull_damage_s_mean, mean_win_hull_damage_s_std, mean_win_hull_damage_s_min, mean_win_hull_damage_s_max,
]

mean_loss_hull_damage_total = locmean("loss", "hull_damage_total")
mean_loss_hull_damage_med =  locmean("loss", "hull_damage_med")
mean_loss_hull_damage_mean =  locmean("loss", "hull_damage_mean")
mean_loss_hull_damage_std =  locmean("loss", "hull_damage_std")
mean_loss_hull_damage_min =  locmean("loss", "hull_damage_min")
mean_loss_hull_damage_max =  locmean("loss", "hull_damage_max")
mean_loss_hull_damage_s1 =  locmean("loss", "hull_damage_s1")
mean_loss_hull_damage_s2 =  locmean("loss", "hull_damage_s2")
mean_loss_hull_damage_s3 =  locmean("loss", "hull_damage_s3")
mean_loss_hull_damage_s4 =  locmean("loss", "hull_damage_s4")
mean_loss_hull_damage_s5 =  locmean("loss", "hull_damage_s5")
mean_loss_hull_damage_s6 =  locmean("loss", "hull_damage_s6")
mean_loss_hull_damage_s7 =  locmean("loss", "hull_damage_s7")
mean_loss_hull_damage_s8 =  locmean("loss", "hull_damage_s8")
mean_loss_hull_damage_s_med =  locmean("loss", "hull_damage_s_med")
mean_loss_hull_damage_s_mean =  locmean("loss", "hull_damage_s_mean")
mean_loss_hull_damage_s_std =  locmean("loss", "hull_damage_s_std")
mean_loss_hull_damage_s_min =  locmean("loss", "hull_damage_s_min")
mean_loss_hull_damage_s_max =  locmean("loss", "hull_damage_s_max")
mean_loss_hull_damage_observation = [
    mean_loss_hull_damage_total, mean_loss_hull_damage_med, mean_loss_hull_damage_mean, mean_loss_hull_damage_std, mean_loss_hull_damage_min, 
    mean_loss_hull_damage_max, mean_loss_hull_damage_s1, mean_loss_hull_damage_s2, mean_loss_hull_damage_s3, mean_loss_hull_damage_s4,
    mean_loss_hull_damage_s5, mean_loss_hull_damage_s6, mean_loss_hull_damage_s7, mean_loss_hull_damage_s8, mean_loss_hull_damage_s_med,
    mean_loss_hull_damage_s_mean, mean_loss_hull_damage_s_std, mean_loss_hull_damage_s_min, mean_loss_hull_damage_s_max,
]

# cargo
cargo_total = df["cargo_total"].iloc[-1]
cargo_med = df["cargo_med"].iloc[-1]
cargo_mean = df["cargo_mean"].iloc[-1]
cargo_std = df["cargo_std"].iloc[-1]
cargo_min = df["cargo_min"].iloc[-1]
cargo_max = df["cargo_max"].iloc[-1]
cargo_s1 = df["cargo_s1"].iloc[-1]
cargo_s2 = df["cargo_s2"].iloc[-1]
cargo_s3 = df["cargo_s3"].iloc[-1]
cargo_s4 = df["cargo_s4"].iloc[-1]
cargo_s5 = df["cargo_s5"].iloc[-1]
cargo_s6 = df["cargo_s6"].iloc[-1]
cargo_s7 = df["cargo_s7"].iloc[-1]
cargo_s8 = df["cargo_s8"].iloc[-1]
cargo_s_med = df["cargo_s_med"].iloc[-1]
cargo_s_mean = df["cargo_s_mean"].iloc[-1]
cargo_s_std = df["cargo_s_std"].iloc[-1]
cargo_s_min = df["cargo_s_min"].iloc[-1]
cargo_s_max = df["cargo_s_max"].iloc[-1]
cargo_observation = [
    cargo_total, cargo_med, cargo_mean, cargo_std, cargo_min, cargo_max, cargo_s1,
    cargo_s2, cargo_s3,cargo_s4, cargo_s5, cargo_s6, cargo_s7, cargo_s8,
    cargo_s_med, cargo_s_mean, cargo_s_std, cargo_s_min, cargo_s_max,
]

mean_cargo_total = mean("cargo_total")
mean_cargo_med = mean("cargo_med")
mean_cargo_mean = mean("cargo_mean")
mean_cargo_std = mean("cargo_std")
mean_cargo_min = mean("cargo_min")
mean_cargo_max = mean("cargo_max")
mean_cargo_s1 = mean("cargo_s1")
mean_cargo_s2 = mean("cargo_s2")
mean_cargo_s3 = mean("cargo_s3")
mean_cargo_s4 = mean("cargo_s4")
mean_cargo_s5 = mean("cargo_s5")
mean_cargo_s6 = mean("cargo_s6")
mean_cargo_s7 = mean("cargo_s7")
mean_cargo_s8 = mean("cargo_s8")
mean_cargo_s_med = mean("cargo_s_med")
mean_cargo_s_mean = mean("cargo_s_mean")
mean_cargo_s_std = mean("cargo_s_std")
mean_cargo_s_min = mean("cargo_s_min")
mean_cargo_s_max = mean("cargo_s_max")
mean_cargo_observation = [
    mean_cargo_total, mean_cargo_med, mean_cargo_mean, mean_cargo_std, mean_cargo_min, 
    mean_cargo_max, mean_cargo_s1, mean_cargo_s2, mean_cargo_s3, mean_cargo_s4,
    mean_cargo_s5, mean_cargo_s6, mean_cargo_s7, mean_cargo_s8, mean_cargo_s_med,
    mean_cargo_s_mean, mean_cargo_s_std, mean_cargo_s_min, mean_cargo_s_max,
]

mean_win_cargo_total = locmean("victory", "cargo_total")
mean_win_cargo_med =  locmean("victory", "cargo_med")
mean_win_cargo_mean =  locmean("victory", "cargo_mean")
mean_win_cargo_std =  locmean("victory", "cargo_std")
mean_win_cargo_min =  locmean("victory", "cargo_min")
mean_win_cargo_max =  locmean("victory", "cargo_max")
mean_win_cargo_s1 =  locmean("victory", "cargo_s1")
mean_win_cargo_s2 =  locmean("victory", "cargo_s2")
mean_win_cargo_s3 =  locmean("victory", "cargo_s3")
mean_win_cargo_s4 =  locmean("victory", "cargo_s4")
mean_win_cargo_s5 =  locmean("victory", "cargo_s5")
mean_win_cargo_s6 =  locmean("victory", "cargo_s6")
mean_win_cargo_s7 =  locmean("victory", "cargo_s7")
mean_win_cargo_s8 =  locmean("victory", "cargo_s8")
mean_win_cargo_s_med =  locmean("victory", "cargo_s_med")
mean_win_cargo_s_mean =  locmean("victory", "cargo_s_mean")
mean_win_cargo_s_std =  locmean("victory", "cargo_s_std")
mean_win_cargo_s_min =  locmean("victory", "cargo_s_min")
mean_win_cargo_s_max =  locmean("victory", "cargo_s_max")
mean_win_cargo_observation = [
    mean_win_cargo_total, mean_win_cargo_med, mean_win_cargo_mean, mean_win_cargo_std, mean_win_cargo_min, 
    mean_win_cargo_max, mean_win_cargo_s1, mean_win_cargo_s2, mean_win_cargo_s3, mean_win_cargo_s4,
    mean_win_cargo_s5, mean_win_cargo_s6, mean_win_cargo_s7, mean_win_cargo_s8, mean_win_cargo_s_med,
    mean_win_cargo_s_mean, mean_win_cargo_s_std, mean_win_cargo_s_min, mean_win_cargo_s_max,
]

mean_loss_cargo_total = locmean("loss", "cargo_total")
mean_loss_cargo_med =  locmean("loss", "cargo_med")
mean_loss_cargo_mean =  locmean("loss", "cargo_mean")
mean_loss_cargo_std =  locmean("loss", "cargo_std")
mean_loss_cargo_min =  locmean("loss", "cargo_min")
mean_loss_cargo_max =  locmean("loss", "cargo_max")
mean_loss_cargo_s1 =  locmean("loss", "cargo_s1")
mean_loss_cargo_s2 =  locmean("loss", "cargo_s2")
mean_loss_cargo_s3 =  locmean("loss", "cargo_s3")
mean_loss_cargo_s4 =  locmean("loss", "cargo_s4")
mean_loss_cargo_s5 =  locmean("loss", "cargo_s5")
mean_loss_cargo_s6 =  locmean("loss", "cargo_s6")
mean_loss_cargo_s7 =  locmean("loss", "cargo_s7")
mean_loss_cargo_s8 =  locmean("loss", "cargo_s8")
mean_loss_cargo_s_med =  locmean("loss", "cargo_s_med")
mean_loss_cargo_s_mean =  locmean("loss", "cargo_s_mean")
mean_loss_cargo_s_std =  locmean("loss", "cargo_s_std")
mean_loss_cargo_s_min =  locmean("loss", "cargo_s_min")
mean_loss_cargo_s_max =  locmean("loss", "cargo_s_max")
mean_loss_cargo_observation = [
    mean_loss_cargo_total, mean_loss_cargo_med, mean_loss_cargo_mean, mean_loss_cargo_std, mean_loss_cargo_min, 
    mean_loss_cargo_max, mean_loss_cargo_s1, mean_loss_cargo_s2, mean_loss_cargo_s3, mean_loss_cargo_s4,
    mean_loss_cargo_s5, mean_loss_cargo_s6, mean_loss_cargo_s7, mean_loss_cargo_s8, mean_loss_cargo_s_med,
    mean_loss_cargo_s_mean, mean_loss_cargo_s_std, mean_loss_cargo_s_min, mean_loss_cargo_s_max,
]

# stores_visited
stores_visited_total = df["stores_visited_total"].iloc[-1]
stores_visited_med = df["stores_visited_med"].iloc[-1]
stores_visited_mean = df["stores_visited_mean"].iloc[-1]
stores_visited_std = df["stores_visited_std"].iloc[-1]
stores_visited_min = df["stores_visited_min"].iloc[-1]
stores_visited_max = df["stores_visited_max"].iloc[-1]
stores_visited_s1 = df["stores_visited_s1"].iloc[-1]
stores_visited_s2 = df["stores_visited_s2"].iloc[-1]
stores_visited_s3 = df["stores_visited_s3"].iloc[-1]
stores_visited_s4 = df["stores_visited_s4"].iloc[-1]
stores_visited_s5 = df["stores_visited_s5"].iloc[-1]
stores_visited_s6 = df["stores_visited_s6"].iloc[-1]
stores_visited_s7 = df["stores_visited_s7"].iloc[-1]
stores_visited_s8 = df["stores_visited_s8"].iloc[-1]
stores_visited_s_med = df["stores_visited_s_med"].iloc[-1]
stores_visited_s_mean = df["stores_visited_s_mean"].iloc[-1]
stores_visited_s_std = df["stores_visited_s_std"].iloc[-1]
stores_visited_s_min = df["stores_visited_s_min"].iloc[-1]
stores_visited_s_max = df["stores_visited_s_max"].iloc[-1]
stores_visited_observation = [
    stores_visited_total, stores_visited_med, stores_visited_mean, stores_visited_std, stores_visited_min, stores_visited_max, stores_visited_s1,
    stores_visited_s2, stores_visited_s3,stores_visited_s4, stores_visited_s5, stores_visited_s6, stores_visited_s7, stores_visited_s8,
    stores_visited_s_med, stores_visited_s_mean, stores_visited_s_std, stores_visited_s_min, stores_visited_s_max,
]

mean_stores_visited_total = mean("stores_visited_total")
mean_stores_visited_med = mean("stores_visited_med")
mean_stores_visited_mean = mean("stores_visited_mean")
mean_stores_visited_std = mean("stores_visited_std")
mean_stores_visited_min = mean("stores_visited_min")
mean_stores_visited_max = mean("stores_visited_max")
mean_stores_visited_s1 = mean("stores_visited_s1")
mean_stores_visited_s2 = mean("stores_visited_s2")
mean_stores_visited_s3 = mean("stores_visited_s3")
mean_stores_visited_s4 = mean("stores_visited_s4")
mean_stores_visited_s5 = mean("stores_visited_s5")
mean_stores_visited_s6 = mean("stores_visited_s6")
mean_stores_visited_s7 = mean("stores_visited_s7")
mean_stores_visited_s8 = mean("stores_visited_s8")
mean_stores_visited_s_med = mean("stores_visited_s_med")
mean_stores_visited_s_mean = mean("stores_visited_s_mean")
mean_stores_visited_s_std = mean("stores_visited_s_std")
mean_stores_visited_s_min = mean("stores_visited_s_min")
mean_stores_visited_s_max = mean("stores_visited_s_max")
mean_stores_visited_observation = [
    mean_stores_visited_total, mean_stores_visited_med, mean_stores_visited_mean, mean_stores_visited_std, mean_stores_visited_min, 
    mean_stores_visited_max, mean_stores_visited_s1, mean_stores_visited_s2, mean_stores_visited_s3, mean_stores_visited_s4,
    mean_stores_visited_s5, mean_stores_visited_s6, mean_stores_visited_s7, mean_stores_visited_s8, mean_stores_visited_s_med,
    mean_stores_visited_s_mean, mean_stores_visited_s_std, mean_stores_visited_s_min, mean_stores_visited_s_max,
]

mean_win_stores_visited_total = locmean("victory", "stores_visited_total")
mean_win_stores_visited_med =  locmean("victory", "stores_visited_med")
mean_win_stores_visited_mean =  locmean("victory", "stores_visited_mean")
mean_win_stores_visited_std =  locmean("victory", "stores_visited_std")
mean_win_stores_visited_min =  locmean("victory", "stores_visited_min")
mean_win_stores_visited_max =  locmean("victory", "stores_visited_max")
mean_win_stores_visited_s1 =  locmean("victory", "stores_visited_s1")
mean_win_stores_visited_s2 =  locmean("victory", "stores_visited_s2")
mean_win_stores_visited_s3 =  locmean("victory", "stores_visited_s3")
mean_win_stores_visited_s4 =  locmean("victory", "stores_visited_s4")
mean_win_stores_visited_s5 =  locmean("victory", "stores_visited_s5")
mean_win_stores_visited_s6 =  locmean("victory", "stores_visited_s6")
mean_win_stores_visited_s7 =  locmean("victory", "stores_visited_s7")
mean_win_stores_visited_s8 =  locmean("victory", "stores_visited_s8")
mean_win_stores_visited_s_med =  locmean("victory", "stores_visited_s_med")
mean_win_stores_visited_s_mean =  locmean("victory", "stores_visited_s_mean")
mean_win_stores_visited_s_std =  locmean("victory", "stores_visited_s_std")
mean_win_stores_visited_s_min =  locmean("victory", "stores_visited_s_min")
mean_win_stores_visited_s_max =  locmean("victory", "stores_visited_s_max")
mean_win_stores_visited_observation = [
    mean_win_stores_visited_total, mean_win_stores_visited_med, mean_win_stores_visited_mean, mean_win_stores_visited_std, mean_win_stores_visited_min, 
    mean_win_stores_visited_max, mean_win_stores_visited_s1, mean_win_stores_visited_s2, mean_win_stores_visited_s3, mean_win_stores_visited_s4,
    mean_win_stores_visited_s5, mean_win_stores_visited_s6, mean_win_stores_visited_s7, mean_win_stores_visited_s8, mean_win_stores_visited_s_med,
    mean_win_stores_visited_s_mean, mean_win_stores_visited_s_std, mean_win_stores_visited_s_min, mean_win_stores_visited_s_max,
]

mean_loss_stores_visited_total = locmean("loss", "stores_visited_total")
mean_loss_stores_visited_med =  locmean("loss", "stores_visited_med")
mean_loss_stores_visited_mean =  locmean("loss", "stores_visited_mean")
mean_loss_stores_visited_std =  locmean("loss", "stores_visited_std")
mean_loss_stores_visited_min =  locmean("loss", "stores_visited_min")
mean_loss_stores_visited_max =  locmean("loss", "stores_visited_max")
mean_loss_stores_visited_s1 =  locmean("loss", "stores_visited_s1")
mean_loss_stores_visited_s2 =  locmean("loss", "stores_visited_s2")
mean_loss_stores_visited_s3 =  locmean("loss", "stores_visited_s3")
mean_loss_stores_visited_s4 =  locmean("loss", "stores_visited_s4")
mean_loss_stores_visited_s5 =  locmean("loss", "stores_visited_s5")
mean_loss_stores_visited_s6 =  locmean("loss", "stores_visited_s6")
mean_loss_stores_visited_s7 =  locmean("loss", "stores_visited_s7")
mean_loss_stores_visited_s8 =  locmean("loss", "stores_visited_s8")
mean_loss_stores_visited_s_med =  locmean("loss", "stores_visited_s_med")
mean_loss_stores_visited_s_mean =  locmean("loss", "stores_visited_s_mean")
mean_loss_stores_visited_s_std =  locmean("loss", "stores_visited_s_std")
mean_loss_stores_visited_s_min =  locmean("loss", "stores_visited_s_min")
mean_loss_stores_visited_s_max =  locmean("loss", "stores_visited_s_max")
mean_loss_stores_visited_observation = [
    mean_loss_stores_visited_total, mean_loss_stores_visited_med, mean_loss_stores_visited_mean, mean_loss_stores_visited_std, mean_loss_stores_visited_min, 
    mean_loss_stores_visited_max, mean_loss_stores_visited_s1, mean_loss_stores_visited_s2, mean_loss_stores_visited_s3, mean_loss_stores_visited_s4,
    mean_loss_stores_visited_s5, mean_loss_stores_visited_s6, mean_loss_stores_visited_s7, mean_loss_stores_visited_s8, mean_loss_stores_visited_s_med,
    mean_loss_stores_visited_s_mean, mean_loss_stores_visited_s_std, mean_loss_stores_visited_s_min, mean_loss_stores_visited_s_max,
]

# fuel
fuel_total = df["fuel_total"].iloc[-1]
fuel_med = df["fuel_med"].iloc[-1]
fuel_mean = df["fuel_mean"].iloc[-1]
fuel_std = df["fuel_std"].iloc[-1]
fuel_min = df["fuel_min"].iloc[-1]
fuel_max = df["fuel_max"].iloc[-1]
fuel_s1 = df["fuel_s1"].iloc[-1]
fuel_s2 = df["fuel_s2"].iloc[-1]
fuel_s3 = df["fuel_s3"].iloc[-1]
fuel_s4 = df["fuel_s4"].iloc[-1]
fuel_s5 = df["fuel_s5"].iloc[-1]
fuel_s6 = df["fuel_s6"].iloc[-1]
fuel_s7 = df["fuel_s7"].iloc[-1]
fuel_s8 = df["fuel_s8"].iloc[-1]
fuel_s_med = df["fuel_s_med"].iloc[-1]
fuel_s_mean = df["fuel_s_mean"].iloc[-1]
fuel_s_std = df["fuel_s_std"].iloc[-1]
fuel_s_min = df["fuel_s_min"].iloc[-1]
fuel_s_max = df["fuel_s_max"].iloc[-1]
fuel_observation = [
    fuel_total, fuel_med, fuel_mean, fuel_std, fuel_min, fuel_max, fuel_s1,
    fuel_s2, fuel_s3,fuel_s4, fuel_s5, fuel_s6, fuel_s7, fuel_s8,
    fuel_s_med, fuel_s_mean, fuel_s_std, fuel_s_min, fuel_s_max,
]

mean_fuel_total = mean("fuel_total")
mean_fuel_med = mean("fuel_med")
mean_fuel_mean = mean("fuel_mean")
mean_fuel_std = mean("fuel_std")
mean_fuel_min = mean("fuel_min")
mean_fuel_max = mean("fuel_max")
mean_fuel_s1 = mean("fuel_s1")
mean_fuel_s2 = mean("fuel_s2")
mean_fuel_s3 = mean("fuel_s3")
mean_fuel_s4 = mean("fuel_s4")
mean_fuel_s5 = mean("fuel_s5")
mean_fuel_s6 = mean("fuel_s6")
mean_fuel_s7 = mean("fuel_s7")
mean_fuel_s8 = mean("fuel_s8")
mean_fuel_s_med = mean("fuel_s_med")
mean_fuel_s_mean = mean("fuel_s_mean")
mean_fuel_s_std = mean("fuel_s_std")
mean_fuel_s_min = mean("fuel_s_min")
mean_fuel_s_max = mean("fuel_s_max")
mean_fuel_observation = [
    mean_fuel_total, mean_fuel_med, mean_fuel_mean, mean_fuel_std, mean_fuel_min, 
    mean_fuel_max, mean_fuel_s1, mean_fuel_s2, mean_fuel_s3, mean_fuel_s4,
    mean_fuel_s5, mean_fuel_s6, mean_fuel_s7, mean_fuel_s8, mean_fuel_s_med,
    mean_fuel_s_mean, mean_fuel_s_std, mean_fuel_s_min, mean_fuel_s_max,
]

mean_win_fuel_total = locmean("victory", "fuel_total")
mean_win_fuel_med =  locmean("victory", "fuel_med")
mean_win_fuel_mean =  locmean("victory", "fuel_mean")
mean_win_fuel_std =  locmean("victory", "fuel_std")
mean_win_fuel_min =  locmean("victory", "fuel_min")
mean_win_fuel_max =  locmean("victory", "fuel_max")
mean_win_fuel_s1 =  locmean("victory", "fuel_s1")
mean_win_fuel_s2 =  locmean("victory", "fuel_s2")
mean_win_fuel_s3 =  locmean("victory", "fuel_s3")
mean_win_fuel_s4 =  locmean("victory", "fuel_s4")
mean_win_fuel_s5 =  locmean("victory", "fuel_s5")
mean_win_fuel_s6 =  locmean("victory", "fuel_s6")
mean_win_fuel_s7 =  locmean("victory", "fuel_s7")
mean_win_fuel_s8 =  locmean("victory", "fuel_s8")
mean_win_fuel_s_med =  locmean("victory", "fuel_s_med")
mean_win_fuel_s_mean =  locmean("victory", "fuel_s_mean")
mean_win_fuel_s_std =  locmean("victory", "fuel_s_std")
mean_win_fuel_s_min =  locmean("victory", "fuel_s_min")
mean_win_fuel_s_max =  locmean("victory", "fuel_s_max")
mean_win_fuel_observation = [
    mean_win_fuel_total, mean_win_fuel_med, mean_win_fuel_mean, mean_win_fuel_std, mean_win_fuel_min, 
    mean_win_fuel_max, mean_win_fuel_s1, mean_win_fuel_s2, mean_win_fuel_s3, mean_win_fuel_s4,
    mean_win_fuel_s5, mean_win_fuel_s6, mean_win_fuel_s7, mean_win_fuel_s8, mean_win_fuel_s_med,
    mean_win_fuel_s_mean, mean_win_fuel_s_std, mean_win_fuel_s_min, mean_win_fuel_s_max,
]

mean_loss_fuel_total = locmean("loss", "fuel_total")
mean_loss_fuel_med =  locmean("loss", "fuel_med")
mean_loss_fuel_mean =  locmean("loss", "fuel_mean")
mean_loss_fuel_std =  locmean("loss", "fuel_std")
mean_loss_fuel_min =  locmean("loss", "fuel_min")
mean_loss_fuel_max =  locmean("loss", "fuel_max")
mean_loss_fuel_s1 =  locmean("loss", "fuel_s1")
mean_loss_fuel_s2 =  locmean("loss", "fuel_s2")
mean_loss_fuel_s3 =  locmean("loss", "fuel_s3")
mean_loss_fuel_s4 =  locmean("loss", "fuel_s4")
mean_loss_fuel_s5 =  locmean("loss", "fuel_s5")
mean_loss_fuel_s6 =  locmean("loss", "fuel_s6")
mean_loss_fuel_s7 =  locmean("loss", "fuel_s7")
mean_loss_fuel_s8 =  locmean("loss", "fuel_s8")
mean_loss_fuel_s_med =  locmean("loss", "fuel_s_med")
mean_loss_fuel_s_mean =  locmean("loss", "fuel_s_mean")
mean_loss_fuel_s_std =  locmean("loss", "fuel_s_std")
mean_loss_fuel_s_min =  locmean("loss", "fuel_s_min")
mean_loss_fuel_s_max =  locmean("loss", "fuel_s_max")
mean_loss_fuel_observation = [
    mean_loss_fuel_total, mean_loss_fuel_med, mean_loss_fuel_mean, mean_loss_fuel_std, mean_loss_fuel_min, 
    mean_loss_fuel_max, mean_loss_fuel_s1, mean_loss_fuel_s2, mean_loss_fuel_s3, mean_loss_fuel_s4,
    mean_loss_fuel_s5, mean_loss_fuel_s6, mean_loss_fuel_s7, mean_loss_fuel_s8, mean_loss_fuel_s_med,
    mean_loss_fuel_s_mean, mean_loss_fuel_s_std, mean_loss_fuel_s_min, mean_loss_fuel_s_max,
]

# missiles
missiles_total = df["missiles_total"].iloc[-1]
missiles_med = df["missiles_med"].iloc[-1]
missiles_mean = df["missiles_mean"].iloc[-1]
missiles_std = df["missiles_std"].iloc[-1]
missiles_min = df["missiles_min"].iloc[-1]
missiles_max = df["missiles_max"].iloc[-1]
missiles_s1 = df["missiles_s1"].iloc[-1]
missiles_s2 = df["missiles_s2"].iloc[-1]
missiles_s3 = df["missiles_s3"].iloc[-1]
missiles_s4 = df["missiles_s4"].iloc[-1]
missiles_s5 = df["missiles_s5"].iloc[-1]
missiles_s6 = df["missiles_s6"].iloc[-1]
missiles_s7 = df["missiles_s7"].iloc[-1]
missiles_s8 = df["missiles_s8"].iloc[-1]
missiles_s_med = df["missiles_s_med"].iloc[-1]
missiles_s_mean = df["missiles_s_mean"].iloc[-1]
missiles_s_std = df["missiles_s_std"].iloc[-1]
missiles_s_min = df["missiles_s_min"].iloc[-1]
missiles_s_max = df["missiles_s_max"].iloc[-1]
missiles_observation = [
    missiles_total, missiles_med, missiles_mean, missiles_std, missiles_min, missiles_max, missiles_s1,
    missiles_s2, missiles_s3,missiles_s4, missiles_s5, missiles_s6, missiles_s7, missiles_s8,
    missiles_s_med, missiles_s_mean, missiles_s_std, missiles_s_min, missiles_s_max,
]

mean_missiles_total = mean("missiles_total")
mean_missiles_med = mean("missiles_med")
mean_missiles_mean = mean("missiles_mean")
mean_missiles_std = mean("missiles_std")
mean_missiles_min = mean("missiles_min")
mean_missiles_max = mean("missiles_max")
mean_missiles_s1 = mean("missiles_s1")
mean_missiles_s2 = mean("missiles_s2")
mean_missiles_s3 = mean("missiles_s3")
mean_missiles_s4 = mean("missiles_s4")
mean_missiles_s5 = mean("missiles_s5")
mean_missiles_s6 = mean("missiles_s6")
mean_missiles_s7 = mean("missiles_s7")
mean_missiles_s8 = mean("missiles_s8")
mean_missiles_s_med = mean("missiles_s_med")
mean_missiles_s_mean = mean("missiles_s_mean")
mean_missiles_s_std = mean("missiles_s_std")
mean_missiles_s_min = mean("missiles_s_min")
mean_missiles_s_max = mean("missiles_s_max")
mean_missiles_observation = [
    mean_missiles_total, mean_missiles_med, mean_missiles_mean, mean_missiles_std, mean_missiles_min, 
    mean_missiles_max, mean_missiles_s1, mean_missiles_s2, mean_missiles_s3, mean_missiles_s4,
    mean_missiles_s5, mean_missiles_s6, mean_missiles_s7, mean_missiles_s8, mean_missiles_s_med,
    mean_missiles_s_mean, mean_missiles_s_std, mean_missiles_s_min, mean_missiles_s_max,
]

mean_win_missiles_total = locmean("victory", "missiles_total")
mean_win_missiles_med =  locmean("victory", "missiles_med")
mean_win_missiles_mean =  locmean("victory", "missiles_mean")
mean_win_missiles_std =  locmean("victory", "missiles_std")
mean_win_missiles_min =  locmean("victory", "missiles_min")
mean_win_missiles_max =  locmean("victory", "missiles_max")
mean_win_missiles_s1 =  locmean("victory", "missiles_s1")
mean_win_missiles_s2 =  locmean("victory", "missiles_s2")
mean_win_missiles_s3 =  locmean("victory", "missiles_s3")
mean_win_missiles_s4 =  locmean("victory", "missiles_s4")
mean_win_missiles_s5 =  locmean("victory", "missiles_s5")
mean_win_missiles_s6 =  locmean("victory", "missiles_s6")
mean_win_missiles_s7 =  locmean("victory", "missiles_s7")
mean_win_missiles_s8 =  locmean("victory", "missiles_s8")
mean_win_missiles_s_med =  locmean("victory", "missiles_s_med")
mean_win_missiles_s_mean =  locmean("victory", "missiles_s_mean")
mean_win_missiles_s_std =  locmean("victory", "missiles_s_std")
mean_win_missiles_s_min =  locmean("victory", "missiles_s_min")
mean_win_missiles_s_max =  locmean("victory", "missiles_s_max")
mean_win_missiles_observation = [
    mean_win_missiles_total, mean_win_missiles_med, mean_win_missiles_mean, mean_win_missiles_std, mean_win_missiles_min, 
    mean_win_missiles_max, mean_win_missiles_s1, mean_win_missiles_s2, mean_win_missiles_s3, mean_win_missiles_s4,
    mean_win_missiles_s5, mean_win_missiles_s6, mean_win_missiles_s7, mean_win_missiles_s8, mean_win_missiles_s_med,
    mean_win_missiles_s_mean, mean_win_missiles_s_std, mean_win_missiles_s_min, mean_win_missiles_s_max,
]

mean_loss_missiles_total = locmean("loss", "missiles_total")
mean_loss_missiles_med =  locmean("loss", "missiles_med")
mean_loss_missiles_mean =  locmean("loss", "missiles_mean")
mean_loss_missiles_std =  locmean("loss", "missiles_std")
mean_loss_missiles_min =  locmean("loss", "missiles_min")
mean_loss_missiles_max =  locmean("loss", "missiles_max")
mean_loss_missiles_s1 =  locmean("loss", "missiles_s1")
mean_loss_missiles_s2 =  locmean("loss", "missiles_s2")
mean_loss_missiles_s3 =  locmean("loss", "missiles_s3")
mean_loss_missiles_s4 =  locmean("loss", "missiles_s4")
mean_loss_missiles_s5 =  locmean("loss", "missiles_s5")
mean_loss_missiles_s6 =  locmean("loss", "missiles_s6")
mean_loss_missiles_s7 =  locmean("loss", "missiles_s7")
mean_loss_missiles_s8 =  locmean("loss", "missiles_s8")
mean_loss_missiles_s_med =  locmean("loss", "missiles_s_med")
mean_loss_missiles_s_mean =  locmean("loss", "missiles_s_mean")
mean_loss_missiles_s_std =  locmean("loss", "missiles_s_std")
mean_loss_missiles_s_min =  locmean("loss", "missiles_s_min")
mean_loss_missiles_s_max =  locmean("loss", "missiles_s_max")
mean_loss_missiles_observation = [
    mean_loss_missiles_total, mean_loss_missiles_med, mean_loss_missiles_mean, mean_loss_missiles_std, mean_loss_missiles_min, 
    mean_loss_missiles_max, mean_loss_missiles_s1, mean_loss_missiles_s2, mean_loss_missiles_s3, mean_loss_missiles_s4,
    mean_loss_missiles_s5, mean_loss_missiles_s6, mean_loss_missiles_s7, mean_loss_missiles_s8, mean_loss_missiles_s_med,
    mean_loss_missiles_s_mean, mean_loss_missiles_s_std, mean_loss_missiles_s_min, mean_loss_missiles_s_max,
]

# drone_parts
drone_parts_total = df["drone_parts_total"].iloc[-1]
drone_parts_med = df["drone_parts_med"].iloc[-1]
drone_parts_mean = df["drone_parts_mean"].iloc[-1]
drone_parts_std = df["drone_parts_std"].iloc[-1]
drone_parts_min = df["drone_parts_min"].iloc[-1]
drone_parts_max = df["drone_parts_max"].iloc[-1]
drone_parts_s1 = df["drone_parts_s1"].iloc[-1]
drone_parts_s2 = df["drone_parts_s2"].iloc[-1]
drone_parts_s3 = df["drone_parts_s3"].iloc[-1]
drone_parts_s4 = df["drone_parts_s4"].iloc[-1]
drone_parts_s5 = df["drone_parts_s5"].iloc[-1]
drone_parts_s6 = df["drone_parts_s6"].iloc[-1]
drone_parts_s7 = df["drone_parts_s7"].iloc[-1]
drone_parts_s8 = df["drone_parts_s8"].iloc[-1]
drone_parts_s_med = df["drone_parts_s_med"].iloc[-1]
drone_parts_s_mean = df["drone_parts_s_mean"].iloc[-1]
drone_parts_s_std = df["drone_parts_s_std"].iloc[-1]
drone_parts_s_min = df["drone_parts_s_min"].iloc[-1]
drone_parts_s_max = df["drone_parts_s_max"].iloc[-1]
drone_parts_observation = [
    drone_parts_total, drone_parts_med, drone_parts_mean, drone_parts_std, drone_parts_min, drone_parts_max, drone_parts_s1,
    drone_parts_s2, drone_parts_s3,drone_parts_s4, drone_parts_s5, drone_parts_s6, drone_parts_s7, drone_parts_s8,
    drone_parts_s_med, drone_parts_s_mean, drone_parts_s_std, drone_parts_s_min, drone_parts_s_max,
]

mean_drone_parts_total = mean("drone_parts_total")
mean_drone_parts_med = mean("drone_parts_med")
mean_drone_parts_mean = mean("drone_parts_mean")
mean_drone_parts_std = mean("drone_parts_std")
mean_drone_parts_min = mean("drone_parts_min")
mean_drone_parts_max = mean("drone_parts_max")
mean_drone_parts_s1 = mean("drone_parts_s1")
mean_drone_parts_s2 = mean("drone_parts_s2")
mean_drone_parts_s3 = mean("drone_parts_s3")
mean_drone_parts_s4 = mean("drone_parts_s4")
mean_drone_parts_s5 = mean("drone_parts_s5")
mean_drone_parts_s6 = mean("drone_parts_s6")
mean_drone_parts_s7 = mean("drone_parts_s7")
mean_drone_parts_s8 = mean("drone_parts_s8")
mean_drone_parts_s_med = mean("drone_parts_s_med")
mean_drone_parts_s_mean = mean("drone_parts_s_mean")
mean_drone_parts_s_std = mean("drone_parts_s_std")
mean_drone_parts_s_min = mean("drone_parts_s_min")
mean_drone_parts_s_max = mean("drone_parts_s_max")
mean_drone_parts_observation = [
    mean_drone_parts_total, mean_drone_parts_med, mean_drone_parts_mean, mean_drone_parts_std, mean_drone_parts_min, 
    mean_drone_parts_max, mean_drone_parts_s1, mean_drone_parts_s2, mean_drone_parts_s3, mean_drone_parts_s4,
    mean_drone_parts_s5, mean_drone_parts_s6, mean_drone_parts_s7, mean_drone_parts_s8, mean_drone_parts_s_med,
    mean_drone_parts_s_mean, mean_drone_parts_s_std, mean_drone_parts_s_min, mean_drone_parts_s_max,
]

mean_win_drone_parts_total = locmean("victory", "drone_parts_total")
mean_win_drone_parts_med =  locmean("victory", "drone_parts_med")
mean_win_drone_parts_mean =  locmean("victory", "drone_parts_mean")
mean_win_drone_parts_std =  locmean("victory", "drone_parts_std")
mean_win_drone_parts_min =  locmean("victory", "drone_parts_min")
mean_win_drone_parts_max =  locmean("victory", "drone_parts_max")
mean_win_drone_parts_s1 =  locmean("victory", "drone_parts_s1")
mean_win_drone_parts_s2 =  locmean("victory", "drone_parts_s2")
mean_win_drone_parts_s3 =  locmean("victory", "drone_parts_s3")
mean_win_drone_parts_s4 =  locmean("victory", "drone_parts_s4")
mean_win_drone_parts_s5 =  locmean("victory", "drone_parts_s5")
mean_win_drone_parts_s6 =  locmean("victory", "drone_parts_s6")
mean_win_drone_parts_s7 =  locmean("victory", "drone_parts_s7")
mean_win_drone_parts_s8 =  locmean("victory", "drone_parts_s8")
mean_win_drone_parts_s_med =  locmean("victory", "drone_parts_s_med")
mean_win_drone_parts_s_mean =  locmean("victory", "drone_parts_s_mean")
mean_win_drone_parts_s_std =  locmean("victory", "drone_parts_s_std")
mean_win_drone_parts_s_min =  locmean("victory", "drone_parts_s_min")
mean_win_drone_parts_s_max =  locmean("victory", "drone_parts_s_max")
mean_win_drone_parts_observation = [
    mean_win_drone_parts_total, mean_win_drone_parts_med, mean_win_drone_parts_mean, mean_win_drone_parts_std, mean_win_drone_parts_min, 
    mean_win_drone_parts_max, mean_win_drone_parts_s1, mean_win_drone_parts_s2, mean_win_drone_parts_s3, mean_win_drone_parts_s4,
    mean_win_drone_parts_s5, mean_win_drone_parts_s6, mean_win_drone_parts_s7, mean_win_drone_parts_s8, mean_win_drone_parts_s_med,
    mean_win_drone_parts_s_mean, mean_win_drone_parts_s_std, mean_win_drone_parts_s_min, mean_win_drone_parts_s_max,
]

mean_loss_drone_parts_total = locmean("loss", "drone_parts_total")
mean_loss_drone_parts_med =  locmean("loss", "drone_parts_med")
mean_loss_drone_parts_mean =  locmean("loss", "drone_parts_mean")
mean_loss_drone_parts_std =  locmean("loss", "drone_parts_std")
mean_loss_drone_parts_min =  locmean("loss", "drone_parts_min")
mean_loss_drone_parts_max =  locmean("loss", "drone_parts_max")
mean_loss_drone_parts_s1 =  locmean("loss", "drone_parts_s1")
mean_loss_drone_parts_s2 =  locmean("loss", "drone_parts_s2")
mean_loss_drone_parts_s3 =  locmean("loss", "drone_parts_s3")
mean_loss_drone_parts_s4 =  locmean("loss", "drone_parts_s4")
mean_loss_drone_parts_s5 =  locmean("loss", "drone_parts_s5")
mean_loss_drone_parts_s6 =  locmean("loss", "drone_parts_s6")
mean_loss_drone_parts_s7 =  locmean("loss", "drone_parts_s7")
mean_loss_drone_parts_s8 =  locmean("loss", "drone_parts_s8")
mean_loss_drone_parts_s_med =  locmean("loss", "drone_parts_s_med")
mean_loss_drone_parts_s_mean =  locmean("loss", "drone_parts_s_mean")
mean_loss_drone_parts_s_std =  locmean("loss", "drone_parts_s_std")
mean_loss_drone_parts_s_min =  locmean("loss", "drone_parts_s_min")
mean_loss_drone_parts_s_max =  locmean("loss", "drone_parts_s_max")
mean_loss_drone_parts_observation = [
    mean_loss_drone_parts_total, mean_loss_drone_parts_med, mean_loss_drone_parts_mean, mean_loss_drone_parts_std, mean_loss_drone_parts_min, 
    mean_loss_drone_parts_max, mean_loss_drone_parts_s1, mean_loss_drone_parts_s2, mean_loss_drone_parts_s3, mean_loss_drone_parts_s4,
    mean_loss_drone_parts_s5, mean_loss_drone_parts_s6, mean_loss_drone_parts_s7, mean_loss_drone_parts_s8, mean_loss_drone_parts_s_med,
    mean_loss_drone_parts_s_mean, mean_loss_drone_parts_s_std, mean_loss_drone_parts_s_min, mean_loss_drone_parts_s_max,
]

# crew_hired
crew_hired_total = df["crew_hired_total"].iloc[-1]
crew_hired_med = df["crew_hired_med"].iloc[-1]
crew_hired_mean = df["crew_hired_mean"].iloc[-1]
crew_hired_std = df["crew_hired_std"].iloc[-1]
crew_hired_min = df["crew_hired_min"].iloc[-1]
crew_hired_max = df["crew_hired_max"].iloc[-1]
crew_hired_s1 = df["crew_hired_s1"].iloc[-1]
crew_hired_s2 = df["crew_hired_s2"].iloc[-1]
crew_hired_s3 = df["crew_hired_s3"].iloc[-1]
crew_hired_s4 = df["crew_hired_s4"].iloc[-1]
crew_hired_s5 = df["crew_hired_s5"].iloc[-1]
crew_hired_s6 = df["crew_hired_s6"].iloc[-1]
crew_hired_s7 = df["crew_hired_s7"].iloc[-1]
crew_hired_s8 = df["crew_hired_s8"].iloc[-1]
crew_hired_s_med = df["crew_hired_s_med"].iloc[-1]
crew_hired_s_mean = df["crew_hired_s_mean"].iloc[-1]
crew_hired_s_std = df["crew_hired_s_std"].iloc[-1]
crew_hired_s_min = df["crew_hired_s_min"].iloc[-1]
crew_hired_s_max = df["crew_hired_s_max"].iloc[-1]
crew_hired_observation = [
    crew_hired_total, crew_hired_med, crew_hired_mean, crew_hired_std, crew_hired_min, crew_hired_max, crew_hired_s1,
    crew_hired_s2, crew_hired_s3,crew_hired_s4, crew_hired_s5, crew_hired_s6, crew_hired_s7, crew_hired_s8,
    crew_hired_s_med, crew_hired_s_mean, crew_hired_s_std, crew_hired_s_min, crew_hired_s_max,
]

mean_crew_hired_total = mean("crew_hired_total")
mean_crew_hired_med = mean("crew_hired_med")
mean_crew_hired_mean = mean("crew_hired_mean")
mean_crew_hired_std = mean("crew_hired_std")
mean_crew_hired_min = mean("crew_hired_min")
mean_crew_hired_max = mean("crew_hired_max")
mean_crew_hired_s1 = mean("crew_hired_s1")
mean_crew_hired_s2 = mean("crew_hired_s2")
mean_crew_hired_s3 = mean("crew_hired_s3")
mean_crew_hired_s4 = mean("crew_hired_s4")
mean_crew_hired_s5 = mean("crew_hired_s5")
mean_crew_hired_s6 = mean("crew_hired_s6")
mean_crew_hired_s7 = mean("crew_hired_s7")
mean_crew_hired_s8 = mean("crew_hired_s8")
mean_crew_hired_s_med = mean("crew_hired_s_med")
mean_crew_hired_s_mean = mean("crew_hired_s_mean")
mean_crew_hired_s_std = mean("crew_hired_s_std")
mean_crew_hired_s_min = mean("crew_hired_s_min")
mean_crew_hired_s_max = mean("crew_hired_s_max")
mean_crew_hired_observation = [
    mean_crew_hired_total, mean_crew_hired_med, mean_crew_hired_mean, mean_crew_hired_std, mean_crew_hired_min, 
    mean_crew_hired_max, mean_crew_hired_s1, mean_crew_hired_s2, mean_crew_hired_s3, mean_crew_hired_s4,
    mean_crew_hired_s5, mean_crew_hired_s6, mean_crew_hired_s7, mean_crew_hired_s8, mean_crew_hired_s_med,
    mean_crew_hired_s_mean, mean_crew_hired_s_std, mean_crew_hired_s_min, mean_crew_hired_s_max,
]

mean_win_crew_hired_total = locmean("victory", "crew_hired_total")
mean_win_crew_hired_med =  locmean("victory", "crew_hired_med")
mean_win_crew_hired_mean =  locmean("victory", "crew_hired_mean")
mean_win_crew_hired_std =  locmean("victory", "crew_hired_std")
mean_win_crew_hired_min =  locmean("victory", "crew_hired_min")
mean_win_crew_hired_max =  locmean("victory", "crew_hired_max")
mean_win_crew_hired_s1 =  locmean("victory", "crew_hired_s1")
mean_win_crew_hired_s2 =  locmean("victory", "crew_hired_s2")
mean_win_crew_hired_s3 =  locmean("victory", "crew_hired_s3")
mean_win_crew_hired_s4 =  locmean("victory", "crew_hired_s4")
mean_win_crew_hired_s5 =  locmean("victory", "crew_hired_s5")
mean_win_crew_hired_s6 =  locmean("victory", "crew_hired_s6")
mean_win_crew_hired_s7 =  locmean("victory", "crew_hired_s7")
mean_win_crew_hired_s8 =  locmean("victory", "crew_hired_s8")
mean_win_crew_hired_s_med =  locmean("victory", "crew_hired_s_med")
mean_win_crew_hired_s_mean =  locmean("victory", "crew_hired_s_mean")
mean_win_crew_hired_s_std =  locmean("victory", "crew_hired_s_std")
mean_win_crew_hired_s_min =  locmean("victory", "crew_hired_s_min")
mean_win_crew_hired_s_max =  locmean("victory", "crew_hired_s_max")
mean_win_crew_hired_observation = [
    mean_win_crew_hired_total, mean_win_crew_hired_med, mean_win_crew_hired_mean, mean_win_crew_hired_std, mean_win_crew_hired_min, 
    mean_win_crew_hired_max, mean_win_crew_hired_s1, mean_win_crew_hired_s2, mean_win_crew_hired_s3, mean_win_crew_hired_s4,
    mean_win_crew_hired_s5, mean_win_crew_hired_s6, mean_win_crew_hired_s7, mean_win_crew_hired_s8, mean_win_crew_hired_s_med,
    mean_win_crew_hired_s_mean, mean_win_crew_hired_s_std, mean_win_crew_hired_s_min, mean_win_crew_hired_s_max,
]

mean_loss_crew_hired_total = locmean("loss", "crew_hired_total")
mean_loss_crew_hired_med =  locmean("loss", "crew_hired_med")
mean_loss_crew_hired_mean =  locmean("loss", "crew_hired_mean")
mean_loss_crew_hired_std =  locmean("loss", "crew_hired_std")
mean_loss_crew_hired_min =  locmean("loss", "crew_hired_min")
mean_loss_crew_hired_max =  locmean("loss", "crew_hired_max")
mean_loss_crew_hired_s1 =  locmean("loss", "crew_hired_s1")
mean_loss_crew_hired_s2 =  locmean("loss", "crew_hired_s2")
mean_loss_crew_hired_s3 =  locmean("loss", "crew_hired_s3")
mean_loss_crew_hired_s4 =  locmean("loss", "crew_hired_s4")
mean_loss_crew_hired_s5 =  locmean("loss", "crew_hired_s5")
mean_loss_crew_hired_s6 =  locmean("loss", "crew_hired_s6")
mean_loss_crew_hired_s7 =  locmean("loss", "crew_hired_s7")
mean_loss_crew_hired_s8 =  locmean("loss", "crew_hired_s8")
mean_loss_crew_hired_s_med =  locmean("loss", "crew_hired_s_med")
mean_loss_crew_hired_s_mean =  locmean("loss", "crew_hired_s_mean")
mean_loss_crew_hired_s_std =  locmean("loss", "crew_hired_s_std")
mean_loss_crew_hired_s_min =  locmean("loss", "crew_hired_s_min")
mean_loss_crew_hired_s_max =  locmean("loss", "crew_hired_s_max")
mean_loss_crew_hired_observation = [
    mean_loss_crew_hired_total, mean_loss_crew_hired_med, mean_loss_crew_hired_mean, mean_loss_crew_hired_std, mean_loss_crew_hired_min, 
    mean_loss_crew_hired_max, mean_loss_crew_hired_s1, mean_loss_crew_hired_s2, mean_loss_crew_hired_s3, mean_loss_crew_hired_s4,
    mean_loss_crew_hired_s5, mean_loss_crew_hired_s6, mean_loss_crew_hired_s7, mean_loss_crew_hired_s8, mean_loss_crew_hired_s_med,
    mean_loss_crew_hired_s_mean, mean_loss_crew_hired_s_std, mean_loss_crew_hired_s_min, mean_loss_crew_hired_s_max,
]

# crew_lost
crew_lost_total = df["crew_lost_total"].iloc[-1]
crew_lost_med = df["crew_lost_med"].iloc[-1]
crew_lost_mean = df["crew_lost_mean"].iloc[-1]
crew_lost_std = df["crew_lost_std"].iloc[-1]
crew_lost_min = df["crew_lost_min"].iloc[-1]
crew_lost_max = df["crew_lost_max"].iloc[-1]
crew_lost_s1 = df["crew_lost_s1"].iloc[-1]
crew_lost_s2 = df["crew_lost_s2"].iloc[-1]
crew_lost_s3 = df["crew_lost_s3"].iloc[-1]
crew_lost_s4 = df["crew_lost_s4"].iloc[-1]
crew_lost_s5 = df["crew_lost_s5"].iloc[-1]
crew_lost_s6 = df["crew_lost_s6"].iloc[-1]
crew_lost_s7 = df["crew_lost_s7"].iloc[-1]
crew_lost_s8 = df["crew_lost_s8"].iloc[-1]
crew_lost_s_med = df["crew_lost_s_med"].iloc[-1]
crew_lost_s_mean = df["crew_lost_s_mean"].iloc[-1]
crew_lost_s_std = df["crew_lost_s_std"].iloc[-1]
crew_lost_s_min = df["crew_lost_s_min"].iloc[-1]
crew_lost_s_max = df["crew_lost_s_max"].iloc[-1]
crew_lost_observation = [
    crew_lost_total, crew_lost_med, crew_lost_mean, crew_lost_std, crew_lost_min, crew_lost_max, crew_lost_s1,
    crew_lost_s2, crew_lost_s3,crew_lost_s4, crew_lost_s5, crew_lost_s6, crew_lost_s7, crew_lost_s8,
    crew_lost_s_med, crew_lost_s_mean, crew_lost_s_std, crew_lost_s_min, crew_lost_s_max,
]

mean_crew_lost_total = mean("crew_lost_total")
mean_crew_lost_med = mean("crew_lost_med")
mean_crew_lost_mean = mean("crew_lost_mean")
mean_crew_lost_std = mean("crew_lost_std")
mean_crew_lost_min = mean("crew_lost_min")
mean_crew_lost_max = mean("crew_lost_max")
mean_crew_lost_s1 = mean("crew_lost_s1")
mean_crew_lost_s2 = mean("crew_lost_s2")
mean_crew_lost_s3 = mean("crew_lost_s3")
mean_crew_lost_s4 = mean("crew_lost_s4")
mean_crew_lost_s5 = mean("crew_lost_s5")
mean_crew_lost_s6 = mean("crew_lost_s6")
mean_crew_lost_s7 = mean("crew_lost_s7")
mean_crew_lost_s8 = mean("crew_lost_s8")
mean_crew_lost_s_med = mean("crew_lost_s_med")
mean_crew_lost_s_mean = mean("crew_lost_s_mean")
mean_crew_lost_s_std = mean("crew_lost_s_std")
mean_crew_lost_s_min = mean("crew_lost_s_min")
mean_crew_lost_s_max = mean("crew_lost_s_max")
mean_crew_lost_observation = [
    mean_crew_lost_total, mean_crew_lost_med, mean_crew_lost_mean, mean_crew_lost_std, mean_crew_lost_min, 
    mean_crew_lost_max, mean_crew_lost_s1, mean_crew_lost_s2, mean_crew_lost_s3, mean_crew_lost_s4,
    mean_crew_lost_s5, mean_crew_lost_s6, mean_crew_lost_s7, mean_crew_lost_s8, mean_crew_lost_s_med,
    mean_crew_lost_s_mean, mean_crew_lost_s_std, mean_crew_lost_s_min, mean_crew_lost_s_max,
]

mean_win_crew_lost_total = locmean("victory", "crew_lost_total")
mean_win_crew_lost_med =  locmean("victory", "crew_lost_med")
mean_win_crew_lost_mean =  locmean("victory", "crew_lost_mean")
mean_win_crew_lost_std =  locmean("victory", "crew_lost_std")
mean_win_crew_lost_min =  locmean("victory", "crew_lost_min")
mean_win_crew_lost_max =  locmean("victory", "crew_lost_max")
mean_win_crew_lost_s1 =  locmean("victory", "crew_lost_s1")
mean_win_crew_lost_s2 =  locmean("victory", "crew_lost_s2")
mean_win_crew_lost_s3 =  locmean("victory", "crew_lost_s3")
mean_win_crew_lost_s4 =  locmean("victory", "crew_lost_s4")
mean_win_crew_lost_s5 =  locmean("victory", "crew_lost_s5")
mean_win_crew_lost_s6 =  locmean("victory", "crew_lost_s6")
mean_win_crew_lost_s7 =  locmean("victory", "crew_lost_s7")
mean_win_crew_lost_s8 =  locmean("victory", "crew_lost_s8")
mean_win_crew_lost_s_med =  locmean("victory", "crew_lost_s_med")
mean_win_crew_lost_s_mean =  locmean("victory", "crew_lost_s_mean")
mean_win_crew_lost_s_std =  locmean("victory", "crew_lost_s_std")
mean_win_crew_lost_s_min =  locmean("victory", "crew_lost_s_min")
mean_win_crew_lost_s_max =  locmean("victory", "crew_lost_s_max")
mean_win_crew_lost_observation = [
    mean_win_crew_lost_total, mean_win_crew_lost_med, mean_win_crew_lost_mean, mean_win_crew_lost_std, mean_win_crew_lost_min, 
    mean_win_crew_lost_max, mean_win_crew_lost_s1, mean_win_crew_lost_s2, mean_win_crew_lost_s3, mean_win_crew_lost_s4,
    mean_win_crew_lost_s5, mean_win_crew_lost_s6, mean_win_crew_lost_s7, mean_win_crew_lost_s8, mean_win_crew_lost_s_med,
    mean_win_crew_lost_s_mean, mean_win_crew_lost_s_std, mean_win_crew_lost_s_min, mean_win_crew_lost_s_max,
]

mean_loss_crew_lost_total = locmean("loss", "crew_lost_total")
mean_loss_crew_lost_med =  locmean("loss", "crew_lost_med")
mean_loss_crew_lost_mean =  locmean("loss", "crew_lost_mean")
mean_loss_crew_lost_std =  locmean("loss", "crew_lost_std")
mean_loss_crew_lost_min =  locmean("loss", "crew_lost_min")
mean_loss_crew_lost_max =  locmean("loss", "crew_lost_max")
mean_loss_crew_lost_s1 =  locmean("loss", "crew_lost_s1")
mean_loss_crew_lost_s2 =  locmean("loss", "crew_lost_s2")
mean_loss_crew_lost_s3 =  locmean("loss", "crew_lost_s3")
mean_loss_crew_lost_s4 =  locmean("loss", "crew_lost_s4")
mean_loss_crew_lost_s5 =  locmean("loss", "crew_lost_s5")
mean_loss_crew_lost_s6 =  locmean("loss", "crew_lost_s6")
mean_loss_crew_lost_s7 =  locmean("loss", "crew_lost_s7")
mean_loss_crew_lost_s8 =  locmean("loss", "crew_lost_s8")
mean_loss_crew_lost_s_med =  locmean("loss", "crew_lost_s_med")
mean_loss_crew_lost_s_mean =  locmean("loss", "crew_lost_s_mean")
mean_loss_crew_lost_s_std =  locmean("loss", "crew_lost_s_std")
mean_loss_crew_lost_s_min =  locmean("loss", "crew_lost_s_min")
mean_loss_crew_lost_s_max =  locmean("loss", "crew_lost_s_max")
mean_loss_crew_lost_observation = [
    mean_loss_crew_lost_total, mean_loss_crew_lost_med, mean_loss_crew_lost_mean, mean_loss_crew_lost_std, mean_loss_crew_lost_min, 
    mean_loss_crew_lost_max, mean_loss_crew_lost_s1, mean_loss_crew_lost_s2, mean_loss_crew_lost_s3, mean_loss_crew_lost_s4,
    mean_loss_crew_lost_s5, mean_loss_crew_lost_s6, mean_loss_crew_lost_s7, mean_loss_crew_lost_s8, mean_loss_crew_lost_s_med,
    mean_loss_crew_lost_s_mean, mean_loss_crew_lost_s_std, mean_loss_crew_lost_s_min, mean_loss_crew_lost_s_max,
]

# crew_size
crew_size_total = df["crew_size_total"].iloc[-1]
crew_size_med = df["crew_size_med"].iloc[-1]
crew_size_mean = df["crew_size_mean"].iloc[-1]
crew_size_std = df["crew_size_std"].iloc[-1]
crew_size_min = df["crew_size_min"].iloc[-1]
crew_size_max = df["crew_size_max"].iloc[-1]
crew_size_s1 = df["crew_size_s1"].iloc[-1]
crew_size_s2 = df["crew_size_s2"].iloc[-1]
crew_size_s3 = df["crew_size_s3"].iloc[-1]
crew_size_s4 = df["crew_size_s4"].iloc[-1]
crew_size_s5 = df["crew_size_s5"].iloc[-1]
crew_size_s6 = df["crew_size_s6"].iloc[-1]
crew_size_s7 = df["crew_size_s7"].iloc[-1]
crew_size_s8 = df["crew_size_s8"].iloc[-1]
crew_size_s_med = df["crew_size_s_med"].iloc[-1]
crew_size_s_mean = df["crew_size_s_mean"].iloc[-1]
crew_size_s_std = df["crew_size_s_std"].iloc[-1]
crew_size_s_min = df["crew_size_s_min"].iloc[-1]
crew_size_s_max = df["crew_size_s_max"].iloc[-1]
crew_size_observation = [
    crew_size_total, crew_size_med, crew_size_mean, crew_size_std, crew_size_min, crew_size_max, crew_size_s1,
    crew_size_s2, crew_size_s3,crew_size_s4, crew_size_s5, crew_size_s6, crew_size_s7, crew_size_s8,
    crew_size_s_med, crew_size_s_mean, crew_size_s_std, crew_size_s_min, crew_size_s_max,
]

mean_crew_size_total = mean("crew_size_total")
mean_crew_size_med = mean("crew_size_med")
mean_crew_size_mean = mean("crew_size_mean")
mean_crew_size_std = mean("crew_size_std")
mean_crew_size_min = mean("crew_size_min")
mean_crew_size_max = mean("crew_size_max")
mean_crew_size_s1 = mean("crew_size_s1")
mean_crew_size_s2 = mean("crew_size_s2")
mean_crew_size_s3 = mean("crew_size_s3")
mean_crew_size_s4 = mean("crew_size_s4")
mean_crew_size_s5 = mean("crew_size_s5")
mean_crew_size_s6 = mean("crew_size_s6")
mean_crew_size_s7 = mean("crew_size_s7")
mean_crew_size_s8 = mean("crew_size_s8")
mean_crew_size_s_med = mean("crew_size_s_med")
mean_crew_size_s_mean = mean("crew_size_s_mean")
mean_crew_size_s_std = mean("crew_size_s_std")
mean_crew_size_s_min = mean("crew_size_s_min")
mean_crew_size_s_max = mean("crew_size_s_max")
mean_crew_size_observation = [
    mean_crew_size_total, mean_crew_size_med, mean_crew_size_mean, mean_crew_size_std, mean_crew_size_min, 
    mean_crew_size_max, mean_crew_size_s1, mean_crew_size_s2, mean_crew_size_s3, mean_crew_size_s4,
    mean_crew_size_s5, mean_crew_size_s6, mean_crew_size_s7, mean_crew_size_s8, mean_crew_size_s_med,
    mean_crew_size_s_mean, mean_crew_size_s_std, mean_crew_size_s_min, mean_crew_size_s_max,
]

mean_win_crew_size_total = locmean("victory", "crew_size_total")
mean_win_crew_size_med =  locmean("victory", "crew_size_med")
mean_win_crew_size_mean =  locmean("victory", "crew_size_mean")
mean_win_crew_size_std =  locmean("victory", "crew_size_std")
mean_win_crew_size_min =  locmean("victory", "crew_size_min")
mean_win_crew_size_max =  locmean("victory", "crew_size_max")
mean_win_crew_size_s1 =  locmean("victory", "crew_size_s1")
mean_win_crew_size_s2 =  locmean("victory", "crew_size_s2")
mean_win_crew_size_s3 =  locmean("victory", "crew_size_s3")
mean_win_crew_size_s4 =  locmean("victory", "crew_size_s4")
mean_win_crew_size_s5 =  locmean("victory", "crew_size_s5")
mean_win_crew_size_s6 =  locmean("victory", "crew_size_s6")
mean_win_crew_size_s7 =  locmean("victory", "crew_size_s7")
mean_win_crew_size_s8 =  locmean("victory", "crew_size_s8")
mean_win_crew_size_s_med =  locmean("victory", "crew_size_s_med")
mean_win_crew_size_s_mean =  locmean("victory", "crew_size_s_mean")
mean_win_crew_size_s_std =  locmean("victory", "crew_size_s_std")
mean_win_crew_size_s_min =  locmean("victory", "crew_size_s_min")
mean_win_crew_size_s_max =  locmean("victory", "crew_size_s_max")
mean_win_crew_size_observation = [
    mean_win_crew_size_total, mean_win_crew_size_med, mean_win_crew_size_mean, mean_win_crew_size_std, mean_win_crew_size_min, 
    mean_win_crew_size_max, mean_win_crew_size_s1, mean_win_crew_size_s2, mean_win_crew_size_s3, mean_win_crew_size_s4,
    mean_win_crew_size_s5, mean_win_crew_size_s6, mean_win_crew_size_s7, mean_win_crew_size_s8, mean_win_crew_size_s_med,
    mean_win_crew_size_s_mean, mean_win_crew_size_s_std, mean_win_crew_size_s_min, mean_win_crew_size_s_max,
]

mean_loss_crew_size_total = locmean("loss", "crew_size_total")
mean_loss_crew_size_med =  locmean("loss", "crew_size_med")
mean_loss_crew_size_mean =  locmean("loss", "crew_size_mean")
mean_loss_crew_size_std =  locmean("loss", "crew_size_std")
mean_loss_crew_size_min =  locmean("loss", "crew_size_min")
mean_loss_crew_size_max =  locmean("loss", "crew_size_max")
mean_loss_crew_size_s1 =  locmean("loss", "crew_size_s1")
mean_loss_crew_size_s2 =  locmean("loss", "crew_size_s2")
mean_loss_crew_size_s3 =  locmean("loss", "crew_size_s3")
mean_loss_crew_size_s4 =  locmean("loss", "crew_size_s4")
mean_loss_crew_size_s5 =  locmean("loss", "crew_size_s5")
mean_loss_crew_size_s6 =  locmean("loss", "crew_size_s6")
mean_loss_crew_size_s7 =  locmean("loss", "crew_size_s7")
mean_loss_crew_size_s8 =  locmean("loss", "crew_size_s8")
mean_loss_crew_size_s_med =  locmean("loss", "crew_size_s_med")
mean_loss_crew_size_s_mean =  locmean("loss", "crew_size_s_mean")
mean_loss_crew_size_s_std =  locmean("loss", "crew_size_s_std")
mean_loss_crew_size_s_min =  locmean("loss", "crew_size_s_min")
mean_loss_crew_size_s_max =  locmean("loss", "crew_size_s_max")
mean_loss_crew_size_observation = [
    mean_loss_crew_size_total, mean_loss_crew_size_med, mean_loss_crew_size_mean, mean_loss_crew_size_std, mean_loss_crew_size_min, 
    mean_loss_crew_size_max, mean_loss_crew_size_s1, mean_loss_crew_size_s2, mean_loss_crew_size_s3, mean_loss_crew_size_s4,
    mean_loss_crew_size_s5, mean_loss_crew_size_s6, mean_loss_crew_size_s7, mean_loss_crew_size_s8, mean_loss_crew_size_s_med,
    mean_loss_crew_size_s_mean, mean_loss_crew_size_s_std, mean_loss_crew_size_s_min, mean_loss_crew_size_s_max,
]

# power_capacity
power_capacity_total = df["power_capacity_total"].iloc[-1]
power_capacity_med = df["power_capacity_med"].iloc[-1]
power_capacity_mean = df["power_capacity_mean"].iloc[-1]
power_capacity_std = df["power_capacity_std"].iloc[-1]
power_capacity_min = df["power_capacity_min"].iloc[-1]
power_capacity_max = df["power_capacity_max"].iloc[-1]
power_capacity_s1 = df["power_capacity_s1"].iloc[-1]
power_capacity_s2 = df["power_capacity_s2"].iloc[-1]
power_capacity_s3 = df["power_capacity_s3"].iloc[-1]
power_capacity_s4 = df["power_capacity_s4"].iloc[-1]
power_capacity_s5 = df["power_capacity_s5"].iloc[-1]
power_capacity_s6 = df["power_capacity_s6"].iloc[-1]
power_capacity_s7 = df["power_capacity_s7"].iloc[-1]
power_capacity_s8 = df["power_capacity_s8"].iloc[-1]
power_capacity_s_med = df["power_capacity_s_med"].iloc[-1]
power_capacity_s_mean = df["power_capacity_s_mean"].iloc[-1]
power_capacity_s_std = df["power_capacity_s_std"].iloc[-1]
power_capacity_s_min = df["power_capacity_s_min"].iloc[-1]
power_capacity_s_max = df["power_capacity_s_max"].iloc[-1]
power_capacity_observation = [
    power_capacity_total, power_capacity_med, power_capacity_mean, power_capacity_std, power_capacity_min, power_capacity_max, power_capacity_s1,
    power_capacity_s2, power_capacity_s3,power_capacity_s4, power_capacity_s5, power_capacity_s6, power_capacity_s7, power_capacity_s8,
    power_capacity_s_med, power_capacity_s_mean, power_capacity_s_std, power_capacity_s_min, power_capacity_s_max,
]

mean_power_capacity_total = mean("power_capacity_total")
mean_power_capacity_med = mean("power_capacity_med")
mean_power_capacity_mean = mean("power_capacity_mean")
mean_power_capacity_std = mean("power_capacity_std")
mean_power_capacity_min = mean("power_capacity_min")
mean_power_capacity_max = mean("power_capacity_max")
mean_power_capacity_s1 = mean("power_capacity_s1")
mean_power_capacity_s2 = mean("power_capacity_s2")
mean_power_capacity_s3 = mean("power_capacity_s3")
mean_power_capacity_s4 = mean("power_capacity_s4")
mean_power_capacity_s5 = mean("power_capacity_s5")
mean_power_capacity_s6 = mean("power_capacity_s6")
mean_power_capacity_s7 = mean("power_capacity_s7")
mean_power_capacity_s8 = mean("power_capacity_s8")
mean_power_capacity_s_med = mean("power_capacity_s_med")
mean_power_capacity_s_mean = mean("power_capacity_s_mean")
mean_power_capacity_s_std = mean("power_capacity_s_std")
mean_power_capacity_s_min = mean("power_capacity_s_min")
mean_power_capacity_s_max = mean("power_capacity_s_max")
mean_power_capacity_observation = [
    mean_power_capacity_total, mean_power_capacity_med, mean_power_capacity_mean, mean_power_capacity_std, mean_power_capacity_min, 
    mean_power_capacity_max, mean_power_capacity_s1, mean_power_capacity_s2, mean_power_capacity_s3, mean_power_capacity_s4,
    mean_power_capacity_s5, mean_power_capacity_s6, mean_power_capacity_s7, mean_power_capacity_s8, mean_power_capacity_s_med,
    mean_power_capacity_s_mean, mean_power_capacity_s_std, mean_power_capacity_s_min, mean_power_capacity_s_max,
]

mean_win_power_capacity_total = locmean("victory", "power_capacity_total")
mean_win_power_capacity_med =  locmean("victory", "power_capacity_med")
mean_win_power_capacity_mean =  locmean("victory", "power_capacity_mean")
mean_win_power_capacity_std =  locmean("victory", "power_capacity_std")
mean_win_power_capacity_min =  locmean("victory", "power_capacity_min")
mean_win_power_capacity_max =  locmean("victory", "power_capacity_max")
mean_win_power_capacity_s1 =  locmean("victory", "power_capacity_s1")
mean_win_power_capacity_s2 =  locmean("victory", "power_capacity_s2")
mean_win_power_capacity_s3 =  locmean("victory", "power_capacity_s3")
mean_win_power_capacity_s4 =  locmean("victory", "power_capacity_s4")
mean_win_power_capacity_s5 =  locmean("victory", "power_capacity_s5")
mean_win_power_capacity_s6 =  locmean("victory", "power_capacity_s6")
mean_win_power_capacity_s7 =  locmean("victory", "power_capacity_s7")
mean_win_power_capacity_s8 =  locmean("victory", "power_capacity_s8")
mean_win_power_capacity_s_med =  locmean("victory", "power_capacity_s_med")
mean_win_power_capacity_s_mean =  locmean("victory", "power_capacity_s_mean")
mean_win_power_capacity_s_std =  locmean("victory", "power_capacity_s_std")
mean_win_power_capacity_s_min =  locmean("victory", "power_capacity_s_min")
mean_win_power_capacity_s_max =  locmean("victory", "power_capacity_s_max")
mean_win_power_capacity_observation = [
    mean_win_power_capacity_total, mean_win_power_capacity_med, mean_win_power_capacity_mean, mean_win_power_capacity_std, mean_win_power_capacity_min, 
    mean_win_power_capacity_max, mean_win_power_capacity_s1, mean_win_power_capacity_s2, mean_win_power_capacity_s3, mean_win_power_capacity_s4,
    mean_win_power_capacity_s5, mean_win_power_capacity_s6, mean_win_power_capacity_s7, mean_win_power_capacity_s8, mean_win_power_capacity_s_med,
    mean_win_power_capacity_s_mean, mean_win_power_capacity_s_std, mean_win_power_capacity_s_min, mean_win_power_capacity_s_max,
]

mean_loss_power_capacity_total = locmean("loss", "power_capacity_total")
mean_loss_power_capacity_med =  locmean("loss", "power_capacity_med")
mean_loss_power_capacity_mean =  locmean("loss", "power_capacity_mean")
mean_loss_power_capacity_std =  locmean("loss", "power_capacity_std")
mean_loss_power_capacity_min =  locmean("loss", "power_capacity_min")
mean_loss_power_capacity_max =  locmean("loss", "power_capacity_max")
mean_loss_power_capacity_s1 =  locmean("loss", "power_capacity_s1")
mean_loss_power_capacity_s2 =  locmean("loss", "power_capacity_s2")
mean_loss_power_capacity_s3 =  locmean("loss", "power_capacity_s3")
mean_loss_power_capacity_s4 =  locmean("loss", "power_capacity_s4")
mean_loss_power_capacity_s5 =  locmean("loss", "power_capacity_s5")
mean_loss_power_capacity_s6 =  locmean("loss", "power_capacity_s6")
mean_loss_power_capacity_s7 =  locmean("loss", "power_capacity_s7")
mean_loss_power_capacity_s8 =  locmean("loss", "power_capacity_s8")
mean_loss_power_capacity_s_med =  locmean("loss", "power_capacity_s_med")
mean_loss_power_capacity_s_mean =  locmean("loss", "power_capacity_s_mean")
mean_loss_power_capacity_s_std =  locmean("loss", "power_capacity_s_std")
mean_loss_power_capacity_s_min =  locmean("loss", "power_capacity_s_min")
mean_loss_power_capacity_s_max =  locmean("loss", "power_capacity_s_max")
mean_loss_power_capacity_observation = [
    mean_loss_power_capacity_total, mean_loss_power_capacity_med, mean_loss_power_capacity_mean, mean_loss_power_capacity_std, mean_loss_power_capacity_min, 
    mean_loss_power_capacity_max, mean_loss_power_capacity_s1, mean_loss_power_capacity_s2, mean_loss_power_capacity_s3, mean_loss_power_capacity_s4,
    mean_loss_power_capacity_s5, mean_loss_power_capacity_s6, mean_loss_power_capacity_s7, mean_loss_power_capacity_s8, mean_loss_power_capacity_s_med,
    mean_loss_power_capacity_s_mean, mean_loss_power_capacity_s_std, mean_loss_power_capacity_s_min, mean_loss_power_capacity_s_max,
]

# weapons_capacity
weapons_capacity_total = df["weapons_capacity_total"].iloc[-1]
weapons_capacity_med = df["weapons_capacity_med"].iloc[-1]
weapons_capacity_mean = df["weapons_capacity_mean"].iloc[-1]
weapons_capacity_std = df["weapons_capacity_std"].iloc[-1]
weapons_capacity_min = df["weapons_capacity_min"].iloc[-1]
weapons_capacity_max = df["weapons_capacity_max"].iloc[-1]
weapons_capacity_s1 = df["weapons_capacity_s1"].iloc[-1]
weapons_capacity_s2 = df["weapons_capacity_s2"].iloc[-1]
weapons_capacity_s3 = df["weapons_capacity_s3"].iloc[-1]
weapons_capacity_s4 = df["weapons_capacity_s4"].iloc[-1]
weapons_capacity_s5 = df["weapons_capacity_s5"].iloc[-1]
weapons_capacity_s6 = df["weapons_capacity_s6"].iloc[-1]
weapons_capacity_s7 = df["weapons_capacity_s7"].iloc[-1]
weapons_capacity_s8 = df["weapons_capacity_s8"].iloc[-1]
weapons_capacity_s_med = df["weapons_capacity_s_med"].iloc[-1]
weapons_capacity_s_mean = df["weapons_capacity_s_mean"].iloc[-1]
weapons_capacity_s_std = df["weapons_capacity_s_std"].iloc[-1]
weapons_capacity_s_min = df["weapons_capacity_s_min"].iloc[-1]
weapons_capacity_s_max = df["weapons_capacity_s_max"].iloc[-1]
weapons_capacity_observation = [
    weapons_capacity_total, weapons_capacity_med, weapons_capacity_mean, weapons_capacity_std, weapons_capacity_min, weapons_capacity_max, weapons_capacity_s1,
    weapons_capacity_s2, weapons_capacity_s3,weapons_capacity_s4, weapons_capacity_s5, weapons_capacity_s6, weapons_capacity_s7, weapons_capacity_s8,
    weapons_capacity_s_med, weapons_capacity_s_mean, weapons_capacity_s_std, weapons_capacity_s_min, weapons_capacity_s_max,
]

mean_weapons_capacity_total = mean("weapons_capacity_total")
mean_weapons_capacity_med = mean("weapons_capacity_med")
mean_weapons_capacity_mean = mean("weapons_capacity_mean")
mean_weapons_capacity_std = mean("weapons_capacity_std")
mean_weapons_capacity_min = mean("weapons_capacity_min")
mean_weapons_capacity_max = mean("weapons_capacity_max")
mean_weapons_capacity_s1 = mean("weapons_capacity_s1")
mean_weapons_capacity_s2 = mean("weapons_capacity_s2")
mean_weapons_capacity_s3 = mean("weapons_capacity_s3")
mean_weapons_capacity_s4 = mean("weapons_capacity_s4")
mean_weapons_capacity_s5 = mean("weapons_capacity_s5")
mean_weapons_capacity_s6 = mean("weapons_capacity_s6")
mean_weapons_capacity_s7 = mean("weapons_capacity_s7")
mean_weapons_capacity_s8 = mean("weapons_capacity_s8")
mean_weapons_capacity_s_med = mean("weapons_capacity_s_med")
mean_weapons_capacity_s_mean = mean("weapons_capacity_s_mean")
mean_weapons_capacity_s_std = mean("weapons_capacity_s_std")
mean_weapons_capacity_s_min = mean("weapons_capacity_s_min")
mean_weapons_capacity_s_max = mean("weapons_capacity_s_max")
mean_weapons_capacity_observation = [
    mean_weapons_capacity_total, mean_weapons_capacity_med, mean_weapons_capacity_mean, mean_weapons_capacity_std, mean_weapons_capacity_min, 
    mean_weapons_capacity_max, mean_weapons_capacity_s1, mean_weapons_capacity_s2, mean_weapons_capacity_s3, mean_weapons_capacity_s4,
    mean_weapons_capacity_s5, mean_weapons_capacity_s6, mean_weapons_capacity_s7, mean_weapons_capacity_s8, mean_weapons_capacity_s_med,
    mean_weapons_capacity_s_mean, mean_weapons_capacity_s_std, mean_weapons_capacity_s_min, mean_weapons_capacity_s_max,
]

mean_win_weapons_capacity_total = locmean("victory", "weapons_capacity_total")
mean_win_weapons_capacity_med =  locmean("victory", "weapons_capacity_med")
mean_win_weapons_capacity_mean =  locmean("victory", "weapons_capacity_mean")
mean_win_weapons_capacity_std =  locmean("victory", "weapons_capacity_std")
mean_win_weapons_capacity_min =  locmean("victory", "weapons_capacity_min")
mean_win_weapons_capacity_max =  locmean("victory", "weapons_capacity_max")
mean_win_weapons_capacity_s1 =  locmean("victory", "weapons_capacity_s1")
mean_win_weapons_capacity_s2 =  locmean("victory", "weapons_capacity_s2")
mean_win_weapons_capacity_s3 =  locmean("victory", "weapons_capacity_s3")
mean_win_weapons_capacity_s4 =  locmean("victory", "weapons_capacity_s4")
mean_win_weapons_capacity_s5 =  locmean("victory", "weapons_capacity_s5")
mean_win_weapons_capacity_s6 =  locmean("victory", "weapons_capacity_s6")
mean_win_weapons_capacity_s7 =  locmean("victory", "weapons_capacity_s7")
mean_win_weapons_capacity_s8 =  locmean("victory", "weapons_capacity_s8")
mean_win_weapons_capacity_s_med =  locmean("victory", "weapons_capacity_s_med")
mean_win_weapons_capacity_s_mean =  locmean("victory", "weapons_capacity_s_mean")
mean_win_weapons_capacity_s_std =  locmean("victory", "weapons_capacity_s_std")
mean_win_weapons_capacity_s_min =  locmean("victory", "weapons_capacity_s_min")
mean_win_weapons_capacity_s_max =  locmean("victory", "weapons_capacity_s_max")
mean_win_weapons_capacity_observation = [
    mean_win_weapons_capacity_total, mean_win_weapons_capacity_med, mean_win_weapons_capacity_mean, mean_win_weapons_capacity_std, mean_win_weapons_capacity_min, 
    mean_win_weapons_capacity_max, mean_win_weapons_capacity_s1, mean_win_weapons_capacity_s2, mean_win_weapons_capacity_s3, mean_win_weapons_capacity_s4,
    mean_win_weapons_capacity_s5, mean_win_weapons_capacity_s6, mean_win_weapons_capacity_s7, mean_win_weapons_capacity_s8, mean_win_weapons_capacity_s_med,
    mean_win_weapons_capacity_s_mean, mean_win_weapons_capacity_s_std, mean_win_weapons_capacity_s_min, mean_win_weapons_capacity_s_max,
]

mean_loss_weapons_capacity_total = locmean("loss", "weapons_capacity_total")
mean_loss_weapons_capacity_med =  locmean("loss", "weapons_capacity_med")
mean_loss_weapons_capacity_mean =  locmean("loss", "weapons_capacity_mean")
mean_loss_weapons_capacity_std =  locmean("loss", "weapons_capacity_std")
mean_loss_weapons_capacity_min =  locmean("loss", "weapons_capacity_min")
mean_loss_weapons_capacity_max =  locmean("loss", "weapons_capacity_max")
mean_loss_weapons_capacity_s1 =  locmean("loss", "weapons_capacity_s1")
mean_loss_weapons_capacity_s2 =  locmean("loss", "weapons_capacity_s2")
mean_loss_weapons_capacity_s3 =  locmean("loss", "weapons_capacity_s3")
mean_loss_weapons_capacity_s4 =  locmean("loss", "weapons_capacity_s4")
mean_loss_weapons_capacity_s5 =  locmean("loss", "weapons_capacity_s5")
mean_loss_weapons_capacity_s6 =  locmean("loss", "weapons_capacity_s6")
mean_loss_weapons_capacity_s7 =  locmean("loss", "weapons_capacity_s7")
mean_loss_weapons_capacity_s8 =  locmean("loss", "weapons_capacity_s8")
mean_loss_weapons_capacity_s_med =  locmean("loss", "weapons_capacity_s_med")
mean_loss_weapons_capacity_s_mean =  locmean("loss", "weapons_capacity_s_mean")
mean_loss_weapons_capacity_s_std =  locmean("loss", "weapons_capacity_s_std")
mean_loss_weapons_capacity_s_min =  locmean("loss", "weapons_capacity_s_min")
mean_loss_weapons_capacity_s_max =  locmean("loss", "weapons_capacity_s_max")
mean_loss_weapons_capacity_observation = [
    mean_loss_weapons_capacity_total, mean_loss_weapons_capacity_med, mean_loss_weapons_capacity_mean, mean_loss_weapons_capacity_std, mean_loss_weapons_capacity_min, 
    mean_loss_weapons_capacity_max, mean_loss_weapons_capacity_s1, mean_loss_weapons_capacity_s2, mean_loss_weapons_capacity_s3, mean_loss_weapons_capacity_s4,
    mean_loss_weapons_capacity_s5, mean_loss_weapons_capacity_s6, mean_loss_weapons_capacity_s7, mean_loss_weapons_capacity_s8, mean_loss_weapons_capacity_s_med,
    mean_loss_weapons_capacity_s_mean, mean_loss_weapons_capacity_s_std, mean_loss_weapons_capacity_s_min, mean_loss_weapons_capacity_s_max,
]

# engines_capacity
engines_capacity_total = df["engines_capacity_total"].iloc[-1]
engines_capacity_med = df["engines_capacity_med"].iloc[-1]
engines_capacity_mean = df["engines_capacity_mean"].iloc[-1]
engines_capacity_std = df["engines_capacity_std"].iloc[-1]
engines_capacity_min = df["engines_capacity_min"].iloc[-1]
engines_capacity_max = df["engines_capacity_max"].iloc[-1]
engines_capacity_s1 = df["engines_capacity_s1"].iloc[-1]
engines_capacity_s2 = df["engines_capacity_s2"].iloc[-1]
engines_capacity_s3 = df["engines_capacity_s3"].iloc[-1]
engines_capacity_s4 = df["engines_capacity_s4"].iloc[-1]
engines_capacity_s5 = df["engines_capacity_s5"].iloc[-1]
engines_capacity_s6 = df["engines_capacity_s6"].iloc[-1]
engines_capacity_s7 = df["engines_capacity_s7"].iloc[-1]
engines_capacity_s8 = df["engines_capacity_s8"].iloc[-1]
engines_capacity_s_med = df["engines_capacity_s_med"].iloc[-1]
engines_capacity_s_mean = df["engines_capacity_s_mean"].iloc[-1]
engines_capacity_s_std = df["engines_capacity_s_std"].iloc[-1]
engines_capacity_s_min = df["engines_capacity_s_min"].iloc[-1]
engines_capacity_s_max = df["engines_capacity_s_max"].iloc[-1]
engines_capacity_observation = [
    engines_capacity_total, engines_capacity_med, engines_capacity_mean, engines_capacity_std, engines_capacity_min, engines_capacity_max, engines_capacity_s1,
    engines_capacity_s2, engines_capacity_s3,engines_capacity_s4, engines_capacity_s5, engines_capacity_s6, engines_capacity_s7, engines_capacity_s8,
    engines_capacity_s_med, engines_capacity_s_mean, engines_capacity_s_std, engines_capacity_s_min, engines_capacity_s_max,
]

mean_engines_capacity_total = mean("engines_capacity_total")
mean_engines_capacity_med = mean("engines_capacity_med")
mean_engines_capacity_mean = mean("engines_capacity_mean")
mean_engines_capacity_std = mean("engines_capacity_std")
mean_engines_capacity_min = mean("engines_capacity_min")
mean_engines_capacity_max = mean("engines_capacity_max")
mean_engines_capacity_s1 = mean("engines_capacity_s1")
mean_engines_capacity_s2 = mean("engines_capacity_s2")
mean_engines_capacity_s3 = mean("engines_capacity_s3")
mean_engines_capacity_s4 = mean("engines_capacity_s4")
mean_engines_capacity_s5 = mean("engines_capacity_s5")
mean_engines_capacity_s6 = mean("engines_capacity_s6")
mean_engines_capacity_s7 = mean("engines_capacity_s7")
mean_engines_capacity_s8 = mean("engines_capacity_s8")
mean_engines_capacity_s_med = mean("engines_capacity_s_med")
mean_engines_capacity_s_mean = mean("engines_capacity_s_mean")
mean_engines_capacity_s_std = mean("engines_capacity_s_std")
mean_engines_capacity_s_min = mean("engines_capacity_s_min")
mean_engines_capacity_s_max = mean("engines_capacity_s_max")
mean_engines_capacity_observation = [
    mean_engines_capacity_total, mean_engines_capacity_med, mean_engines_capacity_mean, mean_engines_capacity_std, mean_engines_capacity_min, 
    mean_engines_capacity_max, mean_engines_capacity_s1, mean_engines_capacity_s2, mean_engines_capacity_s3, mean_engines_capacity_s4,
    mean_engines_capacity_s5, mean_engines_capacity_s6, mean_engines_capacity_s7, mean_engines_capacity_s8, mean_engines_capacity_s_med,
    mean_engines_capacity_s_mean, mean_engines_capacity_s_std, mean_engines_capacity_s_min, mean_engines_capacity_s_max,
]

mean_win_engines_capacity_total = locmean("victory", "engines_capacity_total")
mean_win_engines_capacity_med =  locmean("victory", "engines_capacity_med")
mean_win_engines_capacity_mean =  locmean("victory", "engines_capacity_mean")
mean_win_engines_capacity_std =  locmean("victory", "engines_capacity_std")
mean_win_engines_capacity_min =  locmean("victory", "engines_capacity_min")
mean_win_engines_capacity_max =  locmean("victory", "engines_capacity_max")
mean_win_engines_capacity_s1 =  locmean("victory", "engines_capacity_s1")
mean_win_engines_capacity_s2 =  locmean("victory", "engines_capacity_s2")
mean_win_engines_capacity_s3 =  locmean("victory", "engines_capacity_s3")
mean_win_engines_capacity_s4 =  locmean("victory", "engines_capacity_s4")
mean_win_engines_capacity_s5 =  locmean("victory", "engines_capacity_s5")
mean_win_engines_capacity_s6 =  locmean("victory", "engines_capacity_s6")
mean_win_engines_capacity_s7 =  locmean("victory", "engines_capacity_s7")
mean_win_engines_capacity_s8 =  locmean("victory", "engines_capacity_s8")
mean_win_engines_capacity_s_med =  locmean("victory", "engines_capacity_s_med")
mean_win_engines_capacity_s_mean =  locmean("victory", "engines_capacity_s_mean")
mean_win_engines_capacity_s_std =  locmean("victory", "engines_capacity_s_std")
mean_win_engines_capacity_s_min =  locmean("victory", "engines_capacity_s_min")
mean_win_engines_capacity_s_max =  locmean("victory", "engines_capacity_s_max")
mean_win_engines_capacity_observation = [
    mean_win_engines_capacity_total, mean_win_engines_capacity_med, mean_win_engines_capacity_mean, mean_win_engines_capacity_std, mean_win_engines_capacity_min, 
    mean_win_engines_capacity_max, mean_win_engines_capacity_s1, mean_win_engines_capacity_s2, mean_win_engines_capacity_s3, mean_win_engines_capacity_s4,
    mean_win_engines_capacity_s5, mean_win_engines_capacity_s6, mean_win_engines_capacity_s7, mean_win_engines_capacity_s8, mean_win_engines_capacity_s_med,
    mean_win_engines_capacity_s_mean, mean_win_engines_capacity_s_std, mean_win_engines_capacity_s_min, mean_win_engines_capacity_s_max,
]

mean_loss_engines_capacity_total = locmean("loss", "engines_capacity_total")
mean_loss_engines_capacity_med =  locmean("loss", "engines_capacity_med")
mean_loss_engines_capacity_mean =  locmean("loss", "engines_capacity_mean")
mean_loss_engines_capacity_std =  locmean("loss", "engines_capacity_std")
mean_loss_engines_capacity_min =  locmean("loss", "engines_capacity_min")
mean_loss_engines_capacity_max =  locmean("loss", "engines_capacity_max")
mean_loss_engines_capacity_s1 =  locmean("loss", "engines_capacity_s1")
mean_loss_engines_capacity_s2 =  locmean("loss", "engines_capacity_s2")
mean_loss_engines_capacity_s3 =  locmean("loss", "engines_capacity_s3")
mean_loss_engines_capacity_s4 =  locmean("loss", "engines_capacity_s4")
mean_loss_engines_capacity_s5 =  locmean("loss", "engines_capacity_s5")
mean_loss_engines_capacity_s6 =  locmean("loss", "engines_capacity_s6")
mean_loss_engines_capacity_s7 =  locmean("loss", "engines_capacity_s7")
mean_loss_engines_capacity_s8 =  locmean("loss", "engines_capacity_s8")
mean_loss_engines_capacity_s_med =  locmean("loss", "engines_capacity_s_med")
mean_loss_engines_capacity_s_mean =  locmean("loss", "engines_capacity_s_mean")
mean_loss_engines_capacity_s_std =  locmean("loss", "engines_capacity_s_std")
mean_loss_engines_capacity_s_min =  locmean("loss", "engines_capacity_s_min")
mean_loss_engines_capacity_s_max =  locmean("loss", "engines_capacity_s_max")
mean_loss_engines_capacity_observation = [
    mean_loss_engines_capacity_total, mean_loss_engines_capacity_med, mean_loss_engines_capacity_mean, mean_loss_engines_capacity_std, mean_loss_engines_capacity_min, 
    mean_loss_engines_capacity_max, mean_loss_engines_capacity_s1, mean_loss_engines_capacity_s2, mean_loss_engines_capacity_s3, mean_loss_engines_capacity_s4,
    mean_loss_engines_capacity_s5, mean_loss_engines_capacity_s6, mean_loss_engines_capacity_s7, mean_loss_engines_capacity_s8, mean_loss_engines_capacity_s_med,
    mean_loss_engines_capacity_s_mean, mean_loss_engines_capacity_s_std, mean_loss_engines_capacity_s_min, mean_loss_engines_capacity_s_max,
]

# shields_capacity
shields_capacity_total = df["shields_capacity_total"].iloc[-1]
shields_capacity_med = df["shields_capacity_med"].iloc[-1]
shields_capacity_mean = df["shields_capacity_mean"].iloc[-1]
shields_capacity_std = df["shields_capacity_std"].iloc[-1]
shields_capacity_min = df["shields_capacity_min"].iloc[-1]
shields_capacity_max = df["shields_capacity_max"].iloc[-1]
shields_capacity_s1 = df["shields_capacity_s1"].iloc[-1]
shields_capacity_s2 = df["shields_capacity_s2"].iloc[-1]
shields_capacity_s3 = df["shields_capacity_s3"].iloc[-1]
shields_capacity_s4 = df["shields_capacity_s4"].iloc[-1]
shields_capacity_s5 = df["shields_capacity_s5"].iloc[-1]
shields_capacity_s6 = df["shields_capacity_s6"].iloc[-1]
shields_capacity_s7 = df["shields_capacity_s7"].iloc[-1]
shields_capacity_s8 = df["shields_capacity_s8"].iloc[-1]
shields_capacity_s_med = df["shields_capacity_s_med"].iloc[-1]
shields_capacity_s_mean = df["shields_capacity_s_mean"].iloc[-1]
shields_capacity_s_std = df["shields_capacity_s_std"].iloc[-1]
shields_capacity_s_min = df["shields_capacity_s_min"].iloc[-1]
shields_capacity_s_max = df["shields_capacity_s_max"].iloc[-1]
shields_capacity_observation = [
    shields_capacity_total, shields_capacity_med, shields_capacity_mean, shields_capacity_std, shields_capacity_min, shields_capacity_max, shields_capacity_s1,
    shields_capacity_s2, shields_capacity_s3,shields_capacity_s4, shields_capacity_s5, shields_capacity_s6, shields_capacity_s7, shields_capacity_s8,
    shields_capacity_s_med, shields_capacity_s_mean, shields_capacity_s_std, shields_capacity_s_min, shields_capacity_s_max,
]

mean_shields_capacity_total = mean("shields_capacity_total")
mean_shields_capacity_med = mean("shields_capacity_med")
mean_shields_capacity_mean = mean("shields_capacity_mean")
mean_shields_capacity_std = mean("shields_capacity_std")
mean_shields_capacity_min = mean("shields_capacity_min")
mean_shields_capacity_max = mean("shields_capacity_max")
mean_shields_capacity_s1 = mean("shields_capacity_s1")
mean_shields_capacity_s2 = mean("shields_capacity_s2")
mean_shields_capacity_s3 = mean("shields_capacity_s3")
mean_shields_capacity_s4 = mean("shields_capacity_s4")
mean_shields_capacity_s5 = mean("shields_capacity_s5")
mean_shields_capacity_s6 = mean("shields_capacity_s6")
mean_shields_capacity_s7 = mean("shields_capacity_s7")
mean_shields_capacity_s8 = mean("shields_capacity_s8")
mean_shields_capacity_s_med = mean("shields_capacity_s_med")
mean_shields_capacity_s_mean = mean("shields_capacity_s_mean")
mean_shields_capacity_s_std = mean("shields_capacity_s_std")
mean_shields_capacity_s_min = mean("shields_capacity_s_min")
mean_shields_capacity_s_max = mean("shields_capacity_s_max")
mean_shields_capacity_observation = [
    mean_shields_capacity_total, mean_shields_capacity_med, mean_shields_capacity_mean, mean_shields_capacity_std, mean_shields_capacity_min, 
    mean_shields_capacity_max, mean_shields_capacity_s1, mean_shields_capacity_s2, mean_shields_capacity_s3, mean_shields_capacity_s4,
    mean_shields_capacity_s5, mean_shields_capacity_s6, mean_shields_capacity_s7, mean_shields_capacity_s8, mean_shields_capacity_s_med,
    mean_shields_capacity_s_mean, mean_shields_capacity_s_std, mean_shields_capacity_s_min, mean_shields_capacity_s_max,
]

mean_win_shields_capacity_total = locmean("victory", "shields_capacity_total")
mean_win_shields_capacity_med =  locmean("victory", "shields_capacity_med")
mean_win_shields_capacity_mean =  locmean("victory", "shields_capacity_mean")
mean_win_shields_capacity_std =  locmean("victory", "shields_capacity_std")
mean_win_shields_capacity_min =  locmean("victory", "shields_capacity_min")
mean_win_shields_capacity_max =  locmean("victory", "shields_capacity_max")
mean_win_shields_capacity_s1 =  locmean("victory", "shields_capacity_s1")
mean_win_shields_capacity_s2 =  locmean("victory", "shields_capacity_s2")
mean_win_shields_capacity_s3 =  locmean("victory", "shields_capacity_s3")
mean_win_shields_capacity_s4 =  locmean("victory", "shields_capacity_s4")
mean_win_shields_capacity_s5 =  locmean("victory", "shields_capacity_s5")
mean_win_shields_capacity_s6 =  locmean("victory", "shields_capacity_s6")
mean_win_shields_capacity_s7 =  locmean("victory", "shields_capacity_s7")
mean_win_shields_capacity_s8 =  locmean("victory", "shields_capacity_s8")
mean_win_shields_capacity_s_med =  locmean("victory", "shields_capacity_s_med")
mean_win_shields_capacity_s_mean =  locmean("victory", "shields_capacity_s_mean")
mean_win_shields_capacity_s_std =  locmean("victory", "shields_capacity_s_std")
mean_win_shields_capacity_s_min =  locmean("victory", "shields_capacity_s_min")
mean_win_shields_capacity_s_max =  locmean("victory", "shields_capacity_s_max")
mean_win_shields_capacity_observation = [
    mean_win_shields_capacity_total, mean_win_shields_capacity_med, mean_win_shields_capacity_mean, mean_win_shields_capacity_std, mean_win_shields_capacity_min, 
    mean_win_shields_capacity_max, mean_win_shields_capacity_s1, mean_win_shields_capacity_s2, mean_win_shields_capacity_s3, mean_win_shields_capacity_s4,
    mean_win_shields_capacity_s5, mean_win_shields_capacity_s6, mean_win_shields_capacity_s7, mean_win_shields_capacity_s8, mean_win_shields_capacity_s_med,
    mean_win_shields_capacity_s_mean, mean_win_shields_capacity_s_std, mean_win_shields_capacity_s_min, mean_win_shields_capacity_s_max,
]

mean_loss_shields_capacity_total = locmean("loss", "shields_capacity_total")
mean_loss_shields_capacity_med =  locmean("loss", "shields_capacity_med")
mean_loss_shields_capacity_mean =  locmean("loss", "shields_capacity_mean")
mean_loss_shields_capacity_std =  locmean("loss", "shields_capacity_std")
mean_loss_shields_capacity_min =  locmean("loss", "shields_capacity_min")
mean_loss_shields_capacity_max =  locmean("loss", "shields_capacity_max")
mean_loss_shields_capacity_s1 =  locmean("loss", "shields_capacity_s1")
mean_loss_shields_capacity_s2 =  locmean("loss", "shields_capacity_s2")
mean_loss_shields_capacity_s3 =  locmean("loss", "shields_capacity_s3")
mean_loss_shields_capacity_s4 =  locmean("loss", "shields_capacity_s4")
mean_loss_shields_capacity_s5 =  locmean("loss", "shields_capacity_s5")
mean_loss_shields_capacity_s6 =  locmean("loss", "shields_capacity_s6")
mean_loss_shields_capacity_s7 =  locmean("loss", "shields_capacity_s7")
mean_loss_shields_capacity_s8 =  locmean("loss", "shields_capacity_s8")
mean_loss_shields_capacity_s_med =  locmean("loss", "shields_capacity_s_med")
mean_loss_shields_capacity_s_mean =  locmean("loss", "shields_capacity_s_mean")
mean_loss_shields_capacity_s_std =  locmean("loss", "shields_capacity_s_std")
mean_loss_shields_capacity_s_min =  locmean("loss", "shields_capacity_s_min")
mean_loss_shields_capacity_s_max =  locmean("loss", "shields_capacity_s_max")
mean_loss_shields_capacity_observation = [
    mean_loss_shields_capacity_total, mean_loss_shields_capacity_med, mean_loss_shields_capacity_mean, mean_loss_shields_capacity_std, mean_loss_shields_capacity_min, 
    mean_loss_shields_capacity_max, mean_loss_shields_capacity_s1, mean_loss_shields_capacity_s2, mean_loss_shields_capacity_s3, mean_loss_shields_capacity_s4,
    mean_loss_shields_capacity_s5, mean_loss_shields_capacity_s6, mean_loss_shields_capacity_s7, mean_loss_shields_capacity_s8, mean_loss_shields_capacity_s_med,
    mean_loss_shields_capacity_s_mean, mean_loss_shields_capacity_s_std, mean_loss_shields_capacity_s_min, mean_loss_shields_capacity_s_max,
]

# oxygen_capacity
oxygen_capacity_total = df["oxygen_capacity_total"].iloc[-1]
oxygen_capacity_med = df["oxygen_capacity_med"].iloc[-1]
oxygen_capacity_mean = df["oxygen_capacity_mean"].iloc[-1]
oxygen_capacity_std = df["oxygen_capacity_std"].iloc[-1]
oxygen_capacity_min = df["oxygen_capacity_min"].iloc[-1]
oxygen_capacity_max = df["oxygen_capacity_max"].iloc[-1]
oxygen_capacity_s1 = df["oxygen_capacity_s1"].iloc[-1]
oxygen_capacity_s2 = df["oxygen_capacity_s2"].iloc[-1]
oxygen_capacity_s3 = df["oxygen_capacity_s3"].iloc[-1]
oxygen_capacity_s4 = df["oxygen_capacity_s4"].iloc[-1]
oxygen_capacity_s5 = df["oxygen_capacity_s5"].iloc[-1]
oxygen_capacity_s6 = df["oxygen_capacity_s6"].iloc[-1]
oxygen_capacity_s7 = df["oxygen_capacity_s7"].iloc[-1]
oxygen_capacity_s8 = df["oxygen_capacity_s8"].iloc[-1]
oxygen_capacity_s_med = df["oxygen_capacity_s_med"].iloc[-1]
oxygen_capacity_s_mean = df["oxygen_capacity_s_mean"].iloc[-1]
oxygen_capacity_s_std = df["oxygen_capacity_s_std"].iloc[-1]
oxygen_capacity_s_min = df["oxygen_capacity_s_min"].iloc[-1]
oxygen_capacity_s_max = df["oxygen_capacity_s_max"].iloc[-1]
oxygen_capacity_observation = [
    oxygen_capacity_total, oxygen_capacity_med, oxygen_capacity_mean, oxygen_capacity_std, oxygen_capacity_min, oxygen_capacity_max, oxygen_capacity_s1,
    oxygen_capacity_s2, oxygen_capacity_s3,oxygen_capacity_s4, oxygen_capacity_s5, oxygen_capacity_s6, oxygen_capacity_s7, oxygen_capacity_s8,
    oxygen_capacity_s_med, oxygen_capacity_s_mean, oxygen_capacity_s_std, oxygen_capacity_s_min, oxygen_capacity_s_max,
]

mean_oxygen_capacity_total = mean("oxygen_capacity_total")
mean_oxygen_capacity_med = mean("oxygen_capacity_med")
mean_oxygen_capacity_mean = mean("oxygen_capacity_mean")
mean_oxygen_capacity_std = mean("oxygen_capacity_std")
mean_oxygen_capacity_min = mean("oxygen_capacity_min")
mean_oxygen_capacity_max = mean("oxygen_capacity_max")
mean_oxygen_capacity_s1 = mean("oxygen_capacity_s1")
mean_oxygen_capacity_s2 = mean("oxygen_capacity_s2")
mean_oxygen_capacity_s3 = mean("oxygen_capacity_s3")
mean_oxygen_capacity_s4 = mean("oxygen_capacity_s4")
mean_oxygen_capacity_s5 = mean("oxygen_capacity_s5")
mean_oxygen_capacity_s6 = mean("oxygen_capacity_s6")
mean_oxygen_capacity_s7 = mean("oxygen_capacity_s7")
mean_oxygen_capacity_s8 = mean("oxygen_capacity_s8")
mean_oxygen_capacity_s_med = mean("oxygen_capacity_s_med")
mean_oxygen_capacity_s_mean = mean("oxygen_capacity_s_mean")
mean_oxygen_capacity_s_std = mean("oxygen_capacity_s_std")
mean_oxygen_capacity_s_min = mean("oxygen_capacity_s_min")
mean_oxygen_capacity_s_max = mean("oxygen_capacity_s_max")
mean_oxygen_capacity_observation = [
    mean_oxygen_capacity_total, mean_oxygen_capacity_med, mean_oxygen_capacity_mean, mean_oxygen_capacity_std, mean_oxygen_capacity_min, 
    mean_oxygen_capacity_max, mean_oxygen_capacity_s1, mean_oxygen_capacity_s2, mean_oxygen_capacity_s3, mean_oxygen_capacity_s4,
    mean_oxygen_capacity_s5, mean_oxygen_capacity_s6, mean_oxygen_capacity_s7, mean_oxygen_capacity_s8, mean_oxygen_capacity_s_med,
    mean_oxygen_capacity_s_mean, mean_oxygen_capacity_s_std, mean_oxygen_capacity_s_min, mean_oxygen_capacity_s_max,
]

mean_win_oxygen_capacity_total = locmean("victory", "oxygen_capacity_total")
mean_win_oxygen_capacity_med =  locmean("victory", "oxygen_capacity_med")
mean_win_oxygen_capacity_mean =  locmean("victory", "oxygen_capacity_mean")
mean_win_oxygen_capacity_std =  locmean("victory", "oxygen_capacity_std")
mean_win_oxygen_capacity_min =  locmean("victory", "oxygen_capacity_min")
mean_win_oxygen_capacity_max =  locmean("victory", "oxygen_capacity_max")
mean_win_oxygen_capacity_s1 =  locmean("victory", "oxygen_capacity_s1")
mean_win_oxygen_capacity_s2 =  locmean("victory", "oxygen_capacity_s2")
mean_win_oxygen_capacity_s3 =  locmean("victory", "oxygen_capacity_s3")
mean_win_oxygen_capacity_s4 =  locmean("victory", "oxygen_capacity_s4")
mean_win_oxygen_capacity_s5 =  locmean("victory", "oxygen_capacity_s5")
mean_win_oxygen_capacity_s6 =  locmean("victory", "oxygen_capacity_s6")
mean_win_oxygen_capacity_s7 =  locmean("victory", "oxygen_capacity_s7")
mean_win_oxygen_capacity_s8 =  locmean("victory", "oxygen_capacity_s8")
mean_win_oxygen_capacity_s_med =  locmean("victory", "oxygen_capacity_s_med")
mean_win_oxygen_capacity_s_mean =  locmean("victory", "oxygen_capacity_s_mean")
mean_win_oxygen_capacity_s_std =  locmean("victory", "oxygen_capacity_s_std")
mean_win_oxygen_capacity_s_min =  locmean("victory", "oxygen_capacity_s_min")
mean_win_oxygen_capacity_s_max =  locmean("victory", "oxygen_capacity_s_max")
mean_win_oxygen_capacity_observation = [
    mean_win_oxygen_capacity_total, mean_win_oxygen_capacity_med, mean_win_oxygen_capacity_mean, mean_win_oxygen_capacity_std, mean_win_oxygen_capacity_min, 
    mean_win_oxygen_capacity_max, mean_win_oxygen_capacity_s1, mean_win_oxygen_capacity_s2, mean_win_oxygen_capacity_s3, mean_win_oxygen_capacity_s4,
    mean_win_oxygen_capacity_s5, mean_win_oxygen_capacity_s6, mean_win_oxygen_capacity_s7, mean_win_oxygen_capacity_s8, mean_win_oxygen_capacity_s_med,
    mean_win_oxygen_capacity_s_mean, mean_win_oxygen_capacity_s_std, mean_win_oxygen_capacity_s_min, mean_win_oxygen_capacity_s_max,
]

mean_loss_oxygen_capacity_total = locmean("loss", "oxygen_capacity_total")
mean_loss_oxygen_capacity_med =  locmean("loss", "oxygen_capacity_med")
mean_loss_oxygen_capacity_mean =  locmean("loss", "oxygen_capacity_mean")
mean_loss_oxygen_capacity_std =  locmean("loss", "oxygen_capacity_std")
mean_loss_oxygen_capacity_min =  locmean("loss", "oxygen_capacity_min")
mean_loss_oxygen_capacity_max =  locmean("loss", "oxygen_capacity_max")
mean_loss_oxygen_capacity_s1 =  locmean("loss", "oxygen_capacity_s1")
mean_loss_oxygen_capacity_s2 =  locmean("loss", "oxygen_capacity_s2")
mean_loss_oxygen_capacity_s3 =  locmean("loss", "oxygen_capacity_s3")
mean_loss_oxygen_capacity_s4 =  locmean("loss", "oxygen_capacity_s4")
mean_loss_oxygen_capacity_s5 =  locmean("loss", "oxygen_capacity_s5")
mean_loss_oxygen_capacity_s6 =  locmean("loss", "oxygen_capacity_s6")
mean_loss_oxygen_capacity_s7 =  locmean("loss", "oxygen_capacity_s7")
mean_loss_oxygen_capacity_s8 =  locmean("loss", "oxygen_capacity_s8")
mean_loss_oxygen_capacity_s_med =  locmean("loss", "oxygen_capacity_s_med")
mean_loss_oxygen_capacity_s_mean =  locmean("loss", "oxygen_capacity_s_mean")
mean_loss_oxygen_capacity_s_std =  locmean("loss", "oxygen_capacity_s_std")
mean_loss_oxygen_capacity_s_min =  locmean("loss", "oxygen_capacity_s_min")
mean_loss_oxygen_capacity_s_max =  locmean("loss", "oxygen_capacity_s_max")
mean_loss_oxygen_capacity_observation = [
    mean_loss_oxygen_capacity_total, mean_loss_oxygen_capacity_med, mean_loss_oxygen_capacity_mean, mean_loss_oxygen_capacity_std, mean_loss_oxygen_capacity_min, 
    mean_loss_oxygen_capacity_max, mean_loss_oxygen_capacity_s1, mean_loss_oxygen_capacity_s2, mean_loss_oxygen_capacity_s3, mean_loss_oxygen_capacity_s4,
    mean_loss_oxygen_capacity_s5, mean_loss_oxygen_capacity_s6, mean_loss_oxygen_capacity_s7, mean_loss_oxygen_capacity_s8, mean_loss_oxygen_capacity_s_med,
    mean_loss_oxygen_capacity_s_mean, mean_loss_oxygen_capacity_s_std, mean_loss_oxygen_capacity_s_min, mean_loss_oxygen_capacity_s_max,
]

# medbay_capacity
medbay_capacity_total = df["medbay_capacity_total"].iloc[-1]
medbay_capacity_med = df["medbay_capacity_med"].iloc[-1]
medbay_capacity_mean = df["medbay_capacity_mean"].iloc[-1]
medbay_capacity_std = df["medbay_capacity_std"].iloc[-1]
medbay_capacity_min = df["medbay_capacity_min"].iloc[-1]
medbay_capacity_max = df["medbay_capacity_max"].iloc[-1]
medbay_capacity_s1 = df["medbay_capacity_s1"].iloc[-1]
medbay_capacity_s2 = df["medbay_capacity_s2"].iloc[-1]
medbay_capacity_s3 = df["medbay_capacity_s3"].iloc[-1]
medbay_capacity_s4 = df["medbay_capacity_s4"].iloc[-1]
medbay_capacity_s5 = df["medbay_capacity_s5"].iloc[-1]
medbay_capacity_s6 = df["medbay_capacity_s6"].iloc[-1]
medbay_capacity_s7 = df["medbay_capacity_s7"].iloc[-1]
medbay_capacity_s8 = df["medbay_capacity_s8"].iloc[-1]
medbay_capacity_s_med = df["medbay_capacity_s_med"].iloc[-1]
medbay_capacity_s_mean = df["medbay_capacity_s_mean"].iloc[-1]
medbay_capacity_s_std = df["medbay_capacity_s_std"].iloc[-1]
medbay_capacity_s_min = df["medbay_capacity_s_min"].iloc[-1]
medbay_capacity_s_max = df["medbay_capacity_s_max"].iloc[-1]
medbay_capacity_observation = [
    medbay_capacity_total, medbay_capacity_med, medbay_capacity_mean, medbay_capacity_std, medbay_capacity_min, medbay_capacity_max, medbay_capacity_s1,
    medbay_capacity_s2, medbay_capacity_s3,medbay_capacity_s4, medbay_capacity_s5, medbay_capacity_s6, medbay_capacity_s7, medbay_capacity_s8,
    medbay_capacity_s_med, medbay_capacity_s_mean, medbay_capacity_s_std, medbay_capacity_s_min, medbay_capacity_s_max,
]

mean_medbay_capacity_total = mean("medbay_capacity_total")
mean_medbay_capacity_med = mean("medbay_capacity_med")
mean_medbay_capacity_mean = mean("medbay_capacity_mean")
mean_medbay_capacity_std = mean("medbay_capacity_std")
mean_medbay_capacity_min = mean("medbay_capacity_min")
mean_medbay_capacity_max = mean("medbay_capacity_max")
mean_medbay_capacity_s1 = mean("medbay_capacity_s1")
mean_medbay_capacity_s2 = mean("medbay_capacity_s2")
mean_medbay_capacity_s3 = mean("medbay_capacity_s3")
mean_medbay_capacity_s4 = mean("medbay_capacity_s4")
mean_medbay_capacity_s5 = mean("medbay_capacity_s5")
mean_medbay_capacity_s6 = mean("medbay_capacity_s6")
mean_medbay_capacity_s7 = mean("medbay_capacity_s7")
mean_medbay_capacity_s8 = mean("medbay_capacity_s8")
mean_medbay_capacity_s_med = mean("medbay_capacity_s_med")
mean_medbay_capacity_s_mean = mean("medbay_capacity_s_mean")
mean_medbay_capacity_s_std = mean("medbay_capacity_s_std")
mean_medbay_capacity_s_min = mean("medbay_capacity_s_min")
mean_medbay_capacity_s_max = mean("medbay_capacity_s_max")
mean_medbay_capacity_observation = [
    mean_medbay_capacity_total, mean_medbay_capacity_med, mean_medbay_capacity_mean, mean_medbay_capacity_std, mean_medbay_capacity_min, 
    mean_medbay_capacity_max, mean_medbay_capacity_s1, mean_medbay_capacity_s2, mean_medbay_capacity_s3, mean_medbay_capacity_s4,
    mean_medbay_capacity_s5, mean_medbay_capacity_s6, mean_medbay_capacity_s7, mean_medbay_capacity_s8, mean_medbay_capacity_s_med,
    mean_medbay_capacity_s_mean, mean_medbay_capacity_s_std, mean_medbay_capacity_s_min, mean_medbay_capacity_s_max,
]

mean_win_medbay_capacity_total = locmean("victory", "medbay_capacity_total")
mean_win_medbay_capacity_med =  locmean("victory", "medbay_capacity_med")
mean_win_medbay_capacity_mean =  locmean("victory", "medbay_capacity_mean")
mean_win_medbay_capacity_std =  locmean("victory", "medbay_capacity_std")
mean_win_medbay_capacity_min =  locmean("victory", "medbay_capacity_min")
mean_win_medbay_capacity_max =  locmean("victory", "medbay_capacity_max")
mean_win_medbay_capacity_s1 =  locmean("victory", "medbay_capacity_s1")
mean_win_medbay_capacity_s2 =  locmean("victory", "medbay_capacity_s2")
mean_win_medbay_capacity_s3 =  locmean("victory", "medbay_capacity_s3")
mean_win_medbay_capacity_s4 =  locmean("victory", "medbay_capacity_s4")
mean_win_medbay_capacity_s5 =  locmean("victory", "medbay_capacity_s5")
mean_win_medbay_capacity_s6 =  locmean("victory", "medbay_capacity_s6")
mean_win_medbay_capacity_s7 =  locmean("victory", "medbay_capacity_s7")
mean_win_medbay_capacity_s8 =  locmean("victory", "medbay_capacity_s8")
mean_win_medbay_capacity_s_med =  locmean("victory", "medbay_capacity_s_med")
mean_win_medbay_capacity_s_mean =  locmean("victory", "medbay_capacity_s_mean")
mean_win_medbay_capacity_s_std =  locmean("victory", "medbay_capacity_s_std")
mean_win_medbay_capacity_s_min =  locmean("victory", "medbay_capacity_s_min")
mean_win_medbay_capacity_s_max =  locmean("victory", "medbay_capacity_s_max")
mean_win_medbay_capacity_observation = [
    mean_win_medbay_capacity_total, mean_win_medbay_capacity_med, mean_win_medbay_capacity_mean, mean_win_medbay_capacity_std, mean_win_medbay_capacity_min, 
    mean_win_medbay_capacity_max, mean_win_medbay_capacity_s1, mean_win_medbay_capacity_s2, mean_win_medbay_capacity_s3, mean_win_medbay_capacity_s4,
    mean_win_medbay_capacity_s5, mean_win_medbay_capacity_s6, mean_win_medbay_capacity_s7, mean_win_medbay_capacity_s8, mean_win_medbay_capacity_s_med,
    mean_win_medbay_capacity_s_mean, mean_win_medbay_capacity_s_std, mean_win_medbay_capacity_s_min, mean_win_medbay_capacity_s_max,
]

mean_loss_medbay_capacity_total = locmean("loss", "medbay_capacity_total")
mean_loss_medbay_capacity_med =  locmean("loss", "medbay_capacity_med")
mean_loss_medbay_capacity_mean =  locmean("loss", "medbay_capacity_mean")
mean_loss_medbay_capacity_std =  locmean("loss", "medbay_capacity_std")
mean_loss_medbay_capacity_min =  locmean("loss", "medbay_capacity_min")
mean_loss_medbay_capacity_max =  locmean("loss", "medbay_capacity_max")
mean_loss_medbay_capacity_s1 =  locmean("loss", "medbay_capacity_s1")
mean_loss_medbay_capacity_s2 =  locmean("loss", "medbay_capacity_s2")
mean_loss_medbay_capacity_s3 =  locmean("loss", "medbay_capacity_s3")
mean_loss_medbay_capacity_s4 =  locmean("loss", "medbay_capacity_s4")
mean_loss_medbay_capacity_s5 =  locmean("loss", "medbay_capacity_s5")
mean_loss_medbay_capacity_s6 =  locmean("loss", "medbay_capacity_s6")
mean_loss_medbay_capacity_s7 =  locmean("loss", "medbay_capacity_s7")
mean_loss_medbay_capacity_s8 =  locmean("loss", "medbay_capacity_s8")
mean_loss_medbay_capacity_s_med =  locmean("loss", "medbay_capacity_s_med")
mean_loss_medbay_capacity_s_mean =  locmean("loss", "medbay_capacity_s_mean")
mean_loss_medbay_capacity_s_std =  locmean("loss", "medbay_capacity_s_std")
mean_loss_medbay_capacity_s_min =  locmean("loss", "medbay_capacity_s_min")
mean_loss_medbay_capacity_s_max =  locmean("loss", "medbay_capacity_s_max")
mean_loss_medbay_capacity_observation = [
    mean_loss_medbay_capacity_total, mean_loss_medbay_capacity_med, mean_loss_medbay_capacity_mean, mean_loss_medbay_capacity_std, mean_loss_medbay_capacity_min, 
    mean_loss_medbay_capacity_max, mean_loss_medbay_capacity_s1, mean_loss_medbay_capacity_s2, mean_loss_medbay_capacity_s3, mean_loss_medbay_capacity_s4,
    mean_loss_medbay_capacity_s5, mean_loss_medbay_capacity_s6, mean_loss_medbay_capacity_s7, mean_loss_medbay_capacity_s8, mean_loss_medbay_capacity_s_med,
    mean_loss_medbay_capacity_s_mean, mean_loss_medbay_capacity_s_std, mean_loss_medbay_capacity_s_min, mean_loss_medbay_capacity_s_max,
]

# clonebay_capacity
clonebay_capacity_total = df["clonebay_capacity_total"].iloc[-1]
clonebay_capacity_med = df["clonebay_capacity_med"].iloc[-1]
clonebay_capacity_mean = df["clonebay_capacity_mean"].iloc[-1]
clonebay_capacity_std = df["clonebay_capacity_std"].iloc[-1]
clonebay_capacity_min = df["clonebay_capacity_min"].iloc[-1]
clonebay_capacity_max = df["clonebay_capacity_max"].iloc[-1]
clonebay_capacity_s1 = df["clonebay_capacity_s1"].iloc[-1]
clonebay_capacity_s2 = df["clonebay_capacity_s2"].iloc[-1]
clonebay_capacity_s3 = df["clonebay_capacity_s3"].iloc[-1]
clonebay_capacity_s4 = df["clonebay_capacity_s4"].iloc[-1]
clonebay_capacity_s5 = df["clonebay_capacity_s5"].iloc[-1]
clonebay_capacity_s6 = df["clonebay_capacity_s6"].iloc[-1]
clonebay_capacity_s7 = df["clonebay_capacity_s7"].iloc[-1]
clonebay_capacity_s8 = df["clonebay_capacity_s8"].iloc[-1]
clonebay_capacity_s_med = df["clonebay_capacity_s_med"].iloc[-1]
clonebay_capacity_s_mean = df["clonebay_capacity_s_mean"].iloc[-1]
clonebay_capacity_s_std = df["clonebay_capacity_s_std"].iloc[-1]
clonebay_capacity_s_min = df["clonebay_capacity_s_min"].iloc[-1]
clonebay_capacity_s_max = df["clonebay_capacity_s_max"].iloc[-1]
clonebay_capacity_observation = [
    clonebay_capacity_total, clonebay_capacity_med, clonebay_capacity_mean, clonebay_capacity_std, clonebay_capacity_min, clonebay_capacity_max, clonebay_capacity_s1,
    clonebay_capacity_s2, clonebay_capacity_s3,clonebay_capacity_s4, clonebay_capacity_s5, clonebay_capacity_s6, clonebay_capacity_s7, clonebay_capacity_s8,
    clonebay_capacity_s_med, clonebay_capacity_s_mean, clonebay_capacity_s_std, clonebay_capacity_s_min, clonebay_capacity_s_max,
]

mean_clonebay_capacity_total = mean("clonebay_capacity_total")
mean_clonebay_capacity_med = mean("clonebay_capacity_med")
mean_clonebay_capacity_mean = mean("clonebay_capacity_mean")
mean_clonebay_capacity_std = mean("clonebay_capacity_std")
mean_clonebay_capacity_min = mean("clonebay_capacity_min")
mean_clonebay_capacity_max = mean("clonebay_capacity_max")
mean_clonebay_capacity_s1 = mean("clonebay_capacity_s1")
mean_clonebay_capacity_s2 = mean("clonebay_capacity_s2")
mean_clonebay_capacity_s3 = mean("clonebay_capacity_s3")
mean_clonebay_capacity_s4 = mean("clonebay_capacity_s4")
mean_clonebay_capacity_s5 = mean("clonebay_capacity_s5")
mean_clonebay_capacity_s6 = mean("clonebay_capacity_s6")
mean_clonebay_capacity_s7 = mean("clonebay_capacity_s7")
mean_clonebay_capacity_s8 = mean("clonebay_capacity_s8")
mean_clonebay_capacity_s_med = mean("clonebay_capacity_s_med")
mean_clonebay_capacity_s_mean = mean("clonebay_capacity_s_mean")
mean_clonebay_capacity_s_std = mean("clonebay_capacity_s_std")
mean_clonebay_capacity_s_min = mean("clonebay_capacity_s_min")
mean_clonebay_capacity_s_max = mean("clonebay_capacity_s_max")
mean_clonebay_capacity_observation = [
    mean_clonebay_capacity_total, mean_clonebay_capacity_med, mean_clonebay_capacity_mean, mean_clonebay_capacity_std, mean_clonebay_capacity_min, 
    mean_clonebay_capacity_max, mean_clonebay_capacity_s1, mean_clonebay_capacity_s2, mean_clonebay_capacity_s3, mean_clonebay_capacity_s4,
    mean_clonebay_capacity_s5, mean_clonebay_capacity_s6, mean_clonebay_capacity_s7, mean_clonebay_capacity_s8, mean_clonebay_capacity_s_med,
    mean_clonebay_capacity_s_mean, mean_clonebay_capacity_s_std, mean_clonebay_capacity_s_min, mean_clonebay_capacity_s_max,
]

mean_win_clonebay_capacity_total = locmean("victory", "clonebay_capacity_total")
mean_win_clonebay_capacity_med =  locmean("victory", "clonebay_capacity_med")
mean_win_clonebay_capacity_mean =  locmean("victory", "clonebay_capacity_mean")
mean_win_clonebay_capacity_std =  locmean("victory", "clonebay_capacity_std")
mean_win_clonebay_capacity_min =  locmean("victory", "clonebay_capacity_min")
mean_win_clonebay_capacity_max =  locmean("victory", "clonebay_capacity_max")
mean_win_clonebay_capacity_s1 =  locmean("victory", "clonebay_capacity_s1")
mean_win_clonebay_capacity_s2 =  locmean("victory", "clonebay_capacity_s2")
mean_win_clonebay_capacity_s3 =  locmean("victory", "clonebay_capacity_s3")
mean_win_clonebay_capacity_s4 =  locmean("victory", "clonebay_capacity_s4")
mean_win_clonebay_capacity_s5 =  locmean("victory", "clonebay_capacity_s5")
mean_win_clonebay_capacity_s6 =  locmean("victory", "clonebay_capacity_s6")
mean_win_clonebay_capacity_s7 =  locmean("victory", "clonebay_capacity_s7")
mean_win_clonebay_capacity_s8 =  locmean("victory", "clonebay_capacity_s8")
mean_win_clonebay_capacity_s_med =  locmean("victory", "clonebay_capacity_s_med")
mean_win_clonebay_capacity_s_mean =  locmean("victory", "clonebay_capacity_s_mean")
mean_win_clonebay_capacity_s_std =  locmean("victory", "clonebay_capacity_s_std")
mean_win_clonebay_capacity_s_min =  locmean("victory", "clonebay_capacity_s_min")
mean_win_clonebay_capacity_s_max =  locmean("victory", "clonebay_capacity_s_max")
mean_win_clonebay_capacity_observation = [
    mean_win_clonebay_capacity_total, mean_win_clonebay_capacity_med, mean_win_clonebay_capacity_mean, mean_win_clonebay_capacity_std, mean_win_clonebay_capacity_min, 
    mean_win_clonebay_capacity_max, mean_win_clonebay_capacity_s1, mean_win_clonebay_capacity_s2, mean_win_clonebay_capacity_s3, mean_win_clonebay_capacity_s4,
    mean_win_clonebay_capacity_s5, mean_win_clonebay_capacity_s6, mean_win_clonebay_capacity_s7, mean_win_clonebay_capacity_s8, mean_win_clonebay_capacity_s_med,
    mean_win_clonebay_capacity_s_mean, mean_win_clonebay_capacity_s_std, mean_win_clonebay_capacity_s_min, mean_win_clonebay_capacity_s_max,
]

mean_loss_clonebay_capacity_total = locmean("loss", "clonebay_capacity_total")
mean_loss_clonebay_capacity_med =  locmean("loss", "clonebay_capacity_med")
mean_loss_clonebay_capacity_mean =  locmean("loss", "clonebay_capacity_mean")
mean_loss_clonebay_capacity_std =  locmean("loss", "clonebay_capacity_std")
mean_loss_clonebay_capacity_min =  locmean("loss", "clonebay_capacity_min")
mean_loss_clonebay_capacity_max =  locmean("loss", "clonebay_capacity_max")
mean_loss_clonebay_capacity_s1 =  locmean("loss", "clonebay_capacity_s1")
mean_loss_clonebay_capacity_s2 =  locmean("loss", "clonebay_capacity_s2")
mean_loss_clonebay_capacity_s3 =  locmean("loss", "clonebay_capacity_s3")
mean_loss_clonebay_capacity_s4 =  locmean("loss", "clonebay_capacity_s4")
mean_loss_clonebay_capacity_s5 =  locmean("loss", "clonebay_capacity_s5")
mean_loss_clonebay_capacity_s6 =  locmean("loss", "clonebay_capacity_s6")
mean_loss_clonebay_capacity_s7 =  locmean("loss", "clonebay_capacity_s7")
mean_loss_clonebay_capacity_s8 =  locmean("loss", "clonebay_capacity_s8")
mean_loss_clonebay_capacity_s_med =  locmean("loss", "clonebay_capacity_s_med")
mean_loss_clonebay_capacity_s_mean =  locmean("loss", "clonebay_capacity_s_mean")
mean_loss_clonebay_capacity_s_std =  locmean("loss", "clonebay_capacity_s_std")
mean_loss_clonebay_capacity_s_min =  locmean("loss", "clonebay_capacity_s_min")
mean_loss_clonebay_capacity_s_max =  locmean("loss", "clonebay_capacity_s_max")
mean_loss_clonebay_capacity_observation = [
    mean_loss_clonebay_capacity_total, mean_loss_clonebay_capacity_med, mean_loss_clonebay_capacity_mean, mean_loss_clonebay_capacity_std, mean_loss_clonebay_capacity_min, 
    mean_loss_clonebay_capacity_max, mean_loss_clonebay_capacity_s1, mean_loss_clonebay_capacity_s2, mean_loss_clonebay_capacity_s3, mean_loss_clonebay_capacity_s4,
    mean_loss_clonebay_capacity_s5, mean_loss_clonebay_capacity_s6, mean_loss_clonebay_capacity_s7, mean_loss_clonebay_capacity_s8, mean_loss_clonebay_capacity_s_med,
    mean_loss_clonebay_capacity_s_mean, mean_loss_clonebay_capacity_s_std, mean_loss_clonebay_capacity_s_min, mean_loss_clonebay_capacity_s_max,
]

# pilot_capacity
pilot_capacity_total = df["pilot_capacity_total"].iloc[-1]
pilot_capacity_med = df["pilot_capacity_med"].iloc[-1]
pilot_capacity_mean = df["pilot_capacity_mean"].iloc[-1]
pilot_capacity_std = df["pilot_capacity_std"].iloc[-1]
pilot_capacity_min = df["pilot_capacity_min"].iloc[-1]
pilot_capacity_max = df["pilot_capacity_max"].iloc[-1]
pilot_capacity_s1 = df["pilot_capacity_s1"].iloc[-1]
pilot_capacity_s2 = df["pilot_capacity_s2"].iloc[-1]
pilot_capacity_s3 = df["pilot_capacity_s3"].iloc[-1]
pilot_capacity_s4 = df["pilot_capacity_s4"].iloc[-1]
pilot_capacity_s5 = df["pilot_capacity_s5"].iloc[-1]
pilot_capacity_s6 = df["pilot_capacity_s6"].iloc[-1]
pilot_capacity_s7 = df["pilot_capacity_s7"].iloc[-1]
pilot_capacity_s8 = df["pilot_capacity_s8"].iloc[-1]
pilot_capacity_s_med = df["pilot_capacity_s_med"].iloc[-1]
pilot_capacity_s_mean = df["pilot_capacity_s_mean"].iloc[-1]
pilot_capacity_s_std = df["pilot_capacity_s_std"].iloc[-1]
pilot_capacity_s_min = df["pilot_capacity_s_min"].iloc[-1]
pilot_capacity_s_max = df["pilot_capacity_s_max"].iloc[-1]
pilot_capacity_observation = [
    pilot_capacity_total, pilot_capacity_med, pilot_capacity_mean, pilot_capacity_std, pilot_capacity_min, pilot_capacity_max, pilot_capacity_s1,
    pilot_capacity_s2, pilot_capacity_s3,pilot_capacity_s4, pilot_capacity_s5, pilot_capacity_s6, pilot_capacity_s7, pilot_capacity_s8,
    pilot_capacity_s_med, pilot_capacity_s_mean, pilot_capacity_s_std, pilot_capacity_s_min, pilot_capacity_s_max,
]

mean_pilot_capacity_total = mean("pilot_capacity_total")
mean_pilot_capacity_med = mean("pilot_capacity_med")
mean_pilot_capacity_mean = mean("pilot_capacity_mean")
mean_pilot_capacity_std = mean("pilot_capacity_std")
mean_pilot_capacity_min = mean("pilot_capacity_min")
mean_pilot_capacity_max = mean("pilot_capacity_max")
mean_pilot_capacity_s1 = mean("pilot_capacity_s1")
mean_pilot_capacity_s2 = mean("pilot_capacity_s2")
mean_pilot_capacity_s3 = mean("pilot_capacity_s3")
mean_pilot_capacity_s4 = mean("pilot_capacity_s4")
mean_pilot_capacity_s5 = mean("pilot_capacity_s5")
mean_pilot_capacity_s6 = mean("pilot_capacity_s6")
mean_pilot_capacity_s7 = mean("pilot_capacity_s7")
mean_pilot_capacity_s8 = mean("pilot_capacity_s8")
mean_pilot_capacity_s_med = mean("pilot_capacity_s_med")
mean_pilot_capacity_s_mean = mean("pilot_capacity_s_mean")
mean_pilot_capacity_s_std = mean("pilot_capacity_s_std")
mean_pilot_capacity_s_min = mean("pilot_capacity_s_min")
mean_pilot_capacity_s_max = mean("pilot_capacity_s_max")
mean_pilot_capacity_observation = [
    mean_pilot_capacity_total, mean_pilot_capacity_med, mean_pilot_capacity_mean, mean_pilot_capacity_std, mean_pilot_capacity_min, 
    mean_pilot_capacity_max, mean_pilot_capacity_s1, mean_pilot_capacity_s2, mean_pilot_capacity_s3, mean_pilot_capacity_s4,
    mean_pilot_capacity_s5, mean_pilot_capacity_s6, mean_pilot_capacity_s7, mean_pilot_capacity_s8, mean_pilot_capacity_s_med,
    mean_pilot_capacity_s_mean, mean_pilot_capacity_s_std, mean_pilot_capacity_s_min, mean_pilot_capacity_s_max,
]

mean_win_pilot_capacity_total = locmean("victory", "pilot_capacity_total")
mean_win_pilot_capacity_med =  locmean("victory", "pilot_capacity_med")
mean_win_pilot_capacity_mean =  locmean("victory", "pilot_capacity_mean")
mean_win_pilot_capacity_std =  locmean("victory", "pilot_capacity_std")
mean_win_pilot_capacity_min =  locmean("victory", "pilot_capacity_min")
mean_win_pilot_capacity_max =  locmean("victory", "pilot_capacity_max")
mean_win_pilot_capacity_s1 =  locmean("victory", "pilot_capacity_s1")
mean_win_pilot_capacity_s2 =  locmean("victory", "pilot_capacity_s2")
mean_win_pilot_capacity_s3 =  locmean("victory", "pilot_capacity_s3")
mean_win_pilot_capacity_s4 =  locmean("victory", "pilot_capacity_s4")
mean_win_pilot_capacity_s5 =  locmean("victory", "pilot_capacity_s5")
mean_win_pilot_capacity_s6 =  locmean("victory", "pilot_capacity_s6")
mean_win_pilot_capacity_s7 =  locmean("victory", "pilot_capacity_s7")
mean_win_pilot_capacity_s8 =  locmean("victory", "pilot_capacity_s8")
mean_win_pilot_capacity_s_med =  locmean("victory", "pilot_capacity_s_med")
mean_win_pilot_capacity_s_mean =  locmean("victory", "pilot_capacity_s_mean")
mean_win_pilot_capacity_s_std =  locmean("victory", "pilot_capacity_s_std")
mean_win_pilot_capacity_s_min =  locmean("victory", "pilot_capacity_s_min")
mean_win_pilot_capacity_s_max =  locmean("victory", "pilot_capacity_s_max")
mean_win_pilot_capacity_observation = [
    mean_win_pilot_capacity_total, mean_win_pilot_capacity_med, mean_win_pilot_capacity_mean, mean_win_pilot_capacity_std, mean_win_pilot_capacity_min, 
    mean_win_pilot_capacity_max, mean_win_pilot_capacity_s1, mean_win_pilot_capacity_s2, mean_win_pilot_capacity_s3, mean_win_pilot_capacity_s4,
    mean_win_pilot_capacity_s5, mean_win_pilot_capacity_s6, mean_win_pilot_capacity_s7, mean_win_pilot_capacity_s8, mean_win_pilot_capacity_s_med,
    mean_win_pilot_capacity_s_mean, mean_win_pilot_capacity_s_std, mean_win_pilot_capacity_s_min, mean_win_pilot_capacity_s_max,
]

mean_loss_pilot_capacity_total = locmean("loss", "pilot_capacity_total")
mean_loss_pilot_capacity_med =  locmean("loss", "pilot_capacity_med")
mean_loss_pilot_capacity_mean =  locmean("loss", "pilot_capacity_mean")
mean_loss_pilot_capacity_std =  locmean("loss", "pilot_capacity_std")
mean_loss_pilot_capacity_min =  locmean("loss", "pilot_capacity_min")
mean_loss_pilot_capacity_max =  locmean("loss", "pilot_capacity_max")
mean_loss_pilot_capacity_s1 =  locmean("loss", "pilot_capacity_s1")
mean_loss_pilot_capacity_s2 =  locmean("loss", "pilot_capacity_s2")
mean_loss_pilot_capacity_s3 =  locmean("loss", "pilot_capacity_s3")
mean_loss_pilot_capacity_s4 =  locmean("loss", "pilot_capacity_s4")
mean_loss_pilot_capacity_s5 =  locmean("loss", "pilot_capacity_s5")
mean_loss_pilot_capacity_s6 =  locmean("loss", "pilot_capacity_s6")
mean_loss_pilot_capacity_s7 =  locmean("loss", "pilot_capacity_s7")
mean_loss_pilot_capacity_s8 =  locmean("loss", "pilot_capacity_s8")
mean_loss_pilot_capacity_s_med =  locmean("loss", "pilot_capacity_s_med")
mean_loss_pilot_capacity_s_mean =  locmean("loss", "pilot_capacity_s_mean")
mean_loss_pilot_capacity_s_std =  locmean("loss", "pilot_capacity_s_std")
mean_loss_pilot_capacity_s_min =  locmean("loss", "pilot_capacity_s_min")
mean_loss_pilot_capacity_s_max =  locmean("loss", "pilot_capacity_s_max")
mean_loss_pilot_capacity_observation = [
    mean_loss_pilot_capacity_total, mean_loss_pilot_capacity_med, mean_loss_pilot_capacity_mean, mean_loss_pilot_capacity_std, mean_loss_pilot_capacity_min, 
    mean_loss_pilot_capacity_max, mean_loss_pilot_capacity_s1, mean_loss_pilot_capacity_s2, mean_loss_pilot_capacity_s3, mean_loss_pilot_capacity_s4,
    mean_loss_pilot_capacity_s5, mean_loss_pilot_capacity_s6, mean_loss_pilot_capacity_s7, mean_loss_pilot_capacity_s8, mean_loss_pilot_capacity_s_med,
    mean_loss_pilot_capacity_s_mean, mean_loss_pilot_capacity_s_std, mean_loss_pilot_capacity_s_min, mean_loss_pilot_capacity_s_max,
]

# sensors_capacity
sensors_capacity_total = df["sensors_capacity_total"].iloc[-1]
sensors_capacity_med = df["sensors_capacity_med"].iloc[-1]
sensors_capacity_mean = df["sensors_capacity_mean"].iloc[-1]
sensors_capacity_std = df["sensors_capacity_std"].iloc[-1]
sensors_capacity_min = df["sensors_capacity_min"].iloc[-1]
sensors_capacity_max = df["sensors_capacity_max"].iloc[-1]
sensors_capacity_s1 = df["sensors_capacity_s1"].iloc[-1]
sensors_capacity_s2 = df["sensors_capacity_s2"].iloc[-1]
sensors_capacity_s3 = df["sensors_capacity_s3"].iloc[-1]
sensors_capacity_s4 = df["sensors_capacity_s4"].iloc[-1]
sensors_capacity_s5 = df["sensors_capacity_s5"].iloc[-1]
sensors_capacity_s6 = df["sensors_capacity_s6"].iloc[-1]
sensors_capacity_s7 = df["sensors_capacity_s7"].iloc[-1]
sensors_capacity_s8 = df["sensors_capacity_s8"].iloc[-1]
sensors_capacity_s_med = df["sensors_capacity_s_med"].iloc[-1]
sensors_capacity_s_mean = df["sensors_capacity_s_mean"].iloc[-1]
sensors_capacity_s_std = df["sensors_capacity_s_std"].iloc[-1]
sensors_capacity_s_min = df["sensors_capacity_s_min"].iloc[-1]
sensors_capacity_s_max = df["sensors_capacity_s_max"].iloc[-1]
sensors_capacity_observation = [
    sensors_capacity_total, sensors_capacity_med, sensors_capacity_mean, sensors_capacity_std, sensors_capacity_min, sensors_capacity_max, sensors_capacity_s1,
    sensors_capacity_s2, sensors_capacity_s3,sensors_capacity_s4, sensors_capacity_s5, sensors_capacity_s6, sensors_capacity_s7, sensors_capacity_s8,
    sensors_capacity_s_med, sensors_capacity_s_mean, sensors_capacity_s_std, sensors_capacity_s_min, sensors_capacity_s_max,
]

mean_sensors_capacity_total = mean("sensors_capacity_total")
mean_sensors_capacity_med = mean("sensors_capacity_med")
mean_sensors_capacity_mean = mean("sensors_capacity_mean")
mean_sensors_capacity_std = mean("sensors_capacity_std")
mean_sensors_capacity_min = mean("sensors_capacity_min")
mean_sensors_capacity_max = mean("sensors_capacity_max")
mean_sensors_capacity_s1 = mean("sensors_capacity_s1")
mean_sensors_capacity_s2 = mean("sensors_capacity_s2")
mean_sensors_capacity_s3 = mean("sensors_capacity_s3")
mean_sensors_capacity_s4 = mean("sensors_capacity_s4")
mean_sensors_capacity_s5 = mean("sensors_capacity_s5")
mean_sensors_capacity_s6 = mean("sensors_capacity_s6")
mean_sensors_capacity_s7 = mean("sensors_capacity_s7")
mean_sensors_capacity_s8 = mean("sensors_capacity_s8")
mean_sensors_capacity_s_med = mean("sensors_capacity_s_med")
mean_sensors_capacity_s_mean = mean("sensors_capacity_s_mean")
mean_sensors_capacity_s_std = mean("sensors_capacity_s_std")
mean_sensors_capacity_s_min = mean("sensors_capacity_s_min")
mean_sensors_capacity_s_max = mean("sensors_capacity_s_max")
mean_sensors_capacity_observation = [
    mean_sensors_capacity_total, mean_sensors_capacity_med, mean_sensors_capacity_mean, mean_sensors_capacity_std, mean_sensors_capacity_min, 
    mean_sensors_capacity_max, mean_sensors_capacity_s1, mean_sensors_capacity_s2, mean_sensors_capacity_s3, mean_sensors_capacity_s4,
    mean_sensors_capacity_s5, mean_sensors_capacity_s6, mean_sensors_capacity_s7, mean_sensors_capacity_s8, mean_sensors_capacity_s_med,
    mean_sensors_capacity_s_mean, mean_sensors_capacity_s_std, mean_sensors_capacity_s_min, mean_sensors_capacity_s_max,
]

mean_win_sensors_capacity_total = locmean("victory", "sensors_capacity_total")
mean_win_sensors_capacity_med =  locmean("victory", "sensors_capacity_med")
mean_win_sensors_capacity_mean =  locmean("victory", "sensors_capacity_mean")
mean_win_sensors_capacity_std =  locmean("victory", "sensors_capacity_std")
mean_win_sensors_capacity_min =  locmean("victory", "sensors_capacity_min")
mean_win_sensors_capacity_max =  locmean("victory", "sensors_capacity_max")
mean_win_sensors_capacity_s1 =  locmean("victory", "sensors_capacity_s1")
mean_win_sensors_capacity_s2 =  locmean("victory", "sensors_capacity_s2")
mean_win_sensors_capacity_s3 =  locmean("victory", "sensors_capacity_s3")
mean_win_sensors_capacity_s4 =  locmean("victory", "sensors_capacity_s4")
mean_win_sensors_capacity_s5 =  locmean("victory", "sensors_capacity_s5")
mean_win_sensors_capacity_s6 =  locmean("victory", "sensors_capacity_s6")
mean_win_sensors_capacity_s7 =  locmean("victory", "sensors_capacity_s7")
mean_win_sensors_capacity_s8 =  locmean("victory", "sensors_capacity_s8")
mean_win_sensors_capacity_s_med =  locmean("victory", "sensors_capacity_s_med")
mean_win_sensors_capacity_s_mean =  locmean("victory", "sensors_capacity_s_mean")
mean_win_sensors_capacity_s_std =  locmean("victory", "sensors_capacity_s_std")
mean_win_sensors_capacity_s_min =  locmean("victory", "sensors_capacity_s_min")
mean_win_sensors_capacity_s_max =  locmean("victory", "sensors_capacity_s_max")
mean_win_sensors_capacity_observation = [
    mean_win_sensors_capacity_total, mean_win_sensors_capacity_med, mean_win_sensors_capacity_mean, mean_win_sensors_capacity_std, mean_win_sensors_capacity_min, 
    mean_win_sensors_capacity_max, mean_win_sensors_capacity_s1, mean_win_sensors_capacity_s2, mean_win_sensors_capacity_s3, mean_win_sensors_capacity_s4,
    mean_win_sensors_capacity_s5, mean_win_sensors_capacity_s6, mean_win_sensors_capacity_s7, mean_win_sensors_capacity_s8, mean_win_sensors_capacity_s_med,
    mean_win_sensors_capacity_s_mean, mean_win_sensors_capacity_s_std, mean_win_sensors_capacity_s_min, mean_win_sensors_capacity_s_max,
]

mean_loss_sensors_capacity_total = locmean("loss", "sensors_capacity_total")
mean_loss_sensors_capacity_med =  locmean("loss", "sensors_capacity_med")
mean_loss_sensors_capacity_mean =  locmean("loss", "sensors_capacity_mean")
mean_loss_sensors_capacity_std =  locmean("loss", "sensors_capacity_std")
mean_loss_sensors_capacity_min =  locmean("loss", "sensors_capacity_min")
mean_loss_sensors_capacity_max =  locmean("loss", "sensors_capacity_max")
mean_loss_sensors_capacity_s1 =  locmean("loss", "sensors_capacity_s1")
mean_loss_sensors_capacity_s2 =  locmean("loss", "sensors_capacity_s2")
mean_loss_sensors_capacity_s3 =  locmean("loss", "sensors_capacity_s3")
mean_loss_sensors_capacity_s4 =  locmean("loss", "sensors_capacity_s4")
mean_loss_sensors_capacity_s5 =  locmean("loss", "sensors_capacity_s5")
mean_loss_sensors_capacity_s6 =  locmean("loss", "sensors_capacity_s6")
mean_loss_sensors_capacity_s7 =  locmean("loss", "sensors_capacity_s7")
mean_loss_sensors_capacity_s8 =  locmean("loss", "sensors_capacity_s8")
mean_loss_sensors_capacity_s_med =  locmean("loss", "sensors_capacity_s_med")
mean_loss_sensors_capacity_s_mean =  locmean("loss", "sensors_capacity_s_mean")
mean_loss_sensors_capacity_s_std =  locmean("loss", "sensors_capacity_s_std")
mean_loss_sensors_capacity_s_min =  locmean("loss", "sensors_capacity_s_min")
mean_loss_sensors_capacity_s_max =  locmean("loss", "sensors_capacity_s_max")
mean_loss_sensors_capacity_observation = [
    mean_loss_sensors_capacity_total, mean_loss_sensors_capacity_med, mean_loss_sensors_capacity_mean, mean_loss_sensors_capacity_std, mean_loss_sensors_capacity_min, 
    mean_loss_sensors_capacity_max, mean_loss_sensors_capacity_s1, mean_loss_sensors_capacity_s2, mean_loss_sensors_capacity_s3, mean_loss_sensors_capacity_s4,
    mean_loss_sensors_capacity_s5, mean_loss_sensors_capacity_s6, mean_loss_sensors_capacity_s7, mean_loss_sensors_capacity_s8, mean_loss_sensors_capacity_s_med,
    mean_loss_sensors_capacity_s_mean, mean_loss_sensors_capacity_s_std, mean_loss_sensors_capacity_s_min, mean_loss_sensors_capacity_s_max,
]

# doors_capacity
doors_capacity_total = df["doors_capacity_total"].iloc[-1]
doors_capacity_med = df["doors_capacity_med"].iloc[-1]
doors_capacity_mean = df["doors_capacity_mean"].iloc[-1]
doors_capacity_std = df["doors_capacity_std"].iloc[-1]
doors_capacity_min = df["doors_capacity_min"].iloc[-1]
doors_capacity_max = df["doors_capacity_max"].iloc[-1]
doors_capacity_s1 = df["doors_capacity_s1"].iloc[-1]
doors_capacity_s2 = df["doors_capacity_s2"].iloc[-1]
doors_capacity_s3 = df["doors_capacity_s3"].iloc[-1]
doors_capacity_s4 = df["doors_capacity_s4"].iloc[-1]
doors_capacity_s5 = df["doors_capacity_s5"].iloc[-1]
doors_capacity_s6 = df["doors_capacity_s6"].iloc[-1]
doors_capacity_s7 = df["doors_capacity_s7"].iloc[-1]
doors_capacity_s8 = df["doors_capacity_s8"].iloc[-1]
doors_capacity_s_med = df["doors_capacity_s_med"].iloc[-1]
doors_capacity_s_mean = df["doors_capacity_s_mean"].iloc[-1]
doors_capacity_s_std = df["doors_capacity_s_std"].iloc[-1]
doors_capacity_s_min = df["doors_capacity_s_min"].iloc[-1]
doors_capacity_s_max = df["doors_capacity_s_max"].iloc[-1]
doors_capacity_observation = [
    doors_capacity_total, doors_capacity_med, doors_capacity_mean, doors_capacity_std, doors_capacity_min, doors_capacity_max, doors_capacity_s1,
    doors_capacity_s2, doors_capacity_s3,doors_capacity_s4, doors_capacity_s5, doors_capacity_s6, doors_capacity_s7, doors_capacity_s8,
    doors_capacity_s_med, doors_capacity_s_mean, doors_capacity_s_std, doors_capacity_s_min, doors_capacity_s_max,
]

mean_doors_capacity_total = mean("doors_capacity_total")
mean_doors_capacity_med = mean("doors_capacity_med")
mean_doors_capacity_mean = mean("doors_capacity_mean")
mean_doors_capacity_std = mean("doors_capacity_std")
mean_doors_capacity_min = mean("doors_capacity_min")
mean_doors_capacity_max = mean("doors_capacity_max")
mean_doors_capacity_s1 = mean("doors_capacity_s1")
mean_doors_capacity_s2 = mean("doors_capacity_s2")
mean_doors_capacity_s3 = mean("doors_capacity_s3")
mean_doors_capacity_s4 = mean("doors_capacity_s4")
mean_doors_capacity_s5 = mean("doors_capacity_s5")
mean_doors_capacity_s6 = mean("doors_capacity_s6")
mean_doors_capacity_s7 = mean("doors_capacity_s7")
mean_doors_capacity_s8 = mean("doors_capacity_s8")
mean_doors_capacity_s_med = mean("doors_capacity_s_med")
mean_doors_capacity_s_mean = mean("doors_capacity_s_mean")
mean_doors_capacity_s_std = mean("doors_capacity_s_std")
mean_doors_capacity_s_min = mean("doors_capacity_s_min")
mean_doors_capacity_s_max = mean("doors_capacity_s_max")
mean_doors_capacity_observation = [
    mean_doors_capacity_total, mean_doors_capacity_med, mean_doors_capacity_mean, mean_doors_capacity_std, mean_doors_capacity_min, 
    mean_doors_capacity_max, mean_doors_capacity_s1, mean_doors_capacity_s2, mean_doors_capacity_s3, mean_doors_capacity_s4,
    mean_doors_capacity_s5, mean_doors_capacity_s6, mean_doors_capacity_s7, mean_doors_capacity_s8, mean_doors_capacity_s_med,
    mean_doors_capacity_s_mean, mean_doors_capacity_s_std, mean_doors_capacity_s_min, mean_doors_capacity_s_max,
]

mean_win_doors_capacity_total = locmean("victory", "doors_capacity_total")
mean_win_doors_capacity_med =  locmean("victory", "doors_capacity_med")
mean_win_doors_capacity_mean =  locmean("victory", "doors_capacity_mean")
mean_win_doors_capacity_std =  locmean("victory", "doors_capacity_std")
mean_win_doors_capacity_min =  locmean("victory", "doors_capacity_min")
mean_win_doors_capacity_max =  locmean("victory", "doors_capacity_max")
mean_win_doors_capacity_s1 =  locmean("victory", "doors_capacity_s1")
mean_win_doors_capacity_s2 =  locmean("victory", "doors_capacity_s2")
mean_win_doors_capacity_s3 =  locmean("victory", "doors_capacity_s3")
mean_win_doors_capacity_s4 =  locmean("victory", "doors_capacity_s4")
mean_win_doors_capacity_s5 =  locmean("victory", "doors_capacity_s5")
mean_win_doors_capacity_s6 =  locmean("victory", "doors_capacity_s6")
mean_win_doors_capacity_s7 =  locmean("victory", "doors_capacity_s7")
mean_win_doors_capacity_s8 =  locmean("victory", "doors_capacity_s8")
mean_win_doors_capacity_s_med =  locmean("victory", "doors_capacity_s_med")
mean_win_doors_capacity_s_mean =  locmean("victory", "doors_capacity_s_mean")
mean_win_doors_capacity_s_std =  locmean("victory", "doors_capacity_s_std")
mean_win_doors_capacity_s_min =  locmean("victory", "doors_capacity_s_min")
mean_win_doors_capacity_s_max =  locmean("victory", "doors_capacity_s_max")
mean_win_doors_capacity_observation = [
    mean_win_doors_capacity_total, mean_win_doors_capacity_med, mean_win_doors_capacity_mean, mean_win_doors_capacity_std, mean_win_doors_capacity_min, 
    mean_win_doors_capacity_max, mean_win_doors_capacity_s1, mean_win_doors_capacity_s2, mean_win_doors_capacity_s3, mean_win_doors_capacity_s4,
    mean_win_doors_capacity_s5, mean_win_doors_capacity_s6, mean_win_doors_capacity_s7, mean_win_doors_capacity_s8, mean_win_doors_capacity_s_med,
    mean_win_doors_capacity_s_mean, mean_win_doors_capacity_s_std, mean_win_doors_capacity_s_min, mean_win_doors_capacity_s_max,
]

mean_loss_doors_capacity_total = locmean("loss", "doors_capacity_total")
mean_loss_doors_capacity_med =  locmean("loss", "doors_capacity_med")
mean_loss_doors_capacity_mean =  locmean("loss", "doors_capacity_mean")
mean_loss_doors_capacity_std =  locmean("loss", "doors_capacity_std")
mean_loss_doors_capacity_min =  locmean("loss", "doors_capacity_min")
mean_loss_doors_capacity_max =  locmean("loss", "doors_capacity_max")
mean_loss_doors_capacity_s1 =  locmean("loss", "doors_capacity_s1")
mean_loss_doors_capacity_s2 =  locmean("loss", "doors_capacity_s2")
mean_loss_doors_capacity_s3 =  locmean("loss", "doors_capacity_s3")
mean_loss_doors_capacity_s4 =  locmean("loss", "doors_capacity_s4")
mean_loss_doors_capacity_s5 =  locmean("loss", "doors_capacity_s5")
mean_loss_doors_capacity_s6 =  locmean("loss", "doors_capacity_s6")
mean_loss_doors_capacity_s7 =  locmean("loss", "doors_capacity_s7")
mean_loss_doors_capacity_s8 =  locmean("loss", "doors_capacity_s8")
mean_loss_doors_capacity_s_med =  locmean("loss", "doors_capacity_s_med")
mean_loss_doors_capacity_s_mean =  locmean("loss", "doors_capacity_s_mean")
mean_loss_doors_capacity_s_std =  locmean("loss", "doors_capacity_s_std")
mean_loss_doors_capacity_s_min =  locmean("loss", "doors_capacity_s_min")
mean_loss_doors_capacity_s_max =  locmean("loss", "doors_capacity_s_max")
mean_loss_doors_capacity_observation = [
    mean_loss_doors_capacity_total, mean_loss_doors_capacity_med, mean_loss_doors_capacity_mean, mean_loss_doors_capacity_std, mean_loss_doors_capacity_min, 
    mean_loss_doors_capacity_max, mean_loss_doors_capacity_s1, mean_loss_doors_capacity_s2, mean_loss_doors_capacity_s3, mean_loss_doors_capacity_s4,
    mean_loss_doors_capacity_s5, mean_loss_doors_capacity_s6, mean_loss_doors_capacity_s7, mean_loss_doors_capacity_s8, mean_loss_doors_capacity_s_med,
    mean_loss_doors_capacity_s_mean, mean_loss_doors_capacity_s_std, mean_loss_doors_capacity_s_min, mean_loss_doors_capacity_s_max,
]

# drone_capacity
drone_capacity_total = df["drone_capacity_total"].iloc[-1]
drone_capacity_med = df["drone_capacity_med"].iloc[-1]
drone_capacity_mean = df["drone_capacity_mean"].iloc[-1]
drone_capacity_std = df["drone_capacity_std"].iloc[-1]
drone_capacity_min = df["drone_capacity_min"].iloc[-1]
drone_capacity_max = df["drone_capacity_max"].iloc[-1]
drone_capacity_s1 = df["drone_capacity_s1"].iloc[-1]
drone_capacity_s2 = df["drone_capacity_s2"].iloc[-1]
drone_capacity_s3 = df["drone_capacity_s3"].iloc[-1]
drone_capacity_s4 = df["drone_capacity_s4"].iloc[-1]
drone_capacity_s5 = df["drone_capacity_s5"].iloc[-1]
drone_capacity_s6 = df["drone_capacity_s6"].iloc[-1]
drone_capacity_s7 = df["drone_capacity_s7"].iloc[-1]
drone_capacity_s8 = df["drone_capacity_s8"].iloc[-1]
drone_capacity_s_med = df["drone_capacity_s_med"].iloc[-1]
drone_capacity_s_mean = df["drone_capacity_s_mean"].iloc[-1]
drone_capacity_s_std = df["drone_capacity_s_std"].iloc[-1]
drone_capacity_s_min = df["drone_capacity_s_min"].iloc[-1]
drone_capacity_s_max = df["drone_capacity_s_max"].iloc[-1]
drone_capacity_observation = [
    drone_capacity_total, drone_capacity_med, drone_capacity_mean, drone_capacity_std, drone_capacity_min, drone_capacity_max, drone_capacity_s1,
    drone_capacity_s2, drone_capacity_s3,drone_capacity_s4, drone_capacity_s5, drone_capacity_s6, drone_capacity_s7, drone_capacity_s8,
    drone_capacity_s_med, drone_capacity_s_mean, drone_capacity_s_std, drone_capacity_s_min, drone_capacity_s_max,
]

mean_drone_capacity_total = mean("drone_capacity_total")
mean_drone_capacity_med = mean("drone_capacity_med")
mean_drone_capacity_mean = mean("drone_capacity_mean")
mean_drone_capacity_std = mean("drone_capacity_std")
mean_drone_capacity_min = mean("drone_capacity_min")
mean_drone_capacity_max = mean("drone_capacity_max")
mean_drone_capacity_s1 = mean("drone_capacity_s1")
mean_drone_capacity_s2 = mean("drone_capacity_s2")
mean_drone_capacity_s3 = mean("drone_capacity_s3")
mean_drone_capacity_s4 = mean("drone_capacity_s4")
mean_drone_capacity_s5 = mean("drone_capacity_s5")
mean_drone_capacity_s6 = mean("drone_capacity_s6")
mean_drone_capacity_s7 = mean("drone_capacity_s7")
mean_drone_capacity_s8 = mean("drone_capacity_s8")
mean_drone_capacity_s_med = mean("drone_capacity_s_med")
mean_drone_capacity_s_mean = mean("drone_capacity_s_mean")
mean_drone_capacity_s_std = mean("drone_capacity_s_std")
mean_drone_capacity_s_min = mean("drone_capacity_s_min")
mean_drone_capacity_s_max = mean("drone_capacity_s_max")
mean_drone_capacity_observation = [
    mean_drone_capacity_total, mean_drone_capacity_med, mean_drone_capacity_mean, mean_drone_capacity_std, mean_drone_capacity_min, 
    mean_drone_capacity_max, mean_drone_capacity_s1, mean_drone_capacity_s2, mean_drone_capacity_s3, mean_drone_capacity_s4,
    mean_drone_capacity_s5, mean_drone_capacity_s6, mean_drone_capacity_s7, mean_drone_capacity_s8, mean_drone_capacity_s_med,
    mean_drone_capacity_s_mean, mean_drone_capacity_s_std, mean_drone_capacity_s_min, mean_drone_capacity_s_max,
]

mean_win_drone_capacity_total = locmean("victory", "drone_capacity_total")
mean_win_drone_capacity_med =  locmean("victory", "drone_capacity_med")
mean_win_drone_capacity_mean =  locmean("victory", "drone_capacity_mean")
mean_win_drone_capacity_std =  locmean("victory", "drone_capacity_std")
mean_win_drone_capacity_min =  locmean("victory", "drone_capacity_min")
mean_win_drone_capacity_max =  locmean("victory", "drone_capacity_max")
mean_win_drone_capacity_s1 =  locmean("victory", "drone_capacity_s1")
mean_win_drone_capacity_s2 =  locmean("victory", "drone_capacity_s2")
mean_win_drone_capacity_s3 =  locmean("victory", "drone_capacity_s3")
mean_win_drone_capacity_s4 =  locmean("victory", "drone_capacity_s4")
mean_win_drone_capacity_s5 =  locmean("victory", "drone_capacity_s5")
mean_win_drone_capacity_s6 =  locmean("victory", "drone_capacity_s6")
mean_win_drone_capacity_s7 =  locmean("victory", "drone_capacity_s7")
mean_win_drone_capacity_s8 =  locmean("victory", "drone_capacity_s8")
mean_win_drone_capacity_s_med =  locmean("victory", "drone_capacity_s_med")
mean_win_drone_capacity_s_mean =  locmean("victory", "drone_capacity_s_mean")
mean_win_drone_capacity_s_std =  locmean("victory", "drone_capacity_s_std")
mean_win_drone_capacity_s_min =  locmean("victory", "drone_capacity_s_min")
mean_win_drone_capacity_s_max =  locmean("victory", "drone_capacity_s_max")
mean_win_drone_capacity_observation = [
    mean_win_drone_capacity_total, mean_win_drone_capacity_med, mean_win_drone_capacity_mean, mean_win_drone_capacity_std, mean_win_drone_capacity_min, 
    mean_win_drone_capacity_max, mean_win_drone_capacity_s1, mean_win_drone_capacity_s2, mean_win_drone_capacity_s3, mean_win_drone_capacity_s4,
    mean_win_drone_capacity_s5, mean_win_drone_capacity_s6, mean_win_drone_capacity_s7, mean_win_drone_capacity_s8, mean_win_drone_capacity_s_med,
    mean_win_drone_capacity_s_mean, mean_win_drone_capacity_s_std, mean_win_drone_capacity_s_min, mean_win_drone_capacity_s_max,
]

mean_loss_drone_capacity_total = locmean("loss", "drone_capacity_total")
mean_loss_drone_capacity_med =  locmean("loss", "drone_capacity_med")
mean_loss_drone_capacity_mean =  locmean("loss", "drone_capacity_mean")
mean_loss_drone_capacity_std =  locmean("loss", "drone_capacity_std")
mean_loss_drone_capacity_min =  locmean("loss", "drone_capacity_min")
mean_loss_drone_capacity_max =  locmean("loss", "drone_capacity_max")
mean_loss_drone_capacity_s1 =  locmean("loss", "drone_capacity_s1")
mean_loss_drone_capacity_s2 =  locmean("loss", "drone_capacity_s2")
mean_loss_drone_capacity_s3 =  locmean("loss", "drone_capacity_s3")
mean_loss_drone_capacity_s4 =  locmean("loss", "drone_capacity_s4")
mean_loss_drone_capacity_s5 =  locmean("loss", "drone_capacity_s5")
mean_loss_drone_capacity_s6 =  locmean("loss", "drone_capacity_s6")
mean_loss_drone_capacity_s7 =  locmean("loss", "drone_capacity_s7")
mean_loss_drone_capacity_s8 =  locmean("loss", "drone_capacity_s8")
mean_loss_drone_capacity_s_med =  locmean("loss", "drone_capacity_s_med")
mean_loss_drone_capacity_s_mean =  locmean("loss", "drone_capacity_s_mean")
mean_loss_drone_capacity_s_std =  locmean("loss", "drone_capacity_s_std")
mean_loss_drone_capacity_s_min =  locmean("loss", "drone_capacity_s_min")
mean_loss_drone_capacity_s_max =  locmean("loss", "drone_capacity_s_max")
mean_loss_drone_capacity_observation = [
    mean_loss_drone_capacity_total, mean_loss_drone_capacity_med, mean_loss_drone_capacity_mean, mean_loss_drone_capacity_std, mean_loss_drone_capacity_min, 
    mean_loss_drone_capacity_max, mean_loss_drone_capacity_s1, mean_loss_drone_capacity_s2, mean_loss_drone_capacity_s3, mean_loss_drone_capacity_s4,
    mean_loss_drone_capacity_s5, mean_loss_drone_capacity_s6, mean_loss_drone_capacity_s7, mean_loss_drone_capacity_s8, mean_loss_drone_capacity_s_med,
    mean_loss_drone_capacity_s_mean, mean_loss_drone_capacity_s_std, mean_loss_drone_capacity_s_min, mean_loss_drone_capacity_s_max,
]

# teleporter_capacity
teleporter_capacity_total = df["teleporter_capacity_total"].iloc[-1]
teleporter_capacity_med = df["teleporter_capacity_med"].iloc[-1]
teleporter_capacity_mean = df["teleporter_capacity_mean"].iloc[-1]
teleporter_capacity_std = df["teleporter_capacity_std"].iloc[-1]
teleporter_capacity_min = df["teleporter_capacity_min"].iloc[-1]
teleporter_capacity_max = df["teleporter_capacity_max"].iloc[-1]
teleporter_capacity_s1 = df["teleporter_capacity_s1"].iloc[-1]
teleporter_capacity_s2 = df["teleporter_capacity_s2"].iloc[-1]
teleporter_capacity_s3 = df["teleporter_capacity_s3"].iloc[-1]
teleporter_capacity_s4 = df["teleporter_capacity_s4"].iloc[-1]
teleporter_capacity_s5 = df["teleporter_capacity_s5"].iloc[-1]
teleporter_capacity_s6 = df["teleporter_capacity_s6"].iloc[-1]
teleporter_capacity_s7 = df["teleporter_capacity_s7"].iloc[-1]
teleporter_capacity_s8 = df["teleporter_capacity_s8"].iloc[-1]
teleporter_capacity_s_med = df["teleporter_capacity_s_med"].iloc[-1]
teleporter_capacity_s_mean = df["teleporter_capacity_s_mean"].iloc[-1]
teleporter_capacity_s_std = df["teleporter_capacity_s_std"].iloc[-1]
teleporter_capacity_s_min = df["teleporter_capacity_s_min"].iloc[-1]
teleporter_capacity_s_max = df["teleporter_capacity_s_max"].iloc[-1]
teleporter_capacity_observation = [
    teleporter_capacity_total, teleporter_capacity_med, teleporter_capacity_mean, teleporter_capacity_std, teleporter_capacity_min, teleporter_capacity_max, teleporter_capacity_s1,
    teleporter_capacity_s2, teleporter_capacity_s3,teleporter_capacity_s4, teleporter_capacity_s5, teleporter_capacity_s6, teleporter_capacity_s7, teleporter_capacity_s8,
    teleporter_capacity_s_med, teleporter_capacity_s_mean, teleporter_capacity_s_std, teleporter_capacity_s_min, teleporter_capacity_s_max,
]

mean_teleporter_capacity_total = mean("teleporter_capacity_total")
mean_teleporter_capacity_med = mean("teleporter_capacity_med")
mean_teleporter_capacity_mean = mean("teleporter_capacity_mean")
mean_teleporter_capacity_std = mean("teleporter_capacity_std")
mean_teleporter_capacity_min = mean("teleporter_capacity_min")
mean_teleporter_capacity_max = mean("teleporter_capacity_max")
mean_teleporter_capacity_s1 = mean("teleporter_capacity_s1")
mean_teleporter_capacity_s2 = mean("teleporter_capacity_s2")
mean_teleporter_capacity_s3 = mean("teleporter_capacity_s3")
mean_teleporter_capacity_s4 = mean("teleporter_capacity_s4")
mean_teleporter_capacity_s5 = mean("teleporter_capacity_s5")
mean_teleporter_capacity_s6 = mean("teleporter_capacity_s6")
mean_teleporter_capacity_s7 = mean("teleporter_capacity_s7")
mean_teleporter_capacity_s8 = mean("teleporter_capacity_s8")
mean_teleporter_capacity_s_med = mean("teleporter_capacity_s_med")
mean_teleporter_capacity_s_mean = mean("teleporter_capacity_s_mean")
mean_teleporter_capacity_s_std = mean("teleporter_capacity_s_std")
mean_teleporter_capacity_s_min = mean("teleporter_capacity_s_min")
mean_teleporter_capacity_s_max = mean("teleporter_capacity_s_max")
mean_teleporter_capacity_observation = [
    mean_teleporter_capacity_total, mean_teleporter_capacity_med, mean_teleporter_capacity_mean, mean_teleporter_capacity_std, mean_teleporter_capacity_min, 
    mean_teleporter_capacity_max, mean_teleporter_capacity_s1, mean_teleporter_capacity_s2, mean_teleporter_capacity_s3, mean_teleporter_capacity_s4,
    mean_teleporter_capacity_s5, mean_teleporter_capacity_s6, mean_teleporter_capacity_s7, mean_teleporter_capacity_s8, mean_teleporter_capacity_s_med,
    mean_teleporter_capacity_s_mean, mean_teleporter_capacity_s_std, mean_teleporter_capacity_s_min, mean_teleporter_capacity_s_max,
]

mean_win_teleporter_capacity_total = locmean("victory", "teleporter_capacity_total")
mean_win_teleporter_capacity_med =  locmean("victory", "teleporter_capacity_med")
mean_win_teleporter_capacity_mean =  locmean("victory", "teleporter_capacity_mean")
mean_win_teleporter_capacity_std =  locmean("victory", "teleporter_capacity_std")
mean_win_teleporter_capacity_min =  locmean("victory", "teleporter_capacity_min")
mean_win_teleporter_capacity_max =  locmean("victory", "teleporter_capacity_max")
mean_win_teleporter_capacity_s1 =  locmean("victory", "teleporter_capacity_s1")
mean_win_teleporter_capacity_s2 =  locmean("victory", "teleporter_capacity_s2")
mean_win_teleporter_capacity_s3 =  locmean("victory", "teleporter_capacity_s3")
mean_win_teleporter_capacity_s4 =  locmean("victory", "teleporter_capacity_s4")
mean_win_teleporter_capacity_s5 =  locmean("victory", "teleporter_capacity_s5")
mean_win_teleporter_capacity_s6 =  locmean("victory", "teleporter_capacity_s6")
mean_win_teleporter_capacity_s7 =  locmean("victory", "teleporter_capacity_s7")
mean_win_teleporter_capacity_s8 =  locmean("victory", "teleporter_capacity_s8")
mean_win_teleporter_capacity_s_med =  locmean("victory", "teleporter_capacity_s_med")
mean_win_teleporter_capacity_s_mean =  locmean("victory", "teleporter_capacity_s_mean")
mean_win_teleporter_capacity_s_std =  locmean("victory", "teleporter_capacity_s_std")
mean_win_teleporter_capacity_s_min =  locmean("victory", "teleporter_capacity_s_min")
mean_win_teleporter_capacity_s_max =  locmean("victory", "teleporter_capacity_s_max")
mean_win_teleporter_capacity_observation = [
    mean_win_teleporter_capacity_total, mean_win_teleporter_capacity_med, mean_win_teleporter_capacity_mean, mean_win_teleporter_capacity_std, mean_win_teleporter_capacity_min, 
    mean_win_teleporter_capacity_max, mean_win_teleporter_capacity_s1, mean_win_teleporter_capacity_s2, mean_win_teleporter_capacity_s3, mean_win_teleporter_capacity_s4,
    mean_win_teleporter_capacity_s5, mean_win_teleporter_capacity_s6, mean_win_teleporter_capacity_s7, mean_win_teleporter_capacity_s8, mean_win_teleporter_capacity_s_med,
    mean_win_teleporter_capacity_s_mean, mean_win_teleporter_capacity_s_std, mean_win_teleporter_capacity_s_min, mean_win_teleporter_capacity_s_max,
]

mean_loss_teleporter_capacity_total = locmean("loss", "teleporter_capacity_total")
mean_loss_teleporter_capacity_med =  locmean("loss", "teleporter_capacity_med")
mean_loss_teleporter_capacity_mean =  locmean("loss", "teleporter_capacity_mean")
mean_loss_teleporter_capacity_std =  locmean("loss", "teleporter_capacity_std")
mean_loss_teleporter_capacity_min =  locmean("loss", "teleporter_capacity_min")
mean_loss_teleporter_capacity_max =  locmean("loss", "teleporter_capacity_max")
mean_loss_teleporter_capacity_s1 =  locmean("loss", "teleporter_capacity_s1")
mean_loss_teleporter_capacity_s2 =  locmean("loss", "teleporter_capacity_s2")
mean_loss_teleporter_capacity_s3 =  locmean("loss", "teleporter_capacity_s3")
mean_loss_teleporter_capacity_s4 =  locmean("loss", "teleporter_capacity_s4")
mean_loss_teleporter_capacity_s5 =  locmean("loss", "teleporter_capacity_s5")
mean_loss_teleporter_capacity_s6 =  locmean("loss", "teleporter_capacity_s6")
mean_loss_teleporter_capacity_s7 =  locmean("loss", "teleporter_capacity_s7")
mean_loss_teleporter_capacity_s8 =  locmean("loss", "teleporter_capacity_s8")
mean_loss_teleporter_capacity_s_med =  locmean("loss", "teleporter_capacity_s_med")
mean_loss_teleporter_capacity_s_mean =  locmean("loss", "teleporter_capacity_s_mean")
mean_loss_teleporter_capacity_s_std =  locmean("loss", "teleporter_capacity_s_std")
mean_loss_teleporter_capacity_s_min =  locmean("loss", "teleporter_capacity_s_min")
mean_loss_teleporter_capacity_s_max =  locmean("loss", "teleporter_capacity_s_max")
mean_loss_teleporter_capacity_observation = [
    mean_loss_teleporter_capacity_total, mean_loss_teleporter_capacity_med, mean_loss_teleporter_capacity_mean, mean_loss_teleporter_capacity_std, mean_loss_teleporter_capacity_min, 
    mean_loss_teleporter_capacity_max, mean_loss_teleporter_capacity_s1, mean_loss_teleporter_capacity_s2, mean_loss_teleporter_capacity_s3, mean_loss_teleporter_capacity_s4,
    mean_loss_teleporter_capacity_s5, mean_loss_teleporter_capacity_s6, mean_loss_teleporter_capacity_s7, mean_loss_teleporter_capacity_s8, mean_loss_teleporter_capacity_s_med,
    mean_loss_teleporter_capacity_s_mean, mean_loss_teleporter_capacity_s_std, mean_loss_teleporter_capacity_s_min, mean_loss_teleporter_capacity_s_max,
]

# cloaking_capacity
cloaking_capacity_total = df["cloaking_capacity_total"].iloc[-1]
cloaking_capacity_med = df["cloaking_capacity_med"].iloc[-1]
cloaking_capacity_mean = df["cloaking_capacity_mean"].iloc[-1]
cloaking_capacity_std = df["cloaking_capacity_std"].iloc[-1]
cloaking_capacity_min = df["cloaking_capacity_min"].iloc[-1]
cloaking_capacity_max = df["cloaking_capacity_max"].iloc[-1]
cloaking_capacity_s1 = df["cloaking_capacity_s1"].iloc[-1]
cloaking_capacity_s2 = df["cloaking_capacity_s2"].iloc[-1]
cloaking_capacity_s3 = df["cloaking_capacity_s3"].iloc[-1]
cloaking_capacity_s4 = df["cloaking_capacity_s4"].iloc[-1]
cloaking_capacity_s5 = df["cloaking_capacity_s5"].iloc[-1]
cloaking_capacity_s6 = df["cloaking_capacity_s6"].iloc[-1]
cloaking_capacity_s7 = df["cloaking_capacity_s7"].iloc[-1]
cloaking_capacity_s8 = df["cloaking_capacity_s8"].iloc[-1]
cloaking_capacity_s_med = df["cloaking_capacity_s_med"].iloc[-1]
cloaking_capacity_s_mean = df["cloaking_capacity_s_mean"].iloc[-1]
cloaking_capacity_s_std = df["cloaking_capacity_s_std"].iloc[-1]
cloaking_capacity_s_min = df["cloaking_capacity_s_min"].iloc[-1]
cloaking_capacity_s_max = df["cloaking_capacity_s_max"].iloc[-1]
cloaking_capacity_observation = [
    cloaking_capacity_total, cloaking_capacity_med, cloaking_capacity_mean, cloaking_capacity_std, cloaking_capacity_min, cloaking_capacity_max, cloaking_capacity_s1,
    cloaking_capacity_s2, cloaking_capacity_s3,cloaking_capacity_s4, cloaking_capacity_s5, cloaking_capacity_s6, cloaking_capacity_s7, cloaking_capacity_s8,
    cloaking_capacity_s_med, cloaking_capacity_s_mean, cloaking_capacity_s_std, cloaking_capacity_s_min, cloaking_capacity_s_max,
]

mean_cloaking_capacity_total = mean("cloaking_capacity_total")
mean_cloaking_capacity_med = mean("cloaking_capacity_med")
mean_cloaking_capacity_mean = mean("cloaking_capacity_mean")
mean_cloaking_capacity_std = mean("cloaking_capacity_std")
mean_cloaking_capacity_min = mean("cloaking_capacity_min")
mean_cloaking_capacity_max = mean("cloaking_capacity_max")
mean_cloaking_capacity_s1 = mean("cloaking_capacity_s1")
mean_cloaking_capacity_s2 = mean("cloaking_capacity_s2")
mean_cloaking_capacity_s3 = mean("cloaking_capacity_s3")
mean_cloaking_capacity_s4 = mean("cloaking_capacity_s4")
mean_cloaking_capacity_s5 = mean("cloaking_capacity_s5")
mean_cloaking_capacity_s6 = mean("cloaking_capacity_s6")
mean_cloaking_capacity_s7 = mean("cloaking_capacity_s7")
mean_cloaking_capacity_s8 = mean("cloaking_capacity_s8")
mean_cloaking_capacity_s_med = mean("cloaking_capacity_s_med")
mean_cloaking_capacity_s_mean = mean("cloaking_capacity_s_mean")
mean_cloaking_capacity_s_std = mean("cloaking_capacity_s_std")
mean_cloaking_capacity_s_min = mean("cloaking_capacity_s_min")
mean_cloaking_capacity_s_max = mean("cloaking_capacity_s_max")
mean_cloaking_capacity_observation = [
    mean_cloaking_capacity_total, mean_cloaking_capacity_med, mean_cloaking_capacity_mean, mean_cloaking_capacity_std, mean_cloaking_capacity_min, 
    mean_cloaking_capacity_max, mean_cloaking_capacity_s1, mean_cloaking_capacity_s2, mean_cloaking_capacity_s3, mean_cloaking_capacity_s4,
    mean_cloaking_capacity_s5, mean_cloaking_capacity_s6, mean_cloaking_capacity_s7, mean_cloaking_capacity_s8, mean_cloaking_capacity_s_med,
    mean_cloaking_capacity_s_mean, mean_cloaking_capacity_s_std, mean_cloaking_capacity_s_min, mean_cloaking_capacity_s_max,
]

mean_win_cloaking_capacity_total = locmean("victory", "cloaking_capacity_total")
mean_win_cloaking_capacity_med =  locmean("victory", "cloaking_capacity_med")
mean_win_cloaking_capacity_mean =  locmean("victory", "cloaking_capacity_mean")
mean_win_cloaking_capacity_std =  locmean("victory", "cloaking_capacity_std")
mean_win_cloaking_capacity_min =  locmean("victory", "cloaking_capacity_min")
mean_win_cloaking_capacity_max =  locmean("victory", "cloaking_capacity_max")
mean_win_cloaking_capacity_s1 =  locmean("victory", "cloaking_capacity_s1")
mean_win_cloaking_capacity_s2 =  locmean("victory", "cloaking_capacity_s2")
mean_win_cloaking_capacity_s3 =  locmean("victory", "cloaking_capacity_s3")
mean_win_cloaking_capacity_s4 =  locmean("victory", "cloaking_capacity_s4")
mean_win_cloaking_capacity_s5 =  locmean("victory", "cloaking_capacity_s5")
mean_win_cloaking_capacity_s6 =  locmean("victory", "cloaking_capacity_s6")
mean_win_cloaking_capacity_s7 =  locmean("victory", "cloaking_capacity_s7")
mean_win_cloaking_capacity_s8 =  locmean("victory", "cloaking_capacity_s8")
mean_win_cloaking_capacity_s_med =  locmean("victory", "cloaking_capacity_s_med")
mean_win_cloaking_capacity_s_mean =  locmean("victory", "cloaking_capacity_s_mean")
mean_win_cloaking_capacity_s_std =  locmean("victory", "cloaking_capacity_s_std")
mean_win_cloaking_capacity_s_min =  locmean("victory", "cloaking_capacity_s_min")
mean_win_cloaking_capacity_s_max =  locmean("victory", "cloaking_capacity_s_max")
mean_win_cloaking_capacity_observation = [
    mean_win_cloaking_capacity_total, mean_win_cloaking_capacity_med, mean_win_cloaking_capacity_mean, mean_win_cloaking_capacity_std, mean_win_cloaking_capacity_min, 
    mean_win_cloaking_capacity_max, mean_win_cloaking_capacity_s1, mean_win_cloaking_capacity_s2, mean_win_cloaking_capacity_s3, mean_win_cloaking_capacity_s4,
    mean_win_cloaking_capacity_s5, mean_win_cloaking_capacity_s6, mean_win_cloaking_capacity_s7, mean_win_cloaking_capacity_s8, mean_win_cloaking_capacity_s_med,
    mean_win_cloaking_capacity_s_mean, mean_win_cloaking_capacity_s_std, mean_win_cloaking_capacity_s_min, mean_win_cloaking_capacity_s_max,
]

mean_loss_cloaking_capacity_total = locmean("loss", "cloaking_capacity_total")
mean_loss_cloaking_capacity_med =  locmean("loss", "cloaking_capacity_med")
mean_loss_cloaking_capacity_mean =  locmean("loss", "cloaking_capacity_mean")
mean_loss_cloaking_capacity_std =  locmean("loss", "cloaking_capacity_std")
mean_loss_cloaking_capacity_min =  locmean("loss", "cloaking_capacity_min")
mean_loss_cloaking_capacity_max =  locmean("loss", "cloaking_capacity_max")
mean_loss_cloaking_capacity_s1 =  locmean("loss", "cloaking_capacity_s1")
mean_loss_cloaking_capacity_s2 =  locmean("loss", "cloaking_capacity_s2")
mean_loss_cloaking_capacity_s3 =  locmean("loss", "cloaking_capacity_s3")
mean_loss_cloaking_capacity_s4 =  locmean("loss", "cloaking_capacity_s4")
mean_loss_cloaking_capacity_s5 =  locmean("loss", "cloaking_capacity_s5")
mean_loss_cloaking_capacity_s6 =  locmean("loss", "cloaking_capacity_s6")
mean_loss_cloaking_capacity_s7 =  locmean("loss", "cloaking_capacity_s7")
mean_loss_cloaking_capacity_s8 =  locmean("loss", "cloaking_capacity_s8")
mean_loss_cloaking_capacity_s_med =  locmean("loss", "cloaking_capacity_s_med")
mean_loss_cloaking_capacity_s_mean =  locmean("loss", "cloaking_capacity_s_mean")
mean_loss_cloaking_capacity_s_std =  locmean("loss", "cloaking_capacity_s_std")
mean_loss_cloaking_capacity_s_min =  locmean("loss", "cloaking_capacity_s_min")
mean_loss_cloaking_capacity_s_max =  locmean("loss", "cloaking_capacity_s_max")
mean_loss_cloaking_capacity_observation = [
    mean_loss_cloaking_capacity_total, mean_loss_cloaking_capacity_med, mean_loss_cloaking_capacity_mean, mean_loss_cloaking_capacity_std, mean_loss_cloaking_capacity_min, 
    mean_loss_cloaking_capacity_max, mean_loss_cloaking_capacity_s1, mean_loss_cloaking_capacity_s2, mean_loss_cloaking_capacity_s3, mean_loss_cloaking_capacity_s4,
    mean_loss_cloaking_capacity_s5, mean_loss_cloaking_capacity_s6, mean_loss_cloaking_capacity_s7, mean_loss_cloaking_capacity_s8, mean_loss_cloaking_capacity_s_med,
    mean_loss_cloaking_capacity_s_mean, mean_loss_cloaking_capacity_s_std, mean_loss_cloaking_capacity_s_min, mean_loss_cloaking_capacity_s_max,
]

# mindcontrol_capacity
mindcontrol_capacity_total = df["mindcontrol_capacity_total"].iloc[-1]
mindcontrol_capacity_med = df["mindcontrol_capacity_med"].iloc[-1]
mindcontrol_capacity_mean = df["mindcontrol_capacity_mean"].iloc[-1]
mindcontrol_capacity_std = df["mindcontrol_capacity_std"].iloc[-1]
mindcontrol_capacity_min = df["mindcontrol_capacity_min"].iloc[-1]
mindcontrol_capacity_max = df["mindcontrol_capacity_max"].iloc[-1]
mindcontrol_capacity_s1 = df["mindcontrol_capacity_s1"].iloc[-1]
mindcontrol_capacity_s2 = df["mindcontrol_capacity_s2"].iloc[-1]
mindcontrol_capacity_s3 = df["mindcontrol_capacity_s3"].iloc[-1]
mindcontrol_capacity_s4 = df["mindcontrol_capacity_s4"].iloc[-1]
mindcontrol_capacity_s5 = df["mindcontrol_capacity_s5"].iloc[-1]
mindcontrol_capacity_s6 = df["mindcontrol_capacity_s6"].iloc[-1]
mindcontrol_capacity_s7 = df["mindcontrol_capacity_s7"].iloc[-1]
mindcontrol_capacity_s8 = df["mindcontrol_capacity_s8"].iloc[-1]
mindcontrol_capacity_s_med = df["mindcontrol_capacity_s_med"].iloc[-1]
mindcontrol_capacity_s_mean = df["mindcontrol_capacity_s_mean"].iloc[-1]
mindcontrol_capacity_s_std = df["mindcontrol_capacity_s_std"].iloc[-1]
mindcontrol_capacity_s_min = df["mindcontrol_capacity_s_min"].iloc[-1]
mindcontrol_capacity_s_max = df["mindcontrol_capacity_s_max"].iloc[-1]
mindcontrol_capacity_observation = [
    mindcontrol_capacity_total, mindcontrol_capacity_med, mindcontrol_capacity_mean, mindcontrol_capacity_std, mindcontrol_capacity_min, mindcontrol_capacity_max, mindcontrol_capacity_s1,
    mindcontrol_capacity_s2, mindcontrol_capacity_s3,mindcontrol_capacity_s4, mindcontrol_capacity_s5, mindcontrol_capacity_s6, mindcontrol_capacity_s7, mindcontrol_capacity_s8,
    mindcontrol_capacity_s_med, mindcontrol_capacity_s_mean, mindcontrol_capacity_s_std, mindcontrol_capacity_s_min, mindcontrol_capacity_s_max,
]

mean_mindcontrol_capacity_total = mean("mindcontrol_capacity_total")
mean_mindcontrol_capacity_med = mean("mindcontrol_capacity_med")
mean_mindcontrol_capacity_mean = mean("mindcontrol_capacity_mean")
mean_mindcontrol_capacity_std = mean("mindcontrol_capacity_std")
mean_mindcontrol_capacity_min = mean("mindcontrol_capacity_min")
mean_mindcontrol_capacity_max = mean("mindcontrol_capacity_max")
mean_mindcontrol_capacity_s1 = mean("mindcontrol_capacity_s1")
mean_mindcontrol_capacity_s2 = mean("mindcontrol_capacity_s2")
mean_mindcontrol_capacity_s3 = mean("mindcontrol_capacity_s3")
mean_mindcontrol_capacity_s4 = mean("mindcontrol_capacity_s4")
mean_mindcontrol_capacity_s5 = mean("mindcontrol_capacity_s5")
mean_mindcontrol_capacity_s6 = mean("mindcontrol_capacity_s6")
mean_mindcontrol_capacity_s7 = mean("mindcontrol_capacity_s7")
mean_mindcontrol_capacity_s8 = mean("mindcontrol_capacity_s8")
mean_mindcontrol_capacity_s_med = mean("mindcontrol_capacity_s_med")
mean_mindcontrol_capacity_s_mean = mean("mindcontrol_capacity_s_mean")
mean_mindcontrol_capacity_s_std = mean("mindcontrol_capacity_s_std")
mean_mindcontrol_capacity_s_min = mean("mindcontrol_capacity_s_min")
mean_mindcontrol_capacity_s_max = mean("mindcontrol_capacity_s_max")
mean_mindcontrol_capacity_observation = [
    mean_mindcontrol_capacity_total, mean_mindcontrol_capacity_med, mean_mindcontrol_capacity_mean, mean_mindcontrol_capacity_std, mean_mindcontrol_capacity_min, 
    mean_mindcontrol_capacity_max, mean_mindcontrol_capacity_s1, mean_mindcontrol_capacity_s2, mean_mindcontrol_capacity_s3, mean_mindcontrol_capacity_s4,
    mean_mindcontrol_capacity_s5, mean_mindcontrol_capacity_s6, mean_mindcontrol_capacity_s7, mean_mindcontrol_capacity_s8, mean_mindcontrol_capacity_s_med,
    mean_mindcontrol_capacity_s_mean, mean_mindcontrol_capacity_s_std, mean_mindcontrol_capacity_s_min, mean_mindcontrol_capacity_s_max,
]

mean_win_mindcontrol_capacity_total = locmean("victory", "mindcontrol_capacity_total")
mean_win_mindcontrol_capacity_med =  locmean("victory", "mindcontrol_capacity_med")
mean_win_mindcontrol_capacity_mean =  locmean("victory", "mindcontrol_capacity_mean")
mean_win_mindcontrol_capacity_std =  locmean("victory", "mindcontrol_capacity_std")
mean_win_mindcontrol_capacity_min =  locmean("victory", "mindcontrol_capacity_min")
mean_win_mindcontrol_capacity_max =  locmean("victory", "mindcontrol_capacity_max")
mean_win_mindcontrol_capacity_s1 =  locmean("victory", "mindcontrol_capacity_s1")
mean_win_mindcontrol_capacity_s2 =  locmean("victory", "mindcontrol_capacity_s2")
mean_win_mindcontrol_capacity_s3 =  locmean("victory", "mindcontrol_capacity_s3")
mean_win_mindcontrol_capacity_s4 =  locmean("victory", "mindcontrol_capacity_s4")
mean_win_mindcontrol_capacity_s5 =  locmean("victory", "mindcontrol_capacity_s5")
mean_win_mindcontrol_capacity_s6 =  locmean("victory", "mindcontrol_capacity_s6")
mean_win_mindcontrol_capacity_s7 =  locmean("victory", "mindcontrol_capacity_s7")
mean_win_mindcontrol_capacity_s8 =  locmean("victory", "mindcontrol_capacity_s8")
mean_win_mindcontrol_capacity_s_med =  locmean("victory", "mindcontrol_capacity_s_med")
mean_win_mindcontrol_capacity_s_mean =  locmean("victory", "mindcontrol_capacity_s_mean")
mean_win_mindcontrol_capacity_s_std =  locmean("victory", "mindcontrol_capacity_s_std")
mean_win_mindcontrol_capacity_s_min =  locmean("victory", "mindcontrol_capacity_s_min")
mean_win_mindcontrol_capacity_s_max =  locmean("victory", "mindcontrol_capacity_s_max")
mean_win_mindcontrol_capacity_observation = [
    mean_win_mindcontrol_capacity_total, mean_win_mindcontrol_capacity_med, mean_win_mindcontrol_capacity_mean, mean_win_mindcontrol_capacity_std, mean_win_mindcontrol_capacity_min, 
    mean_win_mindcontrol_capacity_max, mean_win_mindcontrol_capacity_s1, mean_win_mindcontrol_capacity_s2, mean_win_mindcontrol_capacity_s3, mean_win_mindcontrol_capacity_s4,
    mean_win_mindcontrol_capacity_s5, mean_win_mindcontrol_capacity_s6, mean_win_mindcontrol_capacity_s7, mean_win_mindcontrol_capacity_s8, mean_win_mindcontrol_capacity_s_med,
    mean_win_mindcontrol_capacity_s_mean, mean_win_mindcontrol_capacity_s_std, mean_win_mindcontrol_capacity_s_min, mean_win_mindcontrol_capacity_s_max,
]

mean_loss_mindcontrol_capacity_total = locmean("loss", "mindcontrol_capacity_total")
mean_loss_mindcontrol_capacity_med =  locmean("loss", "mindcontrol_capacity_med")
mean_loss_mindcontrol_capacity_mean =  locmean("loss", "mindcontrol_capacity_mean")
mean_loss_mindcontrol_capacity_std =  locmean("loss", "mindcontrol_capacity_std")
mean_loss_mindcontrol_capacity_min =  locmean("loss", "mindcontrol_capacity_min")
mean_loss_mindcontrol_capacity_max =  locmean("loss", "mindcontrol_capacity_max")
mean_loss_mindcontrol_capacity_s1 =  locmean("loss", "mindcontrol_capacity_s1")
mean_loss_mindcontrol_capacity_s2 =  locmean("loss", "mindcontrol_capacity_s2")
mean_loss_mindcontrol_capacity_s3 =  locmean("loss", "mindcontrol_capacity_s3")
mean_loss_mindcontrol_capacity_s4 =  locmean("loss", "mindcontrol_capacity_s4")
mean_loss_mindcontrol_capacity_s5 =  locmean("loss", "mindcontrol_capacity_s5")
mean_loss_mindcontrol_capacity_s6 =  locmean("loss", "mindcontrol_capacity_s6")
mean_loss_mindcontrol_capacity_s7 =  locmean("loss", "mindcontrol_capacity_s7")
mean_loss_mindcontrol_capacity_s8 =  locmean("loss", "mindcontrol_capacity_s8")
mean_loss_mindcontrol_capacity_s_med =  locmean("loss", "mindcontrol_capacity_s_med")
mean_loss_mindcontrol_capacity_s_mean =  locmean("loss", "mindcontrol_capacity_s_mean")
mean_loss_mindcontrol_capacity_s_std =  locmean("loss", "mindcontrol_capacity_s_std")
mean_loss_mindcontrol_capacity_s_min =  locmean("loss", "mindcontrol_capacity_s_min")
mean_loss_mindcontrol_capacity_s_max =  locmean("loss", "mindcontrol_capacity_s_max")
mean_loss_mindcontrol_capacity_observation = [
    mean_loss_mindcontrol_capacity_total, mean_loss_mindcontrol_capacity_med, mean_loss_mindcontrol_capacity_mean, mean_loss_mindcontrol_capacity_std, mean_loss_mindcontrol_capacity_min, 
    mean_loss_mindcontrol_capacity_max, mean_loss_mindcontrol_capacity_s1, mean_loss_mindcontrol_capacity_s2, mean_loss_mindcontrol_capacity_s3, mean_loss_mindcontrol_capacity_s4,
    mean_loss_mindcontrol_capacity_s5, mean_loss_mindcontrol_capacity_s6, mean_loss_mindcontrol_capacity_s7, mean_loss_mindcontrol_capacity_s8, mean_loss_mindcontrol_capacity_s_med,
    mean_loss_mindcontrol_capacity_s_mean, mean_loss_mindcontrol_capacity_s_std, mean_loss_mindcontrol_capacity_s_min, mean_loss_mindcontrol_capacity_s_max,
]

# hacking_capacity
hacking_capacity_total = df["hacking_capacity_total"].iloc[-1]
hacking_capacity_med = df["hacking_capacity_med"].iloc[-1]
hacking_capacity_mean = df["hacking_capacity_mean"].iloc[-1]
hacking_capacity_std = df["hacking_capacity_std"].iloc[-1]
hacking_capacity_min = df["hacking_capacity_min"].iloc[-1]
hacking_capacity_max = df["hacking_capacity_max"].iloc[-1]
hacking_capacity_s1 = df["hacking_capacity_s1"].iloc[-1]
hacking_capacity_s2 = df["hacking_capacity_s2"].iloc[-1]
hacking_capacity_s3 = df["hacking_capacity_s3"].iloc[-1]
hacking_capacity_s4 = df["hacking_capacity_s4"].iloc[-1]
hacking_capacity_s5 = df["hacking_capacity_s5"].iloc[-1]
hacking_capacity_s6 = df["hacking_capacity_s6"].iloc[-1]
hacking_capacity_s7 = df["hacking_capacity_s7"].iloc[-1]
hacking_capacity_s8 = df["hacking_capacity_s8"].iloc[-1]
hacking_capacity_s_med = df["hacking_capacity_s_med"].iloc[-1]
hacking_capacity_s_mean = df["hacking_capacity_s_mean"].iloc[-1]
hacking_capacity_s_std = df["hacking_capacity_s_std"].iloc[-1]
hacking_capacity_s_min = df["hacking_capacity_s_min"].iloc[-1]
hacking_capacity_s_max = df["hacking_capacity_s_max"].iloc[-1]
hacking_capacity_observation = [
    hacking_capacity_total, hacking_capacity_med, hacking_capacity_mean, hacking_capacity_std, hacking_capacity_min, hacking_capacity_max, hacking_capacity_s1,
    hacking_capacity_s2, hacking_capacity_s3,hacking_capacity_s4, hacking_capacity_s5, hacking_capacity_s6, hacking_capacity_s7, hacking_capacity_s8,
    hacking_capacity_s_med, hacking_capacity_s_mean, hacking_capacity_s_std, hacking_capacity_s_min, hacking_capacity_s_max,
]

mean_hacking_capacity_total = mean("hacking_capacity_total")
mean_hacking_capacity_med = mean("hacking_capacity_med")
mean_hacking_capacity_mean = mean("hacking_capacity_mean")
mean_hacking_capacity_std = mean("hacking_capacity_std")
mean_hacking_capacity_min = mean("hacking_capacity_min")
mean_hacking_capacity_max = mean("hacking_capacity_max")
mean_hacking_capacity_s1 = mean("hacking_capacity_s1")
mean_hacking_capacity_s2 = mean("hacking_capacity_s2")
mean_hacking_capacity_s3 = mean("hacking_capacity_s3")
mean_hacking_capacity_s4 = mean("hacking_capacity_s4")
mean_hacking_capacity_s5 = mean("hacking_capacity_s5")
mean_hacking_capacity_s6 = mean("hacking_capacity_s6")
mean_hacking_capacity_s7 = mean("hacking_capacity_s7")
mean_hacking_capacity_s8 = mean("hacking_capacity_s8")
mean_hacking_capacity_s_med = mean("hacking_capacity_s_med")
mean_hacking_capacity_s_mean = mean("hacking_capacity_s_mean")
mean_hacking_capacity_s_std = mean("hacking_capacity_s_std")
mean_hacking_capacity_s_min = mean("hacking_capacity_s_min")
mean_hacking_capacity_s_max = mean("hacking_capacity_s_max")
mean_hacking_capacity_observation = [
    mean_hacking_capacity_total, mean_hacking_capacity_med, mean_hacking_capacity_mean, mean_hacking_capacity_std, mean_hacking_capacity_min, 
    mean_hacking_capacity_max, mean_hacking_capacity_s1, mean_hacking_capacity_s2, mean_hacking_capacity_s3, mean_hacking_capacity_s4,
    mean_hacking_capacity_s5, mean_hacking_capacity_s6, mean_hacking_capacity_s7, mean_hacking_capacity_s8, mean_hacking_capacity_s_med,
    mean_hacking_capacity_s_mean, mean_hacking_capacity_s_std, mean_hacking_capacity_s_min, mean_hacking_capacity_s_max,
]

mean_win_hacking_capacity_total = locmean("victory", "hacking_capacity_total")
mean_win_hacking_capacity_med =  locmean("victory", "hacking_capacity_med")
mean_win_hacking_capacity_mean =  locmean("victory", "hacking_capacity_mean")
mean_win_hacking_capacity_std =  locmean("victory", "hacking_capacity_std")
mean_win_hacking_capacity_min =  locmean("victory", "hacking_capacity_min")
mean_win_hacking_capacity_max =  locmean("victory", "hacking_capacity_max")
mean_win_hacking_capacity_s1 =  locmean("victory", "hacking_capacity_s1")
mean_win_hacking_capacity_s2 =  locmean("victory", "hacking_capacity_s2")
mean_win_hacking_capacity_s3 =  locmean("victory", "hacking_capacity_s3")
mean_win_hacking_capacity_s4 =  locmean("victory", "hacking_capacity_s4")
mean_win_hacking_capacity_s5 =  locmean("victory", "hacking_capacity_s5")
mean_win_hacking_capacity_s6 =  locmean("victory", "hacking_capacity_s6")
mean_win_hacking_capacity_s7 =  locmean("victory", "hacking_capacity_s7")
mean_win_hacking_capacity_s8 =  locmean("victory", "hacking_capacity_s8")
mean_win_hacking_capacity_s_med =  locmean("victory", "hacking_capacity_s_med")
mean_win_hacking_capacity_s_mean =  locmean("victory", "hacking_capacity_s_mean")
mean_win_hacking_capacity_s_std =  locmean("victory", "hacking_capacity_s_std")
mean_win_hacking_capacity_s_min =  locmean("victory", "hacking_capacity_s_min")
mean_win_hacking_capacity_s_max =  locmean("victory", "hacking_capacity_s_max")
mean_win_hacking_capacity_observation = [
    mean_win_hacking_capacity_total, mean_win_hacking_capacity_med, mean_win_hacking_capacity_mean, mean_win_hacking_capacity_std, mean_win_hacking_capacity_min, 
    mean_win_hacking_capacity_max, mean_win_hacking_capacity_s1, mean_win_hacking_capacity_s2, mean_win_hacking_capacity_s3, mean_win_hacking_capacity_s4,
    mean_win_hacking_capacity_s5, mean_win_hacking_capacity_s6, mean_win_hacking_capacity_s7, mean_win_hacking_capacity_s8, mean_win_hacking_capacity_s_med,
    mean_win_hacking_capacity_s_mean, mean_win_hacking_capacity_s_std, mean_win_hacking_capacity_s_min, mean_win_hacking_capacity_s_max,
]

mean_loss_hacking_capacity_total = locmean("loss", "hacking_capacity_total")
mean_loss_hacking_capacity_med =  locmean("loss", "hacking_capacity_med")
mean_loss_hacking_capacity_mean =  locmean("loss", "hacking_capacity_mean")
mean_loss_hacking_capacity_std =  locmean("loss", "hacking_capacity_std")
mean_loss_hacking_capacity_min =  locmean("loss", "hacking_capacity_min")
mean_loss_hacking_capacity_max =  locmean("loss", "hacking_capacity_max")
mean_loss_hacking_capacity_s1 =  locmean("loss", "hacking_capacity_s1")
mean_loss_hacking_capacity_s2 =  locmean("loss", "hacking_capacity_s2")
mean_loss_hacking_capacity_s3 =  locmean("loss", "hacking_capacity_s3")
mean_loss_hacking_capacity_s4 =  locmean("loss", "hacking_capacity_s4")
mean_loss_hacking_capacity_s5 =  locmean("loss", "hacking_capacity_s5")
mean_loss_hacking_capacity_s6 =  locmean("loss", "hacking_capacity_s6")
mean_loss_hacking_capacity_s7 =  locmean("loss", "hacking_capacity_s7")
mean_loss_hacking_capacity_s8 =  locmean("loss", "hacking_capacity_s8")
mean_loss_hacking_capacity_s_med =  locmean("loss", "hacking_capacity_s_med")
mean_loss_hacking_capacity_s_mean =  locmean("loss", "hacking_capacity_s_mean")
mean_loss_hacking_capacity_s_std =  locmean("loss", "hacking_capacity_s_std")
mean_loss_hacking_capacity_s_min =  locmean("loss", "hacking_capacity_s_min")
mean_loss_hacking_capacity_s_max =  locmean("loss", "hacking_capacity_s_max")
mean_loss_hacking_capacity_observation = [
    mean_loss_hacking_capacity_total, mean_loss_hacking_capacity_med, mean_loss_hacking_capacity_mean, mean_loss_hacking_capacity_std, mean_loss_hacking_capacity_min, 
    mean_loss_hacking_capacity_max, mean_loss_hacking_capacity_s1, mean_loss_hacking_capacity_s2, mean_loss_hacking_capacity_s3, mean_loss_hacking_capacity_s4,
    mean_loss_hacking_capacity_s5, mean_loss_hacking_capacity_s6, mean_loss_hacking_capacity_s7, mean_loss_hacking_capacity_s8, mean_loss_hacking_capacity_s_med,
    mean_loss_hacking_capacity_s_mean, mean_loss_hacking_capacity_s_std, mean_loss_hacking_capacity_s_min, mean_loss_hacking_capacity_s_max,
]

# battery_capacity
battery_capacity_total = df["battery_capacity_total"].iloc[-1]
battery_capacity_med = df["battery_capacity_med"].iloc[-1]
battery_capacity_mean = df["battery_capacity_mean"].iloc[-1]
battery_capacity_std = df["battery_capacity_std"].iloc[-1]
battery_capacity_min = df["battery_capacity_min"].iloc[-1]
battery_capacity_max = df["battery_capacity_max"].iloc[-1]
battery_capacity_s1 = df["battery_capacity_s1"].iloc[-1]
battery_capacity_s2 = df["battery_capacity_s2"].iloc[-1]
battery_capacity_s3 = df["battery_capacity_s3"].iloc[-1]
battery_capacity_s4 = df["battery_capacity_s4"].iloc[-1]
battery_capacity_s5 = df["battery_capacity_s5"].iloc[-1]
battery_capacity_s6 = df["battery_capacity_s6"].iloc[-1]
battery_capacity_s7 = df["battery_capacity_s7"].iloc[-1]
battery_capacity_s8 = df["battery_capacity_s8"].iloc[-1]
battery_capacity_s_med = df["battery_capacity_s_med"].iloc[-1]
battery_capacity_s_mean = df["battery_capacity_s_mean"].iloc[-1]
battery_capacity_s_std = df["battery_capacity_s_std"].iloc[-1]
battery_capacity_s_min = df["battery_capacity_s_min"].iloc[-1]
battery_capacity_s_max = df["battery_capacity_s_max"].iloc[-1]
battery_capacity_observation = [
    battery_capacity_total, battery_capacity_med, battery_capacity_mean, battery_capacity_std, battery_capacity_min, battery_capacity_max, battery_capacity_s1,
    battery_capacity_s2, battery_capacity_s3,battery_capacity_s4, battery_capacity_s5, battery_capacity_s6, battery_capacity_s7, battery_capacity_s8,
    battery_capacity_s_med, battery_capacity_s_mean, battery_capacity_s_std, battery_capacity_s_min, battery_capacity_s_max,
]

mean_battery_capacity_total = mean("battery_capacity_total")
mean_battery_capacity_med = mean("battery_capacity_med")
mean_battery_capacity_mean = mean("battery_capacity_mean")
mean_battery_capacity_std = mean("battery_capacity_std")
mean_battery_capacity_min = mean("battery_capacity_min")
mean_battery_capacity_max = mean("battery_capacity_max")
mean_battery_capacity_s1 = mean("battery_capacity_s1")
mean_battery_capacity_s2 = mean("battery_capacity_s2")
mean_battery_capacity_s3 = mean("battery_capacity_s3")
mean_battery_capacity_s4 = mean("battery_capacity_s4")
mean_battery_capacity_s5 = mean("battery_capacity_s5")
mean_battery_capacity_s6 = mean("battery_capacity_s6")
mean_battery_capacity_s7 = mean("battery_capacity_s7")
mean_battery_capacity_s8 = mean("battery_capacity_s8")
mean_battery_capacity_s_med = mean("battery_capacity_s_med")
mean_battery_capacity_s_mean = mean("battery_capacity_s_mean")
mean_battery_capacity_s_std = mean("battery_capacity_s_std")
mean_battery_capacity_s_min = mean("battery_capacity_s_min")
mean_battery_capacity_s_max = mean("battery_capacity_s_max")
mean_battery_capacity_observation = [
    mean_battery_capacity_total, mean_battery_capacity_med, mean_battery_capacity_mean, mean_battery_capacity_std, mean_battery_capacity_min, 
    mean_battery_capacity_max, mean_battery_capacity_s1, mean_battery_capacity_s2, mean_battery_capacity_s3, mean_battery_capacity_s4,
    mean_battery_capacity_s5, mean_battery_capacity_s6, mean_battery_capacity_s7, mean_battery_capacity_s8, mean_battery_capacity_s_med,
    mean_battery_capacity_s_mean, mean_battery_capacity_s_std, mean_battery_capacity_s_min, mean_battery_capacity_s_max,
]

mean_win_battery_capacity_total = locmean("victory", "battery_capacity_total")
mean_win_battery_capacity_med =  locmean("victory", "battery_capacity_med")
mean_win_battery_capacity_mean =  locmean("victory", "battery_capacity_mean")
mean_win_battery_capacity_std =  locmean("victory", "battery_capacity_std")
mean_win_battery_capacity_min =  locmean("victory", "battery_capacity_min")
mean_win_battery_capacity_max =  locmean("victory", "battery_capacity_max")
mean_win_battery_capacity_s1 =  locmean("victory", "battery_capacity_s1")
mean_win_battery_capacity_s2 =  locmean("victory", "battery_capacity_s2")
mean_win_battery_capacity_s3 =  locmean("victory", "battery_capacity_s3")
mean_win_battery_capacity_s4 =  locmean("victory", "battery_capacity_s4")
mean_win_battery_capacity_s5 =  locmean("victory", "battery_capacity_s5")
mean_win_battery_capacity_s6 =  locmean("victory", "battery_capacity_s6")
mean_win_battery_capacity_s7 =  locmean("victory", "battery_capacity_s7")
mean_win_battery_capacity_s8 =  locmean("victory", "battery_capacity_s8")
mean_win_battery_capacity_s_med =  locmean("victory", "battery_capacity_s_med")
mean_win_battery_capacity_s_mean =  locmean("victory", "battery_capacity_s_mean")
mean_win_battery_capacity_s_std =  locmean("victory", "battery_capacity_s_std")
mean_win_battery_capacity_s_min =  locmean("victory", "battery_capacity_s_min")
mean_win_battery_capacity_s_max =  locmean("victory", "battery_capacity_s_max")
mean_win_battery_capacity_observation = [
    mean_win_battery_capacity_total, mean_win_battery_capacity_med, mean_win_battery_capacity_mean, mean_win_battery_capacity_std, mean_win_battery_capacity_min, 
    mean_win_battery_capacity_max, mean_win_battery_capacity_s1, mean_win_battery_capacity_s2, mean_win_battery_capacity_s3, mean_win_battery_capacity_s4,
    mean_win_battery_capacity_s5, mean_win_battery_capacity_s6, mean_win_battery_capacity_s7, mean_win_battery_capacity_s8, mean_win_battery_capacity_s_med,
    mean_win_battery_capacity_s_mean, mean_win_battery_capacity_s_std, mean_win_battery_capacity_s_min, mean_win_battery_capacity_s_max,
]

mean_loss_battery_capacity_total = locmean("loss", "battery_capacity_total")
mean_loss_battery_capacity_med =  locmean("loss", "battery_capacity_med")
mean_loss_battery_capacity_mean =  locmean("loss", "battery_capacity_mean")
mean_loss_battery_capacity_std =  locmean("loss", "battery_capacity_std")
mean_loss_battery_capacity_min =  locmean("loss", "battery_capacity_min")
mean_loss_battery_capacity_max =  locmean("loss", "battery_capacity_max")
mean_loss_battery_capacity_s1 =  locmean("loss", "battery_capacity_s1")
mean_loss_battery_capacity_s2 =  locmean("loss", "battery_capacity_s2")
mean_loss_battery_capacity_s3 =  locmean("loss", "battery_capacity_s3")
mean_loss_battery_capacity_s4 =  locmean("loss", "battery_capacity_s4")
mean_loss_battery_capacity_s5 =  locmean("loss", "battery_capacity_s5")
mean_loss_battery_capacity_s6 =  locmean("loss", "battery_capacity_s6")
mean_loss_battery_capacity_s7 =  locmean("loss", "battery_capacity_s7")
mean_loss_battery_capacity_s8 =  locmean("loss", "battery_capacity_s8")
mean_loss_battery_capacity_s_med =  locmean("loss", "battery_capacity_s_med")
mean_loss_battery_capacity_s_mean =  locmean("loss", "battery_capacity_s_mean")
mean_loss_battery_capacity_s_std =  locmean("loss", "battery_capacity_s_std")
mean_loss_battery_capacity_s_min =  locmean("loss", "battery_capacity_s_min")
mean_loss_battery_capacity_s_max =  locmean("loss", "battery_capacity_s_max")
mean_loss_battery_capacity_observation = [
    mean_loss_battery_capacity_total, mean_loss_battery_capacity_med, mean_loss_battery_capacity_mean, mean_loss_battery_capacity_std, mean_loss_battery_capacity_min, 
    mean_loss_battery_capacity_max, mean_loss_battery_capacity_s1, mean_loss_battery_capacity_s2, mean_loss_battery_capacity_s3, mean_loss_battery_capacity_s4,
    mean_loss_battery_capacity_s5, mean_loss_battery_capacity_s6, mean_loss_battery_capacity_s7, mean_loss_battery_capacity_s8, mean_loss_battery_capacity_s_med,
    mean_loss_battery_capacity_s_mean, mean_loss_battery_capacity_s_std, mean_loss_battery_capacity_s_min, mean_loss_battery_capacity_s_max,
]

# artillery_capacity
artillery_capacity_total = df["artillery_capacity_total"].iloc[-1]
artillery_capacity_med = df["artillery_capacity_med"].iloc[-1]
artillery_capacity_mean = df["artillery_capacity_mean"].iloc[-1]
artillery_capacity_std = df["artillery_capacity_std"].iloc[-1]
artillery_capacity_min = df["artillery_capacity_min"].iloc[-1]
artillery_capacity_max = df["artillery_capacity_max"].iloc[-1]
artillery_capacity_s1 = df["artillery_capacity_s1"].iloc[-1]
artillery_capacity_s2 = df["artillery_capacity_s2"].iloc[-1]
artillery_capacity_s3 = df["artillery_capacity_s3"].iloc[-1]
artillery_capacity_s4 = df["artillery_capacity_s4"].iloc[-1]
artillery_capacity_s5 = df["artillery_capacity_s5"].iloc[-1]
artillery_capacity_s6 = df["artillery_capacity_s6"].iloc[-1]
artillery_capacity_s7 = df["artillery_capacity_s7"].iloc[-1]
artillery_capacity_s8 = df["artillery_capacity_s8"].iloc[-1]
artillery_capacity_s_med = df["artillery_capacity_s_med"].iloc[-1]
artillery_capacity_s_mean = df["artillery_capacity_s_mean"].iloc[-1]
artillery_capacity_s_std = df["artillery_capacity_s_std"].iloc[-1]
artillery_capacity_s_min = df["artillery_capacity_s_min"].iloc[-1]
artillery_capacity_s_max = df["artillery_capacity_s_max"].iloc[-1]
artillery_capacity_observation = [
    artillery_capacity_total, artillery_capacity_med, artillery_capacity_mean, artillery_capacity_std, artillery_capacity_min, artillery_capacity_max, artillery_capacity_s1,
    artillery_capacity_s2, artillery_capacity_s3,artillery_capacity_s4, artillery_capacity_s5, artillery_capacity_s6, artillery_capacity_s7, artillery_capacity_s8,
    artillery_capacity_s_med, artillery_capacity_s_mean, artillery_capacity_s_std, artillery_capacity_s_min, artillery_capacity_s_max,
]

mean_artillery_capacity_total = mean("artillery_capacity_total")
mean_artillery_capacity_med = mean("artillery_capacity_med")
mean_artillery_capacity_mean = mean("artillery_capacity_mean")
mean_artillery_capacity_std = mean("artillery_capacity_std")
mean_artillery_capacity_min = mean("artillery_capacity_min")
mean_artillery_capacity_max = mean("artillery_capacity_max")
mean_artillery_capacity_s1 = mean("artillery_capacity_s1")
mean_artillery_capacity_s2 = mean("artillery_capacity_s2")
mean_artillery_capacity_s3 = mean("artillery_capacity_s3")
mean_artillery_capacity_s4 = mean("artillery_capacity_s4")
mean_artillery_capacity_s5 = mean("artillery_capacity_s5")
mean_artillery_capacity_s6 = mean("artillery_capacity_s6")
mean_artillery_capacity_s7 = mean("artillery_capacity_s7")
mean_artillery_capacity_s8 = mean("artillery_capacity_s8")
mean_artillery_capacity_s_med = mean("artillery_capacity_s_med")
mean_artillery_capacity_s_mean = mean("artillery_capacity_s_mean")
mean_artillery_capacity_s_std = mean("artillery_capacity_s_std")
mean_artillery_capacity_s_min = mean("artillery_capacity_s_min")
mean_artillery_capacity_s_max = mean("artillery_capacity_s_max")
mean_artillery_capacity_observation = [
    mean_artillery_capacity_total, mean_artillery_capacity_med, mean_artillery_capacity_mean, mean_artillery_capacity_std, mean_artillery_capacity_min, 
    mean_artillery_capacity_max, mean_artillery_capacity_s1, mean_artillery_capacity_s2, mean_artillery_capacity_s3, mean_artillery_capacity_s4,
    mean_artillery_capacity_s5, mean_artillery_capacity_s6, mean_artillery_capacity_s7, mean_artillery_capacity_s8, mean_artillery_capacity_s_med,
    mean_artillery_capacity_s_mean, mean_artillery_capacity_s_std, mean_artillery_capacity_s_min, mean_artillery_capacity_s_max,
]

mean_win_artillery_capacity_total = locmean("victory", "artillery_capacity_total")
mean_win_artillery_capacity_med =  locmean("victory", "artillery_capacity_med")
mean_win_artillery_capacity_mean =  locmean("victory", "artillery_capacity_mean")
mean_win_artillery_capacity_std =  locmean("victory", "artillery_capacity_std")
mean_win_artillery_capacity_min =  locmean("victory", "artillery_capacity_min")
mean_win_artillery_capacity_max =  locmean("victory", "artillery_capacity_max")
mean_win_artillery_capacity_s1 =  locmean("victory", "artillery_capacity_s1")
mean_win_artillery_capacity_s2 =  locmean("victory", "artillery_capacity_s2")
mean_win_artillery_capacity_s3 =  locmean("victory", "artillery_capacity_s3")
mean_win_artillery_capacity_s4 =  locmean("victory", "artillery_capacity_s4")
mean_win_artillery_capacity_s5 =  locmean("victory", "artillery_capacity_s5")
mean_win_artillery_capacity_s6 =  locmean("victory", "artillery_capacity_s6")
mean_win_artillery_capacity_s7 =  locmean("victory", "artillery_capacity_s7")
mean_win_artillery_capacity_s8 =  locmean("victory", "artillery_capacity_s8")
mean_win_artillery_capacity_s_med =  locmean("victory", "artillery_capacity_s_med")
mean_win_artillery_capacity_s_mean =  locmean("victory", "artillery_capacity_s_mean")
mean_win_artillery_capacity_s_std =  locmean("victory", "artillery_capacity_s_std")
mean_win_artillery_capacity_s_min =  locmean("victory", "artillery_capacity_s_min")
mean_win_artillery_capacity_s_max =  locmean("victory", "artillery_capacity_s_max")
mean_win_artillery_capacity_observation = [
    mean_win_artillery_capacity_total, mean_win_artillery_capacity_med, mean_win_artillery_capacity_mean, mean_win_artillery_capacity_std, mean_win_artillery_capacity_min, 
    mean_win_artillery_capacity_max, mean_win_artillery_capacity_s1, mean_win_artillery_capacity_s2, mean_win_artillery_capacity_s3, mean_win_artillery_capacity_s4,
    mean_win_artillery_capacity_s5, mean_win_artillery_capacity_s6, mean_win_artillery_capacity_s7, mean_win_artillery_capacity_s8, mean_win_artillery_capacity_s_med,
    mean_win_artillery_capacity_s_mean, mean_win_artillery_capacity_s_std, mean_win_artillery_capacity_s_min, mean_win_artillery_capacity_s_max,
]

mean_loss_artillery_capacity_total = locmean("loss", "artillery_capacity_total")
mean_loss_artillery_capacity_med =  locmean("loss", "artillery_capacity_med")
mean_loss_artillery_capacity_mean =  locmean("loss", "artillery_capacity_mean")
mean_loss_artillery_capacity_std =  locmean("loss", "artillery_capacity_std")
mean_loss_artillery_capacity_min =  locmean("loss", "artillery_capacity_min")
mean_loss_artillery_capacity_max =  locmean("loss", "artillery_capacity_max")
mean_loss_artillery_capacity_s1 =  locmean("loss", "artillery_capacity_s1")
mean_loss_artillery_capacity_s2 =  locmean("loss", "artillery_capacity_s2")
mean_loss_artillery_capacity_s3 =  locmean("loss", "artillery_capacity_s3")
mean_loss_artillery_capacity_s4 =  locmean("loss", "artillery_capacity_s4")
mean_loss_artillery_capacity_s5 =  locmean("loss", "artillery_capacity_s5")
mean_loss_artillery_capacity_s6 =  locmean("loss", "artillery_capacity_s6")
mean_loss_artillery_capacity_s7 =  locmean("loss", "artillery_capacity_s7")
mean_loss_artillery_capacity_s8 =  locmean("loss", "artillery_capacity_s8")
mean_loss_artillery_capacity_s_med =  locmean("loss", "artillery_capacity_s_med")
mean_loss_artillery_capacity_s_mean =  locmean("loss", "artillery_capacity_s_mean")
mean_loss_artillery_capacity_s_std =  locmean("loss", "artillery_capacity_s_std")
mean_loss_artillery_capacity_s_min =  locmean("loss", "artillery_capacity_s_min")
mean_loss_artillery_capacity_s_max =  locmean("loss", "artillery_capacity_s_max")
mean_loss_artillery_capacity_observation = [
    mean_loss_artillery_capacity_total, mean_loss_artillery_capacity_med, mean_loss_artillery_capacity_mean, mean_loss_artillery_capacity_std, mean_loss_artillery_capacity_min, 
    mean_loss_artillery_capacity_max, mean_loss_artillery_capacity_s1, mean_loss_artillery_capacity_s2, mean_loss_artillery_capacity_s3, mean_loss_artillery_capacity_s4,
    mean_loss_artillery_capacity_s5, mean_loss_artillery_capacity_s6, mean_loss_artillery_capacity_s7, mean_loss_artillery_capacity_s8, mean_loss_artillery_capacity_s_med,
    mean_loss_artillery_capacity_s_mean, mean_loss_artillery_capacity_s_std, mean_loss_artillery_capacity_s_min, mean_loss_artillery_capacity_s_max,
]

# prepare data for overview report

data = [
    # score
    score_observation,
    mean_score_observation,
    mean_win_score_observation,
    mean_loss_score_observation,
    # scrap earned
    scrap_earned_observation,
    mean_scrap_earned_observation,
    mean_win_scrap_earned_observation,
    mean_loss_scrap_earned_observation,
    # scrap held
    scrap_held_observation,
    mean_scrap_held_observation,
    mean_win_scrap_held_observation,
    mean_loss_scrap_held_observation,
    # beacons
    beacons_observation,
    mean_beacons_observation,
    mean_win_beacons_observation,
    mean_loss_beacons_observation,
    # ships defeated
    ships_defeated_observation,
    mean_ships_defeated_observation,
    mean_win_ships_defeated_observation,
    mean_loss_ships_defeated_observation,
    # hull
    hull_observation,
    mean_hull_observation,
    mean_win_hull_observation,
    mean_loss_hull_observation,
    # hull damage
    hull_damage_observation,
    mean_hull_damage_observation,
    mean_win_hull_damage_observation,
    mean_loss_hull_damage_observation,
    # cargo amount
    cargo_observation,
    mean_cargo_observation,
    mean_win_cargo_observation,
    mean_loss_cargo_observation,
    # stores visited
    stores_visited_observation,
    mean_stores_visited_observation,
    mean_win_stores_visited_observation,
    mean_loss_stores_visited_observation,
    # fuel
    fuel_observation,
    mean_fuel_observation,
    mean_win_fuel_observation,
    mean_loss_fuel_observation,
    # missiles
    missiles_observation,
    mean_missiles_observation,
    mean_win_missiles_observation,
    mean_loss_missiles_observation,
    # drone parts
    drone_parts_observation,
    mean_drone_parts_observation,
    mean_win_drone_parts_observation,
    mean_loss_drone_parts_observation,
    # crew hired
    crew_hired_observation,
    mean_crew_hired_observation,
    mean_win_crew_hired_observation,
    mean_loss_crew_hired_observation,
    # crew lost
    crew_lost_observation,
    mean_crew_lost_observation,
    mean_win_crew_lost_observation,
    mean_loss_crew_lost_observation,
    # crew size
    crew_size_observation,
    mean_crew_size_observation,
    mean_win_crew_size_observation,
    mean_loss_crew_size_observation,
    # power capacity
    power_capacity_observation,
    mean_power_capacity_observation,
    mean_win_power_capacity_observation,
    mean_loss_power_capacity_observation,
    # weapons system capacity
    weapons_capacity_observation,
    mean_weapons_capacity_observation,
    mean_win_weapons_capacity_observation,
    mean_loss_weapons_capacity_observation,
    # engines capacity
    engines_capacity_observation,
    mean_engines_capacity_observation,
    mean_win_engines_capacity_observation,
    mean_loss_engines_capacity_observation,
    # shields capacity
    shields_capacity_observation,
    mean_shields_capacity_observation,
    mean_win_shields_capacity_observation,
    mean_loss_shields_capacity_observation,
    # oxygen system capacity
    oxygen_capacity_observation,
    mean_oxygen_capacity_observation,
    mean_win_oxygen_capacity_observation,
    mean_loss_oxygen_capacity_observation,
    # medbay capacity
    medbay_capacity_observation,
    mean_medbay_capacity_observation,
    mean_win_medbay_capacity_observation,
    mean_loss_medbay_capacity_observation,
    # clonebay capacity
    clonebay_capacity_observation,
    mean_clonebay_capacity_observation,
    mean_win_clonebay_capacity_observation,
    mean_loss_clonebay_capacity_observation,
    # pilot system capacity
    pilot_capacity_observation,
    mean_pilot_capacity_observation,
    mean_win_pilot_capacity_observation,
    mean_loss_pilot_capacity_observation,
    # sensors system capacity
    sensors_capacity_observation,
    mean_sensors_capacity_observation,
    mean_win_sensors_capacity_observation,
    mean_loss_sensors_capacity_observation,
    # doors system capacity
    doors_capacity_observation,
    mean_doors_capacity_observation,
    mean_win_doors_capacity_observation,
    mean_loss_doors_capacity_observation,
    # drone control capacity
    drone_capacity_observation,
    mean_drone_capacity_observation,
    mean_win_drone_capacity_observation,
    mean_loss_drone_capacity_observation,
    # teleporter capacity
    teleporter_capacity_observation,
    mean_teleporter_capacity_observation,
    mean_win_teleporter_capacity_observation,
    mean_loss_teleporter_capacity_observation,
    # cloaking capacity
    cloaking_capacity_observation,
    mean_cloaking_capacity_observation,
    mean_win_cloaking_capacity_observation,
    mean_loss_cloaking_capacity_observation,
    # mindcontrol capacity
    mindcontrol_capacity_observation,
    mean_mindcontrol_capacity_observation,
    mean_win_mindcontrol_capacity_observation,
    mean_loss_mindcontrol_capacity_observation,
    # hacking capacity
    hacking_capacity_observation,
    mean_hacking_capacity_observation,
    mean_win_hacking_capacity_observation,
    mean_loss_hacking_capacity_observation,
    # battery system capacity
    battery_capacity_observation,
    mean_battery_capacity_observation,
    mean_win_battery_capacity_observation,
    mean_loss_battery_capacity_observation,
    # artillery capacity
    artillery_capacity_observation,
    mean_artillery_capacity_observation,
    mean_win_artillery_capacity_observation,
    mean_loss_artillery_capacity_observation,
]

category = [
    "general", "general", "general", "general", 
    "general", "general", "general", "general", 
    "general", "general", "general", "general", 
    "general", "general", "general", "general", 
    "general", "general", "general", "general", 
    "hull", "hull", "hull", "hull", 
    "hull", "hull", "hull", "hull", 
    "misc", "misc", "misc", "misc", 
    "misc", "misc", "misc", "misc", 
    "misc", "misc", "misc", "misc", 
    "misc", "misc", "misc", "misc", 
    "misc", "misc", "misc", "misc", 
    "crew", "crew", "crew", "crew", 
    "crew", "crew", "crew", "crew", 
    "crew", "crew", "crew", "crew", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
    "upgrades", "upgrades", "upgrades", "upgrades", 
]
attribute = [
     "score", "score", "score", "score",
    "scrap earned", "scrap earned", "scrap earned", "scrap earned",
    "scrap held", "scrap held", "scrap held", "scrap held",
    "beacons", "beacons", "beacons", "beacons",
    "ships defeated", "ships defeated", "ships defeated", "ships defeated",
    "hull", "hull", "hull", "hull", 
    "hull damage", "hull damage", "hull damage", "hull damage", 
    "cargo amount", "cargo amount", "cargo amount", "cargo amount",
    "stores visited", "stores visited", "stores visited", "stores visited", 
    "fuel", "fuel", "fuel", "fuel", 
    "missiles", "missiles", "missiles", "missiles", 
    "drone parts", "drone parts", "drone parts", "drone parts", 
    "crew hired", "crew hired", "crew hired", "crew hired", 
    "crew lost", "crew lost", "crew lost", "crew lost", 
    "crew size", "crew size", "crew size", "crew size", 
    "power capacity", "power capacity", "power capacity", "power capacity", 
    "weapons capacity", "weapons capacity", "weapons capacity", "weapons capacity", 
    "engines capacity", "engines capacity", "engines capacity", "engines capacity", 
    "shields capacity", "shields capacity", "shields capacity", "shields capacity", 
    "oxygen capacity", "oxygen capacity", "oxygen capacity", "oxygen capacity", 
    "medbay capacity", "medbay capacity", "medbay capacity", "medbay capacity", 
    "clonebay capacity", "clonebay capacity", "clonebay capacity", "clonebay capacity", 
    "pilot capacity", "pilot capacity", "pilot capacity", "pilot capacity", 
    "sensors capacity", "sensors capacity", "sensors capacity", "sensors capacity", 
    "doors capacity", "doors capacity", "doors capacity", "doors capacity",
    "drone control capacity", "drone control capacity", "drone control capacity", "drone control capacity", 
    "teleporter capacity", "teleporter capacity", "teleporter capacity", "teleporter capacity", 
    "cloaking capacity", "cloaking capacity", "cloaking capacity", "cloaking capacity", 
    "mindcontrol capacity", "mindcontrol capacity", "mindcontrol capacity", "mindcontrol capacity", 
    "hacking capacity", "hacking capacity", "hacking capacity", "hacking capacity", 
    "battery capacity", "battery capacity", "battery capacity", "battery capacity", 
    "artillery capacity", "artillery capacity", "artillery capacity", "artillery capacity"
]
observation = [
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
    "observation", "average", "average [win]", "average [loss]",
]
# 19 columns
columns = [
    "total", "median", "mean", "std",
    "min", "max", "s1", "s2", "s3", "s4",
    "s5", "s6", "s7", "s8", "s_median",
    "s_mean", "s_std", "s_min", "s_max"
]

sector_report = pd.DataFrame(
    data,
    index=[category, attribute, observation],
    columns=columns
)

# save overview report

FILE = str(pathlib.Path().absolute()) + r"\analysis.xlsx"

with pd.ExcelWriter(FILE, engine = "openpyxl",  mode='a', float_format="%.1f") as writer:
    workBook = writer.book
    try:
        workBook.remove(workBook['sectors'])
    except:
        print("worksheet doesn't exist")
    finally:
        sector_report.to_excel(writer, sheet_name='sectors', index = True, header = True)
    writer.save()
    writer.close()